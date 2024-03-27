# Codice del modello 'TestCase14', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.gialloaverdea)
        self.set_mainclass_c1_previousva_pv2(False)
        self.set_mainclass_c1_previousva_pv3(GlobalEnumeration.giallogiallo)
        self.set_mainclass_c1_previousva_pv4(0)
        self.set_mainclass_c1_previousva_pv5(False)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.gialloaverdea)
        self.set_mainclass_c1_variabile_v5(GlobalEnumeration.rossogiallox)
        self.set_mainclass_c1_variabile_v8(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2 : set(['eventMainclass_c1_command_comm5',]),
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm4DaSender3e4efa96'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm4DaSender3e4efa96',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm4DaSender3e4efa96',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm5'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.NOOP)


        if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
        # for each manual command that can be received in Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2
            if self.is_triggered('eventMainclass_c1_command_comm5'):
                self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.BLOCKED)

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
        _State2__State2__stateSheet_1__nominalActuation__transitionTo_0 = 2
        _State2__State1__stateSheet_1__nominalActuation__transitionTo_1 = 3
        _State2__State2__stateSheet_1__nominalActuation__transitionTo_2 = 4
        _State2__State1__stateSheet_1__nominalActuation__transitionTo_3 = 5
        _State2__State2__stateSheet_1__normalization__transitionTo_0 = 6
        _State1__State1__stateSheet_0__permanence = 7
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_0 = 8
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_1 = 9
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_2 = 10
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_3 = 11
        _State1__State2__stateSheet_0__normalization__transitionTo_0 = 12

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1_parametro_p3, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(50000)
        self.set_mainclass_c1_restoreti_ti1_restore(50000)
        self.set_mainclass_c1_restoreti_ti2(1000)
        self.set_mainclass_c1_restoreti_ti2_restore(1000)
        self.set_mainclass_c1_restoreti_ti3(5000)
        self.set_mainclass_c1_restoreti_ti3_restore(5000)
        self.set_mainclass_c1_restoreti_ti4(5000)
        self.set_mainclass_c1_restoreti_ti4_restore(5000)
        self.set_mainclass_c1_timer_t2(4000)
        self.set_mainclass_c1_timer_t6(52145000)
        self.set_mainclass_c1_timer_t8(43000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_timer_t2,self.mainclass_c1_timer_t6,self.mainclass_c1_timer_t8,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co2(0)
        self.set_mainclass_c1_contatore_co4(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)

    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c2(self, mainclass_c1_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c2",mainclass_c1_comando_c2)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c1")

    def get_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c10")

    def get_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c2")

    def get_mainclass_c1_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c5")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3")

    def get_mainclass_c1_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6")

    def get_mainclass_c1_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7")

    def get_mainclass_c1_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8")


    # setters for state variables
    def set_mainclass_c1_previousco_c3_prev(self, mainclass_c1_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev",mainclass_c1_previousco_c3_prev)
    def set_mainclass_c1_previousco_c6_prev(self, mainclass_c1_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev",mainclass_c1_previousco_c6_prev)
    def set_mainclass_c1_previousco_c7_prev(self, mainclass_c1_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7_prev",mainclass_c1_previousco_c7_prev)
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
    def set_mainclass_c1_previousva_pv5(self, mainclass_c1_previousva_pv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5",mainclass_c1_previousva_pv5)
    def set_mainclass_c1_previousva_pv5_prev(self, mainclass_c1_previousva_pv5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5_prev",mainclass_c1_previousva_pv5_prev)
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

    # getters for state variables
    def get_mainclass_c1_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev")

    def get_mainclass_c1_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev")

    def get_mainclass_c1_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7_prev")

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

    def get_mainclass_c1_previousva_pv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5")

    def get_mainclass_c1_previousva_pv5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5_prev")

    def get_mainclass_c1_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1")

    def get_mainclass_c1_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1_restore")

    def get_mainclass_c1_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2")

    def get_mainclass_c1_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2_restore")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

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

    def set_mainclass_c1_restoreti_ti4(self, timerDuration):
        self.mainclass_c1_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4", self.memory)

    def set_mainclass_c1_restoreti_ti4_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4_restore", self.memory)

    def set_mainclass_c1_timer_t2(self, timerDuration):
        self.mainclass_c1_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t2", self.memory)

    def set_mainclass_c1_timer_t6(self, timerDuration):
        self.mainclass_c1_timer_t6 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t6", self.memory)

    def set_mainclass_c1_timer_t8(self, timerDuration):
        self.mainclass_c1_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t8", self.memory)


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

    def get_mainclass_c1_timer_t6(self):
        return self.mainclass_c1_timer_t6

    def get_mainclass_c1_timer_t8(self):
        return self.mainclass_c1_timer_t8


    # setters for counters
    def set_mainclass_c1_contatore_co2(self, counterInitValue):
        self.mainclass_c1_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co2", self.memory)

    def set_mainclass_c1_contatore_co4(self, counterInitValue):
        self.mainclass_c1_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co4", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co2(self):
        return self.mainclass_c1_contatore_co2

    def get_mainclass_c1_contatore_co4(self):
        return self.mainclass_c1_contatore_co4



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 15


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 15


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C5 è  uguale a  True""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 15""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde""", [
                    DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 1""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da Verde""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V5 non è  diverso da c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 è  diverso da Verde""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 15""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (15))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (15)""", [
                    ]),#0
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
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*86,*/  Almeno una delle seguenti {
 /*82,*/  Ricezione del comando manuale   MainClass_C1_command_comm5   /*75,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm5   /*75,*/
 /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x


}
}""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*86,*/  Almeno una delle seguenti {
 /*82,*/  Ricezione del comando manuale   MainClass_C1_command_comm5   /*75,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm5   /*75,*/
 /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x


}
}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm5"""),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n/*75,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm5   /*75,*/
 /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm5"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*75,*/
 /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#10
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#11
                    DIBoolExpr("""NAryLogicOP (AND)\n/*86,*/  Almeno una delle seguenti {
 /*82,*/  Ricezione del comando manuale   MainClass_C1_command_comm5   /*75,*/

}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm5"""),#0
                    ]),#12
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto""", [
                    ]),#0
                    ]),#13
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 3, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore RossoGialloxVerdex

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 3""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde)) ) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (150))) ) )  o  
( il timer 'mainclass_c1_timer_t6' è inattivo ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde)) ) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (150))) ) )  o  
( il timer 'mainclass_c1_timer_t6' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde)) ) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (150))) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde)) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (150)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (150))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (150)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (3))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (3)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#14
                    DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 153 /*36,*/ o  se il timer MainClass_C1_timer_T2 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da RossoGialloxVerdex, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 8

 ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 153 /*36,*/ o  se il timer MainClass_C1_timer_T2 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da RossoGialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (153)) )  o  
