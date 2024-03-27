# Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_subclass_c3_previousva_pv1(GlobalEnumeration.spento)
        self.set_subclass_c3_previousva_pv2(GlobalEnumeration.rossogialloxverdex)
        self.set_subclass_c3_previousva_pv3(0)
        self.set_subclass_c3_previousva_pv4(False)
        self.set_subclass_c3_restoreva_rv1(False)
        self.set_subclass_c3_variabile_v10(False)
        self.set_subclass_c3_variabile_v3(0)
        self.set_subclass_c3_variabile_v8(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C3
        None


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
        _State2__State2__stateSheet_1__permanence = 1
        _State1__State1__stateSheet_0__permanence = 2
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_0 = 3
        _State1__State5__stateSheet_0__nominalActuation__transitionTo_1 = 4
        _State1__State4__stateSheet_0__nominalActuation__transitionTo_2 = 5
        _State1__State4__stateSheet_0__nominalActuation__transitionTo_3 = 6
        _State1__State3__stateSheet_0__normalization__transitionTo_0 = 7
        _State5__State5__stateSheet_4__permanence = 8
        _State5__State5__stateSheet_4__nominalActuation__transitionTo_0 = 9
        _State5__State5__stateSheet_4__nominalActuation__transitionTo_1 = 10
        _State5__State1__stateSheet_4__nominalActuation__transitionTo_2 = 11
        _State5__State2__stateSheet_4__nominalActuation__transitionTo_3 = 12
        _State5__State4__stateSheet_4__nominalActuation__transitionTo_4 = 13
        _State4__State4__stateSheet_3__permanence = 14
        _State3__State3__stateSheet_2__permanence = 15

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c3_lista_l10, subclass_c3_lista_l8, subclass_c3_parametro_p1, subclass_c3_parametro_p2, subclass_c3_parametro_p3, subclass_c3_parametro_p4, subclass_c3_parametro_p9):
        # initialize the record type parameters
        self.set_subclass_c3_lista_l10(subclass_c3_lista_l10)
        self.set_subclass_c3_lista_l8(subclass_c3_lista_l8)
        # initialize the simple type parameters
        self.set_subclass_c3_parametro_p1(subclass_c3_parametro_p1)
        self.set_subclass_c3_parametro_p2(subclass_c3_parametro_p2)
        self.set_subclass_c3_parametro_p3(subclass_c3_parametro_p3)
        self.set_subclass_c3_parametro_p4(subclass_c3_parametro_p4)
        self.set_subclass_c3_parametro_p9(subclass_c3_parametro_p9)

        # initialize the timers
        self.set_subclass_c3_restoreti_ti1(351000)
        self.set_subclass_c3_restoreti_ti1_restore(351000)
        self.set_subclass_c3_restoreti_ti2(5230000)
        self.set_subclass_c3_restoreti_ti2_restore(5230000)
        self.set_subclass_c3_restoreti_ti3(14000)
        self.set_subclass_c3_restoreti_ti3_restore(14000)
        self.set_subclass_c3_restoreti_ti4(551000)
        self.set_subclass_c3_restoreti_ti4_restore(551000)
        self.set_subclass_c3_restoreti_ti5(423000)
        self.set_subclass_c3_restoreti_ti5_restore(423000)
        self.set_subclass_c3_timer_t10(14000)
        self.set_subclass_c3_timer_t2(31000)
        self.set_subclass_c3_timer_t3(2000)
        self.set_subclass_c3_timer_t5(1230000)
        self.set_subclass_c3_timer_t7(345000)

        self.timers = [self.subclass_c3_restoreti_ti1,self.subclass_c3_restoreti_ti1_restore,self.subclass_c3_restoreti_ti2,self.subclass_c3_restoreti_ti2_restore,self.subclass_c3_restoreti_ti3,self.subclass_c3_restoreti_ti3_restore,self.subclass_c3_restoreti_ti4,self.subclass_c3_restoreti_ti4_restore,self.subclass_c3_restoreti_ti5,self.subclass_c3_restoreti_ti5_restore,self.subclass_c3_timer_t10,self.subclass_c3_timer_t2,self.subclass_c3_timer_t3,self.subclass_c3_timer_t5,self.subclass_c3_timer_t7,]

        # initialize the counters
        self.set_subclass_c3_contatore_co3(0)
        self.set_subclass_c3_contatore_co5(0)
        self.set_subclass_c3_contatore_co9(0)

    # setters for record type parameters
    def set_subclass_c3_lista_l10(self, subclass_c3_lista_l10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l10",subclass_c3_lista_l10)

    def set_subclass_c3_lista_l8(self, subclass_c3_lista_l8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l8",subclass_c3_lista_l8)


    # getters for record type parameters
    def get_subclass_c3_lista_l10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l10")

    def get_subclass_c3_lista_l8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l8")


    # setters for simple type parameters
    def set_subclass_c3_parametro_p1(self, subclass_c3_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p1",subclass_c3_parametro_p1)

    def set_subclass_c3_parametro_p2(self, subclass_c3_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p2",subclass_c3_parametro_p2)

    def set_subclass_c3_parametro_p3(self, subclass_c3_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p3",subclass_c3_parametro_p3)

    def set_subclass_c3_parametro_p4(self, subclass_c3_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p4",subclass_c3_parametro_p4)

    def set_subclass_c3_parametro_p9(self, subclass_c3_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p9",subclass_c3_parametro_p9)


    # getters for simple type parameters
    def get_subclass_c3_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p1")

    def get_subclass_c3_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p2")

    def get_subclass_c3_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p3")

    def get_subclass_c3_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p4")

    def get_subclass_c3_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p9")


    # setters for comandi al piazzale
    def set_subclass_c3_comando_c1(self, subclass_c3_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c1",subclass_c3_comando_c1)

    def set_subclass_c3_comando_c5(self, subclass_c3_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c5",subclass_c3_comando_c5)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c3_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c10")

    def get_subclass_c3_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c2")

    def get_subclass_c3_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c4")

    def get_subclass_c3_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c6")

    def get_subclass_c3_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3")

    def get_subclass_c3_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c7")

    def get_subclass_c3_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c8")

    def get_subclass_c3_previousco_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c9")


    # setters for state variables
    def set_subclass_c3_previousco_c3_prev(self, subclass_c3_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3_prev",subclass_c3_previousco_c3_prev)
    def set_subclass_c3_previousco_c7_prev(self, subclass_c3_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c7_prev",subclass_c3_previousco_c7_prev)
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
    def set_subclass_c3_variabile_v10(self, subclass_c3_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v10",subclass_c3_variabile_v10)
    def set_subclass_c3_variabile_v3(self, subclass_c3_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v3",subclass_c3_variabile_v3)
    def set_subclass_c3_variabile_v8(self, subclass_c3_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v8",subclass_c3_variabile_v8)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c3_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3_prev")

    def get_subclass_c3_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c7_prev")

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

    def get_subclass_c3_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v10")

    def get_subclass_c3_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v3")

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

    def set_subclass_c3_timer_t10(self, timerDuration):
        self.subclass_c3_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t10", self.memory)

    def set_subclass_c3_timer_t2(self, timerDuration):
        self.subclass_c3_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t2", self.memory)

    def set_subclass_c3_timer_t3(self, timerDuration):
        self.subclass_c3_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t3", self.memory)

    def set_subclass_c3_timer_t5(self, timerDuration):
        self.subclass_c3_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t5", self.memory)

    def set_subclass_c3_timer_t7(self, timerDuration):
        self.subclass_c3_timer_t7 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t7", self.memory)


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

    def get_subclass_c3_timer_t10(self):
        return self.subclass_c3_timer_t10

    def get_subclass_c3_timer_t2(self):
        return self.subclass_c3_timer_t2

    def get_subclass_c3_timer_t3(self):
        return self.subclass_c3_timer_t3

    def get_subclass_c3_timer_t5(self):
        return self.subclass_c3_timer_t5

    def get_subclass_c3_timer_t7(self):
        return self.subclass_c3_timer_t7


    # setters for counters
    def set_subclass_c3_contatore_co3(self, counterInitValue):
        self.subclass_c3_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co3", self.memory)

    def set_subclass_c3_contatore_co5(self, counterInitValue):
        self.subclass_c3_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co5", self.memory)

    def set_subclass_c3_contatore_co9(self, counterInitValue):
        self.subclass_c3_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co9", self.memory)


    # getters for counters
    def get_subclass_c3_contatore_co3(self):
        return self.subclass_c3_contatore_co3

    def get_subclass_c3_contatore_co5(self):
        return self.subclass_c3_contatore_co5

    def get_subclass_c3_contatore_co9(self):
        return self.subclass_c3_contatore_co9



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  /*53,*/ 8 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 133, Almeno una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T10 non è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 140 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 non sia  minore di  /*55,*/ 130


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 non sia attivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  /*53,*/ 8 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 133, Almeno una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T10 non è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 140 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 non sia  minore di  /*55,*/ 130


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 non sia attivo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  /*53,*/ 8 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 133""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  /*53,*/ 8 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  /*53,*/ 8""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P2 non è  diverso da c120x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P4 non è  uguale a  /*53,*/ 8""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (8)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C2 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 133""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (133)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T10 non è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 140 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 non sia  minore di  /*55,*/ 130


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 non sia attivo


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T10 non è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 140 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 non sia  minore di  /*55,*/ 130


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T10 non è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 140 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T10 non è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 140""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T10 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t10' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 140""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co3)  è maggiore di  (140)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C2 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 non sia  minore di  /*55,*/ 130


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T7 è scaduto""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V10 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C10 è  uguale a c120x""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111, Tutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 1245""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co5)  è uguale a  (1245)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co5 non è  uguale a  /*53,*/ 111""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co5)  è uguale a  (111)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*37,*/  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C10 non è  diverso da c120x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C3_variabile_V3 è  maggiore di  /*54,*/ 1""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T7 è disattivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 6""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C10 non è  uguale a c120x""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V8 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V10 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C3_contatore_Co5 è  maggiore di  /*54,*/ 14""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T7 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo


 }""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C10 è  uguale a c120x""", [
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C2 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V8 è  uguale a  False""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C3_timer_T2 non sia disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 12""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (12)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 2""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 non sia  minore di  /*55,*/ 130""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co5)  è minore di  (130)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 non sia attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#3
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 115 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C6 sia  uguale a RossoVerde


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  uguale a  False""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo, Tutte le seguenti { 
 /*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 115 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C6 sia  uguale a RossoVerde


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*34,*/  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P2 non è  diverso da c120x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T7 è attivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 115 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C6 sia  uguale a RossoVerde""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 115 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T2 è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C10 è  uguale a c120x""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C2 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T2 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 115 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 115""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C10 è  diverso da c120x""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 115""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C6 sia  uguale a RossoVerde""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#4
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#5
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#6
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#7
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#8
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#9
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#10
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#11
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#12
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#13
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#14
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#15
                    DIStatement("""ITStatement\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 non è  minore di  /*55,*/ 114 /*34,*/ o  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T5 non è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto, /*69,*/Disattiva il timer SubClass_C3_timer_T7""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 non è  minore di  /*55,*/ 114 /*34,*/ o  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T5 non è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False))} )  o  
( negazione di ((subclass_c3_contatore_co5)  è minore di  (114)) )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False))}""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co5)  è minore di  (114))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co5)  è minore di  (114)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x)) )  e  ( negazione di ((subclass_c3_variabile_v8)  è uguale a  (True)) ) )  e  ( negazione di (il timer 'subclass_c3_timer_t5' è scaduto) ) )  e  
( negazione di (il timer 'subclass_c3_timer_t7' è scaduto) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x)) )  e  ( negazione di ((subclass_c3_variabile_v8)  è uguale a  (True)) ) )  e  ( negazione di (il timer 'subclass_c3_timer_t5' è scaduto) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x)) )  e  ( negazione di ((subclass_c3_variabile_v8)  è uguale a  (True)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t5' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t5' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#16
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro SubClass_C3_macroef_M2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_restoreti_ti2_restore' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti2_restore' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M2"""),#1
                    ]),#17
                    DIStatement("""ITStatement\n/*73,*/

   
 /*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x,  Applica gli effetti
       della macro SubClass_C3_macroef_M10""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)) )  o  
( (subclass_c3_variabile_v10)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (subclass_c3_parametro_p2)  è uguale a  (c120x) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M10"""),#1
                    ]),#18
                    DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  minore di  /*55,*/ 12230 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 1445, /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  minore di  /*55,*/ 12230 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 1445""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( negazione di (negazione di ((subclass_c3_variabile_v10)  è uguale a  (False))) ) )  e  ( negazione di ((subclass_c3_contatore_co5)  è minore di  (12230)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( negazione di (negazione di ((subclass_c3_variabile_v10)  è uguale a  (False))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co5)  è minore di  (12230))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co5)  è minore di  (12230)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co9)  è minore di  (1445)""", [
                    ]),#1
                    ]),#0
                    ]),#19
                    DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C3_variabile_V8 è  uguale a  True ,  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  minore di  /*55,*/ 153, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo /*34,*/ e  se il parametro SubClass_C3_parametro_P3 è  maggiore di  /*54,*/ 6, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C3_variabile_V8 è  uguale a  True ,  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  minore di  /*55,*/ 153, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo /*34,*/ e  se il parametro SubClass_C3_parametro_P3 è  maggiore di  /*54,*/ 6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (subclass_c3_variabile_v8)  è uguale a  (True) )  e  ( per ognuna delle seguenti {se (negazione di ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (15))) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (153))} ) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c3_variabile_v8)  è uguale a  (True) )  e  ( per ognuna delle seguenti {se (negazione di ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (15))) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (153))} ) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_variabile_v8)  è uguale a  (True) )  e  ( per ognuna delle seguenti {se (negazione di ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (15))) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (153))} )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#0
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se (negazione di ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (15))) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (153))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (15))) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (153))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (15))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (15)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (153)""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c3_timer_t2' è inattivo) )  e  
( (subclass_c3_parametro_p3)  è maggiore di  (6) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t2' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_parametro_p3)  è maggiore di  (6)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#20
                    DIStatement("""ITStatement\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 1404 /*34,*/ o  se il parametro SubClass_C3_parametro_P3 è  diverso da  /*56,*/ 1 /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 1404 /*34,*/ o  se il parametro SubClass_C3_parametro_P3 è  diverso da  /*56,*/ 1 /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co9)  è maggiore di  (1404))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co9)  è maggiore di  (1404)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_parametro_p3)  è uguale a  (1)) )  e  
( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p3)  è uguale a  (1))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p3)  è uguale a  (1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#21
                    DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  diverso da  /*56,*/ 14, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M2""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  diverso da  /*56,*/ 14""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è uguale a  (14))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (14)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M2"""),#1
                    ]),#22
                    DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto, /*68,*/Attiva il timer SubClass_C3_timer_T5""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è scaduto""", [
                    ]),#0
                    ]),#0
                    ]),#23
                    DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/ 4, /*72,*/Azzera il contatore SubClass_C3_contatore_Co3

 ,altrimenti  /*70,*/Incrementa il contatore SubClass_C3_contatore_Co5""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/ 4""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (4))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (4)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    ]),#24
                    DIStatement("""ITStatement\n/*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  minore di  /*55,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 144 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  diverso da  True , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V10 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  minore di  /*55,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 144 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (11))} )  o  
( negazione di ((subclass_c3_contatore_co3)  è minore di  (144)) ) )  o  
( (subclass_c3_contatore_co3)  è uguale a  (14) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (11))} )  o  
( negazione di ((subclass_c3_contatore_co3)  è minore di  (144)) )""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (11))}""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è minore di  (11)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è minore di  (144))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co3)  è minore di  (144)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (14)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#25
                    DIStatement("""ITStatement\n/*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/ 145 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C3_timer_T2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/ 145 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (145))}""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (145)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c3_controllo_c10)  è uguale a  (c120x) )  e  ( negazione di (il timer 'subclass_c3_timer_t7' è scaduto) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_controllo_c10)  è uguale a  (c120x) )  e  ( negazione di (il timer 'subclass_c3_timer_t7' è scaduto) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#26
                    DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  True , /*71,*/Decrementa il contatore SubClass_C3_contatore_Co5""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c3_controllo_c2)  è uguale a  (True)) )  e  ( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) ) )  e  ( negazione di ((subclass_c3_variabile_v3)  è uguale a  (10)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_controllo_c2)  è uguale a  (True)) )  e  ( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v3)  è uguale a  (10))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v3)  è uguale a  (10)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_variabile_v10)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#27
                    DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C3_parametro_P4 è  diverso da  /*56,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro SubClass_C3_macroef_M2  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C3_parametro_P4 è  diverso da  /*56,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (2))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (2)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M2"""),#1
                    ]),#28
                    DIStatement("""ITStatement\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x e  se il controllo ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore SubClass_C3_contatore_Co5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (False)))} )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di (negazione di ((subclass_c3_parametro_p1)  è uguale a  (False))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(negazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (False)))} )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (False)))}""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_parametro_p1)  è uguale a  (False)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_controllo_c10)  è uguale a  (c120x) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#29
                    DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 ,  Applica gli effetti
       della macro SubClass_C3_macroef_M1  /*73,*/

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M4""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/  state1""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M4"""),#2
                    ]),#30
                    DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è disattivo, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M2""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c3_lista_l10' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M2"""),#1
                    ]),#31
                    DIStatement("""ITStatement\n/*73,*/


 /*37,*/  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 7 /*35,*/ e  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T7 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T3 è scaduto, /*71,*/Decrementa il contatore SubClass_C3_contatore_Co9""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*37,*/  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 7 /*35,*/ e  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T7 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T3 è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c3_variabile_v3)  è maggiore di  (7)) )  e  
( (subclass_c3_controllo_c2)  è uguale a  (True) ) )  o  
( il timer 'subclass_c3_timer_t7' è attivo )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_variabile_v3)  è maggiore di  (7)) )  e  
( (subclass_c3_controllo_c2)  è uguale a  (True) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v3)  è maggiore di  (7))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v3)  è maggiore di  (7)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t3' è scaduto""", [
                    ]),#1
                    ]),#0
                    ]),#32
                    DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C3_lista_L8 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  uguale a  /*53,*/ 12 /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 1, /*68,*/Attiva il timer SubClass_C3_timer_T7

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C3_contatore_Co5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C3_lista_L8 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  uguale a  /*53,*/ 12 /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c3_lista_l8' è inattivo)} )  o  
( ( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) )  e  
( (subclass_c3_contatore_co9)  è uguale a  (12) ) )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c3_lista_l8' è inattivo)}""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c3_lista_l8' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) )  e  
( (subclass_c3_contatore_co9)  è uguale a  (12) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co9)  è uguale a  (12)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (1))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (1)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#33
                    DIStatement("""ITEStatementImpl\nse la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a RossoGiallox ,argomento_a8   uguale a c120  e argomento_a10   uguale a spento )   è  uguale a  True  /*40,*/ ,  Applica gli effetti
       della macro SubClass_C3_macroef_M4  /*73,*/

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T7""", [
                    DIBoolExpr("""EqualImpl\nla macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a RossoGiallox ,argomento_a8   uguale a c120  e argomento_a10   uguale a spento )   è  uguale a  True""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c3_macrova_m2'"""),#0
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M4"""),#1
                    ]),#34
                    DIStatement("""ITStatement\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è disattivo, /*69,*/Disattiva il timer SubClass_C3_timer_T7""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c3_lista_l10' è inattivo""", [
                    ]),#0
                    ]),#0
                    ]),#35
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T7 è attivo,  Applica gli effetti
       della macro SubClass_C3_macroef_M5  /*73,*/

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T7 è attivo""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è attivo""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M5"""),#1
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#2
                    ]),#36
                    DIStatement("""ITStatement\n/*73,*/


 /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 7 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True ,  Applica gli effetti
       della macro SubClass_C3_macroef_M1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 7 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'subclass_c3_restoreti_ti2_restore' è inattivo )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (7))) ) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti2_restore' è inattivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (7))) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (7)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (7))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (7)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c3_timer_t7' è attivo) )  e  ( negazione di ((subclass_c3_contatore_co5)  è uguale a  (150)) ) )  e  
