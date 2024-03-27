# Codice del modello 'TestCase4', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_subclass_c2_previousva_pv1(GlobalEnumeration.avanzamento)
        self.set_subclass_c2_previousva_pv2(0)
        self.set_subclass_c2_previousva_pv3(GlobalEnumeration.avanzamento)
        self.set_subclass_c2_restoreva_rv1(GlobalEnumeration.avanzamento)
        self.set_subclass_c2_restoreva_rv2(0)
        self.set_subclass_c2_restoreva_rv3(0)
        self.set_subclass_c2_variabile_v10(0)
        self.set_subclass_c2_variabile_v4(False)
        self.set_subclass_c2_variabile_v6(GlobalEnumeration.giallogiallo)
        self.set_subclass_c2_variabile_v7(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
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
        _State1__State1__stateSheet_0__permanence = 1
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_0 = 2

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c2_lista_l1, subclass_c2_lista_l2, subclass_c2_parametro_p1, subclass_c2_parametro_p2, subclass_c2_parametro_p5, subclass_c2_parametro_p9):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l1(subclass_c2_lista_l1)
        self.set_subclass_c2_lista_l2(subclass_c2_lista_l2)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p1(subclass_c2_parametro_p1)
        self.set_subclass_c2_parametro_p2(subclass_c2_parametro_p2)
        self.set_subclass_c2_parametro_p5(subclass_c2_parametro_p5)
        self.set_subclass_c2_parametro_p9(subclass_c2_parametro_p9)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(4245000)
        self.set_subclass_c2_restoreti_ti1_restore(4245000)
        self.set_subclass_c2_restoreti_ti2(530000)
        self.set_subclass_c2_restoreti_ti2_restore(530000)
        self.set_subclass_c2_restoreti_ti3(4124000)
        self.set_subclass_c2_restoreti_ti3_restore(4124000)
        self.set_subclass_c2_restoreti_ti4(1000)
        self.set_subclass_c2_restoreti_ti4_restore(1000)
        self.set_subclass_c2_restoreti_ti5(25000)
        self.set_subclass_c2_restoreti_ti5_restore(25000)
        self.set_subclass_c2_timer_t4(53000)
        self.set_subclass_c2_timer_t7(101000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_restoreti_ti3,self.subclass_c2_restoreti_ti3_restore,self.subclass_c2_restoreti_ti4,self.subclass_c2_restoreti_ti4_restore,self.subclass_c2_restoreti_ti5,self.subclass_c2_restoreti_ti5_restore,self.subclass_c2_timer_t4,self.subclass_c2_timer_t7,]

        # initialize the counters
        self.set_subclass_c2_contatore_co7(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l1(self, subclass_c2_lista_l1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l1",subclass_c2_lista_l1)

    def set_subclass_c2_lista_l2(self, subclass_c2_lista_l2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2",subclass_c2_lista_l2)


    # getters for record type parameters
    def get_subclass_c2_lista_l1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l1")

    def get_subclass_c2_lista_l2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p1(self, subclass_c2_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1",subclass_c2_parametro_p1)

    def set_subclass_c2_parametro_p2(self, subclass_c2_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2",subclass_c2_parametro_p2)

    def set_subclass_c2_parametro_p5(self, subclass_c2_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5",subclass_c2_parametro_p5)

    def set_subclass_c2_parametro_p9(self, subclass_c2_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p9",subclass_c2_parametro_p9)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1")

    def get_subclass_c2_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2")

    def get_subclass_c2_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5")

    def get_subclass_c2_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p9")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c1(self, subclass_c2_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c1",subclass_c2_comando_c1)

    def set_subclass_c2_comando_c10(self, subclass_c2_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c10",subclass_c2_comando_c10)

    def set_subclass_c2_comando_c3(self, subclass_c2_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c3",subclass_c2_comando_c3)

    def set_subclass_c2_comando_c5(self, subclass_c2_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c5",subclass_c2_comando_c5)

    def set_subclass_c2_comando_c7(self, subclass_c2_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c7",subclass_c2_comando_c7)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c1")

    def get_subclass_c2_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c2")

    def get_subclass_c2_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c7")

    def get_subclass_c2_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4")

    def get_subclass_c2_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c6")

    def get_subclass_c2_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8")

    def get_subclass_c2_previousco_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c9")


    # setters for state variables
    def set_subclass_c2_previousco_c4_prev(self, subclass_c2_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev",subclass_c2_previousco_c4_prev)
    def set_subclass_c2_previousco_c6_prev(self, subclass_c2_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c6_prev",subclass_c2_previousco_c6_prev)
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
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_restoreva_rv3(self, subclass_c2_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3",subclass_c2_restoreva_rv3)
    def set_subclass_c2_variabile_v10(self, subclass_c2_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v10",subclass_c2_variabile_v10)
    def set_subclass_c2_variabile_v4(self, subclass_c2_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v4",subclass_c2_variabile_v4)
    def set_subclass_c2_variabile_v6(self, subclass_c2_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6",subclass_c2_variabile_v6)
    def set_subclass_c2_variabile_v7(self, subclass_c2_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7",subclass_c2_variabile_v7)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev")

    def get_subclass_c2_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c6_prev")

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

    def get_subclass_c2_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v10")

    def get_subclass_c2_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v4")

    def get_subclass_c2_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6")

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

    def set_subclass_c2_restoreti_ti5(self, timerDuration):
        self.subclass_c2_restoreti_ti5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti5", self.memory)

    def set_subclass_c2_restoreti_ti5_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti5_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti5_restore", self.memory)

    def set_subclass_c2_timer_t4(self, timerDuration):
        self.subclass_c2_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t4", self.memory)

    def set_subclass_c2_timer_t7(self, timerDuration):
        self.subclass_c2_timer_t7 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t7", self.memory)


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

    def get_subclass_c2_restoreti_ti5(self):
        return self.subclass_c2_restoreti_ti5

    def get_subclass_c2_restoreti_ti5_restore(self):
        return self.subclass_c2_restoreti_ti5_restore

    def get_subclass_c2_timer_t4(self):
        return self.subclass_c2_timer_t4

    def get_subclass_c2_timer_t7(self):
        return self.subclass_c2_timer_t7


    # setters for counters
    def set_subclass_c2_contatore_co7(self, counterInitValue):
        self.subclass_c2_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co7", self.memory)


    # getters for counters
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
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#2
                    DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T7 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore  True""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T7 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t7' è inattivo""", [
                    ]),#0
                    ]),#0
                    ]),#3
                    DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  /*56,*/ 6, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  /*56,*/ 6""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1))}""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v10)  è uguale a  (6)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v10)  è uguale a  (6))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v10)  è uguale a  (6)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#4
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
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[4], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[3], ),
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

        self.set_subclass_c2_previousco_c4_prev(GlobalEnumeration.rossoverde)
        self.set_subclass_c2_previousco_c6_prev(GlobalEnumeration.rossoverde)
        self.set_subclass_c2_previousco_c8_prev(GlobalEnumeration.gialloverde)
        self.set_subclass_c2_previousco_c9_prev(GlobalEnumeration.c270)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())

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
                if(self.guard_NOMINAL_ACTUATION_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_PERMANENCE_state1_000()):
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
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state1_000()
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
    
    def guard_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[2])
    
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
        
         commento: {36,}  se il timer SubClass_C2_timer_T7 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore  True 
        
           
        
        }
        """
        #  /*36,*/  se il timer SubClass_C2_timer_T7 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore  True
        if db(not db(self.get_subclass_c2_timer_t7().isDisattivato(), self.dbs[3].subs[0].subs[0]), self.dbs[3].subs[0]):
            self.set_subclass_c2_variabile_v7(True)
    
    def effect_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1  commento: {37,} o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  commento: {56,} 6, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore  False 
        
           
         }
        """
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  /*56,*/ 6, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore  False
        if db((db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[4].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2())), self.dbs[4].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v10() == 6, self.dbs[4].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1])), self.dbs[4].subs[0]):
            self.set_subclass_c2_variabile_v7(False)
    
    # effect macros
    def macroSubclass_c2_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 15124 commento: {37,} o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  commento: {56,} 6 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C2_timer_T7
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore c270
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 15124 /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  /*56,*/ 6 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C2_timer_T7

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 15124 /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  /*56,*/ 6 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  
( negazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (15124))) ) )  o  
( negazione di (negazione di ((subclass_c2_variabile_v10)  è uguale a  (6))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  
( negazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (15124))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (15124)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (15124))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (15124)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v10)  è uguale a  (6)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v10)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v10)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_parametro_p2)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 15124 /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da  /*56,*/ 6 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C2_timer_T7
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore c270
        if db((db((db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 15124, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v10() == 6, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t7().attiva()
        else:
            self.set_subclass_c2_comando_c5(GlobalEnumeration.c270)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m4")
    def macroSubclass_c2_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        {  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 123 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,49,}  commento: {,}  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T7 non sia attivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia disattivo
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T7 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T7 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C7 non è  diverso da GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (123))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (123)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T7 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  uguale a GialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a c270""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T7 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T7 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t7' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 123, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m5")
    def macroSubclass_c2_macrove_m5(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1 , Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P9 non è  uguale a  False , Solo una delle seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 commento: {35,} e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  commento: {54,} 1212
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  diverso da c270
        
        
         } Verifica che   commento: {47,48,49,}  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T7 non sia disattivo
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P9 non è  uguale a  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  /*54,*/ 1212
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  diverso da c270


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P9 non è  uguale a  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  /*54,*/ 1212
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  diverso da c270


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P9 non è  uguale a  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  /*54,*/ 1212
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  diverso da c270


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P9 non è  uguale a  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  /*54,*/ 1212
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  diverso da c270


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P9 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  /*54,*/ 1212
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*35,*/ e  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C2 è  uguale a c120x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C7 è  uguale a GialloVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  /*54,*/ 1212
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  maggiore di  /*54,*/ 1212""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co7)  è maggiore di  (1212)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2())), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() > 1212, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t7().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m6")
    def macroSubclass_c2_macrove_m6(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a  False , Almeno una delle seguenti { 
         commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 141245 commento: {34,} e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 11 commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270, Almeno una delle seguenti { 
         commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  commento: {54,} 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
         commento: {62,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 11, Almeno una delle seguenti { 
         commento: {61,} commento: {36,}  se il timer SubClass_C2_timer_T4 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  commento: {54,} 143, Tutte le seguenti { 
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 commento: {35,} o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,49,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T7 non sia disattivo
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 1501
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270
        
        
         } Verifica che   commento: {47,49,50,}  commento: {,}  il timer SubClass_C2_timer_T7 non sia scaduto
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 
        
        
         } Verifica che   commento: {48,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  commento: {54,} 1224
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V10 sia  uguale a  commento: {53,} 7
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
        
        
         } Verifica che   commento: {48,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 1
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 1230
        
        
         } Verifica che   commento: {47,49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270
        
        
         } Verifica che   commento: {47,48,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a  False , Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270, Almeno una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230


 } Verifica che   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a  False , Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270, Almeno una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230


 } Verifica che   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C1 è  uguale a c270""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270, Almeno una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230


 } Verifica che   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270, Almeno una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230


 } Verifica che   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI3 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245 /*34,*/ e  se il parametro SubClass_C2_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 141245""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (141245)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P1 non è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230


 } Verifica che   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C2_restoreva_RV2 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_restoreva_rv2_restore)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False , Solo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P1 è  diverso da c270 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V4 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 } Verifica che   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P1 non è  uguale a c270 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P1 non è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143, Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  diverso da c120x""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C2 è  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 143""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270 /*35,*/ o  se il controllo SubClass_C2_controllo_C2 è  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 non è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI3 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P1 non è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C2 è  uguale a c120x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1501""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T7 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V4 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V4 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 1224""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a  /*53,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V4 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C2 non sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c2)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 1230""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (1230)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V7 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V4 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C7 sia  uguale a GialloVerde""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c2_restoreti_ti3_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 141245, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_subclass_c2_restoreva_rv2_restore() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co7().get_valore() > 143, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(self.get_subclass_c2_restoreti_ti3_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(not db(self.get_subclass_c2_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co7().get_valore() == 1501, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co7().get_valore() > 1224, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v10() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(self.get_subclass_c2_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co7().get_valore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_controllo_c2() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 1230, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m7")
    def macroSubclass_c2_macrove_m7(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        {  se il controllo ConsDef  è  uguale a FALSE ,  commento: {43,}  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  commento: {55,} 110 commento: {36,} o  se il timer SubClass_C2_timer_T7 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo, Verifica che   commento: {47,48,50,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a RossoVerde
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  /*55,*/ 110 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo, Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a RossoVerde""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  /*55,*/ 110 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo, Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  /*55,*/ 110 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  /*55,*/ 110""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 è attivo, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  /*55,*/ 110""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co4 del campo mainclass_c1 della lista subclass_c2_lista_l1)  è minore di  (110)) allora (il timer 'mainclass_c1_timer_t1 del campo mainclass_c1 della lista subclass_c2_lista_l1' è attivo)""", [
                            DIBoolExpr("""LessThanImpl\n/*45,*/    MainClass_C1_contatore_Co4 del campo  MainClass_C1     è  minore di  /*55,*/ 110""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t1 del campo mainclass_c1 della lista subclass_c2_lista_l1' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T7 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T7 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a c270""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a GialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a RossoVerde""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l1()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co4().get_valore() < 110, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m1")
    def macroSubclass_c2_macrova_m1(self, argomento_a10, argomento_a3, argomento_a5, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c2_macrova_m2")
    def macroSubclass_c2_macrova_m2(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m2_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m2_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m3")
    def macroSubclass_c2_macrova_m3(self, argomento_a1, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c270 commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c270
        return GlobalEnumeration.c270
    
    @srf_value_macro("macroSubclass_c2_macrova_m8")
    def macroSubclass_c2_macrova_m8(self, argomento_a1, argomento_a2, argomento_a4, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c120x commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m8_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c120x
        return GlobalEnumeration.c120x
    
    @srf_value_macro("macroSubclass_c2_macrova_m9")
    def macroSubclass_c2_macrova_m9(self, argomento_a10, argomento_a4, argomento_a5, argomento_a6, argomento_a7, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  commento: {56,}  state1  o  se la macro  SubClass_C2_macrova_M8 ( con argomento_a7   uguale a True ,argomento_a4   uguale a c270 ,argomento_a8   uguale a Rosso ,argomento_a9   uguale a avanzamento ,argomento_a1   uguale a GialloVerde  e argomento_a2   uguale a Rosso )  non  è  uguale a c120x commento: {40,} ,  commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  False , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  diverso da  False  commento: {110,} e  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è scaduto commento: {109,} o  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  commento: {53,} 1 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 non è  uguale a GialloVerde commento: {43,} e  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  commento: {105,} è disattivo , assegna alla macro il valore c120x
        
         commento: {46,} assegna alla macro il valore c120x commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  /*56,*/  state1  o  se la macro  SubClass_C2_macrova_M8 ( con argomento_a7   uguale a True ,argomento_a4   uguale a c270 ,argomento_a8   uguale a Rosso ,argomento_a9   uguale a avanzamento ,argomento_a1   uguale a GialloVerde  e argomento_a2   uguale a Rosso )  non  è  uguale a c120x /*40,*/ ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  diverso da  False  /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è scaduto /*109,*/ o  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  /*53,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a GialloVerde /*43,*/ e  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  /*105,*/ è disattivo , assegna alla macro il valore c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  /*56,*/  state1  o  se la macro  SubClass_C2_macrova_M8 ( con argomento_a7   uguale a True ,argomento_a4   uguale a c270 ,argomento_a8   uguale a Rosso ,argomento_a9   uguale a avanzamento ,argomento_a1   uguale a GialloVerde  e argomento_a2   uguale a Rosso )  non  è  uguale a c120x /*40,*/ ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  diverso da  False  /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è scaduto /*109,*/ o  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  /*53,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a GialloVerde /*43,*/ e  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  /*105,*/ è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)))} )  o  
( ( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m8')  è uguale a  (c120x)) )  e  ( per ognuna delle seguenti {se (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))) allora (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)))} ) )  e  
( il timer 'subclass_c2_restoreti_ti2_restore' è scaduto ) ) )  o  
( (subclass_c2_restoreva_rv3_restore)  è uguale a  (1) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)))} )  o  
( ( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m8')  è uguale a  (c120x)) )  e  ( per ognuna delle seguenti {se (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))) allora (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)))} ) )  e  
( il timer 'subclass_c2_restoreti_ti2_restore' è scaduto ) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m8')  è uguale a  (c120x)) )  e  ( per ognuna delle seguenti {se (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))) allora (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)))} ) )  e  
( il timer 'subclass_c2_restoreti_ti2_restore' è scaduto )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m8')  è uguale a  (c120x)) )  e  ( per ognuna delle seguenti {se (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))) allora (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m8')  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m8')  è uguale a  (c120x)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m8'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))) allora (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))) allora (negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti2_restore' è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv3_restore)  è uguale a  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c7)  è uguale a  (gialloverde)) )  e  
( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t1 del campo mainclass_c1 della lista subclass_c2_lista_l1' è inattivo)} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t1 del campo mainclass_c1 della lista subclass_c2_lista_l1' è inattivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t1 del campo mainclass_c1 della lista subclass_c2_lista_l1' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  /*56,*/  state1  o  se la macro  SubClass_C2_macrova_M8 ( con argomento_a7   uguale a True ,argomento_a4   uguale a c270 ,argomento_a8   uguale a Rosso ,argomento_a9   uguale a avanzamento ,argomento_a1   uguale a GialloVerde  e argomento_a2   uguale a Rosso )  non  è  uguale a c120x /*40,*/ ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P3 del campo  MainClass_C1     è  diverso da  False  /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è scaduto /*109,*/ o  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  /*53,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  uguale a GialloVerde /*43,*/ e  se MainClass_C1_timer_T1 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  /*105,*/ è disattivo , assegna alla macro il valore c120x
        if db((db((db((db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(db(self.macroSubclass_c2_macrova_m8(GlobalEnumeration.gialloverde,GlobalEnumeration.rosso,GlobalEnumeration.c270,True,GlobalEnumeration.rosso,GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_restoreti_ti2_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_restoreva_rv3_restore() == 1, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l1())), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c120x
        #  /*46,*/ assegna alla macro il valore c120x
        return GlobalEnumeration.c120x
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c4_prev(self.get_subclass_c2_previousco_c4())
        self.set_subclass_c2_previousco_c6_prev(self.get_subclass_c2_previousco_c6())
        self.set_subclass_c2_previousco_c8_prev(self.get_subclass_c2_previousco_c8())
        self.set_subclass_c2_previousco_c9_prev(self.get_subclass_c2_previousco_c9())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())

class SubClass_C2_RecordHeaderR7(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled13, recordfiled10, recordfiled18):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled13(recordfiled13)
        self.set_recordfiled10(recordfiled10)
        self.set_recordfiled18(recordfiled18)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled13(self, recordfiled13):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"), recordfiled13)

    def set_recordfiled10(self, recordfiled10):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"), recordfiled10)

    def set_recordfiled18(self, recordfiled18):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"), recordfiled18)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled13(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"))

    def get_recordfiled10(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"))

    def get_recordfiled18(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"))



