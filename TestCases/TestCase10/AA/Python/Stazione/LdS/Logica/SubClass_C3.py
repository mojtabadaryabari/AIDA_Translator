# Codice del modello 'TestCase10', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

class SubClass_C3(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C3, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c3_previousva_pv1(False)
        self.set_subclass_c3_previousva_pv2(False)
        self.set_subclass_c3_previousva_pv3(False)
        self.set_subclass_c3_previousva_pv4(GlobalEnumeration.rossogiallox)
        self.set_subclass_c3_restoreva_rv1(False)
        self.set_subclass_c3_restoreva_rv2(GlobalEnumeration.c270)
        self.set_subclass_c3_restoreva_rv3(False)
        self.set_subclass_c3_restoreva_rv4(0)
        self.set_subclass_c3_variabile_v1(0)
        self.set_subclass_c3_variabile_v2(0)
        self.set_subclass_c3_variabile_v3(0)
        self.set_subclass_c3_variabile_v4(False)
        self.set_subclass_c3_variabile_v8(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C3
        if self.is_triggered('eventSubclass_c3_command_comm10DaSender99fab08d'):
            self.set_man_cmd_response('eventSubclass_c3_command_comm10DaSender99fab08d',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c3_command_comm10DaSender99fab08d',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c3_command_comm6'):
            self.set_man_cmd_response('eventSubclass_c3_command_comm6',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c3_command_comm6',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, subclass_c3_lista_l3, subclass_c3_lista_l8, subclass_c3_parametro_p1, subclass_c3_parametro_p9):
        # initialize the record type parameters
        self.set_subclass_c3_lista_l3(subclass_c3_lista_l3)
        self.set_subclass_c3_lista_l8(subclass_c3_lista_l8)
        # initialize the simple type parameters
        self.set_subclass_c3_parametro_p1(subclass_c3_parametro_p1)
        self.set_subclass_c3_parametro_p9(subclass_c3_parametro_p9)

        # initialize the timers
        self.set_subclass_c3_restoreti_ti1(340000)
        self.set_subclass_c3_restoreti_ti1_restore(340000)
        self.set_subclass_c3_restoreti_ti2(132000)
        self.set_subclass_c3_restoreti_ti2_restore(132000)
        self.set_subclass_c3_restoreti_ti3(41000)
        self.set_subclass_c3_restoreti_ti3_restore(41000)
        self.set_subclass_c3_restoreti_ti4(35000)
        self.set_subclass_c3_restoreti_ti4_restore(35000)
        self.set_subclass_c3_restoreti_ti5(540000)
        self.set_subclass_c3_restoreti_ti5_restore(540000)
        self.set_subclass_c3_timer_t1(2000)
        self.set_subclass_c3_timer_t2(5000)

        self.timers = [self.subclass_c3_restoreti_ti1,self.subclass_c3_restoreti_ti1_restore,self.subclass_c3_restoreti_ti2,self.subclass_c3_restoreti_ti2_restore,self.subclass_c3_restoreti_ti3,self.subclass_c3_restoreti_ti3_restore,self.subclass_c3_restoreti_ti4,self.subclass_c3_restoreti_ti4_restore,self.subclass_c3_restoreti_ti5,self.subclass_c3_restoreti_ti5_restore,self.subclass_c3_timer_t1,self.subclass_c3_timer_t2,]

        # initialize the counters
        self.set_subclass_c3_contatore_co2(0)
        self.set_subclass_c3_contatore_co4(0)

    # setters for record type parameters
    def set_subclass_c3_lista_l3(self, subclass_c3_lista_l3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l3",subclass_c3_lista_l3)

    def set_subclass_c3_lista_l8(self, subclass_c3_lista_l8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l8",subclass_c3_lista_l8)


    # getters for record type parameters
    def get_subclass_c3_lista_l3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l3")

    def get_subclass_c3_lista_l8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l8")


    # setters for simple type parameters
    def set_subclass_c3_parametro_p1(self, subclass_c3_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p1",subclass_c3_parametro_p1)

    def set_subclass_c3_parametro_p9(self, subclass_c3_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p9",subclass_c3_parametro_p9)


    # getters for simple type parameters
    def get_subclass_c3_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p1")

    def get_subclass_c3_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p9")


    # setters for comandi al piazzale
    def set_subclass_c3_comando_c1(self, subclass_c3_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c1",subclass_c3_comando_c1)

    def set_subclass_c3_comando_c10(self, subclass_c3_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c10",subclass_c3_comando_c10)

    def set_subclass_c3_comando_c4(self, subclass_c3_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c4",subclass_c3_comando_c4)

    def set_subclass_c3_comando_c6(self, subclass_c3_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c6",subclass_c3_comando_c6)

    def set_subclass_c3_comando_c7(self, subclass_c3_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c7",subclass_c3_comando_c7)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c3_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c1")

    def get_subclass_c3_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c4")

    def get_subclass_c3_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c6")

    def get_subclass_c3_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c7")

    def get_subclass_c3_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c2")

    def get_subclass_c3_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3")

    def get_subclass_c3_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c5")

    def get_subclass_c3_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c8")

    def get_subclass_c3_previousco_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c9")


    # setters for state variables
    def set_subclass_c3_previousco_c2_prev(self, subclass_c3_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c2_prev",subclass_c3_previousco_c2_prev)
    def set_subclass_c3_previousco_c3_prev(self, subclass_c3_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3_prev",subclass_c3_previousco_c3_prev)
    def set_subclass_c3_previousco_c5_prev(self, subclass_c3_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c5_prev",subclass_c3_previousco_c5_prev)
    def set_subclass_c3_previousco_c8_prev(self, subclass_c3_previousco_c8_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c8_prev",subclass_c3_previousco_c8_prev)
    def set_subclass_c3_previousco_c9_prev(self, subclass_c3_previousco_c9_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c9_prev",subclass_c3_previousco_c9_prev)
    def set_subclass_c3_previousva_pv1(self, subclass_c3_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1",subclass_c3_previousva_pv1)
    def set_subclass_c3_previousva_pv1_prev(self, subclass_c3_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1_prev",subclass_c3_previousva_pv1_prev)
    def set_subclass_c3_previousva_pv2(self, subclass_c3_previousva_pv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2",subclass_c3_previousva_pv2)
    def set_subclass_c3_previousva_pv2_prev(self, subclass_c3_previousva_pv2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2_prev",subclass_c3_previousva_pv2_prev)
    def set_subclass_c3_previousva_pv3(self, subclass_c3_previousva_pv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3",subclass_c3_previousva_pv3)
    def set_subclass_c3_previousva_pv3_prev(self, subclass_c3_previousva_pv3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3_prev",subclass_c3_previousva_pv3_prev)
    def set_subclass_c3_previousva_pv4(self, subclass_c3_previousva_pv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4",subclass_c3_previousva_pv4)
    def set_subclass_c3_previousva_pv4_prev(self, subclass_c3_previousva_pv4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4_prev",subclass_c3_previousva_pv4_prev)
    def set_subclass_c3_restoreva_rv1(self, subclass_c3_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv1",subclass_c3_restoreva_rv1)
    def set_subclass_c3_restoreva_rv2(self, subclass_c3_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv2",subclass_c3_restoreva_rv2)
    def set_subclass_c3_restoreva_rv3(self, subclass_c3_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv3",subclass_c3_restoreva_rv3)
    def set_subclass_c3_restoreva_rv4(self, subclass_c3_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv4",subclass_c3_restoreva_rv4)
    def set_subclass_c3_variabile_v1(self, subclass_c3_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v1",subclass_c3_variabile_v1)
    def set_subclass_c3_variabile_v2(self, subclass_c3_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v2",subclass_c3_variabile_v2)
    def set_subclass_c3_variabile_v3(self, subclass_c3_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v3",subclass_c3_variabile_v3)
    def set_subclass_c3_variabile_v4(self, subclass_c3_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v4",subclass_c3_variabile_v4)
    def set_subclass_c3_variabile_v8(self, subclass_c3_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v8",subclass_c3_variabile_v8)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c3_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c2_prev")

    def get_subclass_c3_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3_prev")

    def get_subclass_c3_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c5_prev")

    def get_subclass_c3_previousco_c8_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c8_prev")

    def get_subclass_c3_previousco_c9_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c9_prev")

    def get_subclass_c3_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1")

    def get_subclass_c3_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1_prev")

    def get_subclass_c3_previousva_pv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2")

    def get_subclass_c3_previousva_pv2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2_prev")

    def get_subclass_c3_previousva_pv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3")

    def get_subclass_c3_previousva_pv3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3_prev")

    def get_subclass_c3_previousva_pv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4")

    def get_subclass_c3_previousva_pv4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4_prev")

    def get_subclass_c3_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv1")

    def get_subclass_c3_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv1_restore")

    def get_subclass_c3_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv2")

    def get_subclass_c3_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv2_restore")

    def get_subclass_c3_restoreva_rv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv3")

    def get_subclass_c3_restoreva_rv3_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv3_restore")

    def get_subclass_c3_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv4")

    def get_subclass_c3_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv4_restore")

    def get_subclass_c3_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v1")

    def get_subclass_c3_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v2")

    def get_subclass_c3_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v3")

    def get_subclass_c3_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v4")

    def get_subclass_c3_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v8")


    # setters for timers
    def set_subclass_c3_restoreti_ti1(self, timerDuration):
        self.subclass_c3_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti1", self.memory)

    def set_subclass_c3_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti1_restore", self.memory)

    def set_subclass_c3_restoreti_ti2(self, timerDuration):
        self.subclass_c3_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti2", self.memory)

    def set_subclass_c3_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti2_restore", self.memory)

    def set_subclass_c3_restoreti_ti3(self, timerDuration):
        self.subclass_c3_restoreti_ti3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti3", self.memory)

    def set_subclass_c3_restoreti_ti3_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti3_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti3_restore", self.memory)

    def set_subclass_c3_restoreti_ti4(self, timerDuration):
        self.subclass_c3_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti4", self.memory)

    def set_subclass_c3_restoreti_ti4_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti4_restore", self.memory)

    def set_subclass_c3_restoreti_ti5(self, timerDuration):
        self.subclass_c3_restoreti_ti5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti5", self.memory)

    def set_subclass_c3_restoreti_ti5_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti5_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti5_restore", self.memory)

    def set_subclass_c3_timer_t1(self, timerDuration):
        self.subclass_c3_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t1", self.memory)

    def set_subclass_c3_timer_t2(self, timerDuration):
        self.subclass_c3_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t2", self.memory)


    # getters for timers
    def get_subclass_c3_restoreti_ti1(self):
        return self.subclass_c3_restoreti_ti1

    def get_subclass_c3_restoreti_ti1_restore(self):
        return self.subclass_c3_restoreti_ti1_restore

    def get_subclass_c3_restoreti_ti2(self):
        return self.subclass_c3_restoreti_ti2

    def get_subclass_c3_restoreti_ti2_restore(self):
        return self.subclass_c3_restoreti_ti2_restore

    def get_subclass_c3_restoreti_ti3(self):
        return self.subclass_c3_restoreti_ti3

    def get_subclass_c3_restoreti_ti3_restore(self):
        return self.subclass_c3_restoreti_ti3_restore

    def get_subclass_c3_restoreti_ti4(self):
        return self.subclass_c3_restoreti_ti4

    def get_subclass_c3_restoreti_ti4_restore(self):
        return self.subclass_c3_restoreti_ti4_restore

    def get_subclass_c3_restoreti_ti5(self):
        return self.subclass_c3_restoreti_ti5

    def get_subclass_c3_restoreti_ti5_restore(self):
        return self.subclass_c3_restoreti_ti5_restore

    def get_subclass_c3_timer_t1(self):
        return self.subclass_c3_timer_t1

    def get_subclass_c3_timer_t2(self):
        return self.subclass_c3_timer_t2


    # setters for counters
    def set_subclass_c3_contatore_co2(self, counterInitValue):
        self.subclass_c3_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co2", self.memory)

    def set_subclass_c3_contatore_co4(self, counterInitValue):
        self.subclass_c3_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co4", self.memory)


    # getters for counters
    def get_subclass_c3_contatore_co2(self):
        return self.subclass_c3_contatore_co2

    def get_subclass_c3_contatore_co4(self):
        return self.subclass_c3_contatore_co4



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 4 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  diverso da  /*56,*/ 13 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 14215 /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 12 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T1 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 4 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  diverso da  /*56,*/ 13 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 14215 /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 12 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T1 non sia disattivo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 4 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  diverso da  /*56,*/ 13 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 4 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  diverso da  /*56,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 4 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è scaduto""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 4""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v1)  è uguale a  (4)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co2 è  diverso da  /*56,*/ 13""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C4 non è  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c4)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 14215 /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 12 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T1 non sia disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 14215 /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 12 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 14215 /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 12""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 14215""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co4)  è uguale a  (14215)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 12""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co2)  è uguale a  (12))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (12)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C7 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C4 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V4 è  uguale a  True""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C3_timer_T1 non sia disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C3_lista_L3
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c3_lista_l3'""", [
                    ]),#0
                    ]),#2
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[2], ),
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_subclass_c3_previousco_c2_prev(False)
        self.set_subclass_c3_previousco_c3_prev(False)
        self.set_subclass_c3_previousco_c5_prev(True)
        self.set_subclass_c3_previousco_c8_prev(GlobalEnumeration.spento)
        self.set_subclass_c3_previousco_c9_prev(True)
        self.set_subclass_c3_previousva_pv1_prev(self.get_subclass_c3_previousva_pv1())
        self.set_subclass_c3_previousva_pv2_prev(self.get_subclass_c3_previousva_pv2())
        self.set_subclass_c3_previousva_pv3_prev(self.get_subclass_c3_previousva_pv3())
        self.set_subclass_c3_previousva_pv4_prev(self.get_subclass_c3_previousva_pv4())

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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1)
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
        
         commento: {68,} commento: {37,}  se la variabile SubClass_C3_variabile_V1 non è  uguale a  commento: {53,} 4 commento: {36,} e  se il timer SubClass_C3_timer_T2 non è scaduto commento: {38,} o  se il contatore SubClass_C3_contatore_Co2 è  diverso da  commento: {56,} 13 commento: {35,} o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Almeno una delle seguenti { 
         commento: {38,}  se il contatore SubClass_C3_contatore_Co4 è  diverso da  commento: {56,} 14215 commento: {38,} e  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  commento: {56,} 12 commento: {35,} o  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C4 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T1 non sia disattivo
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        return db((db(not db((db((db((db(not db(self.get_subclass_c3_variabile_v1() == 4, self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t2().isScaduto(), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 13, self.dbs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_controllo_c4() == True, self.dbs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0]) or db(not db((db((db(not db(self.get_subclass_c3_contatore_co4().get_valore() == 14215, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 12, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c3_controllo_c7() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_controllo_c4() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_variabile_v4() == True, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c3_timer_t1().isDisattivato(), self.dbs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[0].subs[1]), self.dbs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1])), self.dbs[1])
    
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
        
        Comanda al campo MainClass_C1 di SubClass_C3_lista_L3
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C3_lista_L3
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c3_lista_l3()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    # effect macros
    def macroSubclass_c3_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI1 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V1 non è  diverso da  commento: {56,} 2 o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co4
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V1 il valore 8
        
        
         commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C3_lista_L3 è disattivo, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V4 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V1 il valore 1
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  diverso da  /*56,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore SubClass_C3_contatore_Co4

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V1 il valore 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  diverso da  /*56,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'subclass_c3_restoreti_ti1_restore' è inattivo )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di (negazione di ((subclass_c3_variabile_v1)  è uguale a  (2))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c3_restoreti_ti1_restore' è inattivo )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_variabile_v1)  è uguale a  (2)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v1)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v1)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C3_lista_L3 è disattivo, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V4 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V1 il valore 1""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C3_lista_L3 è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c3_lista_l3' è inattivo""", [
                            ]),#0
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  diverso da  /*56,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore SubClass_C3_contatore_Co4
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V1 il valore 8
        if db((db((db((db(self.get_subclass_c3_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_variabile_v1() == 2, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c3_contatore_co4().incrementa()
        else:
            self.set_subclass_c3_variabile_v1(8)
        #  /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C3_lista_L3 è disattivo, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V4 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V1 il valore 1
        if db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[1].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3())), di_ctx.subs[1].subs[0]):
            self.set_subclass_c3_variabile_v4(True)
        else:
            self.set_subclass_c3_variabile_v1(1)
    
    # verify macros
    @srf_value_macro("macroSubclass_c3_macrove_m1")
    def macroSubclass_c3_macrove_m1(self, argomento_ave1, argomento_ave5, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,}  se l'argomento argomento_ave5 è  uguale a c180 commento: {39,} ,  commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è attivo, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True  commento: {34,} o  se il parametro SubClass_C3_parametro_P9 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  commento: {38,} o  se il contatore SubClass_C3_contatore_Co4 è  uguale a  commento: {53,} 113, Almeno una delle seguenti { 
         commento: {61,} commento: {37,}  se la variabile SubClass_C3_variabile_V2 è  maggiore di  commento: {54,} 1 commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
         commento: {62,} commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  diverso da AC commento: {36,} o  se il timer SubClass_C3_timer_T1 è disattivo commento: {34,} o  se il parametro SubClass_C3_parametro_P1 è  uguale a  commento: {53,} 8, Almeno una delle seguenti { 
         commento: {62,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {35,} e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
         commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {36,} e  se il timer SubClass_C3_timer_T1 non è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
         commento: {62,} commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC commento: {34,} e  se il parametro SubClass_C3_parametro_P1 è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  commento: {54,} 10 commento: {35,} o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento commento: {36,} o  se il timer SubClass_C3_timer_T1 non è scaduto commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
         commento: {62,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  commento: {53,}  state1  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
         commento: {62,} commento: {37,}  se la variabile SubClass_C3_variabile_V1 non è  minore di  commento: {55,} 1 commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  commento: {36,} o  se il timer SubClass_C3_timer_T1 non è scaduto commento: {34,} o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  commento: {54,} 4 commento: {34,} e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  commento: {56,} 3, Almeno una delle seguenti { 
         commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  commento: {56,} 12 commento: {37,} e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
         commento: {62,} commento: {36,}  se il timer SubClass_C3_timer_T1 è scaduto commento: {37,} o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  commento: {53,} 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 commento: {39,} , Almeno una delle seguenti { 
         commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a c270x commento: {38,} e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  commento: {56,} 1354, Almeno una delle seguenti { 
         commento: {62,}  se l'argomento argomento_ave5 non  è  uguale a c180 commento: {39,}  commento: {37,} e  se la variabile SubClass_C3_variabile_V2 è  uguale a  commento: {53,} 2 commento: {38,} e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  commento: {56,} 1503 commento: {37,} e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
          se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  commento: {40,}  commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  commento: {36,} e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   commento: {47,49,50,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co4 sia  uguale a  commento: {53,} 11
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T2 sia scaduto
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  commento: {54,} 6
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  uguale a  commento: {53,} 10
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  minore di  commento: {55,} 1121
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  uguale a  commento: {53,} 5
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V2 sia  uguale a  commento: {53,} 5
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  commento: {56,} 135
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 
        
        
         } Verifica che   commento: {49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  commento: {54,} 12
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T1 non sia scaduto
        
        
         } Verifica che   commento: {47,49,52,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  maggiore di  commento: {54,} 4
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T2 sia scaduto
         commento: {104,} e  che   l'argomento argomento_ave1 sia  diverso da spento commento: {,} 
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T1 non sia scaduto
        
        
         } Verifica che   commento: {48,51,52,}   l'argomento argomento_ave5 sia  diverso da c180 commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co4 non sia  minore di  commento: {55,} 12
         commento: {104,} e  che   l'argomento argomento_ave1 non  sia  diverso da spento commento: {39,} 
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 1515
        
        
         } Verifica che   commento: {48,50,}  commento: {,}  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  commento: {54,} 5
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C3_variabile_V1 non sia  uguale a  commento: {53,} 10
        
        
         } Verifica che   commento: {48,49,50,52,}   l'argomento argomento_ave5 sia  uguale a c180 commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V2 non sia  uguale a  commento: {53,} 10
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T2 non sia scaduto
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V1 sia  uguale a  commento: {53,} 9
        
        
         } Verifica che   commento: {48,51,52,}   l'argomento argomento_ave5 non  sia  diverso da c180 commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave5 non  sia  diverso da c180 commento: {39,} 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
         commento: {104,} o  che   l'argomento argomento_ave5 sia  uguale a c180 commento: {39,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  commento: {56,} 154
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C3_contatore_Co4 sia  minore di  commento: {55,} 1
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il timer SubClass_C3_timer_T1 sia scaduto
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T2 non sia scaduto
        
        
         } Verifica che   commento: {49,51,}  commento: {,}  il timer SubClass_C3_timer_T2 non sia disattivo
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  minore di  commento: {55,} 1
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T1 non sia disattivo
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se l'argomento argomento_ave5 è  uguale a c180 /*39,*/ ,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co4 è  uguale a  /*53,*/ 113, Almeno una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V2 è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,49,*/  /*,*/  il timer SubClass_C3_timer_T1 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se l'argomento argomento_ave5 è  uguale a c180 /*39,*/ ,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co4 è  uguale a  /*53,*/ 113, Almeno una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V2 è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,49,*/  /*,*/  il timer SubClass_C3_timer_T1 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se l'argomento argomento_ave5 è  uguale a c180 /*39,*/ ,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co4 è  uguale a  /*53,*/ 113""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se l'argomento argomento_ave5 è  uguale a c180 /*39,*/ ,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se l'argomento argomento_ave5 è  uguale a c180 /*39,*/ ,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave5 è  uguale a c180""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (True))) allora (il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c3_lista_l3' è attivo)""", [
                            DIBoolExpr("""Operatore Logico Not\n/*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c3_lista_l3' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C3_parametro_P9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C3_parametro_P9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 non è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P9 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C3_contatore_Co4 è  uguale a  /*53,*/ 113""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V2 è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,49,*/  /*,*/  il timer SubClass_C3_timer_T1 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V2 è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,49,*/  /*,*/  il timer SubClass_C3_timer_T1 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V2 è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  diverso da  True""", [
                            DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C3_variabile_V2 è  maggiore di  /*54,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C7 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,49,*/  /*,*/  il timer SubClass_C3_timer_T1 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC /*36,*/ o  se il timer SubClass_C3_timer_T1 è disattivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T1 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C3_parametro_P1 è  uguale a  /*53,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento, Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ e  se il controllo SubClass_C3_controllo_C1 non è  uguale a spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C1 non è  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c1)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C3_timer_T1 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180 /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C3_restoreva_RV2 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv2_restore)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C4 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True , Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10 /*35,*/ o  se il controllo SubClass_C3_controllo_C6 non è  uguale a spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P1 è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V2 non è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v2)  è maggiore di  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C6 non è  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C3_parametro_P9 è  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3, Almeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v1)  è minore di  (1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C7 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V1 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v1)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P1 non è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 } Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True , Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 è  uguale a  True""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (12)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V4 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 } Verifica che   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T1 è scaduto /*37,*/ o  se la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T1 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5 e  se l'argomento argomento_ave5 non  è  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V1 non è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v1)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave5 non  è  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 } Verifica che   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co4 non è  diverso da  /*56,*/ 1354""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co4)  è uguale a  (1354))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co4)  è uguale a  (1354)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo, Almeno una delle seguenti { 
  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503 /*37,*/ e  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se l'argomento argomento_ave5 non  è  uguale a c180 /*39,*/  /*37,*/ e  se la variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave5 non  è  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V2 è  uguale a  /*53,*/ 2""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co4 è  diverso da  /*56,*/ 1503""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co4)  è uguale a  (1503)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V4 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C7 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C7 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto, Verifica che   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nla macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a RossoVerde ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a RossoVerde ,argomento_a3   uguale a spento ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a spento )   è  uguale a  True""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c3_macrova_m5'"""),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T2 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 sia  uguale a  /*53,*/ 11""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P9 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v3)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 10""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  minore di  /*55,*/ 1121""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co2)  è minore di  (1121)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  uguale a  /*53,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C3_variabile_V2 sia  uguale a  /*53,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 135""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co4)  è uguale a  (135))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co4)  è uguale a  (135)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  maggiore di  /*54,*/ 12""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co2)  è maggiore di  (12)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C3_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da spento""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C3_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,52,*/   l'argomento argomento_ave5 sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co4)  è minore di  (12)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 non  sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave1)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 1515""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co2)  è uguale a  (1515))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (1515)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v1)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v1)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180 /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,50,52,*/   l'argomento argomento_ave5 sia  uguale a c180""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V2 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C6 non sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V1 sia  uguale a  /*53,*/ 9""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,52,*/   l'argomento argomento_ave5 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave5)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave5 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave5)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave5 sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154""", [
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave5 sia  uguale a c180""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  diverso da  /*56,*/ 154""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co4)  è uguale a  (154))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co4)  è uguale a  (154)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore SubClass_C3_contatore_Co4 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/  /*,*/  il timer SubClass_C3_timer_T1 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,*/  /*,*/  il timer SubClass_C3_timer_T1 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,51,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 non sia disattivo""", [
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C3_timer_T1 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c3_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_contatore_co4().get_valore() == 113, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c3_variabile_v2() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_parametro_p1() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c1() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_subclass_c3_restoreva_rv2_restore() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p1() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v2() > 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(self.get_subclass_c3_variabile_v1() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v1() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p1() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() == 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v1() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_contatore_co4().get_valore() == 1354, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v2() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co4().get_valore() == 1503, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(db(self.macroSubclass_c3_macrova_m5(GlobalEnumeration.avanzamento,GlobalEnumeration.spento,GlobalEnumeration.rossoverde,GlobalEnumeration.spento,GlobalEnumeration.avanzamento,GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_subclass_c3_contatore_co4().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c3_variabile_v3() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c3_parametro_p1() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db((db(not db(self.get_subclass_c3_contatore_co2().get_valore() < 1121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_parametro_p1() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v2() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_contatore_co4().get_valore() == 135, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c3_controllo_c4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(not db(self.get_subclass_c3_contatore_co2().get_valore() > 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c3_parametro_p1() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave1 == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co4().get_valore() < 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave1 == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_controllo_c4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 1515, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(not db(self.get_subclass_c3_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v1() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c3_variabile_v1() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v2() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c3_controllo_c4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c3_variabile_v1() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(not db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(argomento_ave5 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_contatore_co4().get_valore() == 154, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c3_contatore_co4().get_valore() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c3_controllo_c4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_subclass_c3_timer_t2().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c3_contatore_co2().get_valore() < 1, di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t1().isDisattivato(), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m10")
    def macroSubclass_c3_macrove_m10(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  diverso da  True , Tutte le seguenti { 
         commento: {61,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  commento: {54,} 155 commento: {34,} o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False , Tutte le seguenti { 
         commento: {63,}  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  commento: {40,}  o  se l'argomento argomento_ave4 è  uguale a c180 commento: {39,}  commento: {36,} o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  commento: {39,}  e  se l'argomento argomento_ave9 non  è  uguale a  False  commento: {39,}  commento: {35,} o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
         commento: {36,}  se il timer SubClass_C3_timer_T2 non è disattivo commento: {36,} e  se il timer SubClass_C3_timer_T1 è attivo commento: {36,} o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   commento: {47,49,52,}  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T2 non sia attivo
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
         commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {,} 
        
        
         } Verifica che   commento: {47,48,52,}  commento: {,}  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
         commento: {104,} o  che   l'argomento argomento_ave9 non  sia  diverso da  True  commento: {,} 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C4 non sia  uguale a  False 
        
        
         } Verifica che   commento: {52,}   l'argomento argomento_ave9 non  sia  diverso da  False  commento: {,} 
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  diverso da  True , Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 155 /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False  /*39,*/  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  uguale a  False 


 } Verifica che   /*52,*/   l'argomento argomento_ave9 non  sia  diverso da  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  diverso da  True , Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 155 /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False  /*39,*/  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  uguale a  False 


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C3_restoreva_RV1 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv1_restore)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 155 /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False  /*39,*/  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  uguale a  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 155 /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False  /*39,*/  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 155 /*34,*/ o  se il parametro SubClass_C3_parametro_P9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 155""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 155""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C3_parametro_P9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C3_parametro_P9 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C7 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False  /*39,*/  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False  /*39,*/  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False , Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False  /*39,*/  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo o  se l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180 /*39,*/  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True  /*40,*/  o  se l'argomento argomento_ave4 è  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\nla macro  SubClass_C3_macrova_M5 ( con argomento_a4   uguale a spento ,argomento_a8   uguale a avanzamento ,argomento_a9   uguale a spento ,argomento_a3   uguale a RossoGiallox ,argomento_a2   uguale a avanzamento  e argomento_a6   uguale a RossoGiallox )   è  uguale a  True""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c3_macrova_m5'"""),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave4 è  uguale a c180""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave3 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave9 non  è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave3 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave9 non  è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C4 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo, Verifica che   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T1 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T1 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T2 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,52,*/  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C3_timer_T2 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave9 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C4 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*52,*/   l'argomento argomento_ave9 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_subclass_c3_restoreva_rv1_restore() == True, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co2().get_valore() > 155, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c3_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(db(self.macroSubclass_c3_macrova_m5(GlobalEnumeration.avanzamento,GlobalEnumeration.rossogiallox,GlobalEnumeration.spento,GlobalEnumeration.rossogiallox,GlobalEnumeration.avanzamento,GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave4 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(argomento_ave3 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave9 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(self.get_subclass_c3_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(not db(self.get_subclass_c3_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(argomento_ave1 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_subclass_c3_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(argomento_ave9 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_controllo_c4() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(not db(argomento_ave9 == False, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m4")
    def macroSubclass_c3_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  diverso da c270x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da c270x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da c270x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da c270x o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da c270x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C7 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m6")
    def macroSubclass_c3_macrove_m6(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  commento: {36,} o  se il timer SubClass_C3_timer_T2 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T1 non è disattivo commento: {37,} e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  commento: {54,} 1, Solo una delle seguenti { 
         commento: {62,} commento: {36,}  se il timer SubClass_C3_timer_T2 non è scaduto commento: {34,} e  se il parametro SubClass_C3_parametro_P1 è  minore di  commento: {55,} 5, Almeno una delle seguenti { 
         commento: {35,}  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  commento: {42,}  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  diverso da AC, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C6 del campo  MainClass_C1     commento: {105,} è  diverso da AC commento: {36,} e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  minore di  commento: {55,} 1
        
        
         } Verifica che   commento: {47,50,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 non sia  diverso da  commento: {56,} 3
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V1 non sia  minore di  commento: {55,} 3
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 non sia  uguale a  commento: {53,} 2
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T1 non sia attivo
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V1 non sia  uguale a  commento: {53,} 8
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C4 sia  uguale a  False 
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è disattivo /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  minore di  /*55,*/ 5, Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  minore di  /*55,*/ 3


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia attivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è disattivo /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  minore di  /*55,*/ 5, Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T1 non è disattivo /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L3 è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T2 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C3_timer_T1 non è disattivo /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T1 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v3)  è maggiore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  minore di  /*55,*/ 5, Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  minore di  /*55,*/ 5, Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P1 è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C3_parametro_P1 è  minore di  /*55,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC /*36,*/ e  se il timer SubClass_C3_timer_T1 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C6 è  uguale a spento,  /*42,*/  se  MainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C6 è  uguale a spento""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_controllo_C6 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_controllo_c6 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac))) allora (negazione di ((mainclass_c1_controllo_c6 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac)))""", [
                            DIBoolExpr("""Operatore Logico Not\n/*42,*/    MainClass_C1_controllo_C6 del campo  MainClass_C1     /*105,*/ è  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T1 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v1)  è minore di  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia attivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T1 non sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  uguale a  /*53,*/ 2""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C3_timer_T1 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V1 non sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v1)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C3_controllo_C4 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v3() > 1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db(not db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_parametro_p1() < 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db((db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c3_parametro_p1() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db(not db(not db(self.get_subclass_c3_parametro_p1() == 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v1() < 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(self.get_subclass_c3_parametro_p1() == 2, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t1().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v1() == 8, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c3_controllo_c4() == False, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m7")
    def macroSubclass_c3_macrove_m7(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} o  se il timer SubClass_C3_timer_T1 non è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True , Solo una delle seguenti { 
         commento: {62,} commento: {36,}  se il timer SubClass_C3_timer_T2 non è disattivo,  commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  diverso da AC, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V1 non è  minore di  commento: {55,} 1 commento: {38,} o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  commento: {53,} 114, Almeno una delle seguenti { 
         commento: {63,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {37,} o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  commento: {35,} o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {38,} o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  commento: {54,} 13, Verifica che   commento: {48,49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  commento: {54,} 1
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T2 sia disattivo
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C3_contatore_Co4 non sia  minore di  commento: {55,} 15
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C3_timer_T2 sia attivo
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,49,50,51,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 sia  maggiore di  commento: {54,} 7
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T2 sia scaduto
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  diverso da  commento: {56,} 13
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T1 sia disattivo
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V3 non sia  minore di  commento: {55,} 4
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo,  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 114, Almeno una delle seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13, Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 sia disattivo


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True , Solo una delle seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo,  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 114, Almeno una delle seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13, Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ o  se il timer SubClass_C3_timer_T1 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C4 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V4 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo,  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 114, Almeno una delle seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13, Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo,  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 114, Almeno una delle seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13, Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo,  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 114""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo,  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer SubClass_C3_timer_T2 non è disattivo,  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  diverso da AC, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (False)) allora (negazione di ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac)))""", [
                            DIBoolExpr("""EqualImpl\n/*44,*/    MainClass_C1_variabile_V5 del campo  MainClass_C1     è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c3_lista_l3)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V1 non è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v1)  è minore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 114""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (114)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13, Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13, Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C4 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V4 non è  uguale a  False""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V4 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C4 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13, Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*38,*/ o  se il contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C3_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C3_contatore_Co2 è  maggiore di  /*54,*/ 13""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co4 non sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co4)  è maggiore di  (1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T2 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C3_contatore_Co4 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co4)  è minore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T2 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V4 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 sia  maggiore di  /*54,*/ 7""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T2 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T1 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C3_timer_T1 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v3)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c4() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(self.get_subclass_c3_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v1() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 114, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_controllo_c4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c3_contatore_co2().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_subclass_c3_contatore_co4().get_valore() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c3_contatore_co4().get_valore() < 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(self.get_subclass_c3_parametro_p1() > 7, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c3_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v3() < 4, di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c3_macrova_m5")
    def macroSubclass_c3_macrova_m5(self, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c3_macrova_m5_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c3_macrova_m9")
    def macroSubclass_c3_macrova_m9(self, argomento_a10, argomento_a5, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  maggiore di  commento: {54,} 7 commento: {109,} o  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  minore di  commento: {55,} 1 commento: {34,} e  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore RossoGialloVerde
        
         commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  maggiore di  /*54,*/ 7 /*109,*/ o  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  minore di  /*55,*/ 1 /*34,*/ e  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  maggiore di  /*54,*/ 7 /*109,*/ o  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  minore di  /*55,*/ 1 /*34,*/ e  se lo stato  è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_restoreva_rv4_restore)  è maggiore di  (7))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_restoreva_rv4_restore)  è maggiore di  (7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_restoreva_rv4_restore)  è minore di  (1)) )  e  
( (lo stato di 'self')  è uguale a  (state1) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_restoreva_rv4_restore)  è minore di  (1))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_restoreva_rv4_restore)  è minore di  (1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  maggiore di  /*54,*/ 7 /*109,*/ o  se il ripristino della variabile  SubClass_C3_restoreva_RV4 non è  minore di  /*55,*/ 1 /*34,*/ e  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore RossoGialloVerde
        if db((db(not db(self.get_subclass_c3_restoreva_rv4_restore() > 7, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_restoreva_rv4_restore() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogialloverde
        #  /*46,*/ assegna alla macro il valore RossoGialloVerde
        return GlobalEnumeration.rossogialloverde
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c3_command_comm10DaSender99fab08d(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c3_command_comm10DaSender99fab08d')
    
    def eventSubclass_c3_command_comm6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c3_command_comm6')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c3_previousco_c2_prev(self.get_subclass_c3_previousco_c2())
        self.set_subclass_c3_previousco_c3_prev(self.get_subclass_c3_previousco_c3())
        self.set_subclass_c3_previousco_c5_prev(self.get_subclass_c3_previousco_c5())
        self.set_subclass_c3_previousco_c8_prev(self.get_subclass_c3_previousco_c8())
        self.set_subclass_c3_previousco_c9_prev(self.get_subclass_c3_previousco_c9())
        self.set_subclass_c3_previousva_pv1_prev(self.get_subclass_c3_previousva_pv1())
        self.set_subclass_c3_previousva_pv2_prev(self.get_subclass_c3_previousva_pv2())
        self.set_subclass_c3_previousva_pv3_prev(self.get_subclass_c3_previousva_pv3())
        self.set_subclass_c3_previousva_pv4_prev(self.get_subclass_c3_previousva_pv4())

class SubClass_C3_RecordHeaderR3(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled12, recordfiled18):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled12(recordfiled12)
        self.set_recordfiled18(recordfiled18)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled12(self, recordfiled12):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"), recordfiled12)

    def set_recordfiled18(self, recordfiled18):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"), recordfiled18)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled12(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"))

    def get_recordfiled18(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"))



class SubClass_C3_RecordHeaderR6(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled11, recordfiled2, recordfiled20, recordfiled16):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled11(recordfiled11)
        self.set_recordfiled2(recordfiled2)
        self.set_recordfiled20(recordfiled20)
        self.set_recordfiled16(recordfiled16)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled11(self, recordfiled11):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"), recordfiled11)

    def set_recordfiled2(self, recordfiled2):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"), recordfiled2)

    def set_recordfiled20(self, recordfiled20):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"), recordfiled20)

    def set_recordfiled16(self, recordfiled16):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled16"), recordfiled16)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled11(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"))

    def get_recordfiled2(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"))

    def get_recordfiled20(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"))

    def get_recordfiled16(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled16"))