( il timer 'mainclass_c1_timer_t2' è inattivo ) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (15))) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (153)) )  o  
( il timer 'mainclass_c1_timer_t2' è inattivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (153))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (153)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (15)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (15))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (15)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#15
                    DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 122 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 122 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde) )  e  ( (mainclass_c1_controllo_c2)  è uguale a  (verde) ) )  e  ( (mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex) ) )  e  
( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (122)) ) )  o  
( (mainclass_c1_variabile_v5)  è uguale a  (c270x) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde) )  e  ( (mainclass_c1_controllo_c2)  è uguale a  (verde) ) )  e  ( (mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex) ) )  e  
( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (122)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde) )  e  ( (mainclass_c1_controllo_c2)  è uguale a  (verde) ) )  e  ( (mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde) )  e  ( (mainclass_c1_controllo_c2)  è uguale a  (verde) )""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (122))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (122)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#16
                    DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 141, /*72,*/Azzera il contatore MainClass_C1_contatore_Co2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 141""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (141)""", [
                    ]),#1
                    ]),#0
                    ]),#17
                    DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro MainClass_C1_macroef_M6""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M6"""),#1
                    ]),#18
                    DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1232 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1232 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (1232))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (1232)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t8' è attivo) )  e  
( negazione di (il timer 'mainclass_c1_timer_t2' è scaduto) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t8' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#19
                    DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 4 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T6

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 4 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)) )  o  
( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)) ) )  o  
( negazione di ((mainclass_c1_variabile_v8)  è maggiore di  (4)) ) )  o  
( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)) )  o  
( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)) ) )  o  
( negazione di ((mainclass_c1_variabile_v8)  è maggiore di  (4)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)) )  o  
( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è maggiore di  (4))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v8)  è maggiore di  (4)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#20
                    DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  minore di  /*55,*/ 12145 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, /*69,*/Disattiva il timer MainClass_C1_timer_T2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  minore di  /*55,*/ 12145 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co2)  è minore di  (12145) )  e  
( (mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex) )""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co2)  è minore di  (12145)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#21
                    DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 1203, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 1203""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (1203)""", [
                    ]),#1
                    ]),#0
                    ]),#22
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 142145 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde,  Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 142145 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_restoreti_ti1_restore' è attivo )  e  
( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (142145)) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (142145))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (142145)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde) ) )  e  
( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde) )""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#23
                    DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*35,*/  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, /*68,*/Attiva il timer MainClass_C1_timer_T8

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T8""", [
                    DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C2 è  uguale a Verde""", [
                    ]),#0
                    ]),#24
                    DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a2   uguale a GialloaVerdea ,argomento_a10   uguale a GialloGiallo ,argomento_a5   uguale a Verde ,argomento_a6   uguale a Verde  e argomento_a1   uguale a RossoGiallox )   è  diverso da  True  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a c270x /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  uguale a RossoGialloxVerdex, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M10""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a2   uguale a GialloaVerdea ,argomento_a10   uguale a GialloGiallo ,argomento_a5   uguale a Verde ,argomento_a6   uguale a Verde  e argomento_a1   uguale a RossoGiallox )   è  diverso da  True  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a c270x /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  uguale a RossoGialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (True)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t2' è inattivo) ) )  e  ( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x)) ) )  e  ( negazione di (il timer 'mainclass_c1_timer_t2' è attivo) ) )  e  
( (mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (True)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t2' è inattivo) ) )  e  ( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x)) ) )  e  ( negazione di (il timer 'mainclass_c1_timer_t2' è attivo) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (True)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t2' è inattivo) ) )  e  ( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (True)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t2' è inattivo) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (True)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M10"""),#1
                    ]),#25
                    DIStatement("""ITEStatementImpl\n/*73,*/


 /*37,*/  se la variabile MainClass_C1_variabile_V8 è  maggiore di  /*54,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 4,  Applica gli effetti
       della macro MainClass_C1_macroef_M8  /*73,*/

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*37,*/  se la variabile MainClass_C1_variabile_V8 è  maggiore di  /*54,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_variabile_v8)  è maggiore di  (10) )  o  
( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (1303)) )""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v8)  è maggiore di  (10)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (1303))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (1303)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (4)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M6"""),#2
                    ]),#26
                    DIStatement("""ITStatement\n/*73,*/


 /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 14214,  Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/


 /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 14214""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) ) )  e  ( negazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (11))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (11)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (11))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (11)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (14214))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (14214)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#27
                    DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a RossoGialloVerde, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co4""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a RossoGialloVerde""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    ]),#28
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a Verde, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a Verde""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti3_restore' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti3_restore' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                    ]),#1
                    ]),#0
                    ]),#29
                    DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è disattivo, /*68,*/Attiva il timer MainClass_C1_timer_T8""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è disattivo""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t8' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#30
                    DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde,  Applica gli effetti
       della macro MainClass_C1_macroef_M6""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M6"""),#1
                    ]),#31
                    DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 11321 /*36,*/ e  se il timer MainClass_C1_timer_T6 è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 11321 /*36,*/ e  se il timer MainClass_C1_timer_T6 è disattivo""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (mainclass_c1_contatore_co4)  è minore di  (12) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (11321))) ) )  e  
( il timer 'mainclass_c1_timer_t6' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_contatore_co4)  è minore di  (12) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (11321))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co4)  è minore di  (12) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co4)  è minore di  (12)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (11321)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (11321))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (11321)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#32
                    DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 1545 /*36,*/ e  se il timer MainClass_C1_timer_T2 è disattivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M8  /*73,*/

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 1545 /*36,*/ e  se il timer MainClass_C1_timer_T2 è disattivo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (rossogialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (rossogialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co2)  è maggiore di  (1545) )  e  
( il timer 'mainclass_c1_timer_t2' è inattivo )""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (1545)""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è inattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#33
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef è uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                    ]),#0
                    ]),#34
                    DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 110 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 143 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 142145 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 6, /*72,*/Azzera il contatore MainClass_C1_contatore_Co4

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 110 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 143 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 142145 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_contatore_co4)  è minore di  (110) )  o  
( ( negazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (143))) )  e  
( (mainclass_c1_variabile_v8)  è maggiore di  (5) ) )""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co4)  è minore di  (110)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (143))) )  e  
( (mainclass_c1_variabile_v8)  è maggiore di  (5) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (143)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (143))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (143)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v8)  è maggiore di  (5)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_contatore_co2)  è minore di  (142145)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( (mainclass_c1_variabile_v8)  è minore di  (6) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co2)  è minore di  (142145)) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è minore di  (142145))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co2)  è minore di  (142145)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v8)  è minore di  (6)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#35
                    DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 120 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 120 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è maggiore di  (120))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (120)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                    ]),#1
                    ]),#0
                    ]),#36
                    DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( il timer 'mainclass_c1_timer_t2' è attivo )  e  ( negazione di (il timer 'mainclass_c1_timer_t6' è inattivo) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t2' è scaduto) ) )  o  
( (mainclass_c1_controllo_c2)  è uguale a  (verde) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'mainclass_c1_timer_t2' è attivo )  e  ( negazione di (il timer 'mainclass_c1_timer_t6' è inattivo) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t2' è scaduto) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t2' è attivo )  e  ( negazione di (il timer 'mainclass_c1_timer_t6' è inattivo) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#37
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                    ]),#1
                    ]),#0
                    ]),#38
                    DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T2 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è attivo""", [
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#39
                    DIStatement("""ITEStatementImpl\n/*73,*/


 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 133214 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 155, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 10""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 133214 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 155""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti4_restore' è scaduto""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (133214)) )  e  