( negazione di (negazione di ((subclass_c3_variabile_v8)  è uguale a  (True))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c3_timer_t7' è attivo) )  e  ( negazione di ((subclass_c3_contatore_co5)  è uguale a  (150)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co5)  è uguale a  (150))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co5)  è uguale a  (150)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_variabile_v8)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                    ]),#37
                    DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  minore di  /*55,*/ 155123, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  minore di  /*55,*/ 155123""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co5)  è minore di  (155123)""", [
                    ]),#1
                    ]),#0
                    ]),#38
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T10 è disattivo, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T10 è disattivo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_restoreva_rv1_restore)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv1_restore)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( il timer 'subclass_c3_timer_t7' è inattivo )  e  ( negazione di (il timer 'subclass_c3_timer_t7' è inattivo) ) )  e  ( negazione di ((subclass_c3_controllo_c2)  è uguale a  (True)) ) )  e  
( il timer 'subclass_c3_timer_t10' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'subclass_c3_timer_t7' è inattivo )  e  ( negazione di (il timer 'subclass_c3_timer_t7' è inattivo) ) )  e  ( negazione di ((subclass_c3_controllo_c2)  è uguale a  (True)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c3_timer_t7' è inattivo )  e  ( negazione di (il timer 'subclass_c3_timer_t7' è inattivo) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è inattivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t10' è inattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#39
                    DIStatement("""ITEStatementImpl\nse la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a c120 ,argomento_a8   uguale a c120  e argomento_a10   uguale a RossoVerde )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 8, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a c120 ,argomento_a8   uguale a c120  e argomento_a10   uguale a RossoVerde )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 8""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m2')  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m2')  è uguale a  (True)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c3_macrova_m2'"""),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è maggiore di  (8))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_parametro_p4)  è maggiore di  (8)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#40
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C3_timer_T2 è disattivo /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  uguale a  /*53,*/ 1, /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  False 

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C3_timer_T2 è disattivo /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  uguale a  /*53,*/ 1""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v3)  è uguale a  (6)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c3_variabile_v3)  è uguale a  (6)) )  e  ( il timer 'subclass_c3_timer_t2' è inattivo ) )  e  
( negazione di ((subclass_c3_variabile_v3)  è uguale a  (1)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_variabile_v3)  è uguale a  (6)) )  e  ( il timer 'subclass_c3_timer_t2' è inattivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v3)  è uguale a  (6))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v3)  è uguale a  (6)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v3)  è uguale a  (1))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v3)  è uguale a  (1)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M5"""),#1
                    ]),#41
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 10 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 141, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 10 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 141""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c3_restoreva_rv1_restore)  è uguale a  (True) )  o  
( ( (subclass_c3_parametro_p4)  è maggiore di  (7) )  e  
( (subclass_c3_parametro_p4)  è minore di  (10) ) ) )  o  
( ( negazione di (il timer 'subclass_c3_timer_t7' è attivo) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c3_restoreva_rv1_restore)  è uguale a  (True) )  o  
( ( (subclass_c3_parametro_p4)  è maggiore di  (7) )  e  
( (subclass_c3_parametro_p4)  è minore di  (10) ) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv1_restore)  è uguale a  (True)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_parametro_p4)  è maggiore di  (7) )  e  
( (subclass_c3_parametro_p4)  è minore di  (10) )""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_parametro_p4)  è maggiore di  (7)""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p4)  è minore di  (10)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c3_timer_t7' è attivo) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co5)  è uguale a  (141))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co5)  è uguale a  (141)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M4"""),#1
                    ]),#42
                    DIStatement("""ITStatement\n/*73,*/


 /*44,*/  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T5 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T2 è disattivo, /*69,*/Disattiva il timer SubClass_C3_timer_T2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*44,*/  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T5 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T2 è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti {((mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True))} )  e  ( il timer 'subclass_c3_timer_t5' è scaduto ) )  e  
( negazione di (il timer 'subclass_c3_timer_t2' è attivo) ) )  o  
( ( negazione di ((subclass_c3_controllo_c2)  è uguale a  (True)) )  e  
( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) ) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti {((mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True))} )  e  ( il timer 'subclass_c3_timer_t5' è scaduto ) )  e  
( negazione di (il timer 'subclass_c3_timer_t2' è attivo) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {((mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True))} )  e  ( il timer 'subclass_c3_timer_t5' è scaduto )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True))}""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t5' è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t2' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_controllo_c2)  è uguale a  (True)) )  e  
( negazione di ((subclass_c3_variabile_v10)  è uguale a  (False)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                    ]),#1
                    ]),#0
                    ]),#43
                    DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 1523 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  minore di  /*55,*/ 8 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a RossoVerde, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 2

 ,altrimenti  /*68,*/Attiva il timer SubClass_C3_timer_T5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 1523 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  minore di  /*55,*/ 8 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a RossoVerde""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (negazione di ((subclass_c3_contatore_co3)  è uguale a  (1523))) ) )  e  ( negazione di ((subclass_c3_parametro_p1)  è uguale a  (False)) ) )  e  ( (subclass_c3_controllo_c6)  è uguale a  (rossoverde) ) )  e  
( (subclass_c3_parametro_p9)  è minore di  (8) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (negazione di ((subclass_c3_contatore_co3)  è uguale a  (1523))) ) )  e  ( negazione di ((subclass_c3_parametro_p1)  è uguale a  (False)) ) )  e  ( (subclass_c3_controllo_c6)  è uguale a  (rossoverde) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (negazione di ((subclass_c3_contatore_co3)  è uguale a  (1523))) ) )  e  ( negazione di ((subclass_c3_parametro_p1)  è uguale a  (False)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (negazione di ((subclass_c3_contatore_co3)  è uguale a  (1523))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_contatore_co3)  è uguale a  (1523)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è uguale a  (1523))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (1523)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (rossoverde)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p9)  è minore di  (8)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (rossoverde)""", [
                    ]),#1
                    ]),#0
                    ]),#44
                    DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C3_lista_L10 è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 1451 /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 non è  maggiore di  /*54,*/ 12230 e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C3_timer_T7

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C3_lista_L10 è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 1451 /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 non è  maggiore di  /*54,*/ 12230 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c3_lista_l10' è inattivo)} )  o  
( ( ( (subclass_c3_contatore_co3)  è uguale a  (1504) )  e  ( (subclass_c3_variabile_v3)  è uguale a  (3) ) )  e  
( (subclass_c3_contatore_co9)  è minore di  (1451) ) )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c3_lista_l10' è inattivo)}""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c3_lista_l10' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c3_contatore_co3)  è uguale a  (1504) )  e  ( (subclass_c3_variabile_v3)  è uguale a  (3) ) )  e  
( (subclass_c3_contatore_co9)  è minore di  (1451) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_contatore_co3)  è uguale a  (1504) )  e  ( (subclass_c3_variabile_v3)  è uguale a  (3) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (1504)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v3)  è uguale a  (3)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co9)  è minore di  (1451)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_contatore_co5)  è maggiore di  (12230)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co5)  è maggiore di  (12230))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co5)  è maggiore di  (12230)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M4"""),#1
                    ]),#45
                    DIStatement("""ITStatement\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  diverso da  False ,  Applica gli effetti
       della macro SubClass_C3_macroef_M1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  diverso da  False""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (rossogialloaverdea)))}""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (rossogialloaverdea))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (rossogialloaverdea)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c2)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                    ]),#46
                    DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*34,*/  se il parametro SubClass_C3_parametro_P1 è  diverso da  True  /*36,*/ o  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 3

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*34,*/  se il parametro SubClass_C3_parametro_P1 è  diverso da  True  /*36,*/ o  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c3_parametro_p1)  è uguale a  (True)) )  o  
( il timer 'subclass_c3_timer_t5' è inattivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t5' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#47
                    DIStatement("""ITEStatementImpl\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/, /*69,*/Disattiva il timer SubClass_C3_timer_T2

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T2""", [
                    DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                    ]),#0
                    ]),#48
                    DIStatement("""ITStatement\n/*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False)))} )  e  
( (subclass_c3_contatore_co9)  è minore di  (12) )""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False)))}""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co9)  è minore di  (12)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#49
                    DIStatement("""ITEStatementImpl\nse la macro  SubClass_C3_macrova_M6 ( con argomento_a5   uguale a True ,argomento_a9   uguale a c120x  e argomento_a6   uguale a RossoVerde )   è  diverso da AC /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  diverso da  /*56,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , /*70,*/Incrementa il contatore SubClass_C3_contatore_Co5

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse la macro  SubClass_C3_macrova_M6 ( con argomento_a5   uguale a True ,argomento_a9   uguale a c120x  e argomento_a6   uguale a RossoVerde )   è  diverso da AC /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  diverso da  /*56,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m6')  è uguale a  (ac)) )  e  
( negazione di ((subclass_c3_parametro_p4)  è uguale a  (6)) ) )  o  
( negazione di ((subclass_c3_variabile_v8)  è uguale a  (True)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m6')  è uguale a  (ac)) )  e  
( negazione di ((subclass_c3_parametro_p4)  è uguale a  (6)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m6')  è uguale a  (ac))""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m6')  è uguale a  (ac)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c3_macrova_m6'"""),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (6))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (6)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_variabile_v8)  è uguale a  (True)) )  e  
( negazione di ((subclass_c3_variabile_v8)  è uguale a  (False)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                    ]),#50
                    DIStatement("""ITEStatementImpl\n/*73,*/


 /*34,*/  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 3,  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co8 del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/ 1145, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C3_contatore_Co3""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/


 /*34,*/  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 3,  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co8 del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/ 1145""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è minore di  (3))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p4)  è minore di  (3)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (1145)) allora (negazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (True)))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (1145)) allora (negazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (True)))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (1145)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#51
                    DIStatement("""ITEStatementImpl\n/*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  maggiore di  /*54,*/ 111230 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  maggiore di  /*54,*/ 3 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 154, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T7""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  maggiore di  /*54,*/ 111230 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  maggiore di  /*54,*/ 3 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 154""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è maggiore di  (111230))} )  e  
( (subclass_c3_parametro_p4)  è maggiore di  (3) )""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è maggiore di  (111230))}""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è maggiore di  (111230)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_parametro_p4)  è maggiore di  (3)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co3)  è maggiore di  (154)""", [
                    ]),#1
                    ]),#0
                    ]),#52
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 12 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 135 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False , /*71,*/Decrementa il contatore SubClass_C3_contatore_Co3

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 12 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 135 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (consdef)  è uguale a  (False) )  e  ( (subclass_c3_parametro_p2)  è uguale a  (c120x) ) )  e  ( negazione di ((subclass_c3_controllo_c6)  è uguale a  (rossoverde)) ) )  e  
( negazione di ((subclass_c3_contatore_co9)  è maggiore di  (12)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( (subclass_c3_parametro_p2)  è uguale a  (c120x) ) )  e  ( negazione di ((subclass_c3_controllo_c6)  è uguale a  (rossoverde)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( (subclass_c3_parametro_p2)  è uguale a  (c120x) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c6)  è uguale a  (rossoverde))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (rossoverde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co9)  è maggiore di  (12))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co9)  è maggiore di  (12)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_contatore_co3)  è minore di  (135) )  e  
( negazione di (negazione di ((subclass_c3_variabile_v8)  è uguale a  (False))) )""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co3)  è minore di  (135)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_variabile_v8)  è uguale a  (False)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                    ]),#53
                    DIStatement("""ITStatement\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  maggiore di  /*54,*/ 131, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co9""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  maggiore di  /*54,*/ 131""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( (consdef)  è uguale a  (False) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (7)) allora ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))} ) )  e  ( (subclass_c3_variabile_v8)  è uguale a  (True) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di (il timer 'subclass_c3_timer_t7' è inattivo) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (consdef)  è uguale a  (False) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (7)) allora ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))} ) )  e  ( (subclass_c3_variabile_v8)  è uguale a  (True) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (7)) allora ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))} ) )  e  ( (subclass_c3_variabile_v8)  è uguale a  (True) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (7)) allora ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))} )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (7)) allora ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (7)) allora ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (7)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1)""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co9)  è maggiore di  (131)""", [
                    ]),#1
                    ]),#0
                    ]),#54
                    DIStatement("""ITEStatementImpl\n/*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde

 ,altrimenti  /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c3_timer_t7' è inattivo )  e  
( negazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x)) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è inattivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#55
                    DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*36,*/ e  se il timer SubClass_C3_timer_T2 è disattivo, /*69,*/Disattiva il timer SubClass_C3_timer_T10

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*36,*/ e  se il timer SubClass_C3_timer_T2 è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c3_controllo_c2)  è uguale a  (False)) )  e  ( (subclass_c3_controllo_c10)  è uguale a  (c120x) ) )  e  
( il timer 'subclass_c3_timer_t2' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_controllo_c2)  è uguale a  (False)) )  e  ( (subclass_c3_controllo_c10)  è uguale a  (c120x) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c2)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è inattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#56
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
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2,
                         guard=(self.dbs[7], ),
                         effect=(self.dbs[31], self.dbs[32], self.dbs[33], self.dbs[34], self.dbs[35], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3,
                         guard=(self.dbs[6], ),
                         effect=(self.dbs[29], self.dbs[30], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[19], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[20], self.dbs[21], self.dbs[22], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4,
                         guard=(self.dbs[4], ),
                         effect=(self.dbs[23], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4,
                         guard=(self.dbs[5], ),
                         effect=(self.dbs[24], self.dbs[25], self.dbs[26], self.dbs[27], self.dbs[28], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[16], self.dbs[17], self.dbs[18], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,
                         guard=(self.dbs[11], ),
                         effect=(self.dbs[42], self.dbs[43], self.dbs[44], self.dbs[45], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,
                         guard=(self.dbs[12], ),
                         effect=(self.dbs[46], self.dbs[47], self.dbs[48], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,
                         guard=(self.dbs[13], ),
                         effect=(self.dbs[49], self.dbs[50], self.dbs[51], self.dbs[52], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2,
                         guard=(self.dbs[14], ),
                         effect=(self.dbs[53], self.dbs[54], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4,
                         guard=(self.dbs[15], ),
                         effect=(self.dbs[55], self.dbs[56], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5,
                         guard=(self.dbs[10], ),
                         effect=(self.dbs[41], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4,
                         guard=(self.dbs[9], ),
                         effect=(self.dbs[38], self.dbs[39], self.dbs[40], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3,
                         guard=(self.dbs[8], ),
                         effect=(self.dbs[36], self.dbs[37], ),
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

        self.set_subclass_c3_previousco_c3_prev(GlobalEnumeration.rossoverde)
        self.set_subclass_c3_previousco_c7_prev(True)
        self.set_subclass_c3_previousco_c8_prev(GlobalEnumeration.rossogiallox)
        self.set_subclass_c3_previousco_c9_prev(False)
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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2):
                if(self.guard_PERMANENCE_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
                if(self.guard_NORMALIZATION_state1_state3_000()):
                    self.curr_transition = self.Transition._State1__State3__stateSheet_0__normalization__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_state2_000()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_state5_000()):
                    self.curr_transition = self.Transition._State1__State5__stateSheet_0__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state1_state4_000()):
                    self.curr_transition = self.Transition._State1__State4__stateSheet_0__nominalActuation__transitionTo_2
                elif(self.guard_NOMINAL_ACTUATION_state1_state4_001()):
                    self.curr_transition = self.Transition._State1__State4__stateSheet_0__nominalActuation__transitionTo_3
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5):
                if(self.guard_NOMINAL_ACTUATION_state5_000()):
                    self.curr_transition = self.Transition._State5__State5__stateSheet_4__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state5_001()):
                    self.curr_transition = self.Transition._State5__State5__stateSheet_4__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state5_state1_000()):
                    self.curr_transition = self.Transition._State5__State1__stateSheet_4__nominalActuation__transitionTo_2
                elif(self.guard_NOMINAL_ACTUATION_state5_state2_000()):
                    self.curr_transition = self.Transition._State5__State2__stateSheet_4__nominalActuation__transitionTo_3
                elif(self.guard_NOMINAL_ACTUATION_state5_state4_000()):
                    self.curr_transition = self.Transition._State5__State4__stateSheet_4__nominalActuation__transitionTo_4
                elif(self.guard_PERMANENCE_state5_000()):
                    self.curr_transition = self.Transition._State5__State5__stateSheet_4__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4):
                if(self.guard_PERMANENCE_state4_000()):
                    self.curr_transition = self.Transition._State4__State4__stateSheet_3__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3):
                if(self.guard_PERMANENCE_state3_000()):
                    self.curr_transition = self.Transition._State3__State3__stateSheet_2__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        # check what is the current transition
        # to set the current state and to execute the effects of the current transition
        if self.curr_transition == self.Transition.T_Undef:
            # if the current transition variable is not set, an exception will be raised
            return DISCARDED(self._logger, command, self.get_fsmState(), self._command_unexpected)
        elif self.curr_transition == self.Transition._State2__State2__stateSheet_1__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2)
            self.effect_PERMANENCE_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State5__stateSheet_0__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5)
            self.effect_NOMINAL_ACTUATION_state1_state5_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State4__stateSheet_0__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4)
            self.effect_NOMINAL_ACTUATION_state1_state4_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State4__stateSheet_0__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4)
            self.effect_NOMINAL_ACTUATION_state1_state4_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State3__stateSheet_0__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3)
            self.effect_NORMALIZATION_state1_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State5__stateSheet_4__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5)
            self.effect_PERMANENCE_state5_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State5__stateSheet_4__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5)
            self.effect_NOMINAL_ACTUATION_state5_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State5__stateSheet_4__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state5)
            self.effect_NOMINAL_ACTUATION_state5_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State1__stateSheet_4__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state5_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State2__stateSheet_4__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state5_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State4__stateSheet_4__nominalActuation__transitionTo_4:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4)
            self.effect_NOMINAL_ACTUATION_state5_state4_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State4__stateSheet_3__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state4)
            self.effect_PERMANENCE_state4_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State3__stateSheet_2__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state3)
            self.effect_PERMANENCE_state3_000()
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
        
         commento: {68,} commento: {34,}  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  uguale a  commento: {53,} 8 commento: {35,} o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  commento: {53,} 133, Almeno una delle seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C3_timer_T10 non è disattivo commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 140 commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  uguale a  False , Tutte le seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C3_timer_T7 è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
         commento: {67,} commento: {38,}  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  commento: {53,} 1245 commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 non è  uguale a  commento: {53,} 111, Tutte le seguenti { 
         commento: {69,} commento: {37,}  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V3 è  maggiore di  commento: {54,} 1, Solo una delle seguenti { 
         commento: {69,} commento: {36,}  se il timer SubClass_C3_timer_T7 è disattivo commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {34,} o  se il parametro SubClass_C3_parametro_P4 è  minore di  commento: {55,} 6 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
         commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  commento: {37,} o  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  maggiore di  commento: {54,} 14 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è scaduto, Almeno una delle seguenti { 
         commento: {67,} commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, Tutte le seguenti { 
         commento: {35,}  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T2 non sia disattivo
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C3_contatore_Co3 sia  diverso da  commento: {56,} 12
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C3_parametro_P1 non sia  diverso da  False 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V3 sia  uguale a  commento: {53,} 2
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C3_contatore_Co5 non sia  minore di  commento: {55,} 130
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T7 non sia attivo
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        return db((db(not db((db((db((db(not db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p4() == 8, self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c2() == True, self.dbs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 133, self.dbs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_subclass_c3_timer_t10().isDisattivato(), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co3().get_valore() > 140, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c2() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(self.get_subclass_c3_timer_t7().isScaduto(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_subclass_c3_contatore_co5().get_valore() == 1245, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co5().get_valore() == 111, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_subclass_c3_variabile_v8() == True, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v3() > 1, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_subclass_c3_timer_t7().isDisattivato(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t2().isAttivato(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_parametro_p4() < 6, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v8() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_contatore_co5().get_valore() > 14, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t7().isScaduto(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(self.get_subclass_c3_controllo_c2() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c3_variabile_v8() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v8() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c3_timer_t2().isDisattivato(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 12, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p1() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_variabile_v3() == 2, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_contatore_co5().get_valore() < 130, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c3_timer_t7().isAttivato(), self.dbs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1]), self.dbs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1])), self.dbs[1])
    
    def guard_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[2])
    
    def guard_NOMINAL_ACTUATION_state1_state5_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[3])
    
    def guard_NOMINAL_ACTUATION_state1_state4_000(self):
        """
        CNL corrispondente:
         {  commento: {67,} commento: {34,}  se il parametro SubClass_C3_parametro_P2 non è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C3_timer_T7 è attivo, Tutte le seguenti { 
         commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C3_timer_T2 è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  minore di  commento: {55,} 115 e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C6 sia  uguale a RossoVerde
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C3_controllo_C2 non sia  uguale a  False 
        
         }
        """
        return db((db(not db((db(not db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[4].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v8() == False, self.dbs[4].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_timer_t7().isAttivato(), self.dbs[4].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[0]) or db(not db((db((db((db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c2() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t2().isScaduto(), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co3().get_valore() < 115, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0]) or db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.rossoverde, self.dbs[4].subs[0].subs[1].subs[1]), self.dbs[4].subs[0].subs[1]), self.dbs[4].subs[0]) and db(not db(self.get_subclass_c3_controllo_c2() == False, self.dbs[4].subs[1].subs[0]), self.dbs[4].subs[1])), self.dbs[4])
    
    def guard_NOMINAL_ACTUATION_state1_state4_001(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[5])
    
    def guard_NORMALIZATION_state1_state3_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[6])
    
    def guard_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[7])
    
    def guard_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[8])
    
    def guard_PERMANENCE_state4_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[9])
    
    def guard_PERMANENCE_state5_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[10])
    
    def guard_NOMINAL_ACTUATION_state5_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[11])
    
    def guard_NOMINAL_ACTUATION_state5_001(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[12])
    
    def guard_NOMINAL_ACTUATION_state5_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[13])
    
    def guard_NOMINAL_ACTUATION_state5_state2_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[14])
    
    def guard_NOMINAL_ACTUATION_state5_state4_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[15])
    
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
        
         commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  uguale a  False  commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 non è  minore di  commento: {55,} 114 commento: {34,} o  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T5 non è scaduto commento: {36,} e  se il timer SubClass_C3_timer_T7 non è scaduto, commento: {69,}Disattiva il timer SubClass_C3_timer_T7
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro SubClass_C3_macroef_M2  commento: {73,}
        
           
         commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x,  Applica gli effetti
               della macro SubClass_C3_macroef_M10  commento: {73,}
        
           
        
        }
        """
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 non è  minore di  /*55,*/ 114 /*34,*/ o  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T5 non è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto, /*69,*/Disattiva il timer SubClass_C3_timer_T7
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == False, self.dbs[16].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[16].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co5().get_valore() < 114, self.dbs[16].subs[0].subs[0].subs[1].subs[0]), self.dbs[16].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0]) or db((db((db((db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[16].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[16].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v8() == True, self.dbs[16].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[16].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t5().isScaduto(), self.dbs[16].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[16].subs[0].subs[1].subs[0].subs[1])), self.dbs[16].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t7().isScaduto(), self.dbs[16].subs[0].subs[1].subs[1].subs[0]), self.dbs[16].subs[0].subs[1].subs[1])), self.dbs[16].subs[0].subs[1])), self.dbs[16].subs[0]):
            self.get_subclass_c3_timer_t7().disattiva()
        #  /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M2
        if db((db(not db(self.get_subclass_c3_restoreti_ti2_restore().isDisattivato(), self.dbs[17].subs[0].subs[0].subs[0]), self.dbs[17].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[17].subs[0].subs[1])), self.dbs[17].subs[0]):
            self.macroSubclass_c3_macroef_m2(self.dbs[17].subs[1])
        #  /*73,*/
        #     
        #   /*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M10
        if db((db((db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[18].subs[0].subs[0].subs[0].subs[0]), self.dbs[18].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v10() == False, self.dbs[18].subs[0].subs[0].subs[1])), self.dbs[18].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[18].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[18].subs[0].subs[1].subs[1])), self.dbs[18].subs[0].subs[1])), self.dbs[18].subs[0]):
            self.macroSubclass_c3_macroef_m10(self.dbs[18].subs[1])
    
    def effect_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 non è  minore di  commento: {55,} 12230 commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  minore di  commento: {55,} 1445, commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  True 
        
           
         }
        """
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 non è  minore di  /*55,*/ 12230 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 1445, /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  True
        if db((db((db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, self.dbs[19].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[19].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[19].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[19].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[19].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[19].subs[0].subs[0].subs[0].subs[1])), self.dbs[19].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co5().get_valore() < 12230, self.dbs[19].subs[0].subs[0].subs[1].subs[0]), self.dbs[19].subs[0].subs[0].subs[1])), self.dbs[19].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co9().get_valore() < 1445, self.dbs[19].subs[0].subs[1])), self.dbs[19].subs[0]):
            self.set_subclass_c3_comando_c1(True)
    
    def effect_NOMINAL_ACTUATION_state1_state5_000(self):
        """
        CNL corrispondente:
         { commento: {37,}  se la variabile SubClass_C3_variabile_V8 è  uguale a  True ,  commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  minore di  commento: {55,} 153, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co8 del campo  MainClass_C1     commento: {105,} è  diverso da  commento: {56,} 15 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  commento: {36,} o  se il timer SubClass_C3_timer_T2 non è disattivo commento: {34,} e  se il parametro SubClass_C3_parametro_P3 è  maggiore di  commento: {54,} 6, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
        
           
         commento: {38,}  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  commento: {54,} 1404 commento: {34,} o  se il parametro SubClass_C3_parametro_P3 è  diverso da  commento: {56,} 1 commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  False 
        
           
         commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  diverso da  commento: {56,} 14, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M2  commento: {73,}
        
        
         }
        """
        #  /*37,*/  se la variabile SubClass_C3_variabile_V8 è  uguale a  True ,  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  minore di  /*55,*/ 153, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è disattivo /*34,*/ e  se il parametro SubClass_C3_parametro_P3 è  maggiore di  /*54,*/ 6, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
        if db((db((db((db((db(self.get_subclass_c3_variabile_v8() == True, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() < 153, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() == 15, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[20].subs[0].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[20].subs[0].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_timer_t2().isDisattivato(), self.dbs[20].subs[0].subs[1].subs[0].subs[0]), self.dbs[20].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_parametro_p3() > 6, self.dbs[20].subs[0].subs[1].subs[1])), self.dbs[20].subs[0].subs[1])), self.dbs[20].subs[0]):
            self.set_subclass_c3_variabile_v3(1)
        #  /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 1404 /*34,*/ o  se il parametro SubClass_C3_parametro_P3 è  diverso da  /*56,*/ 1 /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  False
        if db((db(not db(self.get_subclass_c3_contatore_co9().get_valore() > 1404, self.dbs[21].subs[0].subs[0].subs[0]), self.dbs[21].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_parametro_p3() == 1, self.dbs[21].subs[0].subs[1].subs[0].subs[0]), self.dbs[21].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[21].subs[0].subs[1].subs[1].subs[0]), self.dbs[21].subs[0].subs[1].subs[1])), self.dbs[21].subs[0].subs[1])), self.dbs[21].subs[0]):
            self.set_subclass_c3_comando_c1(False)
        #  /*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  diverso da  /*56,*/ 14, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M2
        if db((db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[22].subs[0].subs[0].subs[0]), self.dbs[22].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 14, self.dbs[22].subs[0].subs[1].subs[0]), self.dbs[22].subs[0].subs[1])), self.dbs[22].subs[0]):
            self.set_subclass_c3_variabile_v8(False)
        else:
            self.macroSubclass_c3_macroef_m2(self.dbs[22].subs[1])
    
    def effect_NOMINAL_ACTUATION_state1_state4_000(self):
        """
        CNL corrispondente:
         { commento: {36,}  se il timer SubClass_C3_timer_T2 non è scaduto, commento: {68,}Attiva il timer SubClass_C3_timer_T5
        
           
         }
        """
        #  /*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto, /*68,*/Attiva il timer SubClass_C3_timer_T5
        if db(not db(self.get_subclass_c3_timer_t2().isScaduto(), self.dbs[23].subs[0].subs[0]), self.dbs[23].subs[0]):
            self.get_subclass_c3_timer_t5().attiva()
    
    def effect_NOMINAL_ACTUATION_state1_state4_001(self):
        """
        CNL corrispondente:
         { commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  diverso da  commento: {56,} 4, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co3
        
         ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co5
        
        
         commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  minore di  commento: {55,} 11 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  minore di  commento: {55,} 144 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 14 commento: {34,} o  se il parametro SubClass_C3_parametro_P1 è  diverso da  True , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V10 il valore  False 
        
           
         commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,} 145 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {36,} e  se il timer SubClass_C3_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C3_timer_T2
        
           
         commento: {35,}  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V3 è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  True , commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co5
        
           
         commento: {34,}  se il parametro SubClass_C3_parametro_P4 è  diverso da  commento: {56,} 2 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro SubClass_C3_macroef_M2  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        
        
         }
        """
        #  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  diverso da  /*56,*/ 4, /*72,*/Azzera il contatore SubClass_C3_contatore_Co3
        #   ,altrimenti  /*70,*/Incrementa il contatore SubClass_C3_contatore_Co5
        if db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == 4, self.dbs[24].subs[0].subs[0].subs[0][idx]), self.dbs[24].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), self.dbs[24].subs[0]):
            self.get_subclass_c3_contatore_co3().resetta()
        else:
            self.get_subclass_c3_contatore_co5().incrementa()
        #  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  minore di  /*55,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 144 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*34,*/ o  se il parametro SubClass_C3_parametro_P1 è  diverso da  True , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V10 il valore  False
        if db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() < 11, self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[25].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co3().get_valore() < 144, self.dbs[25].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[25].subs[0].subs[0].subs[0].subs[1])), self.dbs[25].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_contatore_co3().get_valore() == 14, self.dbs[25].subs[0].subs[0].subs[1])), self.dbs[25].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p1() == True, self.dbs[25].subs[0].subs[1].subs[0]), self.dbs[25].subs[0].subs[1])), self.dbs[25].subs[0]):
            self.set_subclass_c3_variabile_v10(False)
        #  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/ 145 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C3_timer_T2
        if db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() == 145, self.dbs[26].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[26].subs[0].subs[0]) or db((db((db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[26].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t7().isScaduto(), self.dbs[26].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[26].subs[0].subs[1].subs[0].subs[1])), self.dbs[26].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[26].subs[0].subs[1].subs[1])), self.dbs[26].subs[0].subs[1])), self.dbs[26].subs[0]):
            self.get_subclass_c3_timer_t2().attiva()
        #  /*35,*/  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  diverso da  True , /*71,*/Decrementa il contatore SubClass_C3_contatore_Co5
        if db((db((db((db(not db(self.get_subclass_c3_controllo_c2() == True, self.dbs[27].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[27].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[27].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[0].subs[0].subs[1])), self.dbs[27].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v3() == 10, self.dbs[27].subs[0].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[0].subs[1])), self.dbs[27].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_variabile_v10() == True, self.dbs[27].subs[0].subs[1].subs[0].subs[0]), self.dbs[27].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[1])), self.dbs[27].subs[0]):
            self.get_subclass_c3_contatore_co5().decrementa()
        #  /*34,*/  se il parametro SubClass_C3_parametro_P4 è  diverso da  /*56,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M2  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
        if db((db(not db(self.get_subclass_c3_parametro_p4() == 2, self.dbs[28].subs[0].subs[0].subs[0]), self.dbs[28].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[28].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[28].subs[0].subs[1].subs[1])), self.dbs[28].subs[0].subs[1])), self.dbs[28].subs[0]):
            self.macroSubclass_c3_macroef_m2(self.dbs[28].subs[1])
        else:
            self.set_subclass_c3_variabile_v8(True)
    
    def effect_NORMALIZATION_state1_state3_000(self):
        """
        CNL corrispondente:
         { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x e  se il controllo ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
        
           
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 ,  Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M4  commento: {73,}
        
        
         }
        """
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x e  se il controllo ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore SubClass_C3_contatore_Co5
        if db((db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == False, self.dbs[29].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), self.dbs[29].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), self.dbs[29].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[29].subs[0].subs[0].subs[0].subs[1])), self.dbs[29].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_parametro_p1() == False, self.dbs[29].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[29].subs[0].subs[0].subs[1].subs[0]), self.dbs[29].subs[0].subs[0].subs[1])), self.dbs[29].subs[0].subs[0]) or db((db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[29].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[29].subs[0].subs[1].subs[1])), self.dbs[29].subs[0].subs[1])), self.dbs[29].subs[0]):
            self.get_subclass_c3_contatore_co5().resetta()
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M1  /*73,*/
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M4
        if db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[30].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[30].subs[0]):
            self.macroSubclass_c3_macroef_m1(self.dbs[30].subs[1])
        else:
            self.macroSubclass_c3_macroef_m4(self.dbs[30].subs[2])
    
    def effect_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è disattivo, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M2  commento: {73,}
        
        
         commento: {37,}  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  commento: {54,} 7 commento: {35,} e  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  commento: {36,} o  se il timer SubClass_C3_timer_T7 è attivo commento: {36,} o  se il timer SubClass_C3_timer_T3 è scaduto, commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co9
        
           
         commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C3_lista_L8 è disattivo commento: {37,} o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  uguale a  commento: {53,} 12 commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 1, commento: {68,}Attiva il timer SubClass_C3_timer_T7
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co5
        
        
          se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a RossoGiallox ,argomento_a8   uguale a c120  e argomento_a10   uguale a spento )   è  uguale a  True  commento: {40,} ,  Applica gli effetti
               della macro SubClass_C3_macroef_M4  commento: {73,}
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T7
        
        
         commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è disattivo, commento: {69,}Disattiva il timer SubClass_C3_timer_T7
        
           
        
        }
        """
        #  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è disattivo, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M2
        if db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isDisattivato(), self.dbs[31].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[31].subs[0]):
            self.get_subclass_c3_contatore_co3().incrementa()
        else:
            self.macroSubclass_c3_macroef_m2(self.dbs[31].subs[1])
        #  /*73,*/
        #   /*37,*/  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 7 /*35,*/ e  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T7 è attivo /*36,*/ o  se il timer SubClass_C3_timer_T3 è scaduto, /*71,*/Decrementa il contatore SubClass_C3_contatore_Co9
        if db((db((db((db(not db(self.get_subclass_c3_variabile_v3() > 7, self.dbs[32].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[32].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_controllo_c2() == True, self.dbs[32].subs[0].subs[0].subs[0].subs[1])), self.dbs[32].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t7().isAttivato(), self.dbs[32].subs[0].subs[0].subs[1])), self.dbs[32].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t3().isScaduto(), self.dbs[32].subs[0].subs[1])), self.dbs[32].subs[0]):
            self.get_subclass_c3_contatore_co9().decrementa()
        #  /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C3_lista_L8 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  uguale a  /*53,*/ 12 /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 1, /*68,*/Attiva il timer SubClass_C3_timer_T7
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C3_contatore_Co5
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[33].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), self.dbs[33].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[33].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[33].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_contatore_co9().get_valore() == 12, self.dbs[33].subs[0].subs[0].subs[1].subs[1])), self.dbs[33].subs[0].subs[0].subs[1])), self.dbs[33].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_parametro_p4() == 1, self.dbs[33].subs[0].subs[1].subs[0].subs[0]), self.dbs[33].subs[0].subs[1].subs[0]), self.dbs[33].subs[0].subs[1])), self.dbs[33].subs[0]):
            self.get_subclass_c3_timer_t7().attiva()
        else:
            self.get_subclass_c3_contatore_co5().decrementa()
        #  se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a RossoGiallox ,argomento_a8   uguale a c120  e argomento_a10   uguale a spento )   è  uguale a  True  /*40,*/ ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M4  /*73,*/
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T7
        if db(db(self.macroSubclass_c3_macrova_m2(GlobalEnumeration.rossogiallox,GlobalEnumeration.spento,GlobalEnumeration.c120, self.dbs[34].subs[0].subs[0]), self.dbs[34].subs[0].subs[0]) == True, self.dbs[34].subs[0]):
            self.macroSubclass_c3_macroef_m4(self.dbs[34].subs[1])
        else:
            self.get_subclass_c3_timer_t7().disattiva()
        #  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è disattivo, /*69,*/Disattiva il timer SubClass_C3_timer_T7
        if db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isDisattivato(), self.dbs[35].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[35].subs[0]):
            self.get_subclass_c3_timer_t7().disattiva()
    
    def effect_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {37,}  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  commento: {36,} o  se il timer SubClass_C3_timer_T7 è attivo,  Applica gli effetti
               della macro SubClass_C3_macroef_M5  commento: {73,}
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
        
         commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 7 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 150 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True ,  Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
           
        
        }
        """
        #  /*37,*/  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T7 è attivo,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M5  /*73,*/
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M1
        if db((db(self.get_subclass_c3_variabile_v10() == False, self.dbs[36].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t7().isAttivato(), self.dbs[36].subs[0].subs[1])), self.dbs[36].subs[0]):
            self.macroSubclass_c3_macroef_m5(self.dbs[36].subs[1])
        else:
            self.macroSubclass_c3_macroef_m1(self.dbs[36].subs[2])
        #  /*73,*/
        #   /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 7 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M1
        if db((db((db(self.get_subclass_c3_restoreti_ti2_restore().isDisattivato(), self.dbs[37].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[37].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p4() == 7, self.dbs[37].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[37].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[37].subs[0].subs[0].subs[1].subs[1])), self.dbs[37].subs[0].subs[0].subs[1])), self.dbs[37].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c3_timer_t7().isAttivato(), self.dbs[37].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[37].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co5().get_valore() == 150, self.dbs[37].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[37].subs[0].subs[1].subs[0].subs[1])), self.dbs[37].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_variabile_v8() == True, self.dbs[37].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[37].subs[0].subs[1].subs[1].subs[0]), self.dbs[37].subs[0].subs[1].subs[1])), self.dbs[37].subs[0].subs[1])), self.dbs[37].subs[0]):
            self.macroSubclass_c3_macroef_m1(self.dbs[37].subs[1])
    
    def effect_PERMANENCE_state4_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {37,}  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  minore di  commento: {55,} 155123, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a  True  commento: {36,} o  se il timer SubClass_C3_timer_T7 è disattivo commento: {36,} e  se il timer SubClass_C3_timer_T7 non è disattivo commento: {35,} e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T10 è disattivo, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        
        
          se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a c120 ,argomento_a8   uguale a c120  e argomento_a10   uguale a RossoVerde )  non  è  uguale a  True  commento: {40,}  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  commento: {54,} 8, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  True 
        
        
        
        }
        """
        #  /*37,*/  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  minore di  /*55,*/ 155123, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        if db((db(self.get_subclass_c3_variabile_v8() == True, self.dbs[38].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co5().get_valore() < 155123, self.dbs[38].subs[0].subs[1])), self.dbs[38].subs[0]):
            self.set_subclass_c3_comando_c5(GlobalEnumeration.rossoverde)
        #  /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a  True  /*36,*/ o  se il timer SubClass_C3_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T10 è disattivo, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
        if db((db(not db(self.get_subclass_c3_restoreva_rv1_restore() == True, self.dbs[39].subs[0].subs[0].subs[0]), self.dbs[39].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c3_timer_t7().isDisattivato(), self.dbs[39].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t7().isDisattivato(), self.dbs[39].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[39].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[39].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c2() == True, self.dbs[39].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[39].subs[0].subs[1].subs[0].subs[1])), self.dbs[39].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_timer_t10().isDisattivato(), self.dbs[39].subs[0].subs[1].subs[1])), self.dbs[39].subs[0].subs[1])), self.dbs[39].subs[0]):
            self.set_subclass_c3_variabile_v8(True)
        else:
            self.set_subclass_c3_variabile_v8(True)
        #  se la macro  SubClass_C3_macrova_M2 ( con argomento_a1   uguale a c120 ,argomento_a8   uguale a c120  e argomento_a10   uguale a RossoVerde )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 8, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  True
        if db((db(not db(db(self.macroSubclass_c3_macrova_m2(GlobalEnumeration.c120,GlobalEnumeration.rossoverde,GlobalEnumeration.c120, self.dbs[40].subs[0].subs[0].subs[0].subs[0]), self.dbs[40].subs[0].subs[0].subs[0].subs[0]) == True, self.dbs[40].subs[0].subs[0].subs[0]), self.dbs[40].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p4() > 8, self.dbs[40].subs[0].subs[1].subs[0]), self.dbs[40].subs[0].subs[1])), self.dbs[40].subs[0]):
            self.set_subclass_c3_comando_c5(GlobalEnumeration.rossoverde)
        else:
            self.set_subclass_c3_comando_c1(True)
    
    def effect_PERMANENCE_state5_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {37,}  se la variabile SubClass_C3_variabile_V3 è  uguale a  commento: {53,} 6 commento: {37,} o  se la variabile SubClass_C3_variabile_V3 è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer SubClass_C3_timer_T2 è disattivo commento: {37,} e  se la variabile SubClass_C3_variabile_V3 non è  uguale a  commento: {53,} 1, commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  False 
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M5  commento: {73,}
        
        
        
        }
        """
        #  /*37,*/  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C3_timer_T2 è disattivo /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  uguale a  /*53,*/ 1, /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  False 
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M5
        if db((db(self.get_subclass_c3_variabile_v3() == 6, self.dbs[41].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c3_variabile_v3() == 6, self.dbs[41].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[41].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t2().isDisattivato(), self.dbs[41].subs[0].subs[1].subs[0].subs[1])), self.dbs[41].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v3() == 1, self.dbs[41].subs[0].subs[1].subs[1].subs[0]), self.dbs[41].subs[0].subs[1].subs[1])), self.dbs[41].subs[0].subs[1])), self.dbs[41].subs[0]):
            self.set_subclass_c3_comando_c1(False)
        else:
            self.macroSubclass_c3_macroef_m5(self.dbs[41].subs[1])
    
    def effect_NOMINAL_ACTUATION_state5_000(self):
        """
        CNL corrispondente:
         { commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  commento: {34,} o  se il parametro SubClass_C3_parametro_P4 è  maggiore di  commento: {54,} 7 commento: {34,} e  se il parametro SubClass_C3_parametro_P4 è  minore di  commento: {55,} 10 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 141, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M4  commento: {73,}
        
        
         commento: {44,}  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T5 è scaduto commento: {36,} e  se il timer SubClass_C3_timer_T2 non è attivo commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  commento: {36,} o  se il timer SubClass_C3_timer_T2 è disattivo, commento: {69,}Disattiva il timer SubClass_C3_timer_T2
        
           
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  commento: {56,} 1523 commento: {34,} e  se il parametro SubClass_C3_parametro_P1 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 è  uguale a RossoVerde commento: {34,} e  se il parametro SubClass_C3_parametro_P9 è  minore di  commento: {55,} 8 commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  uguale a RossoVerde, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 2
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C3_timer_T5
        
        
         commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C3_lista_L10 è disattivo commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 1504 commento: {37,} e  se la variabile SubClass_C3_variabile_V3 è  uguale a  commento: {53,} 3 commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  minore di  commento: {55,} 1451 commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 non è  maggiore di  commento: {54,} 12230 e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C3_timer_T7
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M4  commento: {73,}
        
        
         }
        """
        #  /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P4 è  maggiore di  /*54,*/ 7 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  minore di  /*55,*/ 10 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 141, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M4
        if db((db((db((db(self.get_subclass_c3_restoreva_rv1_restore() == True, self.dbs[42].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c3_parametro_p4() > 7, self.dbs[42].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_parametro_p4() < 10, self.dbs[42].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[42].subs[0].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_timer_t7().isAttivato(), self.dbs[42].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[42].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[42].subs[0].subs[0].subs[1].subs[1])), self.dbs[42].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co5().get_valore() == 141, self.dbs[42].subs[0].subs[1].subs[0]), self.dbs[42].subs[0].subs[1])), self.dbs[42].subs[0]):
            self.get_subclass_c3_contatore_co3().incrementa()
        else:
            self.macroSubclass_c3_macroef_m4(self.dbs[42].subs[1])
        #  /*73,*/
        #   /*44,*/  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T5 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T2 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C3_timer_T2 è disattivo, /*69,*/Disattiva il timer SubClass_C3_timer_T2
        if db((db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v2() == True, self.dbs[43].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), self.dbs[43].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t5().isScaduto(), self.dbs[43].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[43].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t2().isAttivato(), self.dbs[43].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[43].subs[0].subs[0].subs[0].subs[1])), self.dbs[43].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_controllo_c2() == True, self.dbs[43].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[43].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v10() == False, self.dbs[43].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[43].subs[0].subs[0].subs[1].subs[1])), self.dbs[43].subs[0].subs[0].subs[1])), self.dbs[43].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t2().isDisattivato(), self.dbs[43].subs[0].subs[1])), self.dbs[43].subs[0]):
            self.get_subclass_c3_timer_t2().disattiva()
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 1523 /*34,*/ e  se il parametro SubClass_C3_parametro_P1 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P9 è  minore di  /*55,*/ 8 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  uguale a RossoVerde, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 2
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C3_timer_T5
        if db((db((db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 1523, self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p1() == False, self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[44].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[44].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.rossoverde, self.dbs[44].subs[0].subs[0].subs[0].subs[1])), self.dbs[44].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_parametro_p9() < 8, self.dbs[44].subs[0].subs[0].subs[1])), self.dbs[44].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c4() == GlobalEnumeration.rossoverde, self.dbs[44].subs[0].subs[1])), self.dbs[44].subs[0]):
            self.set_subclass_c3_variabile_v3(2)
        else:
            self.get_subclass_c3_timer_t5().attiva()
        #  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C3_lista_L10 è disattivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 1504 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 1451 /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 non è  maggiore di  /*54,*/ 12230 e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C3_timer_T7
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M4
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t10().isDisattivato(), self.dbs[45].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[45].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c3_contatore_co3().get_valore() == 1504, self.dbs[45].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v3() == 3, self.dbs[45].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[45].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_contatore_co9().get_valore() < 1451, self.dbs[45].subs[0].subs[0].subs[1].subs[1])), self.dbs[45].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_contatore_co5().get_valore() > 12230, self.dbs[45].subs[0].subs[1].subs[0].subs[0]), self.dbs[45].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[45].subs[0].subs[1].subs[1])), self.dbs[45].subs[0].subs[1])), self.dbs[45].subs[0]):
            self.get_subclass_c3_timer_t7().attiva()
        else:
            self.macroSubclass_c3_macroef_m4(self.dbs[45].subs[1])
    
    def effect_NOMINAL_ACTUATION_state5_001(self):
        """
        CNL corrispondente:
         { commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da RossoGialloaVerdea commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  diverso da  False ,  Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
           
         commento: {34,}  se il parametro SubClass_C3_parametro_P1 è  diverso da  True  commento: {36,} o  se il timer SubClass_C3_timer_T5 è disattivo commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 3
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 8
        
        
          se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {69,}Disattiva il timer SubClass_C3_timer_T2
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T2
        
        
         }
        """
        #  /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  diverso da  False ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M1
        if db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, self.dbs[46].subs[0].subs[0].subs[0].subs[0][idx]), self.dbs[46].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[46].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c2() == False, self.dbs[46].subs[0].subs[1].subs[0]), self.dbs[46].subs[0].subs[1])), self.dbs[46].subs[0]):
            self.macroSubclass_c3_macroef_m1(self.dbs[46].subs[1])
        #  /*73,*/
        #     
        #   /*34,*/  se il parametro SubClass_C3_parametro_P1 è  diverso da  True  /*36,*/ o  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 3
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 8
        if db((db((db(not db(self.get_subclass_c3_parametro_p1() == True, self.dbs[47].subs[0].subs[0].subs[0].subs[0]), self.dbs[47].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t5().isDisattivato(), self.dbs[47].subs[0].subs[0].subs[1])), self.dbs[47].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[47].subs[0].subs[1].subs[0]), self.dbs[47].subs[0].subs[1])), self.dbs[47].subs[0]):
            self.set_subclass_c3_variabile_v3(3)
        else:
            self.set_subclass_c3_variabile_v3(8)
        #  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/, /*69,*/Disattiva il timer SubClass_C3_timer_T2
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T2
        if db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, self.dbs[48].subs[0]):
            self.get_subclass_c3_timer_t2().disattiva()
        else:
            self.get_subclass_c3_timer_t2().disattiva()
    
    def effect_NOMINAL_ACTUATION_state5_state1_000(self):
        """
        CNL corrispondente:
         { commento: {44,}  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  minore di  commento: {55,} 12 commento: {34,} o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
        
           
          se la macro  SubClass_C3_macrova_M6 ( con argomento_a5   uguale a True ,argomento_a9   uguale a c120x  e argomento_a6   uguale a RossoVerde )   è  diverso da AC commento: {40,}  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 è  diverso da  commento: {56,} 6 commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co5
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
        
         commento: {34,}  se il parametro SubClass_C3_parametro_P4 non è  minore di  commento: {55,} 3,  commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  True , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co8 del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,} 1145, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co3
        
        
         commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  maggiore di  commento: {54,} 111230 commento: {34,} e  se il parametro SubClass_C3_parametro_P4 è  maggiore di  commento: {54,} 3 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 154, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T7
        
        
         }
        """
        #  /*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False
        if db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v10() == False, self.dbs[49].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), self.dbs[49].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), self.dbs[49].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co9().get_valore() < 12, self.dbs[49].subs[0].subs[0].subs[1])), self.dbs[49].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[49].subs[0].subs[1].subs[0]), self.dbs[49].subs[0].subs[1])), self.dbs[49].subs[0]):
            self.set_subclass_c3_variabile_v8(False)
        #  se la macro  SubClass_C3_macrova_M6 ( con argomento_a5   uguale a True ,argomento_a9   uguale a c120x  e argomento_a6   uguale a RossoVerde )   è  diverso da AC /*40,*/  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  diverso da  /*56,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , /*70,*/Incrementa il contatore SubClass_C3_contatore_Co5
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M1
        if db((db((db((db(not db(db(self.macroSubclass_c3_macrova_m6(True,GlobalEnumeration.rossoverde,GlobalEnumeration.c120x, self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.ac, self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[50].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p4() == 6, self.dbs[50].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[50].subs[0].subs[0].subs[0].subs[1])), self.dbs[50].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v8() == True, self.dbs[50].subs[0].subs[0].subs[1].subs[0]), self.dbs[50].subs[0].subs[0].subs[1])), self.dbs[50].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v8() == True, self.dbs[50].subs[0].subs[1].subs[0].subs[0]), self.dbs[50].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v8() == False, self.dbs[50].subs[0].subs[1].subs[1].subs[0]), self.dbs[50].subs[0].subs[1].subs[1])), self.dbs[50].subs[0].subs[1])), self.dbs[50].subs[0]):
            self.get_subclass_c3_contatore_co5().incrementa()
        else:
            self.macroSubclass_c3_macroef_m1(self.dbs[50].subs[1])
        #  /*73,*/
        #   /*34,*/  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 3,  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co8 del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/ 1145, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C3_contatore_Co3
        if db((db(not db(self.get_subclass_c3_parametro_p4() < 3, self.dbs[51].subs[0].subs[0].subs[0]), self.dbs[51].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == True, self.dbs[51].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), self.dbs[51].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() == 1145, self.dbs[51].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[51].subs[0].subs[1])), self.dbs[51].subs[0]):
            self.set_subclass_c3_comando_c5(GlobalEnumeration.rossoverde)
        else:
            self.get_subclass_c3_contatore_co3().decrementa()
        #  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  maggiore di  /*54,*/ 111230 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 è  maggiore di  /*54,*/ 3 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 154, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T7
        if db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() > 111230, self.dbs[52].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), self.dbs[52].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_parametro_p4() > 3, self.dbs[52].subs[0].subs[0].subs[1])), self.dbs[52].subs[0].subs[0]) or db(self.get_subclass_c3_contatore_co3().get_valore() > 154, self.dbs[52].subs[0].subs[1])), self.dbs[52].subs[0]):
            self.set_subclass_c3_comando_c5(GlobalEnumeration.rossoverde)
        else:
            self.get_subclass_c3_timer_t7().disattiva()
    
    def effect_NOMINAL_ACTUATION_state5_state2_000(self):
        """
        CNL corrispondente:
         {  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  commento: {54,} 12 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  minore di  commento: {55,} 135 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False , commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co3
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
        
          se il controllo ConsDef  è  uguale a FALSE ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C3_timer_T7 non è disattivo commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 è  maggiore di  commento: {54,} 131, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co9
        
           
         }
        """
        #  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 12 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 135 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False , /*71,*/Decrementa il contatore SubClass_C3_contatore_Co3
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M1
        if db((db((db((db((db(self.get_consdef() == False, self.dbs[53].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[53].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[53].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.rossoverde, self.dbs[53].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[53].subs[0].subs[0].subs[0].subs[1])), self.dbs[53].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co9().get_valore() > 12, self.dbs[53].subs[0].subs[0].subs[1].subs[0]), self.dbs[53].subs[0].subs[0].subs[1])), self.dbs[53].subs[0].subs[0]) or db((db(self.get_subclass_c3_contatore_co3().get_valore() < 135, self.dbs[53].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_variabile_v8() == False, self.dbs[53].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[53].subs[0].subs[1].subs[1].subs[0]), self.dbs[53].subs[0].subs[1].subs[1])), self.dbs[53].subs[0].subs[1])), self.dbs[53].subs[0]):
            self.get_subclass_c3_contatore_co3().decrementa()
        else:
            self.macroSubclass_c3_macroef_m1(self.dbs[53].subs[1])
        #  /*73,*/
        #    se il controllo ConsDef  è  uguale a FALSE ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 è  maggiore di  /*54,*/ 131, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co9
        if db((db((db((db((db((db(self.get_consdef() == False, self.dbs[54].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[54].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8()) if db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == 7, self.dbs[54].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[54].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[54].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v8() == True, self.dbs[54].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[54].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[54].subs[0].subs[0].subs[0].subs[1])), self.dbs[54].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t7().isDisattivato(), self.dbs[54].subs[0].subs[0].subs[1].subs[0]), self.dbs[54].subs[0].subs[0].subs[1])), self.dbs[54].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co9().get_valore() > 131, self.dbs[54].subs[0].subs[1])), self.dbs[54].subs[0]):
            self.get_subclass_c3_contatore_co9().incrementa()
    
    def effect_NOMINAL_ACTUATION_state5_state4_000(self):
        """
        CNL corrispondente:
         { commento: {36,}  se il timer SubClass_C3_timer_T7 è disattivo commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x commento: {34,} o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, commento: {66,} Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        
         ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
        
        
         commento: {35,}  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {36,} e  se il timer SubClass_C3_timer_T2 è disattivo, commento: {69,}Disattiva il timer SubClass_C3_timer_T10
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        
        
         }
        """
        #  /*36,*/  se il timer SubClass_C3_timer_T7 è disattivo /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P2 non è  uguale a c120x, /*66,*/ Assegna al comando SubClass_C3_comando_C5 il valore RossoVerde
        #   ,altrimenti  /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3
        if db((db((db(self.get_subclass_c3_timer_t7().isDisattivato(), self.dbs[55].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[55].subs[0].subs[0].subs[1].subs[0]), self.dbs[55].subs[0].subs[0].subs[1])), self.dbs[55].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, self.dbs[55].subs[0].subs[1].subs[0]), self.dbs[55].subs[0].subs[1])), self.dbs[55].subs[0]):
            self.set_subclass_c3_comando_c5(GlobalEnumeration.rossoverde)
        else:
            self.get_subclass_c3_contatore_co3().incrementa()
        #  /*35,*/  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*36,*/ e  se il timer SubClass_C3_timer_T2 è disattivo, /*69,*/Disattiva il timer SubClass_C3_timer_T10
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
        if db((db((db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[56].subs[0].subs[0].subs[0].subs[0]), self.dbs[56].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[56].subs[0].subs[0].subs[1])), self.dbs[56].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c3_controllo_c2() == False, self.dbs[56].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[56].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, self.dbs[56].subs[0].subs[1].subs[0].subs[1])), self.dbs[56].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_timer_t2().isDisattivato(), self.dbs[56].subs[0].subs[1].subs[1])), self.dbs[56].subs[0].subs[1])), self.dbs[56].subs[0]):
            self.get_subclass_c3_timer_t10().disattiva()
        else:
            self.set_subclass_c3_variabile_v8(True)
    
    # effect macros
    def macroSubclass_c3_macroef_m1(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {37,}  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , commento: {69,}Disattiva il timer SubClass_C3_timer_T7
        
           
         commento: {35,}  se il controllo SubClass_C3_controllo_C2 è  diverso da  True , commento: {68,}Attiva il timer SubClass_C3_timer_T5
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è scaduto commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  commento: {54,} 8 commento: {35,} e  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 1530 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co5
        
         ,altrimenti  commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
        
        
         commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore SubClass_C3_contatore_Co3
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
        
        
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  commento: {53,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  commento: {54,} 1245, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
        
           
        
        }
        """
        def populate_macroSubclass_c3_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , /*69,*/Disattiva il timer SubClass_C3_timer_T7""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V10 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C3_controllo_C2 è  diverso da  True , /*68,*/Attiva il timer SubClass_C3_timer_T5""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C2 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 8 /*35,*/ e  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 1530 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, /*71,*/Decrementa il contatore SubClass_C3_contatore_Co5

 ,altrimenti  /*72,*/Azzera il contatore SubClass_C3_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 8 /*35,*/ e  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 1530 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( negazione di (il timer 'subclass_c3_restoreti_ti2_restore' è scaduto) )  e  ( negazione di ((subclass_c3_parametro_p4)  è maggiore di  (8)) ) )  e  ( negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)) ) )  e  ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) ) )  e  
