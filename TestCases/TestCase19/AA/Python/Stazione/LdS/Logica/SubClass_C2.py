# Codice del modello 'TestCase19', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_subclass_c2_previousva_pv1(0)
        self.set_subclass_c2_previousva_pv2(GlobalEnumeration.rossogiallogiallo)
        self.set_subclass_c2_previousva_pv3(0)
        self.set_subclass_c2_previousva_pv4(GlobalEnumeration.giallogiallo)
        self.set_subclass_c2_previousva_pv5(0)
        self.set_subclass_c2_restoreva_rv1(GlobalEnumeration.giallox)
        self.set_subclass_c2_restoreva_rv2(0)
        self.set_subclass_c2_variabile_v7(GlobalEnumeration.rossogiallogiallo)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5 : set(['eventSubclass_c2_command_comm3DaSender855df2bd',]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
        if self.is_triggered('eventSubclass_c2_command_comm1DaSender7ee42824'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm1DaSender7ee42824',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm1DaSender7ee42824',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c2_command_comm2'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm2',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm2',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c2_command_comm3DaSender855df2bd'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm3DaSender855df2bd',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm3DaSender855df2bd',self.ManCmdResponse.NOOP)


        if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5):
        # for each manual command that can be received in Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5
            if self.is_triggered('eventSubclass_c2_command_comm3DaSender855df2bd'):
                self.set_man_cmd_response('eventSubclass_c2_command_comm3DaSender855df2bd',self.ManCmdResponse.BLOCKED)

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
        _State1__State5__stateSheet_0__nominalActuation__transitionTo_0 = 2
        _State5__State5__stateSheet_1__permanence = 3

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c2_lista_l10, subclass_c2_lista_l2, subclass_c2_lista_l5, subclass_c2_parametro_p4, subclass_c2_parametro_p6, subclass_c2_parametro_p7, subclass_c2_parametro_p8):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l10(subclass_c2_lista_l10)
        self.set_subclass_c2_lista_l2(subclass_c2_lista_l2)
        self.set_subclass_c2_lista_l5(subclass_c2_lista_l5)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p4(subclass_c2_parametro_p4)
        self.set_subclass_c2_parametro_p6(subclass_c2_parametro_p6)
        self.set_subclass_c2_parametro_p7(subclass_c2_parametro_p7)
        self.set_subclass_c2_parametro_p8(subclass_c2_parametro_p8)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(204000)
        self.set_subclass_c2_restoreti_ti1_restore(204000)
        self.set_subclass_c2_restoreti_ti2(45000)
        self.set_subclass_c2_restoreti_ti2_restore(45000)
        self.set_subclass_c2_restoreti_ti3(1000)
        self.set_subclass_c2_restoreti_ti3_restore(1000)
        self.set_subclass_c2_restoreti_ti4(332000)
        self.set_subclass_c2_restoreti_ti4_restore(332000)
        self.set_subclass_c2_timer_t10(5000)
        self.set_subclass_c2_timer_t5(2000)
        self.set_subclass_c2_timer_t6(410000)
        self.set_subclass_c2_timer_t8(121000)
        self.set_subclass_c2_timer_t9(4453000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_restoreti_ti3,self.subclass_c2_restoreti_ti3_restore,self.subclass_c2_restoreti_ti4,self.subclass_c2_restoreti_ti4_restore,self.subclass_c2_timer_t10,self.subclass_c2_timer_t5,self.subclass_c2_timer_t6,self.subclass_c2_timer_t8,self.subclass_c2_timer_t9,]

        # initialize the counters
        self.set_subclass_c2_contatore_co4(0)
        self.set_subclass_c2_contatore_co8(0)
        self.set_subclass_c2_contatore_co9(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l10(self, subclass_c2_lista_l10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10",subclass_c2_lista_l10)

    def set_subclass_c2_lista_l2(self, subclass_c2_lista_l2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2",subclass_c2_lista_l2)

    def set_subclass_c2_lista_l5(self, subclass_c2_lista_l5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l5",subclass_c2_lista_l5)


    # getters for record type parameters
    def get_subclass_c2_lista_l10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10")

    def get_subclass_c2_lista_l2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2")

    def get_subclass_c2_lista_l5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l5")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p4(self, subclass_c2_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4",subclass_c2_parametro_p4)

    def set_subclass_c2_parametro_p6(self, subclass_c2_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6",subclass_c2_parametro_p6)

    def set_subclass_c2_parametro_p7(self, subclass_c2_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7",subclass_c2_parametro_p7)

    def set_subclass_c2_parametro_p8(self, subclass_c2_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p8",subclass_c2_parametro_p8)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4")

    def get_subclass_c2_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6")

    def get_subclass_c2_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7")

    def get_subclass_c2_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p8")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c10(self, subclass_c2_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c10",subclass_c2_comando_c10)

    def set_subclass_c2_comando_c6(self, subclass_c2_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c6",subclass_c2_comando_c6)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c1")

    def get_subclass_c2_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c7")

    def get_subclass_c2_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c8")

    def get_subclass_c2_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c2")

    def get_subclass_c2_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c3")

    def get_subclass_c2_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4")

    def get_subclass_c2_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5")

    def get_subclass_c2_previousco_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c9")


    # setters for state variables
    def set_subclass_c2_previousco_c2_prev(self, subclass_c2_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c2_prev",subclass_c2_previousco_c2_prev)
    def set_subclass_c2_previousco_c3_prev(self, subclass_c2_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c3_prev",subclass_c2_previousco_c3_prev)
    def set_subclass_c2_previousco_c4_prev(self, subclass_c2_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev",subclass_c2_previousco_c4_prev)
    def set_subclass_c2_previousco_c5_prev(self, subclass_c2_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev",subclass_c2_previousco_c5_prev)
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
    def set_subclass_c2_variabile_v7(self, subclass_c2_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7",subclass_c2_variabile_v7)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c2_prev")

    def get_subclass_c2_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c3_prev")

    def get_subclass_c2_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev")

    def get_subclass_c2_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev")

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

    def get_subclass_c2_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_restoreti_ti2(self, timerDuration):
        self.subclass_c2_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2", self.memory)

    def set_subclass_c2_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2_restore", self.memory)

    def set_subclass_c2_restoreti_ti3(self, timerDuration):
        self.subclass_c2_restoreti_ti3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti3", self.memory)

    def set_subclass_c2_restoreti_ti3_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti3_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti3_restore", self.memory)

    def set_subclass_c2_restoreti_ti4(self, timerDuration):
        self.subclass_c2_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti4", self.memory)

    def set_subclass_c2_restoreti_ti4_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti4_restore", self.memory)

    def set_subclass_c2_timer_t10(self, timerDuration):
        self.subclass_c2_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t10", self.memory)

    def set_subclass_c2_timer_t5(self, timerDuration):
        self.subclass_c2_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t5", self.memory)

    def set_subclass_c2_timer_t6(self, timerDuration):
        self.subclass_c2_timer_t6 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t6", self.memory)

    def set_subclass_c2_timer_t8(self, timerDuration):
        self.subclass_c2_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t8", self.memory)

    def set_subclass_c2_timer_t9(self, timerDuration):
        self.subclass_c2_timer_t9 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t9", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_restoreti_ti2(self):
        return self.subclass_c2_restoreti_ti2

    def get_subclass_c2_restoreti_ti2_restore(self):
        return self.subclass_c2_restoreti_ti2_restore

    def get_subclass_c2_restoreti_ti3(self):
        return self.subclass_c2_restoreti_ti3

    def get_subclass_c2_restoreti_ti3_restore(self):
        return self.subclass_c2_restoreti_ti3_restore

    def get_subclass_c2_restoreti_ti4(self):
        return self.subclass_c2_restoreti_ti4

    def get_subclass_c2_restoreti_ti4_restore(self):
        return self.subclass_c2_restoreti_ti4_restore

    def get_subclass_c2_timer_t10(self):
        return self.subclass_c2_timer_t10

    def get_subclass_c2_timer_t5(self):
        return self.subclass_c2_timer_t5

    def get_subclass_c2_timer_t6(self):
        return self.subclass_c2_timer_t6

    def get_subclass_c2_timer_t8(self):
        return self.subclass_c2_timer_t8

    def get_subclass_c2_timer_t9(self):
        return self.subclass_c2_timer_t9


    # setters for counters
    def set_subclass_c2_contatore_co4(self, counterInitValue):
        self.subclass_c2_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co4", self.memory)

    def set_subclass_c2_contatore_co8(self, counterInitValue):
        self.subclass_c2_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co8", self.memory)

    def set_subclass_c2_contatore_co9(self, counterInitValue):
        self.subclass_c2_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co9", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co4(self):
        return self.subclass_c2_contatore_co4

    def get_subclass_c2_contatore_co8(self):
        return self.subclass_c2_contatore_co8

    def get_subclass_c2_contatore_co9(self):
        return self.subclass_c2_contatore_co9



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1545 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P7 è  uguale a  True , Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 13, Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a c270""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1545 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P7 è  uguale a  True , Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 13, Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1545 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P7 è  uguale a  True""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1545 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P7 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1545 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270""", [
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 1545""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da c270""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P7 è  uguale a  True""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 13, Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 13, Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T6 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co9)  è uguale a  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 non è  diverso da c270""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153 /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 non è  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 153""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co8)  è maggiore di  (153)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co9 è  uguale a  /*53,*/ 13210""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (rossogialloverde))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 11""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da c270""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C1 è  uguale a c270""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  uguale a c270""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  /*54,*/ 13""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co9)  è maggiore di  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a c270""", [
                    ]),#1
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\n/*86,*/  Almeno una delle seguenti {
 /*82,*/  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   /*76,*/
 /*82,*/  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   /*76,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   /*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 11210


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T6 sia attivo


}
}""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*86,*/  Almeno una delle seguenti {
 /*82,*/  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   /*76,*/
 /*82,*/  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   /*76,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   /*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 11210


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T6 sia attivo


}
}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   SubClass_C2_command_comm3 da  Sender855df2bd"""),#0
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   SubClass_C2_command_comm3 da  Sender855df2bd"""),#1
                    DIBoolExpr("""NAryLogicOP (AND)\n/*76,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   /*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 11210


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T6 sia attivo


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   SubClass_C2_command_comm3 da  Sender855df2bd"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 11210


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*76,*/
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 non è  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 non è  diverso da c270""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C1 è  diverso da c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 è  diverso da c270""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (rossogialloverde))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 11210


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1545""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co9)  è uguale a  (1545)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T10 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co4 non è  minore di  /*55,*/ 123""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co4)  è minore di  (123)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 11210""", [
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T6 sia attivo""", [
                    ]),#2
                    ]),#2
                    ]),#0
                    ]),#3
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L5
 di eseguire  /*113,*/  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm7 del campo mainclass_c1 della lista subclass_c2_lista_l5'""", [
                    ]),#0
                    ]),#4
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L10
 di eseguire  /*113,*/  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm7 del campo mainclass_c1 della lista subclass_c2_lista_l10'""", [
                    ]),#0
                    ]),#5
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L2
 di eseguire  /*113,*/  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm7 del campo mainclass_c1 della lista subclass_c2_lista_l2'""", [
                    ]),#0
                    ]),#6
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[6], ),
                         phase = TransPhase.Manuale
                         ),
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[5], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[4], ),
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

        self.set_subclass_c2_previousco_c2_prev(True)
        self.set_subclass_c2_previousco_c3_prev(False)
        self.set_subclass_c2_previousco_c4_prev(True)
        self.set_subclass_c2_previousco_c5_prev(GlobalEnumeration.avvio)
        self.set_subclass_c2_previousco_c9_prev(False)
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
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5):
                if(self.guard_PERMANENCE_state5_000()):
                    self.curr_transition = self.Transition._State5__State5__stateSheet_1__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                if(self.guard_NOMINAL_ACTUATION_state1_state5_000()):
                    self.curr_transition = self.Transition._State1__State5__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5):
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
        elif self.curr_transition == self.Transition._State1__State5__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5)
            self.effect_NOMINAL_ACTUATION_state1_state5_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State5__stateSheet_1__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state5)
            self.effect_PERMANENCE_state5_000()
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
        
         Nessuna  commento: {80,}
        }
        """
        return db((True), self.dbs[1])
    
    def guard_NOMINAL_ACTUATION_state1_state5_000(self):
        """
        CNL corrispondente:
         {  commento: {69,} commento: {37,}  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 1545 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 commento: {34,} e  se il parametro SubClass_C2_parametro_P7 è  uguale a  True , Solo una delle seguenti { 
         commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde commento: {36,} o  se il timer SubClass_C2_timer_T6 è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 13 commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  commento: {53,} 13, Solo una delle seguenti { 
         commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 153 commento: {38,} e  se il contatore SubClass_C2_contatore_Co9 è  uguale a  commento: {53,} 13210 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  uguale a RossoGialloVerde commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Almeno una delle seguenti { 
         commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C7 non è  diverso da RossoGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  diverso da RossoGiallo commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 è  minore di  commento: {55,} 11, Tutte le seguenti { 
         commento: {69,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270, Solo una delle seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  uguale a c270 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 3, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a  True 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co9 non sia  maggiore di  commento: {54,} 13
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a  False 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a c270
        
         }
        """
        return db((db(not db((db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, self.dbs[2].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_contatore_co4().get_valore() == 1545, self.dbs[2].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, self.dbs[2].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[2].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p7() == True, self.dbs[2].subs[0].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[0]) or db((((db(not db((db((db((db((db(self.get_consdef() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t6().isAttivato(), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co9().get_valore() == 13, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 13, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(not db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db((db(not db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co8().get_valore() > 153, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co9().get_valore() == 13210, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloverde, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(not db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.rossogiallo, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.rossogiallo, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co9().get_valore() < 11, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(not db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() > 3, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co9().get_valore() > 13, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[2].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0])) + (db(self.get_consdef() == False, self.dbs[2].subs[0].subs[1].subs[1]))) == 1), self.dbs[2].subs[0].subs[1]), self.dbs[2].subs[0]) and db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, self.dbs[2].subs[1])), self.dbs[2])
    
    def guard_PERMANENCE_state5_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {86,}  Almeno una delle seguenti {
         commento: {82,}  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   commento: {76,}
         commento: {82,}  Ricezione del comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   commento: {76,}
         commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   SubClass_C2_command_comm3 da  Sender855df2bd   commento: {76,}
         commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {36,} e  se il timer SubClass_C2_timer_T9 non è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270 commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
         commento: {68,} commento: {38,}  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 1545 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True , Almeno una delle seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T8 non è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 non è  minore di  commento: {55,} 123 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  uguale a c270
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co9 sia  minore di  commento: {55,} 11210
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T6 sia attivo
        
        
        }
        }
        }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventSubclass_c2_command_comm3DaSender855df2bd'), self.dbs[3].subs[0].subs[2].subs[0]) and db(not db((db((db((db((db(not db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, self.dbs[3].subs[0].subs[2].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[0]) or db((db(not db((db(not db(self.get_subclass_c2_contatore_co9().get_valore() == 1545, self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(self.get_subclass_c2_timer_t10().isDisattivato(), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isAttivato(), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co4().get_valore() < 123, self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[1]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1]), self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co9().get_valore() < 11210, self.dbs[3].subs[0].subs[2].subs[1].subs[1].subs[1])), self.dbs[3].subs[0].subs[2].subs[1].subs[1]), self.dbs[3].subs[0].subs[2].subs[1]) and db(self.get_subclass_c2_timer_t6().isAttivato(), self.dbs[3].subs[0].subs[2].subs[2]))
        if (db(self.is_triggered('eventSubclass_c2_command_comm3DaSender855df2bd'), self.dbs[3].subs[0].subs[0]) or db(self.is_triggered('eventSubclass_c2_command_comm3DaSender855df2bd'), self.dbs[3].subs[0].subs[1]) or db(res_manCmdCondition_0, self.dbs[3].subs[0].subs[2])):
            self.set_man_cmd_response('eventSubclass_c2_command_comm3DaSender855df2bd',self.ManCmdResponse.PROCESSED)
        return db((db((db(self.is_triggered('eventSubclass_c2_command_comm3DaSender855df2bd'), self.dbs[3].subs[0].subs[0]) or db(self.is_triggered('eventSubclass_c2_command_comm3DaSender855df2bd'), self.dbs[3].subs[0].subs[1]) or db(res_manCmdCondition_0, self.dbs[3].subs[0].subs[2])), self.dbs[3].subs[0])), self.dbs[3])
    
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
        
        Comanda al campo MainClass_C1 di SubClass_C2_lista_L5
         di eseguire  commento: {113,}  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L5
        #   di eseguire  /*113,*/  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
        for idx, it in enumerate(self.get_subclass_c2_lista_l5()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm7(self,True,GlobalEnumeration.gialloverde)
    
    def effect_NOMINAL_ACTUATION_state1_state5_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L10
         di eseguire  commento: {113,}  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde ) }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L10
        #   di eseguire  /*113,*/  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
        for idx, it in enumerate(self.get_subclass_c2_lista_l10()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm7(self,True,GlobalEnumeration.gialloverde)
    
    def effect_PERMANENCE_state5_000(self):
        """
        CNL corrispondente:
        
        {
        
        Comanda al campo MainClass_C1 di SubClass_C2_lista_L2
         di eseguire  commento: {113,}  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L2
        #   di eseguire  /*113,*/  MainClass_C1_command_comm7( con argomento_ave1   uguale a True ,argomento_ave10   uguale a GialloVerde )
        for idx, it in enumerate(self.get_subclass_c2_lista_l2()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm7(self,True,GlobalEnumeration.gialloverde)
    
    # effect macros
    def macroSubclass_c2_macroef_m1(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {37,}  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co8
        
           
         commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  diverso da c270, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co8""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  /*37,*/  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co8
        if db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co8().incrementa()
        #  /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
        if db(not db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co4().decrementa()
        else:
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.rossogialloverde)
    
    def macroSubclass_c2_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  commento: {53,} 4 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True , commento: {69,}Disattiva il timer SubClass_C2_timer_T6
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True , /*69,*/Disattiva il timer SubClass_C2_timer_T6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (4))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (subclass_c2_controllo_c8)  è uguale a  (True) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True , /*69,*/Disattiva il timer SubClass_C2_timer_T6
        if db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t6().disattiva()
    
    def macroSubclass_c2_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  commento: {54,} 9 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloVerde, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co9
        
           
         commento: {34,}  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 9 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloVerde, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 9 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv2_restore)  è maggiore di  (9))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_restoreva_rv2_restore)  è maggiore di  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloverde)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_parametro_p7)  è uguale a  (False)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p7)  è uguale a  (False)) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 9 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  uguale a RossoGialloVerde, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co9
        if db((db(not db(self.get_subclass_c2_restoreva_rv2_restore() > 9, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co9().decrementa()
        #  /*34,*/  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a RossoGialloVerde, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
        if db((db((db((db(not db(self.get_subclass_c2_parametro_p7() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.rossogialloverde)
    
    def macroSubclass_c2_macroef_m5(self, argomento_af3, argomento_af7, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  o  se l'argomento argomento_af3 è  diverso da c270 commento: {39,} ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde commento: {67,}
        
           
         commento: {36,}  se il timer SubClass_C2_timer_T10 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  uguale a c270 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 non è  diverso da RossoGialloVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  minore di  commento: {55,} 1210 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co8
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore RossoGiallo
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  o  se l'argomento argomento_af3 è  diverso da c270 /*39,*/ ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  o  se l'argomento argomento_af3 è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))} )  e  
( negazione di ((subclass_c2_controllo_c8)  è uguale a  (False)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af3)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af3)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*67,*/

   
 /*36,*/  se il timer SubClass_C2_timer_T10 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  diverso da RossoGialloVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 1210 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co8

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/

   
 /*36,*/  se il timer SubClass_C2_timer_T10 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  diverso da RossoGialloVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 1210 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'subclass_c2_timer_t10' è attivo )  o  
( ( ( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  ( (subclass_c2_parametro_p6)  è uguale a  (c270) ) )  e  
( negazione di (negazione di ((subclass_c2_parametro_p4)  è uguale a  (rossogialloverde))) ) ) )  o  
( (subclass_c2_contatore_co8)  è minore di  (1210) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'subclass_c2_timer_t10' è attivo )  o  
( ( ( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  ( (subclass_c2_parametro_p6)  è uguale a  (c270) ) )  e  
( negazione di (negazione di ((subclass_c2_parametro_p4)  è uguale a  (rossogialloverde))) ) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  ( (subclass_c2_parametro_p6)  è uguale a  (c270) ) )  e  
( negazione di (negazione di ((subclass_c2_parametro_p4)  è uguale a  (rossogialloverde))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  ( (subclass_c2_parametro_p6)  è uguale a  (c270) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p4)  è uguale a  (rossogialloverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co8)  è minore di  (1210)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  o  se l'argomento argomento_af3 è  diverso da c270 /*39,*/ ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore RossoGialloVerde
        if db((db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(argomento_af3 == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.rossogialloverde)
        #  /*67,*/
        #     
        #   /*36,*/  se il timer SubClass_C2_timer_T10 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a c270 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 non è  diverso da RossoGialloVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 1210 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co8
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore RossoGiallo
        if db((db((db((db(self.get_subclass_c2_timer_t10().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co8().get_valore() < 1210, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c8() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co8().resetta()
        else:
            self.set_subclass_c2_comando_c6(GlobalEnumeration.rossogiallo)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m9")
    def macroSubclass_c2_macrove_m9(self, argomento_ave10, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {36,}  se il timer SubClass_C2_timer_T9 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 è  minore di  commento: {55,} 142 commento: {36,} o  se il timer SubClass_C2_timer_T10 è scaduto commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a c180, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  e  se l'argomento argomento_ave6 è  uguale a  False  commento: {39,}  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 commento: {34,} o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde commento: {36,} o  se il timer SubClass_C2_timer_T6 è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
         commento: {63,} commento: {43,}  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 7 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
         commento: {62,} commento: {35,}  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 1510, Almeno una delle seguenti { 
         commento: {63,}  se l'argomento argomento_ave5 non  è  uguale a avvio commento: {39,} ,  commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  uguale a c180x, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  commento: {56,} 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo commento: {39,}  commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 13 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 155, Solo una delle seguenti { 
         commento: {61,} commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 commento: {39,}  commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
         commento: {61,} commento: {37,}  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 commento: {39,}  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 commento: {36,} o  se il timer SubClass_C2_timer_T6 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  minore di  commento: {55,} 111, Tutte le seguenti { 
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co9 sia  minore di  commento: {55,} 1
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo
        
        
         } Verifica che   commento: {49,51,}  commento: {,}  il timer SubClass_C2_timer_T9 sia attivo
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 non sia  minore di  commento: {55,} 1232
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T6 sia scaduto
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde
        
        
         } Verifica che   commento: {51,52,}   l'argomento argomento_ave10 non  sia  diverso da c270 commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co9 sia  uguale a  commento: {53,} 1310
        
        
         } Verifica che   commento: {49,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co4 sia  minore di  commento: {55,} 154
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T6 sia disattivo
        
        
         } Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  diverso da  commento: {56,} 13
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il controllo SubClass_C2_controllo_C7 sia  uguale a RossoGiallo
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  uguale a  commento: {53,} 1153
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 142 /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
 /*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 } Verifica che   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T6 sia disattivo


 } Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 13


 } Verifica che   /*48,51,*/  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1153""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 142 /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
 /*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 } Verifica che   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T6 sia disattivo


 } Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 13


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 142 /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 142 /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 142""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co9 è  minore di  /*55,*/ 142""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T10 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
 /*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 } Verifica che   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T6 sia disattivo


 } Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 13


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
 /*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 } Verifica che   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T6 sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T6 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  e  se l'argomento argomento_ave6 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da c270,  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)) allora ((mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n/*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c180)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave6 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 non è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P4 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T6 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T6 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
 /*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 } Verifica che   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T6 sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270, Solo una delle seguenti { 
 /*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 } Verifica che   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 7""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 } Verifica che   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510, Almeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*35,*/  se il controllo SubClass_C2_controllo_C1 non è  uguale a c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 non è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C7 non è  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1510""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co9)  è uguale a  (1510)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144 o  se l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se l'argomento argomento_ave5 non  è  uguale a avvio /*39,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave5 non  è  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  uguale a c180x, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (144))) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c180x))""", [
                            DIBoolExpr("""Operatore Logico Not\n/*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  diverso da  /*56,*/ 144""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (144)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (c180x)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave8 è  diverso da RossoGiallo /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 è  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 155""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 } Verifica che   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde, Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde e  se l'argomento argomento_ave10 è  diverso da c270""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è  diverso da GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave10 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*36,*/ o  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270 /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde o  se l'argomento argomento_ave10 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave10 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C1 è  uguale a c270""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T6 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T6 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co8 è  minore di  /*55,*/ 111""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,51,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co4 non sia  minore di  /*55,*/ 1232""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co4)  è minore di  (1232)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C2_timer_T6 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270 /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*51,52,*/   l'argomento argomento_ave10 non  sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave10)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co9 sia  uguale a  /*53,*/ 1310""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T6 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154""", [
                            DIBoolExpr("""EqualImpl\nche   /*49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a RossoGialloVerde""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co4 sia  minore di  /*55,*/ 154""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T6 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a RossoGiallo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1153""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,51,*/  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a RossoGiallo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1153""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co9().get_valore() < 142, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db((db((db((db(not db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(argomento_ave6 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l5())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p8() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co9().get_valore() == 1510, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(argomento_ave5 == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_contatore_co7().get_valore() == 144, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(argomento_ave8 == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co4().get_valore() > 155, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave10 == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave10 == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co8().get_valore() < 111, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_contatore_co9().get_valore() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_subclass_c2_timer_t9().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co4().get_valore() < 1232, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(not db(not db(argomento_ave10 == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co9().get_valore() == 1310, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co4().get_valore() < 154, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db(not db(not db(self.get_subclass_c2_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co8().get_valore() == 1153, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m1")
    def macroSubclass_c2_macrova_m1(self, argomento_a1, argomento_a10, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se l'argomento argomento_a8 è  uguale a RossoGiallo commento: {39,}  commento: {111,} e  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  commento: {53,}  state1  commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  commento: {53,} 1345 commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se l'argomento argomento_a8 è  uguale a RossoGiallo /*39,*/  /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/  state1  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1345 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se l'argomento argomento_a8 è  uguale a RossoGiallo /*39,*/  /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/  state1  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1345 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (argomento_a8)  è uguale a  (rossogiallo) )  e  
( per ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))} ) )  o  
( negazione di ((subclass_c2_controllo_c8)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (argomento_a8)  è uguale a  (rossogiallo) )  e  
( per ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))} )""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a8)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co9)  è uguale a  (1345)) )  e  
( (subclass_c2_variabile_v7)  è uguale a  (rossogialloverde) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co9)  è uguale a  (1345))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co9)  è uguale a  (1345)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se l'argomento argomento_a8 è  uguale a RossoGiallo /*39,*/  /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/  state1  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co9 non è  uguale a  /*53,*/ 1345 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde , assegna alla macro il valore  False
        if db((db((db((db(argomento_a8 == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co9().get_valore() == 1345, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m10")
    def macroSubclass_c2_macrova_m10(self, argomento_a3, argomento_a4, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se la macro  SubClass_C2_macrova_M4 ( con argomento_a2   uguale a True ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a10   uguale a c120x ,argomento_a8   uguale a RossoGialloGiallo ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a GialloGiallo )  non  è  uguale a avvio commento: {40,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 8 commento: {110,} e  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo commento: {109,} e  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  minore di  commento: {55,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde commento: {45,} o  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  commento: {105,} è  minore di  commento: {55,} 141 , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se la macro  SubClass_C2_macrova_M4 ( con argomento_a2   uguale a True ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a10   uguale a c120x ,argomento_a8   uguale a RossoGialloGiallo ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a GialloGiallo )  non  è  uguale a avvio /*40,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 8 /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*109,*/ e  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde /*45,*/ o  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  minore di  /*55,*/ 141 , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se la macro  SubClass_C2_macrova_M4 ( con argomento_a2   uguale a True ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a10   uguale a c120x ,argomento_a8   uguale a RossoGialloGiallo ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a GialloGiallo )  non  è  uguale a avvio /*40,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 8 /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*109,*/ e  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde /*45,*/ o  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  minore di  /*55,*/ 141""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m4')  è uguale a  (avvio)) )  e  ( (subclass_c2_parametro_p8)  è uguale a  (8) ) )  e  ( il timer 'subclass_c2_restoreti_ti1_restore' è inattivo ) )  e  
( (subclass_c2_restoreva_rv2_restore)  è minore di  (1) ) )  o  
( (subclass_c2_variabile_v7)  è uguale a  (rossogialloverde) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m4')  è uguale a  (avvio)) )  e  ( (subclass_c2_parametro_p8)  è uguale a  (8) ) )  e  ( il timer 'subclass_c2_restoreti_ti1_restore' è inattivo ) )  e  
( (subclass_c2_restoreva_rv2_restore)  è minore di  (1) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m4')  è uguale a  (avvio)) )  e  ( (subclass_c2_parametro_p8)  è uguale a  (8) ) )  e  ( il timer 'subclass_c2_restoreti_ti1_restore' è inattivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m4')  è uguale a  (avvio)) )  e  ( (subclass_c2_parametro_p8)  è uguale a  (8) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m4')  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m4')  è uguale a  (avvio)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m4'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (8)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_restoreva_rv2_restore)  è minore di  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (rossogialloverde)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è minore di  (141))}""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l10)  è minore di  (141)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se la macro  SubClass_C2_macrova_M4 ( con argomento_a2   uguale a True ,argomento_a1   uguale a RossoGialloGiallo ,argomento_a10   uguale a c120x ,argomento_a8   uguale a RossoGialloGiallo ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a GialloGiallo )  non  è  uguale a avvio /*40,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 8 /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo /*109,*/ e  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  uguale a RossoGialloVerde /*45,*/ o  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L10 esiste e  /*105,*/ è  minore di  /*55,*/ 141 , assegna alla macro il valore  True
        if db((db((db((db((db((db(not db(db(self.macroSubclass_c2_macrova_m4(GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.c120x,True,GlobalEnumeration.rossogialloverde,GlobalEnumeration.giallogiallo,GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() == 8, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_restoreva_rv2_restore() < 1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() < 141, di_ctx.subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m4")
    def macroSubclass_c2_macrova_m4(self, argomento_a1, argomento_a10, argomento_a2, argomento_a5, argomento_a6, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore avvio commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore avvio
        return GlobalEnumeration.avvio
    
    @srf_value_macro("macroSubclass_c2_macrova_m6")
    def macroSubclass_c2_macrova_m6(self, argomento_a3, argomento_a4, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se la macro  SubClass_C2_macrova_M10 ( con argomento_a9   uguale a True ,argomento_a4   uguale a RossoGialloVerde  e argomento_a3   uguale a c120x )  non  è  diverso da  True  commento: {40,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T4 del campo  MainClass_C1     è attivo o  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} , assegna alla macro il valore RossoGiallo
        
         commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se la macro  SubClass_C2_macrova_M10 ( con argomento_a9   uguale a True ,argomento_a4   uguale a RossoGialloVerde  e argomento_a3   uguale a c120x )  non  è  diverso da  True  /*40,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T4 del campo  MainClass_C1     è attivo o  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ , assegna alla macro il valore RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se la macro  SubClass_C2_macrova_M10 ( con argomento_a9   uguale a True ,argomento_a4   uguale a RossoGialloVerde  e argomento_a3   uguale a c120x )  non  è  diverso da  True  /*40,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T4 del campo  MainClass_C1     è attivo o  se il ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m10')  è uguale a  (True))) )  e  
( per ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l10' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m10')  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m10')  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m10')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m10'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l10' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l10' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1))""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l10' è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l10')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se la macro  SubClass_C2_macrova_M10 ( con argomento_a9   uguale a True ,argomento_a4   uguale a RossoGialloVerde  e argomento_a3   uguale a c120x )  non  è  diverso da  True  /*40,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L10 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T4 del campo  MainClass_C1     è attivo o  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ , assegna alla macro il valore RossoGiallo
        if db((db((db(not db(not db(db(self.macroSubclass_c2_macrova_m10(GlobalEnumeration.c120x,GlobalEnumeration.rossogialloverde,True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogiallo
        #  /*46,*/ assegna alla macro il valore RossoGiallo
        return GlobalEnumeration.rossogiallo
    
    @srf_value_macro("macroSubclass_c2_macrova_m8")
    def macroSubclass_c2_macrova_m8(self, argomento_a1, argomento_a2, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m8_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c2_command_comm1DaSender7ee42824(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm1DaSender7ee42824')
    
    def eventSubclass_c2_command_comm2(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm2')
    
    def eventSubclass_c2_command_comm3DaSender855df2bd(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm3DaSender855df2bd')
    
    # for each automatic command, the corresponding method is created
    def eventSubclass_c2_command_comm4(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm4')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c2_prev(self.get_subclass_c2_previousco_c2())
        self.set_subclass_c2_previousco_c3_prev(self.get_subclass_c2_previousco_c3())
        self.set_subclass_c2_previousco_c4_prev(self.get_subclass_c2_previousco_c4())
        self.set_subclass_c2_previousco_c5_prev(self.get_subclass_c2_previousco_c5())
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
    def init_configuration(self, mainclass_c1, recordfiled12, recordfiled10, recordfiled9):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled12(recordfiled12)
        self.set_recordfiled10(recordfiled10)
        self.set_recordfiled9(recordfiled9)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled12(self, recordfiled12):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"), recordfiled12)

    def set_recordfiled10(self, recordfiled10):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"), recordfiled10)

    def set_recordfiled9(self, recordfiled9):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"), recordfiled9)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled12(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"))

    def get_recordfiled10(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"))

    def get_recordfiled9(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"))



class SubClass_C2_RecordHeaderR9(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled19, recordfiled20):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled19(recordfiled19)
        self.set_recordfiled20(recordfiled20)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled19(self, recordfiled19):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"), recordfiled19)

    def set_recordfiled20(self, recordfiled20):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"), recordfiled20)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled19(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"))

    def get_recordfiled20(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"))