( (mainclass_c1_contatore_co4)  è maggiore di  (155) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (133214))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (133214)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (155)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#40
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 8 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde,  Applica gli effetti
       della macro MainClass_C1_macroef_M6   /*73,*/

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 8 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (8)) )  o  
( negazione di (il timer 'mainclass_c1_timer_t2' è scaduto) ) )  o  
( negazione di (negazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x))) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (8)) )  o  
( negazione di (il timer 'mainclass_c1_timer_t2' è scaduto) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (8))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (8)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M6"""),#1
                    ]),#41
                    DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12321 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 13 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde,  Applica gli effetti
       della macro MainClass_C1_macroef_M10  /*73,*/

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12321 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 13 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (12321)) ) )  e  
( il timer 'mainclass_c1_timer_t2' è scaduto ) )  o  
( negazione di ((mainclass_c1_contatore_co4)  è minore di  (13)) ) )  o  
( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (12321)) ) )  e  
( il timer 'mainclass_c1_timer_t2' è scaduto ) )  o  
( negazione di ((mainclass_c1_contatore_co4)  è minore di  (13)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (12321)) ) )  e  
( il timer 'mainclass_c1_timer_t2' è scaduto )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (12321)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (12321))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (12321)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è minore di  (13))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co4)  è minore di  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M10"""),#1
                    ]),#42
                    DIStatement("""ITStatement\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15450 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13, /*72,*/Azzera il contatore MainClass_C1_contatore_Co4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15450 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((stato_restore)  è uguale a  (state1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_contatore_co2)  è maggiore di  (15450)) )  e  ( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)) ) )  e  
( negazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (13))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co2)  è maggiore di  (15450)) )  e  ( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è maggiore di  (15450))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (15450)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (13)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (13))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (13)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#43
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, /*69,*/Disattiva il timer MainClass_C1_timer_T2

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T6""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#44
                    DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da Verde /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x,  Applica gli effetti
       della macro MainClass_C1_macroef_M6   /*73,*/

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da Verde /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))) ) ) )  o  
( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))) ) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M6"""),#1
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#2
                    ]),#45
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[12], ),
                         effect=(self.dbs[45], ),
                         phase = TransPhase.Manuale
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[10], ),
                         effect=(self.dbs[43], ),
                         phase = TransPhase.Manuale
                         ),
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[8], ),
                         effect=(self.dbs[37], self.dbs[38], self.dbs[39], self.dbs[40], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[9], ),
                         effect=(self.dbs[41], self.dbs[42], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[11], ),
                         effect=(self.dbs[44], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[7], ),
                         effect=(self.dbs[32], self.dbs[33], self.dbs[34], self.dbs[35], self.dbs[36], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[6], ),
                         effect=(self.dbs[31], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[14], self.dbs[15], self.dbs[16], self.dbs[17], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[18], self.dbs[19], self.dbs[20], self.dbs[21], self.dbs[22], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[4], ),
                         effect=(self.dbs[23], self.dbs[24], self.dbs[25], self.dbs[26], self.dbs[27], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[5], ),
                         effect=(self.dbs[28], self.dbs[29], self.dbs[30], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[13], ),
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

        self.set_mainclass_c1_previousco_c3_prev(False)
        self.set_mainclass_c1_previousco_c6_prev(True)
        self.set_mainclass_c1_previousco_c7_prev(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_previousco_c8_prev(GlobalEnumeration.c270x)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())
        self.set_mainclass_c1_previousva_pv5_prev(self.get_mainclass_c1_previousva_pv5())

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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                if(self.guard_NORMALIZATION_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__normalization__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state2_001()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__nominalActuation__transitionTo_2
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                if(self.guard_NOMINAL_ACTUATION_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state2_state1_000()):
                    self.curr_transition = self.Transition._State2__State1__stateSheet_1__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state2_state1_001()):
                    self.curr_transition = self.Transition._State2__State1__stateSheet_1__nominalActuation__transitionTo_3
                elif(self.guard_PERMANENCE_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                if(self.guard_NORMALIZATION_state1_state2_000()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__normalization__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_state2_000()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state1_001()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_2
                elif(self.guard_NOMINAL_ACTUATION_state1_002()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_3
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_PERMANENCE_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State2__State2__stateSheet_1__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State2__State1__stateSheet_1__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state2_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State2__State2__stateSheet_1__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state2_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State2__State1__stateSheet_1__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state2_state1_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State2__State2__stateSheet_1__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NORMALIZATION_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state1_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state1_002()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NORMALIZATION_state1_state2_000()
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
        
         commento: {69,} commento: {35,}  se il controllo MainClass_C1_controllo_C5 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  commento: {56,} 15
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        return db((db(not db((db(self.get_mainclass_c1_controllo_c5() == True, self.dbs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0]) or db(not db((db((db((db(self.get_mainclass_c1_variabile_v8() < 1, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 15, self.dbs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[0].subs[1]), self.dbs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1])), self.dbs[1])
    
    def guard_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[2])
    
    def guard_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[3])
    
    def guard_NOMINAL_ACTUATION_state1_001(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[4])
    
    def guard_NOMINAL_ACTUATION_state1_002(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[5])
    
    def guard_NORMALIZATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[6])
    
    def guard_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna  commento: {80,}
        }
        """
        return db((True), self.dbs[7])
    
    def guard_NOMINAL_ACTUATION_state2_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[8])
    
    def guard_NOMINAL_ACTUATION_state2_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[9])
    
    def guard_NOMINAL_ACTUATION_state2_001(self):
        """
        CNL corrispondente:
         {  commento: {86,}  Almeno una delle seguenti {
         commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm5   commento: {75,}
         commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   MainClass_C1_command_comm5   commento: {75,}
         commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
        
        
        }
        } }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventMainclass_c1_command_comm5'), self.dbs[10].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[10].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[10].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, self.dbs[10].subs[0].subs[1].subs[1].subs[1].subs[0]), self.dbs[10].subs[0].subs[1].subs[1].subs[1]), self.dbs[10].subs[0].subs[1].subs[1]))
        if (db(self.is_triggered('eventMainclass_c1_command_comm5'), self.dbs[10].subs[0].subs[0]) or db(res_manCmdCondition_0, self.dbs[10].subs[0].subs[1])):
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.PROCESSED)
        return db((db((db(self.is_triggered('eventMainclass_c1_command_comm5'), self.dbs[10].subs[0].subs[0]) or db(res_manCmdCondition_0, self.dbs[10].subs[0].subs[1])), self.dbs[10].subs[0])), self.dbs[10])
    
    def guard_NOMINAL_ACTUATION_state2_state1_001(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[11])
    
    def guard_NORMALIZATION_state2_000(self):
        """
        CNL corrispondente:
         {  commento: {86,}  Almeno una delle seguenti {
         commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm5   commento: {75,}
        
        } }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventMainclass_c1_command_comm5'), self.dbs[12].subs[0]))
        if res_manCmdCondition_0:
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.PROCESSED)
        return db(res_manCmdCondition_0, self.dbs[12])
    
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
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
           
        
        }
        """
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), self.dbs[13].subs[0]):
            self.set_mainclass_c1_comando_c4(True)
    
    def effect_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {  se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 150 commento: {36,} o  se il timer MainClass_C1_timer_T6 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 3, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore RossoGialloxVerdex
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co4
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 153 commento: {36,} o  se il timer MainClass_C1_timer_T2 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  diverso da RossoGialloxVerdex, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 8
        
         ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co4
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 122 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T6
        
           
          se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 141, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co2
        
           
         }
        """
        #  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 3, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore RossoGialloxVerdex
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co4
        if db((db((db((db((db((db(self.get_consdef() == False, self.dbs[14].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, self.dbs[14].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[14].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[14].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 150, self.dbs[14].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[14].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[14].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[14].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[14].subs[0].subs[0].subs[0].subs[1])), self.dbs[14].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[14].subs[0].subs[0].subs[1])), self.dbs[14].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v8() == 3, self.dbs[14].subs[0].subs[1].subs[0]), self.dbs[14].subs[0].subs[1])), self.dbs[14].subs[0]):
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.rossogialloxverdex)
        else:
            self.get_mainclass_c1_contatore_co4().decrementa()
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 153 /*36,*/ o  se il timer MainClass_C1_timer_T2 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  diverso da RossoGialloxVerdex, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 8
        #   ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co4
        if db((db((db((db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 153, self.dbs[15].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[15].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t2().isDisattivato(), self.dbs[15].subs[0].subs[0].subs[0].subs[1])), self.dbs[15].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 15, self.dbs[15].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[15].subs[0].subs[0].subs[1].subs[0]), self.dbs[15].subs[0].subs[0].subs[1])), self.dbs[15].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, self.dbs[15].subs[0].subs[1].subs[0].subs[0]), self.dbs[15].subs[0].subs[1].subs[0]), self.dbs[15].subs[0].subs[1])), self.dbs[15].subs[0]):
            self.set_mainclass_c1_variabile_v8(8)
        else:
            self.get_mainclass_c1_contatore_co4().incrementa()
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 122 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T6
        if db((db((db((db((db((db(self.get_mainclass_c1_restoreva_rv2_restore() == GlobalEnumeration.rossogialloverde, self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 122, self.dbs[16].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[16].subs[0].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, self.dbs[16].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[16].subs[0].subs[1])), self.dbs[16].subs[0]):
            self.get_mainclass_c1_timer_t6().disattiva()
        #  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 141, /*72,*/Azzera il contatore MainClass_C1_contatore_Co2
        if db((db((db(self.get_consdef() == False, self.dbs[17].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[17].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[17].subs[0].subs[0].subs[1].subs[0]), self.dbs[17].subs[0].subs[0].subs[1])), self.dbs[17].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() > 141, self.dbs[17].subs[0].subs[1])), self.dbs[17].subs[0]):
            self.get_mainclass_c1_contatore_co2().resetta()
    
    def effect_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro MainClass_C1_macroef_M6   commento: {73,}
        
           
         commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 1232 commento: {36,} o  se il timer MainClass_C1_timer_T8 non è attivo commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  commento: {54,} 4 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T6
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  minore di  commento: {55,} 12145 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, commento: {69,}Disattiva il timer MainClass_C1_timer_T2
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 1203, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
        
         }
        """
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a Verde e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M6
        if db((db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[18].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[18].subs[0].subs[0].subs[0].subs[0]), self.dbs[18].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, self.dbs[18].subs[0].subs[0].subs[1].subs[0]), self.dbs[18].subs[0].subs[0].subs[1])), self.dbs[18].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[18].subs[0].subs[1])), self.dbs[18].subs[0]):
            self.macroMainclass_c1_macroef_m6(self.dbs[18].subs[1])
        #  /*73,*/
        #     
        #   /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1232 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co4
        if db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 1232, self.dbs[19].subs[0].subs[0].subs[0]), self.dbs[19].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t8().isAttivato(), self.dbs[19].subs[0].subs[1].subs[0].subs[0]), self.dbs[19].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), self.dbs[19].subs[0].subs[1].subs[1].subs[0]), self.dbs[19].subs[0].subs[1].subs[1])), self.dbs[19].subs[0].subs[1])), self.dbs[19].subs[0]):
            self.get_mainclass_c1_contatore_co2().decrementa()
        else:
            self.get_mainclass_c1_contatore_co4().resetta()
        #  /*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 4 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T6
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        if db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v8() > 4, self.dbs[20].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[20].subs[0].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[20].subs[0].subs[1])), self.dbs[20].subs[0]):
            self.get_mainclass_c1_timer_t6().disattiva()
        else:
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c270x)
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  minore di  /*55,*/ 12145 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, /*69,*/Disattiva il timer MainClass_C1_timer_T2
        if db((db(self.get_consdef() == False, self.dbs[21].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co2().get_valore() < 12145, self.dbs[21].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, self.dbs[21].subs[0].subs[1].subs[1])), self.dbs[21].subs[0].subs[1])), self.dbs[21].subs[0]):
            self.get_mainclass_c1_timer_t2().disattiva()
        #  /*35,*/  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 1203, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db((db(self.get_mainclass_c1_controllo_c9() == False, self.dbs[22].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co2().get_valore() > 1203, self.dbs[22].subs[0].subs[1])), self.dbs[22].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c270x)
        else:
            self.set_mainclass_c1_comando_c4(True)
    
    def effect_NOMINAL_ACTUATION_state1_001(self):
        """
        CNL corrispondente:
         { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 142145 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, commento: {68,}Attiva il timer MainClass_C1_timer_T8
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T8
        
        
          se la macro  MainClass_C1_macrova_M1 ( con argomento_a2   uguale a GialloaVerdea ,argomento_a10   uguale a GialloGiallo ,argomento_a5   uguale a Verde ,argomento_a6   uguale a Verde  e argomento_a1   uguale a RossoGiallox )   è  diverso da  True  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T2 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V5 non è  uguale a c270x commento: {36,} e  se il timer MainClass_C1_timer_T2 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde commento: {35,} o  se il controllo MainClass_C1_controllo_C10 non è  uguale a RossoGialloxVerdex, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M10  commento: {73,}
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  maggiore di  commento: {54,} 10 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 1303 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 4,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M6   commento: {73,}
        
        
         commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 11 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 14214,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
           
         }
        """
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 142145 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db((db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), self.dbs[23].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 142145, self.dbs[23].subs[0].subs[0].subs[1].subs[0]), self.dbs[23].subs[0].subs[0].subs[1])), self.dbs[23].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[23].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[23].subs[0].subs[1].subs[0].subs[1])), self.dbs[23].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[23].subs[0].subs[1].subs[1].subs[0]), self.dbs[23].subs[0].subs[1].subs[1])), self.dbs[23].subs[0].subs[1])), self.dbs[23].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[23].subs[1])
        #  /*73,*/
        #     
        #   /*35,*/  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, /*68,*/Attiva il timer MainClass_C1_timer_T8
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T8
        if db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[24].subs[0]):
            self.get_mainclass_c1_timer_t8().attiva()
        else:
            self.get_mainclass_c1_timer_t8().attiva()
        #  se la macro  MainClass_C1_macrova_M1 ( con argomento_a2   uguale a GialloaVerdea ,argomento_a10   uguale a GialloGiallo ,argomento_a5   uguale a Verde ,argomento_a6   uguale a Verde  e argomento_a1   uguale a RossoGiallox )   è  diverso da  True  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a c270x /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo MainClass_C1_controllo_C10 non è  uguale a RossoGialloxVerdex, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M10
        if db((db((db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m1(GlobalEnumeration.rossogiallox,GlobalEnumeration.giallogiallo,GlobalEnumeration.gialloaverdea,GlobalEnumeration.verde,GlobalEnumeration.verde, self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isDisattivato(), self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[25].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[25].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isAttivato(), self.dbs[25].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[25].subs[0].subs[0].subs[0].subs[1])), self.dbs[25].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[25].subs[0].subs[0].subs[1])), self.dbs[25].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, self.dbs[25].subs[0].subs[1].subs[0]), self.dbs[25].subs[0].subs[1])), self.dbs[25].subs[0]):
            self.set_mainclass_c1_comando_c4(True)
        else:
            self.macroMainclass_c1_macroef_m10(self.dbs[25].subs[1])
        #  /*73,*/
        #   /*37,*/  se la variabile MainClass_C1_variabile_V8 è  maggiore di  /*54,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 4,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8  /*73,*/
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M6
        if db((db((db(self.get_mainclass_c1_variabile_v8() > 10, self.dbs[26].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 1303, self.dbs[26].subs[0].subs[0].subs[1].subs[0]), self.dbs[26].subs[0].subs[0].subs[1])), self.dbs[26].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v8() == 4, self.dbs[26].subs[0].subs[1])), self.dbs[26].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[26].subs[1])
        else:
            self.macroMainclass_c1_macroef_m6(self.dbs[26].subs[2])
        #  /*73,*/
        #   /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 14214,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db((db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[27].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[27].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[27].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), self.dbs[27].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[0].subs[0].subs[1])), self.dbs[27].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 11, self.dbs[27].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[27].subs[0].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[0].subs[1])), self.dbs[27].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 14214, self.dbs[27].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[1])), self.dbs[27].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[27].subs[1])
    
    def effect_NOMINAL_ACTUATION_state1_002(self):
        """
        CNL corrispondente:
         { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a RossoGialloVerde, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co4
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a Verde, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
        
           
          se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 non è disattivo, commento: {68,}Attiva il timer MainClass_C1_timer_T8
        
           
         }
        """
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a RossoGialloVerde, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co4
        if db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == GlobalEnumeration.rossogialloverde, self.dbs[28].subs[0].subs[0]), self.dbs[28].subs[0]):
            self.get_mainclass_c1_contatore_co4().decrementa()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a Verde, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False
        if db((db(not db(self.get_mainclass_c1_restoreti_ti3_restore().isAttivato(), self.dbs[29].subs[0].subs[0].subs[0]), self.dbs[29].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, self.dbs[29].subs[0].subs[1])), self.dbs[29].subs[0]):
            self.set_mainclass_c1_comando_c4(False)
        #  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è disattivo, /*68,*/Attiva il timer MainClass_C1_timer_T8
        if db((db(self.get_consdef() == False, self.dbs[30].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t8().isDisattivato(), self.dbs[30].subs[0].subs[1].subs[0]), self.dbs[30].subs[0].subs[1])), self.dbs[30].subs[0]):
            self.get_mainclass_c1_timer_t8().attiva()
    
    def effect_NORMALIZATION_state1_state2_000(self):
        """
        CNL corrispondente:
         { commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde,  Applica gli effetti
               della macro MainClass_C1_macroef_M6   commento: {73,}
        
           
         }
        """
        #  /*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M6
        if db((db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, self.dbs[31].subs[0].subs[0].subs[0]), self.dbs[31].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[31].subs[0].subs[1].subs[0].subs[0]), self.dbs[31].subs[0].subs[1].subs[0]), self.dbs[31].subs[0].subs[1])), self.dbs[31].subs[0]):
            self.macroMainclass_c1_macroef_m6(self.dbs[31].subs[1])
    
    def effect_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 12 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 11321 commento: {36,} e  se il timer MainClass_C1_timer_T6 è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGialloxVerdex commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 1545 commento: {36,} e  se il timer MainClass_C1_timer_T2 è disattivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
        
        
          se il controllo ConsDef è uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 110 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 143 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  maggiore di  commento: {54,} 5 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 142145 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 6, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 120 commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        
           
        
        }
        """
        #  /*35,*/  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 11321 /*36,*/ e  se il timer MainClass_C1_timer_T6 è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False
        if db((db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[32].subs[0].subs[0]) or db((db((db((db(self.get_mainclass_c1_contatore_co4().get_valore() < 12, self.dbs[32].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[32].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[32].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 11321, self.dbs[32].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), self.dbs[32].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[32].subs[0].subs[1].subs[0].subs[1])), self.dbs[32].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[32].subs[0].subs[1].subs[1])), self.dbs[32].subs[0].subs[1])), self.dbs[32].subs[0]):
            self.set_mainclass_c1_comando_c1(False)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C1 è  diverso da RossoGialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 1545 /*36,*/ e  se il timer MainClass_C1_timer_T2 è disattivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8  /*73,*/
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2
        if db((db(not db(self.get_mainclass_c1_controllo_c1() == GlobalEnumeration.rossogialloxverdex, self.dbs[33].subs[0].subs[0].subs[0]), self.dbs[33].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co2().get_valore() > 1545, self.dbs[33].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t2().isDisattivato(), self.dbs[33].subs[0].subs[1].subs[1])), self.dbs[33].subs[0].subs[1])), self.dbs[33].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[33].subs[1])
        else:
            self.get_mainclass_c1_timer_t2().disattiva()
        #  se il controllo ConsDef è uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2
        if db(self.get_consdef() == False, self.dbs[34].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c270x)
        else:
            self.get_mainclass_c1_timer_t2().disattiva()
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 110 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 143 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 142145 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 6, /*72,*/Azzera il contatore MainClass_C1_contatore_Co4
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False
        if db((db((db(self.get_mainclass_c1_contatore_co4().get_valore() < 110, self.dbs[35].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 143, self.dbs[35].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[35].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[35].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() > 5, self.dbs[35].subs[0].subs[0].subs[1].subs[1])), self.dbs[35].subs[0].subs[0].subs[1])), self.dbs[35].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() < 142145, self.dbs[35].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[35].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[35].subs[0].subs[1].subs[0].subs[1])), self.dbs[35].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() < 6, self.dbs[35].subs[0].subs[1].subs[1])), self.dbs[35].subs[0].subs[1])), self.dbs[35].subs[0]):
            self.get_mainclass_c1_contatore_co4().resetta()
        else:
            self.set_mainclass_c1_comando_c4(False)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 120 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        if db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 120, self.dbs[36].subs[0].subs[0].subs[0]), self.dbs[36].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isScaduto(), self.dbs[36].subs[0].subs[1])), self.dbs[36].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c270x)
    
    def effect_NOMINAL_ACTUATION_state2_000(self):
        """
        CNL corrispondente:
         { commento: {36,}  se il timer MainClass_C1_timer_T2 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T6 non è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T2
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloVerde commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
        
         commento: {36,}  se il timer MainClass_C1_timer_T2 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  commento: {53,} 133214 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 155, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 10
        
        
         }
        """
        #  /*36,*/  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T2
        if db((db((db((db((db(self.get_mainclass_c1_timer_t2().isAttivato(), self.dbs[37].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[37].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[37].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[37].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), self.dbs[37].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[37].subs[0].subs[0].subs[0].subs[1])), self.dbs[37].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[37].subs[0].subs[0].subs[1])), self.dbs[37].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[37].subs[0].subs[1])), self.dbs[37].subs[0]):
            self.get_mainclass_c1_contatore_co2().decrementa()
        else:
            self.get_mainclass_c1_timer_t2().disattiva()
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db((db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == GlobalEnumeration.rossogialloverde, self.dbs[38].subs[0].subs[0].subs[0]), self.dbs[38].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t6().isAttivato(), self.dbs[38].subs[0].subs[1])), self.dbs[38].subs[0]):
            self.set_mainclass_c1_comando_c4(False)
        else:
            self.set_mainclass_c1_comando_c4(True)
        #  /*36,*/  se il timer MainClass_C1_timer_T2 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db(self.get_mainclass_c1_timer_t2().isAttivato(), self.dbs[39].subs[0]):
            self.set_mainclass_c1_comando_c4(True)
        else:
            self.macroMainclass_c1_macroef_m8(self.dbs[39].subs[1])
        #  /*73,*/
        #   /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 133214 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 155, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 10
        if db((db(self.get_mainclass_c1_restoreti_ti4_restore().isScaduto(), self.dbs[40].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 133214, self.dbs[40].subs[0].subs[1].subs[0].subs[0]), self.dbs[40].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co4().get_valore() > 155, self.dbs[40].subs[0].subs[1].subs[1])), self.dbs[40].subs[0].subs[1])), self.dbs[40].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.rossogialloverde)
        else:
            self.set_mainclass_c1_variabile_v8(10)
    
    def effect_NOMINAL_ACTUATION_state2_state1_000(self):
        """
        CNL corrispondente:
         { commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 8 commento: {36,} o  se il timer MainClass_C1_timer_T2 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde,  Applica gli effetti
               della macro MainClass_C1_macroef_M6   commento: {73,}
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T2
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 12321 commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  commento: {55,} 13 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde,  Applica gli effetti
               della macro MainClass_C1_macroef_M10  commento: {73,}
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co4
        
        
         }
        """
        #  /*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 8 /*36,*/ o  se il timer MainClass_C1_timer_T2 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M6   /*73,*/
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T2
        if db((db((db((db(not db(self.get_mainclass_c1_variabile_v8() == 8, self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[41].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), self.dbs[41].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[41].subs[0].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, self.dbs[41].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[41].subs[0].subs[0].subs[1].subs[0]), self.dbs[41].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[41].subs[0].subs[1])), self.dbs[41].subs[0]):
            self.macroMainclass_c1_macroef_m6(self.dbs[41].subs[1])
        else:
            self.get_mainclass_c1_timer_t2().attiva()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12321 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 13 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M10  /*73,*/
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co4
        if db((db((db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), self.dbs[42].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[42].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 12321, self.dbs[42].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[42].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isScaduto(), self.dbs[42].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co4().get_valore() < 13, self.dbs[42].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[42].subs[0].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[42].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[42].subs[0].subs[0].subs[1].subs[0]), self.dbs[42].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[42].subs[0].subs[1].subs[0].subs[0]), self.dbs[42].subs[0].subs[1].subs[0]), self.dbs[42].subs[0].subs[1])), self.dbs[42].subs[0]):
            self.macroMainclass_c1_macroef_m10(self.dbs[42].subs[1])
        else:
            self.get_mainclass_c1_contatore_co4().decrementa()
    
    def effect_NOMINAL_ACTUATION_state2_001(self):
        """
        CNL corrispondente:
         {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 15450 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 13, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
        
           
         }
        """
        #  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15450 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13, /*72,*/Azzera il contatore MainClass_C1_contatore_Co4
        if db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[43].subs[0].subs[0].subs[0].subs[0]), self.dbs[43].subs[0].subs[0].subs[0]), self.dbs[43].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 15450, self.dbs[43].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[43].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[43].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[43].subs[0].subs[1].subs[0].subs[1])), self.dbs[43].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 13, self.dbs[43].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[43].subs[0].subs[1].subs[1].subs[0]), self.dbs[43].subs[0].subs[1].subs[1])), self.dbs[43].subs[0].subs[1])), self.dbs[43].subs[0]):
            self.get_mainclass_c1_contatore_co4().resetta()
    
    def effect_NOMINAL_ACTUATION_state2_state1_001(self):
        """
        CNL corrispondente:
         {  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, commento: {69,}Disattiva il timer MainClass_C1_timer_T2
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T6
        
        
         }
        """
        #  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a RossoGialloVerde, /*69,*/Disattiva il timer MainClass_C1_timer_T2
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T6
        if db((db((db(self.get_consdef() == False, self.dbs[44].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[44].subs[0].subs[0].subs[1].subs[0]), self.dbs[44].subs[0].subs[0].subs[1])), self.dbs[44].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, self.dbs[44].subs[0].subs[1].subs[0]), self.dbs[44].subs[0].subs[1])), self.dbs[44].subs[0]):
            self.get_mainclass_c1_timer_t2().disattiva()
        else:
            self.get_mainclass_c1_timer_t6().disattiva()
    
    def effect_NORMALIZATION_state2_000(self):
        """
        CNL corrispondente:
         {  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da Verde commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x,  Applica gli effetti
               della macro MainClass_C1_macroef_M6   commento: {73,}
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
        
         }
        """
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da Verde /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  diverso da c270x,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M6   /*73,*/
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[45].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[45].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[45].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, self.dbs[45].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[45].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[45].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[45].subs[0].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, self.dbs[45].subs[0].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, self.dbs[45].subs[0].subs[1].subs[0].subs[0]), self.dbs[45].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[1])), self.dbs[45].subs[0]):
            self.macroMainclass_c1_macroef_m6(self.dbs[45].subs[1])
        else:
            self.macroMainclass_c1_macroef_m8(self.dbs[45].subs[2])
    
    # effect macros
    def macroMainclass_c1_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  commento: {55,} 6 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 13 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
        
         ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 10 commento: {67,}
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 6 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 13 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2

 ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 6 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 13 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_restoreva_rv1_restore)  è minore di  (6) )  o  
( ( ( (mainclass_c1_contatore_co2)  è maggiore di  (13) )  e  ( negazione di ((mainclass_c1_variabile_v8)  è minore di  (4)) ) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))) ) )""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_restoreva_rv1_restore)  è minore di  (6)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_contatore_co2)  è maggiore di  (13) )  e  ( negazione di ((mainclass_c1_variabile_v8)  è minore di  (4)) ) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co2)  è maggiore di  (13) )  e  ( negazione di ((mainclass_c1_variabile_v8)  è minore di  (4)) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (13)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è minore di  (4))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v8)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_controllo_c2)  è uguale a  (verde) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        if db(self.get_consdef() == False, di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.rossogialloverde)
        else:
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c270x)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 6 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 13 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2
        #   ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 10
        if db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() < 6, di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_contatore_co2().get_valore() > 13, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() < 4, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co2().decrementa()
        else:
            self.set_mainclass_c1_variabile_v8(10)
    
    def macroMainclass_c1_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {36,}  se il timer MainClass_C1_timer_T8 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore c270x
        
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde commento: {36,} e  se il timer MainClass_C1_timer_T2 non è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T6
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde commento: {36,} o  se il timer MainClass_C1_timer_T2 è attivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T6
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T8 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore c270x""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T8 è attivo""", [
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*36,*/ o  se il timer MainClass_C1_timer_T2 è attivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M8  /*73,*/

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*36,*/ o  se il timer MainClass_C1_timer_T2 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer MainClass_C1_timer_T8 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore RossoGialloVerde
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore c270x
        if db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.rossogialloverde)
        else:
            self.set_mainclass_c1_comando_c9(GlobalEnumeration.c270x)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde /*36,*/ e  se il timer MainClass_C1_timer_T2 non è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T6
        if db((db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c4(True)
        else:
            self.get_mainclass_c1_timer_t6().disattiva()
        #  /*35,*/  se il controllo MainClass_C1_controllo_C2 non è  uguale a Verde /*36,*/ o  se il timer MainClass_C1_timer_T2 è attivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8  /*73,*/
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T6
        if db((db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.macroMainclass_c1_macroef_m8(di_ctx.subs[2].subs[1])
        else:
            self.get_mainclass_c1_timer_t6().disattiva()
    
    def macroMainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  commento: {53,} 8 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T6 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co2
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( (mainclass_c1_variabile_v5)  è uguale a  (c270x) ) )  e  ( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (8)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( (mainclass_c1_variabile_v5)  è uguale a  (c270x) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)) )  o  
( negazione di (il timer 'mainclass_c1_timer_t6' è attivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))) )  e  
( (mainclass_c1_variabile_v5)  è uguale a  (c270x) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde, /*72,*/Azzera il contatore MainClass_C1_contatore_Co2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (False)) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 8 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        if db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == 8, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c270x)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C10 è  diverso da RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  uguale a c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c270x
        if db((db((db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c270x)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da Verde, /*72,*/Azzera il contatore MainClass_C1_contatore_Co2
        if db((db((db(not db(self.get_mainclass_c1_controllo_c9() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co2().resetta()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, argomento_ave10, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 5 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  commento: {53,} 1303 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  commento: {53,} 4 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 152, Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 13 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  commento: {54,} 3, Solo una delle seguenti { 
         commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  commento: {53,} 1 o  se l'argomento argomento_ave8 è  uguale a  True  commento: {39,}  commento: {36,} o  se il timer MainClass_C1_timer_T6 è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 12, Almeno una delle seguenti { 
         commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 11 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  commento: {39,} , Almeno una delle seguenti { 
         commento: {62,} commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 121 commento: {36,} e  se il timer MainClass_C1_timer_T2 è attivo commento: {36,} o  se il timer MainClass_C1_timer_T6 è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
         commento: {62,}  se l'argomento argomento_ave8 è  uguale a  True  commento: {39,}  commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
         commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
          se l'argomento argomento_ave8 non  è  diverso da  False  commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 114 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  minore di  commento: {55,} 5 commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da  commento: {56,} 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  commento: {39,} , Verifica che   commento: {49,50,}  commento: {,}  il timer MainClass_C1_timer_T8 sia attivo
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia disattivo
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  diverso da  commento: {56,} 10
        
        
         } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 12
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
         commento: {104,} e  che   l'argomento argomento_ave8 sia  diverso da  False  commento: {,} 
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 10
        
        
         } Verifica che   commento: {48,49,51,52,}  commento: {,}  il timer MainClass_C1_timer_T2 non sia attivo
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  minore di  commento: {55,} 113
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
        
        
         } Verifica che   commento: {47,48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 non sia scaduto
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T2 sia scaduto
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde
        
        
         } Verifica che   commento: {50,52,}  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  minore di  commento: {55,} 6
         commento: {104,} o  che   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {,} 
        
        
         } Verifica che   commento: {49,52,}   l'argomento argomento_ave5 sia  uguale a Verde commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia attivo
         commento: {104,} e  che   l'argomento argomento_ave8 sia  diverso da  True  commento: {39,} 
         commento: {104,} e  che   l'argomento argomento_ave3 non  sia  uguale a  True  commento: {39,} 
        
        
         } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 14
         commento: {104,} o  che   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
         commento: {104,} o  che   l'argomento argomento_ave3 non  sia  diverso da  False  commento: {39,} 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T8 non sia scaduto
        
        
         } Verifica che   commento: {48,50,51,52,}  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
         commento: {104,} o  che   l'argomento argomento_ave8 non  sia  diverso da  False  commento: {,} 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  commento: {54,} 1121
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde
         commento: {104,} e  che   l'argomento argomento_ave4 sia  diverso da  False  commento: {39,} 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  uguale a c270x
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 152, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 } Verifica che   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave5 sia  uguale a Verde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 14
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto


 } Verifica che   /*48,50,51,52,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  /*54,*/ 1121
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a c270x""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 152, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 } Verifica che   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave5 sia  uguale a Verde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 14
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 152""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 1303 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 1303""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 1303""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 152""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 } Verifica che   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave5 sia  uguale a Verde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 14
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 } Verifica che   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave5 sia  uguale a Verde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 7""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v8)  è maggiore di  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 } Verifica che   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 } Verifica che   /*49,52,*/   l'argomento argomento_ave5 sia  uguale a Verde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12, Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 } Verifica che   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave8 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 } Verifica che   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde o  se l'argomento argomento_ave4 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True  /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde e  se l'argomento argomento_ave4 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C2 è  uguale a Verde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave4 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 } Verifica che   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex, Almeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 121""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co2)  è minore di  (121)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C10 è  uguale a RossoGialloxVerdex""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave8 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo, Almeno una delle seguenti { 
  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 è  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114 /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 114""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (114))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (114)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v8)  è minore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 non  è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,50,*/  /*,*/  il timer MainClass_C1_timer_T8 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (12)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a RossoGialloVerde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave8 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 10""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,52,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 113""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T2 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T2 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,52,*/  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v8)  è minore di  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,52,*/   l'argomento argomento_ave5 sia  uguale a Verde /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*49,52,*/   l'argomento argomento_ave5 sia  uguale a Verde""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   l'argomento argomento_ave8 sia  diverso da  True""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T6 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave8 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 14
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 14
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 14
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (14))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave3 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  /*54,*/ 1121
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  /*54,*/ 1121
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  /*54,*/ 1121""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,51,52,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave8 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co4 non sia  maggiore di  /*54,*/ 1121""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (1121)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a Verde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a c270x""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(self.get_mainclass_c1_variabile_v8() == 5, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co2().get_valore() == 1303, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v8() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() > 152, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_variabile_v8() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave8 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co4().get_valore() < 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() < 121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(argomento_ave8 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(not db(not db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 114, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() < 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co4().get_valore() > 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co2().get_valore() < 113, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v8() < 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(argomento_ave5 == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave8 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(argomento_ave3 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(argomento_ave3 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c5() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave8 == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co4().get_valore() > 1121, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.verde, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(argomento_ave4 == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m3")
    def macroMainclass_c1_macrove_m3(self, argomento_ave3, argomento_ave4, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  commento: {53,} 4 commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave8 è  uguale a  False  commento: {39,} , Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T2 non sia attivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave8 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  /*53,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave8 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m9")
    def macroMainclass_c1_macrove_m9(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a10   uguale a Verde ,argomento_a5   uguale a GialloVerde ,argomento_a6   uguale a c270x ,argomento_a1   uguale a c270x ,argomento_a7   uguale a RossoGialloxVerdex  e argomento_a9   uguale a GialloVerde )   è  diverso da  False  commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T2 è attivo, Solo una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 15 o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,49,50,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  uguale a  commento: {53,} 4
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  minore di  commento: {55,} 9
        
        
         } Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  minore di  commento: {55,} 8
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 non sia  uguale a  commento: {53,} 5
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  diverso da  commento: {56,} 11
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co4 non sia  minore di  commento: {55,} 120
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a  True 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a10   uguale a Verde ,argomento_a5   uguale a GialloVerde ,argomento_a6   uguale a c270x ,argomento_a1   uguale a c270x ,argomento_a7   uguale a RossoGialloxVerdex  e argomento_a9   uguale a GialloVerde )   è  diverso da  False  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15 o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 9


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  minore di  /*55,*/ 120
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a10   uguale a Verde ,argomento_a5   uguale a GialloVerde ,argomento_a6   uguale a c270x ,argomento_a1   uguale a c270x ,argomento_a7   uguale a RossoGialloxVerdex  e argomento_a9   uguale a GialloVerde )   è  diverso da  False  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15 o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 9


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a10   uguale a Verde ,argomento_a5   uguale a GialloVerde ,argomento_a6   uguale a c270x ,argomento_a1   uguale a c270x ,argomento_a7   uguale a RossoGialloxVerdex  e argomento_a9   uguale a GialloVerde )   è  diverso da  False  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M4 ( con argomento_a10   uguale a Verde ,argomento_a5   uguale a GialloVerde ,argomento_a6   uguale a c270x ,argomento_a1   uguale a c270x ,argomento_a7   uguale a RossoGialloxVerdex  e argomento_a9   uguale a GialloVerde )   è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T2 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15 o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 15""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (15)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 9""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  minore di  /*55,*/ 120
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""LessThanImpl\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  minore di  /*55,*/ 8""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  minore di  /*55,*/ 120
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  minore di  /*55,*/ 120""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co4)  è minore di  (120)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(db(self.macroMainclass_c1_macrova_m4(GlobalEnumeration.c270x,GlobalEnumeration.verde,GlobalEnumeration.gialloverde,GlobalEnumeration.c270x,GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v8() == 4, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v8() < 9, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(self.get_mainclass_c1_variabile_v8() < 8, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == 5, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 11, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co4().get_valore() < 120, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c5() == True, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m1")
    def macroMainclass_c1_macrova_m1(self, argomento_a1, argomento_a10, argomento_a2, argomento_a5, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  o  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 è  diverso da RossoGialloVerde commento: {39,}  , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  o  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 è  diverso da RossoGialloVerde /*39,*/  , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  o  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c5)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((argomento_a2)  è uguale a  (rossogialloverde)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a2)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a2)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  o  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 è  diverso da RossoGialloVerde /*39,*/  , assegna alla macro il valore  True
        if db((db(not db(not db(self.get_mainclass_c1_controllo_c5() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_a2 == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroMainclass_c1_macrova_m4")
    def macroMainclass_c1_macrova_m4(self, argomento_a1, argomento_a10, argomento_a5, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a3, argomento_a4, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm4DaSender3e4efa96(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm4DaSender3e4efa96')
    
    def eventMainclass_c1_command_comm5(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm5')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm9(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm9')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c3_prev(self.get_mainclass_c1_previousco_c3())
        self.set_mainclass_c1_previousco_c6_prev(self.get_mainclass_c1_previousco_c6())
        self.set_mainclass_c1_previousco_c7_prev(self.get_mainclass_c1_previousco_c7())
        self.set_mainclass_c1_previousco_c8_prev(self.get_mainclass_c1_previousco_c8())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())
        self.set_mainclass_c1_previousva_pv5_prev(self.get_mainclass_c1_previousva_pv5())