( (subclass_c3_contatore_co3)  è maggiore di  (1530) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (il timer 'subclass_c3_restoreti_ti2_restore' è scaduto) )  e  ( negazione di ((subclass_c3_parametro_p4)  è maggiore di  (8)) ) )  e  ( negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)) ) )  e  ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c3_restoreti_ti2_restore' è scaduto) )  e  ( negazione di ((subclass_c3_parametro_p4)  è maggiore di  (8)) ) )  e  ( negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c3_restoreti_ti2_restore' è scaduto) )  e  ( negazione di ((subclass_c3_parametro_p4)  è maggiore di  (8)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_restoreti_ti2_restore' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti2_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è maggiore di  (8))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_parametro_p4)  è maggiore di  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co3)  è maggiore di  (1530)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore SubClass_C3_contatore_Co3

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c3_restoreva_rv1_restore)  è uguale a  (False) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (subclass_c3_controllo_c10)  è uguale a  (c120x) )  e  ( negazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x)) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c3_controllo_c10)  è uguale a  (c120x) )  e  ( negazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x)) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_controllo_c10)  è uguale a  (c120x) )  e  ( negazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p2)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 1245, /*72,*/Azzera il contatore SubClass_C3_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 1245""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))} )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l8')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) ) )  e  
( negazione di ((subclass_c3_contatore_co9)  è maggiore di  (1245)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co9)  è maggiore di  (1245))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co9)  è maggiore di  (1245)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroSubclass_c3_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  /*37,*/  se la variabile SubClass_C3_variabile_V10 è  diverso da  False , /*69,*/Disattiva il timer SubClass_C3_timer_T7
        if db(not db(self.get_subclass_c3_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.get_subclass_c3_timer_t7().disattiva()
        #  /*35,*/  se il controllo SubClass_C3_controllo_C2 è  diverso da  True , /*68,*/Attiva il timer SubClass_C3_timer_T5
        if db(not db(self.get_subclass_c3_controllo_c2() == True, di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.get_subclass_c3_timer_t5().attiva()
        #  /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è scaduto /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 8 /*35,*/ e  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 1530 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x, /*71,*/Decrementa il contatore SubClass_C3_contatore_Co5
        #   ,altrimenti  /*72,*/Azzera il contatore SubClass_C3_contatore_Co5
        if db((db((db((db((db((db(not db(self.get_subclass_c3_restoreti_ti2_restore().isScaduto(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p4() > 8, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co3().get_valore() > 1530, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c3_contatore_co5().decrementa()
        else:
            self.get_subclass_c3_contatore_co5().resetta()
        #  /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore SubClass_C3_contatore_Co3
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V3 il valore 1
        if db((db((db(self.get_subclass_c3_restoreva_rv1_restore() == False, di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c3_contatore_co3().resetta()
        else:
            self.set_subclass_c3_variabile_v3(1)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  maggiore di  /*54,*/ 1245, /*72,*/Azzera il contatore SubClass_C3_contatore_Co5
        if db((db((db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[4].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_contatore_co9().get_valore() > 1245, di_ctx.subs[4].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.get_subclass_c3_contatore_co5().resetta()
    
    def macroSubclass_c3_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  uguale a  commento: {53,} 12123 commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  commento: {54,} 9 commento: {37,} o  se la variabile SubClass_C3_variabile_V3 è  uguale a  commento: {53,} 10, commento: {68,}Attiva il timer SubClass_C3_timer_T2
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  False 
        
        
         commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 1 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C1 il valore  True 
        
        
         commento: {36,}  se il timer SubClass_C3_timer_T2 non è scaduto,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1  commento: {37,} o  se la variabile SubClass_C3_variabile_V3 non è  diverso da  commento: {56,} 9 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 150, commento: {68,}Attiva il timer SubClass_C3_timer_T2
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
        
         commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a RossoGialloaVerdea commento: {36,} o  se il timer SubClass_C3_timer_T7 è scaduto, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co3
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  uguale a  /*53,*/ 12123 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 10, /*68,*/Attiva il timer SubClass_C3_timer_T2

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  uguale a  /*53,*/ 12123 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( (subclass_c3_contatore_co5)  è uguale a  (12123) ) )  e  
( negazione di ((subclass_c3_parametro_p4)  è maggiore di  (9)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( (subclass_c3_contatore_co5)  è uguale a  (12123) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co5)  è uguale a  (12123)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è maggiore di  (9))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_parametro_p4)  è maggiore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v3)  è uguale a  (10)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True))} )  o  
( ( ( ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (1))) ) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (1))) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (1))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (1))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V3 non è  diverso da  /*56,*/ 9 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 150, /*68,*/Attiva il timer SubClass_C3_timer_T2

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V3 non è  diverso da  /*56,*/ 9 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 150""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'subclass_c3_timer_t2' è scaduto) )  e  
( per ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)))} ) )  o  
( ( negazione di (negazione di ((subclass_c3_variabile_v3)  è uguale a  (9))) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c3_timer_t2' è scaduto) )  e  
( per ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t2' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l10')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c3_variabile_v3)  è uguale a  (9))) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_variabile_v3)  è uguale a  (9)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v3)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v3)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_variabile_v8)  è uguale a  (False)) )  e  
( (subclass_c3_contatore_co3)  è uguale a  (150) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (150)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*73,*/


 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a RossoGialloaVerdea /*36,*/ o  se il timer SubClass_C3_timer_T7 è scaduto, /*72,*/Azzera il contatore SubClass_C3_contatore_Co3

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a RossoGialloaVerdea /*36,*/ o  se il timer SubClass_C3_timer_T7 è scaduto""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (rossogialloaverdea))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è scaduto""", [
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c3_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  uguale a  /*53,*/ 12123 /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  maggiore di  /*54,*/ 9 /*37,*/ o  se la variabile SubClass_C3_variabile_V3 è  uguale a  /*53,*/ 10, /*68,*/Attiva il timer SubClass_C3_timer_T2
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  False
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co5().get_valore() == 12123, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p4() > 9, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v3() == 10, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c3_timer_t2().attiva()
        else:
            self.set_subclass_c3_comando_c1(False)
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C1 il valore  True
        if db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p4() == 1, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t7().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c3_variabile_v8(False)
        else:
            self.set_subclass_c3_comando_c1(True)
        #  /*36,*/  se il timer SubClass_C3_timer_T2 non è scaduto,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C3_variabile_V3 non è  diverso da  /*56,*/ 9 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 150, /*68,*/Attiva il timer SubClass_C3_timer_T2
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M1
        if db((db((db((db(not db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c3_variabile_v3() == 9, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v8() == False, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_contatore_co3().get_valore() == 150, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c3_timer_t2().attiva()
        else:
            self.macroSubclass_c3_macroef_m1(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #   /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a RossoGialloaVerdea /*36,*/ o  se il timer SubClass_C3_timer_T7 è scaduto, /*72,*/Azzera il contatore SubClass_C3_contatore_Co3
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False
        if db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[3].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t7().isScaduto(), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c3_contatore_co3().resetta()
        else:
            self.set_subclass_c3_variabile_v8(False)
    
    def macroSubclass_c3_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P7 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  diverso da  commento: {56,} 7, commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co3
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
        
          se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        
           
        
        }
        """
        def populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P7 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  /*56,*/ 7, /*71,*/Decrementa il contatore SubClass_C3_contatore_Co3

 ,altrimenti   Applica gli effetti
       della macro SubClass_C3_macroef_M1""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P7 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p7 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p7 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*41,*/  se MainClass_C1_parametro_P7 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  diverso da  /*56,*/ 7, /*71,*/Decrementa il contatore SubClass_C3_contatore_Co3
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C3_macroef_M1
        if db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p7() == 7, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), di_ctx.subs[0].subs[0]):
            self.get_subclass_c3_contatore_co3().decrementa()
        else:
            self.macroSubclass_c3_macroef_m1(di_ctx.subs[0].subs[1])
        #  /*73,*/
        #    se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
        if db(self.get_consdef() == False, di_ctx.subs[1].subs[0]):
            self.set_subclass_c3_variabile_v8(True)
    
    def macroSubclass_c3_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 6 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C3_variabile_V3 è  minore di  commento: {55,} 9,  Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 6 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  minore di  /*55,*/ 9,  Applica gli effetti
       della macro SubClass_C3_macroef_M1  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 6 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (6))) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_parametro_p4)  è uguale a  (6)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v3)  è minore di  (9)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 6 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C3_variabile_V3 è  minore di  /*55,*/ 9,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M1  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
        if db((db((db(not db(not db(self.get_subclass_c3_parametro_p4() == 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v3() < 9, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c3_macroef_m1(di_ctx.subs[0].subs[1])
        else:
            self.set_subclass_c3_variabile_v8(True)
    
    def macroSubclass_c3_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  commento: {105,} è  uguale a  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  minore di  commento: {55,} 134 commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  diverso da  commento: {56,} 125, commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 1112 commento: {34,} e  se il parametro SubClass_C3_parametro_P3 non è  uguale a  commento: {53,} 6 o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro SubClass_C3_macroef_M2  commento: {73,}
        
         ,altrimenti  commento: {72,}Azzera il contatore SubClass_C3_contatore_Co5
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 134 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  diverso da  /*56,*/ 125, /*72,*/Azzera il contatore SubClass_C3_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 134 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  diverso da  /*56,*/ 125""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (True))} )  o  
( ( ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )  e  ( (subclass_c3_contatore_co3)  è minore di  (134) ) )  e  
( (subclass_c3_variabile_v8)  è uguale a  (True) ) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (True))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )  e  ( (subclass_c3_contatore_co3)  è minore di  (134) ) )  e  
( (subclass_c3_variabile_v8)  è uguale a  (True) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))) )  e  ( (subclass_c3_contatore_co3)  è minore di  (134) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co3)  è minore di  (134)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è uguale a  (125))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (125)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 1112 /*34,*/ e  se il parametro SubClass_C3_parametro_P3 non è  uguale a  /*53,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro SubClass_C3_macroef_M2  /*73,*/

 ,altrimenti  /*72,*/Azzera il contatore SubClass_C3_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 1112 /*34,*/ e  se il parametro SubClass_C3_parametro_P3 non è  uguale a  /*53,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c3_restoreva_rv1_restore)  è uguale a  (False) )  o  
( ( (subclass_c3_contatore_co3)  è uguale a  (1112) )  e  
( negazione di ((subclass_c3_parametro_p3)  è uguale a  (6)) ) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_contatore_co3)  è uguale a  (1112) )  e  
( negazione di ((subclass_c3_parametro_p3)  è uguale a  (6)) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (1112)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p3)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p3)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M2"""),#1
                            ]),#1
                ])

        populate_macroSubclass_c3_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C3_lista_L10 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  minore di  /*55,*/ 134 /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  diverso da  /*56,*/ 125, /*72,*/Azzera il contatore SubClass_C3_contatore_Co5
        if db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co3().get_valore() < 134, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 125, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c3_contatore_co5().resetta()
        #  /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 1112 /*34,*/ e  se il parametro SubClass_C3_parametro_P3 non è  uguale a  /*53,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M2  /*73,*/
        #   ,altrimenti  /*72,*/Azzera il contatore SubClass_C3_contatore_Co5
        if db((db((db(self.get_subclass_c3_restoreva_rv1_restore() == False, di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c3_contatore_co3().get_valore() == 1112, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_parametro_p3() == 6, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.macroSubclass_c3_macroef_m2(di_ctx.subs[1].subs[1])
        else:
            self.get_subclass_c3_contatore_co5().resetta()
    
    # verify macros
    @srf_value_macro("macroSubclass_c3_macrove_m4")
    def macroSubclass_c3_macrove_m4(self, argomento_ave1, argomento_ave10, argomento_ave4, argomento_ave5, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {36,}  se il timer SubClass_C3_timer_T5 è disattivo commento: {35,} o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde commento: {36,} o  se il timer SubClass_C3_timer_T2 è attivo commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False  commento: {35,} e  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
         commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  commento: {53,} 11512 commento: {35,} o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T7 è attivo commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  commento: {53,} 1130 commento: {35,} o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde, Tutte le seguenti { 
          se l'argomento argomento_ave4 non  è  uguale a  False  commento: {39,}  commento: {37,} o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C3_timer_T7 sia attivo
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C3_timer_T7 sia attivo
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  commento: {53,} 134
        
        
         } Verifica che   commento: {50,51,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  commento: {54,} 1
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 1130 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde, Tutte le seguenti { 
  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C3_timer_T7 sia attivo


 } Verifica che   /*48,51,*/  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 134


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x, Solo una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 1130 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde, Tutte le seguenti { 
  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C3_timer_T7 sia attivo


 } Verifica che   /*48,51,*/  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 134


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde /*36,*/ o  se il timer SubClass_C3_timer_T2 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T5 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C2 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C2 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C6 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T2 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V8 non è  diverso da  False  /*35,*/ e  se il controllo SubClass_C3_controllo_C10 non è  uguale a c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C10 non è  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 1130 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde, Tutte le seguenti { 
  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C3_timer_T7 sia attivo


 } Verifica che   /*48,51,*/  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 134


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 1130 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde, Tutte le seguenti { 
  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C3_timer_T7 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 1130 /*35,*/ o  se il controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 1130""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512 /*35,*/ o  se il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C3_lista_L8 è  uguale a  /*53,*/ 11512""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (11512)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C2 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C2 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T7 è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co3 non è  uguale a  /*53,*/ 1130""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (1130)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C4 è  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C3_timer_T7 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V10 non è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 non  è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V10 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C3_timer_T7 sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C3_timer_T7 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C3_timer_T7 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 134""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 134""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (134)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(self.get_subclass_c3_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c3_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c3_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() == 11512, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 1130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c4() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c3_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c3_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db(not db(self.get_subclass_c3_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 134, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_subclass_c3_contatore_co3().get_valore() > 1, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m5")
    def macroSubclass_c3_macrove_m5(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,} commento: {38,}  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 14 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 111 commento: {37,} o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  commento: {34,} o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  minore di  commento: {55,} 9 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x commento: {34,} o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  commento: {56,} 2 commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  commento: {56,} 11230 commento: {35,} e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde, Tutte le seguenti { 
         commento: {63,} commento: {38,}  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  commento: {56,} 124 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 135 commento: {35,} o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
         commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  commento: {105,} è  uguale a RossoGialloVerde commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x commento: {35,} e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x commento: {37,} o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   commento: {48,50,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V3 sia  uguale a  commento: {53,} 7
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 
        
        
         } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co3 sia  diverso da  commento: {56,} 151
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P9 non sia  minore di  commento: {55,} 2
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P4 non sia  diverso da  commento: {56,} 5
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 111 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230 /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 111 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230 /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 111 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True  /*34,*/ o  se il parametro SubClass_C3_parametro_P1 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 111 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 111""", [
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 14""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 111""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C3_parametro_P1 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P1 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230 /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230 /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230 /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C3_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P4 non è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p4)  è minore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C10 è  uguale a c120x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230 /*35,*/ e  se il controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2 /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P4 non è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 11230""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co9)  è uguale a  (11230))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co9)  è uguale a  (11230)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C6 è  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c6)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è scaduto, Solo una delle seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 è  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co9 non è  diverso da  /*56,*/ 124""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co9)  è uguale a  (124))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co9)  è uguale a  (124)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C10 non è  diverso da c120x /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C10 non è  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 135""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C10 è  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False , Verifica che   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x /*37,*/ o  se la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x /*35,*/ e  se il controllo SubClass_C3_controllo_C2 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde /*34,*/ e  se il parametro SubClass_C3_parametro_P2 è  uguale a c120x""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C3_lista_L8 esiste e  /*105,*/ è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c3_lista_l8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C3_parametro_P2 è  uguale a c120x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C2 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P2 è  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p2)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V10 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V10 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V10 è  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,50,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C3_variabile_V3 sia  uguale a  /*53,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C10 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 sia  diverso da  /*56,*/ 151""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (151)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P9 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p9)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p4)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C3_controllo_C4 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c4)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c4)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(self.get_subclass_c3_contatore_co3().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_contatore_co3().get_valore() == 111, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c3_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_subclass_c3_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p4() < 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c3_parametro_p4() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_contatore_co9().get_valore() == 11230, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_controllo_c6() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(not db(self.get_subclass_c3_contatore_co9().get_valore() == 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_contatore_co3().get_valore() > 135, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p2() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c3_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v3() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c3_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db((db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 151, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p9() < 2, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c3_parametro_p4() == 5, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c3_controllo_c4() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v8() == False, di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m7")
    def macroSubclass_c3_macrove_m7(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto commento: {38,} o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 131230 commento: {36,} o  se il timer SubClass_C3_timer_T2 è disattivo, Tutte le seguenti { 
         commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C3_timer_T2 è scaduto commento: {37,} e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {38,}  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  commento: {53,} 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  commento: {55,} 11512 commento: {37,} e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  commento: {54,} 6 commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   commento: {48,50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  commento: {53,} 15
         commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T7 sia disattivo
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  commento: {54,} 15
        
        
         } Verifica che   commento: {47,48,50,}  commento: {,}  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P4 non sia  minore di  commento: {55,} 2
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P4 sia  diverso da  commento: {56,} 5
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 131230 /*36,*/ o  se il timer SubClass_C3_timer_T2 è disattivo, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 15


 } Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P4 sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 131230 /*36,*/ o  se il timer SubClass_C3_timer_T2 è disattivo, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 15


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 131230 /*36,*/ o  se il timer SubClass_C3_timer_T2 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 131230""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C3_restoreTI_TI5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti5_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 131230""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co5)  è uguale a  (131230)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T2 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 15


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C3_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C3_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C3_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V10 è  uguale a  True""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T2 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V10 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True , Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512 /*37,*/ e  se la variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co9 non è  uguale a  /*53,*/ 124""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co9)  è uguale a  (124)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co3 non è  minore di  /*55,*/ 11512""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co3)  è minore di  (11512)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V3 non è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v3)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 15
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co3 non sia  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T7 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore SubClass_C3_contatore_Co3 sia  maggiore di  /*54,*/ 15""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P4 sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P4 sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P4 sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P4 sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*,*/  il controllo SubClass_C3_controllo_C10 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c10)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c10)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P4 sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P4 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p4)  è minore di  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P4 sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p4)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_subclass_c3_restoreti_ti5_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_contatore_co5().get_valore() == 131230, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c3_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db((db(not db(self.get_subclass_c3_contatore_co9().get_valore() == 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co3().get_valore() < 11512, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v3() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c3_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db((db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c3_contatore_co3().get_valore() > 15, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(not db(not db(self.get_subclass_c3_controllo_c10() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_parametro_p4() < 2, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_parametro_p4() == 5, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m9")
    def macroSubclass_c3_macrove_m9(self, argomento_ave1, argomento_ave3, argomento_ave4, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  commento: {56,} 11451 commento: {38,} e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  commento: {56,} 13 o  se l'argomento argomento_ave7 è  uguale a  True  commento: {39,} , Verifica che   commento: {48,49,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co5 sia  uguale a  commento: {53,} 112
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T7 non sia disattivo
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 11451 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 13 o  se l'argomento argomento_ave7 è  uguale a  True  /*39,*/ , Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 sia  uguale a  /*53,*/ 112
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 11451 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 13 o  se l'argomento argomento_ave7 è  uguale a  True  /*39,*/ , Verifica che   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 sia  uguale a  /*53,*/ 112
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 11451 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 13 o  se l'argomento argomento_ave7 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 11451 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 11451 /*38,*/ e  se il contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 11451""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è uguale a  (11451))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (11451)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co5 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co5)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave7 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 sia  uguale a  /*53,*/ 112
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 sia  uguale a  /*53,*/ 112
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co5 sia  uguale a  /*53,*/ 112""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_subclass_c3_restoreva_rv1_restore() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 11451, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_contatore_co5().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave7 == True, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c3_contatore_co5().get_valore() == 112, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c3_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c3_macrova_m2")
    def macroSubclass_c3_macrova_m2(self, argomento_a1, argomento_a10, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m2_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c3_macrova_m2_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c3_macrova_m6")
    def macroSubclass_c3_macrova_m6(self, argomento_a5, argomento_a6, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore AC commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c3_macrova_m6_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore AC
        return GlobalEnumeration.ac
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c3_previousco_c3_prev(self.get_subclass_c3_previousco_c3())
        self.set_subclass_c3_previousco_c7_prev(self.get_subclass_c3_previousco_c7())
        self.set_subclass_c3_previousco_c8_prev(self.get_subclass_c3_previousco_c8())
        self.set_subclass_c3_previousco_c9_prev(self.get_subclass_c3_previousco_c9())
        self.set_subclass_c3_previousva_pv1_prev(self.get_subclass_c3_previousva_pv1())
        self.set_subclass_c3_previousva_pv2_prev(self.get_subclass_c3_previousva_pv2())
        self.set_subclass_c3_previousva_pv3_prev(self.get_subclass_c3_previousva_pv3())
        self.set_subclass_c3_previousva_pv4_prev(self.get_subclass_c3_previousva_pv4())

class SubClass_C3_RecordHeaderR10(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled11, recordfiled20):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled11(recordfiled11)
        self.set_recordfiled20(recordfiled20)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled11(self, recordfiled11):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"), recordfiled11)

    def set_recordfiled20(self, recordfiled20):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"), recordfiled20)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled11(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"))

    def get_recordfiled20(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"))



class SubClass_C3_RecordHeaderR8(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled16, recordfiled3):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled16(recordfiled16)
        self.set_recordfiled3(recordfiled3)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled16(self, recordfiled16):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled16"), recordfiled16)

    def set_recordfiled3(self, recordfiled3):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"), recordfiled3)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled16(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled16"))

    def get_recordfiled3(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"))



