# Codice del modello 'TestCase1', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_subclass_c2_previousva_pv2(GlobalEnumeration.gialloverde)
        self.set_subclass_c2_previousva_pv3(False)
        self.set_subclass_c2_previousva_pv4(0)
        self.set_subclass_c2_previousva_pv5(0)
        self.set_subclass_c2_restoreva_rv1(0)
        self.set_subclass_c2_restoreva_rv2(False)
        self.set_subclass_c2_variabile_v2(GlobalEnumeration.rossogialloaverdea)
        self.set_subclass_c2_variabile_v5(False)
        self.set_subclass_c2_variabile_v7(False)
        self.set_subclass_c2_variabile_v9(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
        if self.is_triggered('eventSubclass_c2_command_comm3DaSender28d36a78'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm3DaSender28d36a78',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm3DaSender28d36a78',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, subclass_c2_lista_l2, subclass_c2_lista_l5, subclass_c2_lista_l7, subclass_c2_lista_l8, subclass_c2_parametro_p5, subclass_c2_parametro_p7):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l2(subclass_c2_lista_l2)
        self.set_subclass_c2_lista_l5(subclass_c2_lista_l5)
        self.set_subclass_c2_lista_l7(subclass_c2_lista_l7)
        self.set_subclass_c2_lista_l8(subclass_c2_lista_l8)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p5(subclass_c2_parametro_p5)
        self.set_subclass_c2_parametro_p7(subclass_c2_parametro_p7)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(3000)
        self.set_subclass_c2_restoreti_ti1_restore(3000)
        self.set_subclass_c2_restoreti_ti2(44000)
        self.set_subclass_c2_restoreti_ti2_restore(44000)
        self.set_subclass_c2_restoreti_ti3(453210000)
        self.set_subclass_c2_restoreti_ti3_restore(453210000)
        self.set_subclass_c2_restoreti_ti4(2000)
        self.set_subclass_c2_restoreti_ti4_restore(2000)
        self.set_subclass_c2_restoreti_ti5(545000)
        self.set_subclass_c2_restoreti_ti5_restore(545000)
        self.set_subclass_c2_timer_t10(2000)
        self.set_subclass_c2_timer_t4(5000)
        self.set_subclass_c2_timer_t9(2210000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_restoreti_ti3,self.subclass_c2_restoreti_ti3_restore,self.subclass_c2_restoreti_ti4,self.subclass_c2_restoreti_ti4_restore,self.subclass_c2_restoreti_ti5,self.subclass_c2_restoreti_ti5_restore,self.subclass_c2_timer_t10,self.subclass_c2_timer_t4,self.subclass_c2_timer_t9,]

        # initialize the counters
        self.set_subclass_c2_contatore_co1(0)
        self.set_subclass_c2_contatore_co10(0)
        self.set_subclass_c2_contatore_co4(0)
        self.set_subclass_c2_contatore_co6(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l2(self, subclass_c2_lista_l2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2",subclass_c2_lista_l2)

    def set_subclass_c2_lista_l5(self, subclass_c2_lista_l5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l5",subclass_c2_lista_l5)

    def set_subclass_c2_lista_l7(self, subclass_c2_lista_l7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l7",subclass_c2_lista_l7)

    def set_subclass_c2_lista_l8(self, subclass_c2_lista_l8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8",subclass_c2_lista_l8)


    # getters for record type parameters
    def get_subclass_c2_lista_l2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2")

    def get_subclass_c2_lista_l5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l5")

    def get_subclass_c2_lista_l7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l7")

    def get_subclass_c2_lista_l8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p5(self, subclass_c2_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5",subclass_c2_parametro_p5)

    def set_subclass_c2_parametro_p7(self, subclass_c2_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7",subclass_c2_parametro_p7)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5")

    def get_subclass_c2_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c10(self, subclass_c2_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c10",subclass_c2_comando_c10)

    def set_subclass_c2_comando_c2(self, subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c2",subclass_c2_comando_c2)

    def set_subclass_c2_comando_c9(self, subclass_c2_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c9",subclass_c2_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c7")

    def get_subclass_c2_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5")


    # setters for state variables
    def set_subclass_c2_previousco_c5_prev(self, subclass_c2_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev",subclass_c2_previousco_c5_prev)
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
    def set_subclass_c2_variabile_v2(self, subclass_c2_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2",subclass_c2_variabile_v2)
    def set_subclass_c2_variabile_v5(self, subclass_c2_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5",subclass_c2_variabile_v5)
    def set_subclass_c2_variabile_v7(self, subclass_c2_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7",subclass_c2_variabile_v7)
    def set_subclass_c2_variabile_v9(self, subclass_c2_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9",subclass_c2_variabile_v9)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev")

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

    def get_subclass_c2_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2")

    def get_subclass_c2_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5")

    def get_subclass_c2_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7")

    def get_subclass_c2_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9")


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

    def set_subclass_c2_timer_t10(self, timerDuration):
        self.subclass_c2_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t10", self.memory)

    def set_subclass_c2_timer_t4(self, timerDuration):
        self.subclass_c2_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t4", self.memory)

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

    def get_subclass_c2_restoreti_ti5(self):
        return self.subclass_c2_restoreti_ti5

    def get_subclass_c2_restoreti_ti5_restore(self):
        return self.subclass_c2_restoreti_ti5_restore

    def get_subclass_c2_timer_t10(self):
        return self.subclass_c2_timer_t10

    def get_subclass_c2_timer_t4(self):
        return self.subclass_c2_timer_t4

    def get_subclass_c2_timer_t9(self):
        return self.subclass_c2_timer_t9


    # setters for counters
    def set_subclass_c2_contatore_co1(self, counterInitValue):
        self.subclass_c2_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co1", self.memory)

    def set_subclass_c2_contatore_co10(self, counterInitValue):
        self.subclass_c2_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co10", self.memory)

    def set_subclass_c2_contatore_co4(self, counterInitValue):
        self.subclass_c2_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co4", self.memory)

    def set_subclass_c2_contatore_co6(self, counterInitValue):
        self.subclass_c2_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co6", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co1(self):
        return self.subclass_c2_contatore_co1

    def get_subclass_c2_contatore_co10(self):
        return self.subclass_c2_contatore_co10

    def get_subclass_c2_contatore_co4(self):
        return self.subclass_c2_contatore_co4

    def get_subclass_c2_contatore_co6(self):
        return self.subclass_c2_contatore_co6



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
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co4

 ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co4""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#2
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_subclass_c2_previousco_c5_prev(GlobalEnumeration.c180x)
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
        
         commento: {37,}  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co4
        
         ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co4
        
        
        
        }
        """
        #  /*37,*/  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co4
        #   ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co4
        if db(not db(self.get_subclass_c2_variabile_v9() == False, self.dbs[2].subs[0].subs[0]), self.dbs[2].subs[0]):
            self.get_subclass_c2_contatore_co4().resetta()
        else:
            self.get_subclass_c2_contatore_co4().resetta()
    
    # effect macros
    def macroSubclass_c2_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro SubClass_C2_macroef_M4  commento: {73,}
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M6   commento: {73,}
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro SubClass_C2_macroef_M4  /*73,*/

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l7')  è uguale a  (state1)))} )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l7')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l7')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l7')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M4"""),#1
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M6"""),#2
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M4  /*73,*/
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M6
        if db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l7())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c2_macroef_m4(di_ctx.subs[0].subs[1])
        else:
            self.macroSubclass_c2_macroef_m6(di_ctx.subs[0].subs[2])
    
    def macroSubclass_c2_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da GialloGiallo commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  commento: {56,} 14, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore RossoGiallox
        
           
         commento: {38,}  se il contatore SubClass_C2_contatore_Co6 è  uguale a  commento: {53,} 1253210 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  commento: {53,} 13 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 15 commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 12 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  True 
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da GialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  /*56,*/ 14, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da GialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo)))} )  e  
( negazione di ((subclass_c2_controllo_c7)  è uguale a  (True)) ) )  o  
( ( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) )  e  
( il timer 'subclass_c2_timer_t9' è inattivo ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo)))} )  e  
( negazione di ((subclass_c2_controllo_c7)  è uguale a  (True)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) )  e  
( il timer 'subclass_c2_timer_t9' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co6)  è uguale a  (14)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co6)  è uguale a  (14))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co6)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*38,*/  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 1253210 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 15 /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 12 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 1253210 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 15 /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 12 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_contatore_co6)  è uguale a  (1253210) )  e  ( (subclass_c2_contatore_co6)  è uguale a  (13) ) )  e  
( negazione di ((subclass_c2_contatore_co6)  è minore di  (15)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_contatore_co6)  è uguale a  (1253210) )  e  ( (subclass_c2_contatore_co6)  è uguale a  (13) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co6)  è uguale a  (1253210)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co6)  è uguale a  (13)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co6)  è minore di  (15))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co6)  è minore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_contatore_co6)  è maggiore di  (12) )  e  
( (subclass_c2_controllo_c7)  è uguale a  (True) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co6)  è maggiore di  (12)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da GialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  /*56,*/ 14, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore RossoGiallox
        if db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l7())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co6().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v2(GlobalEnumeration.rossogiallox)
        #  /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 1253210 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  uguale a  /*53,*/ 13 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 15 /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 12 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  True
        if db((db((db((db(self.get_subclass_c2_contatore_co6().get_valore() == 1253210, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co6().get_valore() == 13, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co6().get_valore() < 15, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c2_contatore_co6().get_valore() > 12, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v9(True)
    
    def macroSubclass_c2_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co6
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co6""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co6
        if db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co6().incrementa()
    
    def macroSubclass_c2_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {43,}  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è attivo commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  maggiore di  commento: {54,} 1 e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C2_timer_T9
        
           
         commento: {36,}  se il timer SubClass_C2_timer_T4 non è scaduto,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L5 è attivo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  diverso da  commento: {56,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T4 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P7 non è  minore di  commento: {55,} 1 commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  minore di  commento: {55,} 7 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  True 
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T4 è attivo,  Applica gli effetti
               della macro SubClass_C2_macroef_M9  commento: {73,}
        
           
         commento: {35,}  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  commento: {56,} 11 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V7 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  False , commento: {69,}Disattiva il timer SubClass_C2_timer_T9
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  False 
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C2_timer_T9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t7 del campo mainclass_c1 della lista subclass_c2_lista_l7' è attivo)} )  o  
( ( il timer 'subclass_c2_timer_t9' è attivo )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t7 del campo mainclass_c1 della lista subclass_c2_lista_l7' è attivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7 del campo mainclass_c1 della lista subclass_c2_lista_l7' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t9' è attivo )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_parametro_p5)  è maggiore di  (1) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p5)  è maggiore di  (1)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L5 è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  diverso da  /*56,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T4 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P7 non è  minore di  /*55,*/ 1 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L5 è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  diverso da  /*56,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T4 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P7 non è  minore di  /*55,*/ 1 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (il timer 'subclass_c2_timer_t4' è scaduto) )  e  
( per ognuna delle seguenti {se (negazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (10))) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è attivo)} ) )  o  
( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) ) )  o  
( negazione di ((subclass_c2_parametro_p7)  è minore di  (1)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'subclass_c2_timer_t4' è scaduto) )  e  
( per ognuna delle seguenti {se (negazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (10))) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è attivo)} ) )  o  
( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t4' è scaduto) )  e  
( per ognuna delle seguenti {se (negazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (10))) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è attivo)} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se (negazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (10))) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è attivo)}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (10))) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è attivo)""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p7)  è minore di  (1))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p7)  è minore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_parametro_p5)  è minore di  (7) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p5)  è minore di  (7)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo,  Applica gli effetti
       della macro SubClass_C2_macroef_M9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_restoreva_rv2_restore)  è uguale a  (False) )  e  ( negazione di ((subclass_c2_controllo_c7)  è uguale a  (True)) ) )  e  
( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_restoreva_rv2_restore)  è uguale a  (False) )  e  ( negazione di ((subclass_c2_controllo_c7)  è uguale a  (True)) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv2_restore)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M9"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*35,*/  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  False , /*69,*/Disattiva il timer SubClass_C2_timer_T9

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*35,*/  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c2_controllo_c7)  è uguale a  (True) )  o  
( ( ( negazione di ((subclass_c2_contatore_co4)  è uguale a  (11)) )  e  ( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) ) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_contatore_co4)  è uguale a  (11)) )  e  ( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co4)  è uguale a  (11)) )  e  ( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co4)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v7)  è uguale a  (False)) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (False))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C2_timer_T9
        if db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l7())), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t9().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_parametro_p5() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t9().attiva()
        #  /*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L5 è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  diverso da  /*56,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T4 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P7 non è  minore di  /*55,*/ 1 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  True
        if db((db((db((db((db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l5()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v10() == 10, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p7() < 1, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c2_parametro_p5() < 7, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v9(True)
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M9
        if db((db((db((db(self.get_subclass_c2_restoreva_rv2_restore() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.macroSubclass_c2_macroef_m9(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #     
        #   /*35,*/  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V7 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  False , /*69,*/Disattiva il timer SubClass_C2_timer_T9
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  False
        if db((db((db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 11, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v7() == False, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v9() == False, di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c2_timer_t9().disattiva()
        else:
            self.set_subclass_c2_variabile_v9(False)
    
    def macroSubclass_c2_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer SubClass_C2_timer_T9 è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 144 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore c180
        
           
         commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  commento: {105,} è  uguale a GialloGiallo commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  uguale a  False  commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a  commento: {53,} 9 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co6
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T10
        
        
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P7 è  uguale a  commento: {53,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
        
         commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer SubClass_C2_timer_T9 è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  commento: {36,} o  se il timer SubClass_C2_timer_T9 non è attivo commento: {36,} o  se il timer SubClass_C2_timer_T4 non è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore c180
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 144 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore c180""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 144 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( il timer 'subclass_c2_timer_t9' è scaduto )  e  ( negazione di (negazione di ((subclass_c2_contatore_co10)  è uguale a  (144))) ) )  e  ( (subclass_c2_controllo_c7)  è uguale a  (True) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (subclass_c2_variabile_v9)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( il timer 'subclass_c2_timer_t9' è scaduto )  e  ( negazione di (negazione di ((subclass_c2_contatore_co10)  è uguale a  (144))) ) )  e  ( (subclass_c2_controllo_c7)  è uguale a  (True) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'subclass_c2_timer_t9' è scaduto )  e  ( negazione di (negazione di ((subclass_c2_contatore_co10)  è uguale a  (144))) ) )  e  ( (subclass_c2_controllo_c7)  è uguale a  (True) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t9' è scaduto )  e  ( negazione di (negazione di ((subclass_c2_contatore_co10)  è uguale a  (144))) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co10)  è uguale a  (144)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (144))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (144)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  uguale a GialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  uguale a  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a  /*53,*/ 9 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , /*70,*/Incrementa il contatore SubClass_C2_contatore_Co6

 ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  uguale a GialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  uguale a  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a  /*53,*/ 9 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo))} )  o  
( ( (subclass_c2_variabile_v9)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) ) ) )  o  
( negazione di ((subclass_c2_parametro_p5)  è uguale a  (9)) ) )  o  
( (subclass_c2_controllo_c7)  è uguale a  (True) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo))} )  o  
( ( (subclass_c2_variabile_v9)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) ) ) )  o  
( negazione di ((subclass_c2_parametro_p5)  è uguale a  (9)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo))} )  o  
( ( (subclass_c2_variabile_v9)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) ) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v9)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P7 è  uguale a  /*53,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo, /*69,*/Disattiva il timer SubClass_C2_timer_T9

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P7 è  uguale a  /*53,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'subclass_c2_restoreti_ti1_restore' è attivo )  o  
( (subclass_c2_parametro_p7)  è uguale a  (10) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p7)  è uguale a  (10)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T4 non è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T4 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (4)))} )  o  
( il timer 'subclass_c2_timer_t9' è inattivo ) )  o  
( (subclass_c2_controllo_c7)  è uguale a  (True) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t9' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (4)))} )  o  
( il timer 'subclass_c2_timer_t9' è inattivo ) )  o  
( (subclass_c2_controllo_c7)  è uguale a  (True) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {(negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (4)))} )  o  
( il timer 'subclass_c2_timer_t9' è inattivo )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (4)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 144 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore c180
        if db((db((db((db((db((db(self.get_subclass_c2_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 144, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v9() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c2(GlobalEnumeration.c180)
        #  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L7 esiste e  /*105,*/ è  uguale a GialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  uguale a  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a  /*53,*/ 9 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , /*70,*/Incrementa il contatore SubClass_C2_contatore_Co6
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T10
        if db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l7())), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v9() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p5() == 9, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co6().incrementa()
        else:
            self.get_subclass_c2_timer_t10().attiva()
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P7 è  uguale a  /*53,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo, /*69,*/Disattiva il timer SubClass_C2_timer_T9
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10
        if db((db((db(self.get_subclass_c2_restoreti_ti1_restore().isAttivato(), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p7() == 10, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t9().isAttivato(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_timer_t9().disattiva()
        else:
            self.get_subclass_c2_timer_t10().disattiva()
        #  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L8 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T4 non è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore c180
        if db((db((db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == 4, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t9().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_comando_c2(GlobalEnumeration.c180)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m10")
    def macroSubclass_c2_macrove_m10(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {44,}  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  commento: {53,} 8 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co6 sia  minore di  commento: {55,} 13
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co6 non sia  minore di  commento: {55,} 11
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 154
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  /*53,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Verifica che   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  minore di  /*55,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co6 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  /*53,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Verifica che   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  minore di  /*55,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co6 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  /*53,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  True""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V9 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  minore di  /*55,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co6 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  minore di  /*55,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co6 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  minore di  /*55,*/ 13
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""LessThanImpl\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co6 sia  minore di  /*55,*/ 13""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co6 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co6)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (154)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v10() == 8, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l7())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v9() == True, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_contatore_co6().get_valore() < 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co6().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 154, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m8")
    def macroSubclass_c2_macrova_m8(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {37,}  se la variabile SubClass_C2_variabile_V9 è  uguale a  True ,  commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  maggiore di  commento: {54,} 6, commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T5 del campo  MainClass_C1     commento: {105,} è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 12,  commento: {45,}  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  minore di  commento: {55,} 12453, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  maggiore di  commento: {54,} 1 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è disattivo,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T5 del campo  MainClass_C1     commento: {105,} è disattivo commento: {45,} e  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  commento: {53,} 14210 commento: {42,} o  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L5 è  diverso da GialloGiallo , assegna alla macro il valore c180
        
         commento: {46,} assegna alla macro il valore c180 commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 è  uguale a  True ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  maggiore di  /*54,*/ 6, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 12,  /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  minore di  /*55,*/ 12453, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  maggiore di  /*54,*/ 1 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo /*45,*/ e  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  /*53,*/ 14210 /*42,*/ o  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L5 è  diverso da GialloGiallo , assegna alla macro il valore c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 è  uguale a  True ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  maggiore di  /*54,*/ 6, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 12,  /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  minore di  /*55,*/ 12453, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  maggiore di  /*54,*/ 1 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo /*45,*/ e  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  /*53,*/ 14210 /*42,*/ o  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L5 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_variabile_v9)  è uguale a  (True) )  e  
( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (6))} ) )  o  
( ( ( ( (subclass_c2_contatore_co4)  è maggiore di  (12) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (1)) allora ((mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è minore di  (12453))} ) )  e  ( ( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))} ) ) )  e  
( per ognuna delle seguenti {((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (14210))} ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v9)  è uguale a  (True) )  e  
( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (6))} )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (6))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (6))""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (6)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (subclass_c2_contatore_co4)  è maggiore di  (12) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (1)) allora ((mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è minore di  (12453))} ) )  e  ( ( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))} ) ) )  e  
( per ognuna delle seguenti {((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (14210))} )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_contatore_co4)  è maggiore di  (12) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (1)) allora ((mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è minore di  (12453))} ) )  e  ( ( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))} ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_contatore_co4)  è maggiore di  (12) )  e  ( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (1)) allora ((mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è minore di  (12453))} )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co4)  è maggiore di  (12)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (1)) allora ((mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è minore di  (12453))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (1)) allora ((mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è minore di  (12453))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è maggiore di  (1)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è minore di  (12453)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t4' è inattivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l5' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l5')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (14210))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l7)  è uguale a  (14210)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (giallogiallo)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l5)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m8_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 è  uguale a  True ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  maggiore di  /*54,*/ 6, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 12,  /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  minore di  /*55,*/ 12453, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     è  maggiore di  /*54,*/ 1 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L5 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T5 del campo  MainClass_C1     /*105,*/ è disattivo /*45,*/ e  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L7 è  uguale a  /*53,*/ 14210 /*42,*/ o  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L5 è  diverso da GialloGiallo , assegna alla macro il valore c180
        if db((db((db((db(self.get_subclass_c2_variabile_v9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() > 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l5()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_contatore_co4().get_valore() > 12, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co10().get_valore() < 12453, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l5()) if db(it.get_mainclass_c1().get_mainclass_c1_variabile_v10() > 1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db((db(not db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l5()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co3().get_valore() == 14210, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l7())), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l5())), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c180
        #  /*46,*/ assegna alla macro il valore c180
        return GlobalEnumeration.c180
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c2_command_comm3DaSender28d36a78(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm3DaSender28d36a78')
    
    # for each automatic command, the corresponding method is created
    def eventSubclass_c2_command_comm8(self, notifying_process, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave7):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm8', argomento_ave1=argomento_ave1, argomento_ave2=argomento_ave2, argomento_ave3=argomento_ave3, argomento_ave7=argomento_ave7)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c5_prev(self.get_subclass_c2_previousco_c5())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())
        self.set_subclass_c2_previousva_pv5_prev(self.get_subclass_c2_previousva_pv5())

class SubClass_C2_RecordHeaderR10(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled5, recordfiled10):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled5(recordfiled5)
        self.set_recordfiled10(recordfiled10)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled5(self, recordfiled5):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"), recordfiled5)

    def set_recordfiled10(self, recordfiled10):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"), recordfiled10)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled5(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"))

    def get_recordfiled10(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"))



class SubClass_C2_RecordHeaderR8(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled6, recordfiled17):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled6(recordfiled6)
        self.set_recordfiled17(recordfiled17)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled6(self, recordfiled6):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"), recordfiled6)

    def set_recordfiled17(self, recordfiled17):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled17"), recordfiled17)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled6(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"))

    def get_recordfiled17(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled17"))



