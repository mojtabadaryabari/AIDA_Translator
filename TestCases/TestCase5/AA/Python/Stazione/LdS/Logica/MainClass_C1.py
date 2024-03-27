# Codice del modello 'TestCase5', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_previousva_pv2(False)
        self.set_mainclass_c1_previousva_pv3(False)
        self.set_mainclass_c1_previousva_pv4(GlobalEnumeration.giallogiallo)
        self.set_mainclass_c1_previousva_pv5(False)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.c270x)
        self.set_mainclass_c1_variabile_v2(0)
        self.set_mainclass_c1_variabile_v4(0)
        self.set_mainclass_c1_variabile_v9(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2 : set([]),
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set(['eventMainclass_c1_command_comm8DaSender1a75134',]),
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7 : set([]),
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5 : set([]),
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4 : set(['eventMainclass_c1_command_comm1',]),
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm2DaSenderb6f8ffb3'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm2DaSenderb6f8ffb3',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm2DaSenderb6f8ffb3',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm3'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm3',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm3',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm6'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm6',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm6',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm8DaSender1a75134'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm8DaSender1a75134',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm8DaSender1a75134',self.ManCmdResponse.NOOP)


        if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
        # for each manual command that can be received in Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1
            if self.is_triggered('eventMainclass_c1_command_comm8DaSender1a75134'):
                self.set_man_cmd_response('eventMainclass_c1_command_comm8DaSender1a75134',self.ManCmdResponse.BLOCKED)

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
        _State2__State1__stateSheet_1__normalization__transitionTo_0 = 2
        _State1__State1__stateSheet_0__permanence = 3
        _State7__State7__stateSheet_5__permanence = 4
        _State7__State4__stateSheet_5__normalization__transitionTo_0 = 5
        _State5__State5__stateSheet_4__permanence = 6
        _State4__State4__stateSheet_3__permanence = 7
        _State4__State2__stateSheet_3__nominalActuation__transitionTo_0 = 8
        _State4__State7__stateSheet_3__nominalActuation__transitionTo_1 = 9
        _State4__State5__stateSheet_3__nominalActuation__transitionTo_2 = 10
        _State4__State1__stateSheet_3__nominalActuation__transitionTo_3 = 11
        _State4__State3__stateSheet_3__nominalActuation__transitionTo_4 = 12
        _State3__State3__stateSheet_2__permanence = 13

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1_parametro_p3, mainclass_c1_parametro_p6, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p6(mainclass_c1_parametro_p6)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(10000)
        self.set_mainclass_c1_restoreti_ti1_restore(10000)
        self.set_mainclass_c1_restoreti_ti2(24000)
        self.set_mainclass_c1_restoreti_ti2_restore(24000)
        self.set_mainclass_c1_restoreti_ti3(42000)
        self.set_mainclass_c1_restoreti_ti3_restore(42000)
        self.set_mainclass_c1_timer_t10(35000)
        self.set_mainclass_c1_timer_t4(43000)
        self.set_mainclass_c1_timer_t9(51000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_timer_t10,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t9,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co8(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p6(self, mainclass_c1_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6",mainclass_c1_parametro_p6)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c7(self, mainclass_c1_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c7",mainclass_c1_comando_c7)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c1")

    def get_mainclass_c1_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c3")

    def get_mainclass_c1_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c5")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6")

    def get_mainclass_c1_previousco_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c9")


    # setters for state variables
    def set_mainclass_c1_previousco_c10_prev(self, mainclass_c1_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev",mainclass_c1_previousco_c10_prev)
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c6_prev(self, mainclass_c1_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev",mainclass_c1_previousco_c6_prev)
    def set_mainclass_c1_previousco_c9_prev(self, mainclass_c1_previousco_c9_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c9_prev",mainclass_c1_previousco_c9_prev)
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
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v4(self, mainclass_c1_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4",mainclass_c1_variabile_v4)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
    def get_mainclass_c1_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev")

    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev")

    def get_mainclass_c1_previousco_c9_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c9_prev")

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

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4")

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

    def set_mainclass_c1_timer_t10(self, timerDuration):
        self.mainclass_c1_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t10", self.memory)

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)

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

    def get_mainclass_c1_timer_t10(self):
        return self.mainclass_c1_timer_t10

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t9(self):
        return self.mainclass_c1_timer_t9


    # setters for counters
    def set_mainclass_c1_contatore_co8(self, counterInitValue):
        self.mainclass_c1_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co8", self.memory)


    # getters for counters
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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*81,*/  Ricezione del  comando manuale   MainClass_C1_command_comm8 da  Sender1a75134   /*76,*/
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 3 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 12 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 2, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 15315 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 6, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 non sia attivo


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a  /*53,*/ 2""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm8 da  Sender1a75134"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*76,*/
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 3 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 12 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 2, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 15315 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 6, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 non sia attivo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*76,*/
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 3 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 12 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*76,*/
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 3""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 non è  uguale a  /*53,*/ 1""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 3""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (3)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 12 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 12""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3)  è maggiore di  (2)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 15315 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 6, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 non sia attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 15315 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 6""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 15315 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 15315""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 6""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""LessThanImpl\nil parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 10""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 6""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (6)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 non sia attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a  /*53,*/ 2""", [
                    ]),#2
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#3
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 123 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 12, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 10""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 123 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 12, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 123 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 12""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 123 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 12""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 123""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (123)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 12""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (12)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 4""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 6""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (6)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 4""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (4)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T10 è attivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 1""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 non è  minore di  /*55,*/ 8""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v2)  è minore di  (8)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V4 è  uguale a  /*53,*/ 4""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 13""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (13)""", [
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
                    DIBoolExpr("""GreaterThanImpl\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 10""", [
                    ]),#1
                    ]),#4
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#5
                    DIBoolExpr("""NAryLogicOP (AND)\n/*87,*/  Almeno una delle seguenti {
 /*85,*/  Tutte le seguenti {
 Ricezione del comando   MainClass_C1_command_comm1    /*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo, Almeno una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T9 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1


}
}""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*85,*/  Tutte le seguenti {
 Ricezione del comando   MainClass_C1_command_comm1    /*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo, Almeno una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T9 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1


}""", [
                    EventDebInfo("""Ricezione Comando Automatico\ncomando   MainClass_C1_command_comm1"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo, Almeno una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T9 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  /*53,*/ 7


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*79,*/
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 non è  diverso da c270""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v2)  è maggiore di  (2)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T9 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  /*53,*/ 7


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T9 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 11


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T9 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T9 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 è  diverso da c270""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 2""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (2)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T9 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 11


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3


 }""", [
                    DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo""", [
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 non è  uguale a c270""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 15150""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (15150))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (15150)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 3""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (3)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 11""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (11)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  /*53,*/ 7""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (7)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""GreaterThanImpl\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1""", [
                    ]),#2
                    ]),#0
                    ]),#6
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#7
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#8
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo, Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo, Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 è attivo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T10 è attivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T4 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  uguale a  False""", [
                    ]),#1
                    ]),#0
                    ]),#9
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#10
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#11
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#12
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T10 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 è  diverso da c270""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#13
                    DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 12, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 3

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 12""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_parametro_p3)  è uguale a  (4) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((mainclass_c1_contatore_co8)  è maggiore di  (12)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_parametro_p3)  è uguale a  (4) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (4)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è maggiore di  (12))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (12)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )"""),#1
                    ]),#14
                    DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 5,  Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 9""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 5""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti3_restore' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti3_restore' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (5))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (5)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )"""),#1
                    ]),#15
                    DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 3

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t4' è inattivo )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#16
                    DIStatement("""ITEStatementImpl\n/*73,*/


 /*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) /*73,*/

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )"""),#1
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#2
                    ]),#17
                    DIStatement("""ITStatement\n/*73,*/


  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )  non  è  uguale a RossoGialloGiallo /*40,*/  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  /*56,*/ 5,  Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )  non  è  uguale a RossoGialloGiallo /*40,*/  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  /*56,*/ 5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( (mainclass_c1_variabile_v9)  è maggiore di  (10) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( (mainclass_c1_variabile_v9)  è maggiore di  (10) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (10)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v9)  è uguale a  (5)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (5))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (5)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )"""),#1
                    ]),#18
                    DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) /*73,*/

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( ( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )  e  
( il timer 'mainclass_c1_timer_t4' è inattivo ) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )  e  
( il timer 'mainclass_c1_timer_t4' è inattivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_variabile_v4)  è minore di  (1) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v4)  è minore di  (1)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )"""),#1
                    ]),#19
                    DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 1

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))) ) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (9))) ) )  e  ( (mainclass_c1_controllo_c3)  è uguale a  (rossogiallo) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))) ) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (9))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (9)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (9))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (9)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#20
                    DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo, /*72,*/Azzera il contatore MainClass_C1_contatore_Co8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)) ) )  o  
( il timer 'mainclass_c1_timer_t4' è inattivo ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( il timer 'mainclass_c1_timer_t9' è inattivo ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)) ) )  o  
( il timer 'mainclass_c1_timer_t4' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( il timer 'mainclass_c1_timer_t9' è inattivo )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è inattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#21
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro MainClass_C1_macroef_M8  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 1""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#22
                    DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 15423 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 13 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo,  Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 15423 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 13 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))) )  e  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (15423)) ) )  o  
( ( negazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)) )  e  
( negazione di (negazione di ((mainclass_c1_contatore_co8)  è uguale a  (13))) ) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))) )  e  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (15423)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (15423))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (15423)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)) )  e  
( negazione di (negazione di ((mainclass_c1_contatore_co8)  è uguale a  (13))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co8)  è uguale a  (13)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (13))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (13)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )  e  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#23
                    DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co8

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))) ) )  o  
( ( ( (mainclass_c1_controllo_c3)  è uguale a  (rossogiallo) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t10' è inattivo) ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_controllo_c3)  è uguale a  (rossogiallo) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t10' è inattivo) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c3)  è uguale a  (rossogiallo) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t10' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#24
                    DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 8, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 5""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 8""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è maggiore di  (8))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v2)  è maggiore di  (8)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#25
                    DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 11150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1542 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 10 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , /*68,*/Attiva il timer MainClass_C1_timer_T4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 11150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1542 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 10 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (2))) ) )  o  
( ( ( negazione di ((mainclass_c1_contatore_co8)  è maggiore di  (11150)) )  e  ( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (1542)) ) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è minore di  (10)) ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (2))) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (2)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (2))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (2)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_contatore_co8)  è maggiore di  (11150)) )  e  ( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (1542)) ) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è minore di  (10)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co8)  è maggiore di  (11150)) )  e  ( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (1542)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è maggiore di  (11150))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (11150)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (1542))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (1542)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è minore di  (10))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (10)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#26
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a  /*53,*/ 7, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T10""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a  /*53,*/ 7""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_restoreva_rv1_restore)  è maggiore di  (5) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_restoreva_rv1_restore)  è maggiore di  (5)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (7))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (7)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#27
                    DIStatement("""ITStatement\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#28
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 14150, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 14150""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è attivo) )  e  
( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (True)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è maggiore di  (14150))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (14150)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#29
                    DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 15423 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9,  Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 15423 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (15423)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v9)  è uguale a  (4)) )  e  
( (mainclass_c1_parametro_p3)  è minore di  (9) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (4))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (4)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (9)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )"""),#1
                    ]),#30
                    DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 14, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 7""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 14""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( ( ( negazione di (il timer 'mainclass_c1_timer_t4' è scaduto) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'mainclass_c1_timer_t4' è scaduto) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t4' è scaduto) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (14))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (14)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#31
                    DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  /*56,*/ 8, /*69,*/Disattiva il timer MainClass_C1_timer_T4""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  /*56,*/ 8""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (8))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (8)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    ]),#32
                    DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co8""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#33
                    DIStatement("""ITStatement\n/*36,*/  se il timer MainClass_C1_timer_T10 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 14150 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 6 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo,  Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T10 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 14150 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 6 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( il timer 'mainclass_c1_timer_t10' è attivo )  e  ( negazione di ((mainclass_c1_variabile_v9)  è minore di  (3)) ) )  e  ( negazione di ((mainclass_c1_contatore_co8)  è minore di  (14150)) ) )  e  ( (mainclass_c1_variabile_v4)  è minore di  (6) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'mainclass_c1_timer_t10' è attivo )  e  ( negazione di ((mainclass_c1_variabile_v9)  è minore di  (3)) ) )  e  ( negazione di ((mainclass_c1_contatore_co8)  è minore di  (14150)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t10' è attivo )  e  ( negazione di ((mainclass_c1_variabile_v9)  è minore di  (3)) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è minore di  (3))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v9)  è minore di  (3)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è minore di  (14150))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (14150)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v4)  è minore di  (6)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )"""),#1
                    ]),#34
                    DIStatement("""ITStatement\n/*73,*/

   
 /*37,*/  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 7 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3, /*69,*/Disattiva il timer MainClass_C1_timer_T4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*37,*/  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 7 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è minore di  (7))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v9)  è minore di  (7)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (3)""", [
                    ]),#1
                    ]),#0
                    ]),#35
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 6 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ o  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 6 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ o  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (mainclass_c1_variabile_v9)  è maggiore di  (6) )  o  
( ( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )  e  
( negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270)) ) ) )  o  
( il timer 'mainclass_c1_timer_t9' è inattivo ) )  o  
( il timer 'mainclass_c1_timer_t9' è attivo )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (mainclass_c1_variabile_v9)  è maggiore di  (6) )  o  
( ( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )  e  
( negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270)) ) ) )  o  
( il timer 'mainclass_c1_timer_t9' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_variabile_v9)  è maggiore di  (6) )  o  
( ( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )  e  
( negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270)) ) )""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (6)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )  e  
( negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#36
                    DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 10""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                    ]),#0
                    ]),#0
                    ]),#37
                    DIStatement("""ITEStatementImpl\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11, /*69,*/Disattiva il timer MainClass_C1_timer_T10

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (1)) ) )  e  ( (mainclass_c1_parametro_p9)  è maggiore di  (9) ) )  e  
( il timer 'mainclass_c1_timer_t4' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (1)) ) )  e  ( (mainclass_c1_parametro_p9)  è maggiore di  (9) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (1)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (1))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (1)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (9)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (11)""", [
                    ]),#1
                    ]),#0
                    ]),#38
                    DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  minore di  /*55,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  /*54,*/ 3 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 9 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 8, /*69,*/Disattiva il timer MainClass_C1_timer_T4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  minore di  /*55,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  /*54,*/ 3 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 9 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 8""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_variabile_v9)  è minore di  (5) )  e  
( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (False)) )""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v9)  è minore di  (5)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_parametro_p9)  è maggiore di  (3)) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (9))) ) )  e  
( negazione di ((mainclass_c1_variabile_v2)  è uguale a  (8)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p9)  è maggiore di  (3)) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (9))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è maggiore di  (3))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (3)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (9)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (9))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (9)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (8))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (8)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#39
                    DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 5,  Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""GreaterThanImpl\nil ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 5""", [
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#40
                    DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 12 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 9, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 12 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 9""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))) )  e  
( negazione di ((mainclass_c1_variabile_v4)  è uguale a  (7)) ) )  o  
( ( (mainclass_c1_contatore_co8)  è uguale a  (11) )  e  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (12)) ) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))) )  e  
( negazione di ((mainclass_c1_variabile_v4)  è uguale a  (7)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (7))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (7)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co8)  è uguale a  (11) )  e  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (12)) )""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (11)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (12))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (12)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è minore di  (9))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v9)  è minore di  (9)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#41
                    DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo, /*72,*/Azzera il contatore MainClass_C1_contatore_Co8

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è attivo) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( il timer 'mainclass_c1_timer_t4' è scaduto )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è attivo) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#1
                    ]),#0
                    ]),#42
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 9,  Applica gli effetti
       della macro MainClass_C1_macroef_M8  /*73,*/

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T4""", [
                    DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 9""", [
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#43
                    DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 4, /*69,*/Disattiva il timer MainClass_C1_timer_T10""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 4""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (8)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (4)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (4))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (4)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#44
                    DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 1323 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 11150 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 10, /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore  False 

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 1323 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 11150 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 10""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (mainclass_c1_parametro_p3)  è minore di  (9) )  o  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (1323)) ) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) ) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co8)  è uguale a  (11150))) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (mainclass_c1_parametro_p3)  è minore di  (9) )  o  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (1323)) ) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_parametro_p3)  è minore di  (9) )  o  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (1323)) )""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (9)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (1323))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (1323)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co8)  è uguale a  (11150)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (11150))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (11150)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (10))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (10)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#45
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo,  Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti3_restore' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti3_restore' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#46
                    DIStatement("""ITStatement\n/*73,*/

   
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 3 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo,  Applica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 3 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270)) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (3)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270)) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (3)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (3))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (3)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c8)  è uguale a  (False)) )  e  
( negazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )"""),#1
                    ]),#47
                    DIStatement("""ITEStatementImpl\n/*73,*/

   
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore  True""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#48
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[14], ),
                         phase = TransPhase.Manuale
                         ),
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[19], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[15], self.dbs[16], self.dbs[17], self.dbs[18], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,
                         guard=(self.dbs[13], ),
                         effect=(self.dbs[46], self.dbs[47], self.dbs[48], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7,
                         guard=(self.dbs[12], ),
                         effect=(self.dbs[45], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5,
                         guard=(self.dbs[11], ),
                         effect=(self.dbs[40], self.dbs[41], self.dbs[42], self.dbs[43], self.dbs[44], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7,
                         guard=(self.dbs[7], ),
                         effect=(self.dbs[27], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5,
                         guard=(self.dbs[8], ),
                         effect=(self.dbs[28], self.dbs[29], self.dbs[30], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[9], ),
                         effect=(self.dbs[31], self.dbs[32], self.dbs[33], self.dbs[34], self.dbs[35], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3,
                         guard=(self.dbs[10], ),
                         effect=(self.dbs[36], self.dbs[37], self.dbs[38], self.dbs[39], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,
                         guard=(self.dbs[5], ),
                         effect=(self.dbs[21], self.dbs[22], self.dbs[23], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3,
                         guard=(self.dbs[4], ),
                         effect=(self.dbs[20], ),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase automatica
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[6], ),
                         effect=(self.dbs[24], self.dbs[25], self.dbs[26], ),
                         phase = TransPhase.Automatica
                         ),
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

        self.set_mainclass_c1_previousco_c10_prev(GlobalEnumeration.c270)
        self.set_mainclass_c1_previousco_c2_prev(True)
        self.set_mainclass_c1_previousco_c6_prev(False)
        self.set_mainclass_c1_previousco_c9_prev(GlobalEnumeration.c270)
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
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                if(self.guard_NORMALIZATION_state2_state1_000()):
                    self.curr_transition = self.Transition._State2__State1__stateSheet_1__normalization__transitionTo_0
                elif(self.guard_PERMANENCE_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7):
                if(self.guard_NORMALIZATION_state7_state4_000()):
                    self.curr_transition = self.Transition._State7__State4__stateSheet_5__normalization__transitionTo_0
                elif(self.guard_PERMANENCE_state7_000()):
                    self.curr_transition = self.Transition._State7__State7__stateSheet_5__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5):
                if(self.guard_PERMANENCE_state5_000()):
                    self.curr_transition = self.Transition._State5__State5__stateSheet_4__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4):
                if(self.guard_NOMINAL_ACTUATION_state4_state7_000()):
                    self.curr_transition = self.Transition._State4__State7__stateSheet_3__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state4_state5_000()):
                    self.curr_transition = self.Transition._State4__State5__stateSheet_3__nominalActuation__transitionTo_2
                elif(self.guard_NOMINAL_ACTUATION_state4_state1_000()):
                    self.curr_transition = self.Transition._State4__State1__stateSheet_3__nominalActuation__transitionTo_3
                elif(self.guard_NOMINAL_ACTUATION_state4_state3_000()):
                    self.curr_transition = self.Transition._State4__State3__stateSheet_3__nominalActuation__transitionTo_4
                elif(self.guard_PERMANENCE_state4_000()):
                    self.curr_transition = self.Transition._State4__State4__stateSheet_3__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3):
                if(self.guard_PERMANENCE_state3_000()):
                    self.curr_transition = self.Transition._State3__State3__stateSheet_2__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4):
                if(self.guard_NOMINAL_ACTUATION_state4_state2_000()):
                    self.curr_transition = self.Transition._State4__State2__stateSheet_3__nominalActuation__transitionTo_0
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3):
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
        elif self.curr_transition == self.Transition._State2__State1__stateSheet_1__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NORMALIZATION_state2_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State7__State7__stateSheet_5__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7)
            self.effect_PERMANENCE_state7_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State7__State4__stateSheet_5__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4)
            self.effect_NORMALIZATION_state7_state4_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State5__State5__stateSheet_4__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5)
            self.effect_PERMANENCE_state5_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State4__stateSheet_3__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state4)
            self.effect_PERMANENCE_state4_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State2__stateSheet_3__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state4_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State7__stateSheet_3__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state7)
            self.effect_NOMINAL_ACTUATION_state4_state7_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State5__stateSheet_3__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state5)
            self.effect_NOMINAL_ACTUATION_state4_state5_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State1__stateSheet_3__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state4_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State3__stateSheet_3__nominalActuation__transitionTo_4:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3)
            self.effect_NOMINAL_ACTUATION_state4_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State3__stateSheet_2__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state3)
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
        
         commento: {81,}  Ricezione del  comando manuale   MainClass_C1_command_comm8 da  Sender1a75134   commento: {76,}
         commento: {69,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 non è  uguale a  commento: {53,} 1 commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  commento: {53,} 3 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  commento: {54,} 12 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 2, Solo una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 15315 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 10 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 6, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T9 non sia attivo
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  uguale a  commento: {53,} 2
        
        
        
        }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventMainclass_c1_command_comm8DaSender1a75134'), self.dbs[1].subs[0]) and db(not db((db((db(not db(self.get_mainclass_c1_parametro_p9() == 1, self.dbs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v4() == 3, self.dbs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co8().get_valore() > 12, self.dbs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() > 2, self.dbs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[1].subs[0].subs[1])), self.dbs[1].subs[1].subs[0]) or db(not db((db((db(self.get_mainclass_c1_contatore_co8().get_valore() == 15315, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p3() < 10, self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() > 6, self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[1].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[1].subs[1].subs[0].subs[1])), self.dbs[1].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t9().isAttivato(), self.dbs[1].subs[1].subs[1].subs[1].subs[0]), self.dbs[1].subs[1].subs[1].subs[1]), self.dbs[1].subs[1].subs[1]), self.dbs[1].subs[1]) and db(self.get_mainclass_c1_variabile_v9() == 2, self.dbs[1].subs[2]))
        if res_manCmdCondition_0:
            self.set_man_cmd_response('eventMainclass_c1_command_comm8DaSender1a75134',self.ManCmdResponse.PROCESSED)
        return db(res_manCmdCondition_0, self.dbs[1])
    
    def guard_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[2])
    
    def guard_NORMALIZATION_state2_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[3])
    
    def guard_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 123 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 12, Tutte le seguenti { 
         commento: {69,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 6 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {36,}  se il timer MainClass_C1_timer_T10 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 1 commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  minore di  commento: {55,} 8 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  uguale a  commento: {53,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 13, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  maggiore di  commento: {54,} 10
        
        
        }
        """
        return db((db(not db((db(self.get_consdef() == False, self.dbs[4].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() < 123, self.dbs[4].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 12, self.dbs[4].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[4].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_mainclass_c1_parametro_p3() == 6, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() > 4, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_mainclass_c1_timer_t10().isAttivato(), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p3() < 1, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v2() < 8, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v4() == 4, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 13, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[4].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1]), self.dbs[4].subs[0]) and db(self.get_mainclass_c1_variabile_v9() > 10, self.dbs[4].subs[1])), self.dbs[4])
    
    def guard_PERMANENCE_state4_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[5])
    
    def guard_NOMINAL_ACTUATION_state4_state2_000(self):
        """
        CNL corrispondente:
         {  commento: {87,}  Almeno una delle seguenti {
         commento: {85,}  Tutte le seguenti {
         Ricezione del comando   MainClass_C1_command_comm1    commento: {79,}
         commento: {68,} commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270 commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {36,} o  se il timer MainClass_C1_timer_T10 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo, Almeno una delle seguenti { 
         commento: {68,} commento: {34,}  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 commento: {36,} e  se il timer MainClass_C1_timer_T4 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 2 commento: {36,} e  se il timer MainClass_C1_timer_T9 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo, Almeno una delle seguenti { 
         commento: {68,} commento: {35,}  se il controllo MainClass_C1_controllo_C5 è  uguale a RossoGialloGiallo, Almeno una delle seguenti { 
         commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a  commento: {53,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 15150 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  commento: {54,} 3
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  commento: {53,} 11
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  commento: {53,} 7
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 1
        
        
        }
        } }
        """
        return db((db((db(self.is_triggered('eventMainclass_c1_command_comm1'), self.dbs[6].subs[0].subs[0]) and db(not db((db((db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isScaduto(), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() > 2, self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isScaduto(), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isAttivato(), self.dbs[6].subs[0].subs[1].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[0]) or db((db(not db((db((db((db((db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isAttivato(), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == 2, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t9().isAttivato(), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogiallogiallo, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v9() == 3, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 15150, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v9() > 3, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 11, self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), self.dbs[6].subs[0].subs[1].subs[1].subs[0].subs[1]), self.dbs[6].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == 7, self.dbs[6].subs[0].subs[1].subs[1].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1].subs[1])), self.dbs[6].subs[0].subs[1].subs[1]), self.dbs[6].subs[0].subs[1]) and db(self.get_mainclass_c1_contatore_co8().get_valore() > 1, self.dbs[6].subs[0].subs[2])), self.dbs[6].subs[0])), self.dbs[6])
    
    def guard_NOMINAL_ACTUATION_state4_state7_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[7])
    
    def guard_NOMINAL_ACTUATION_state4_state5_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[8])
    
    def guard_NOMINAL_ACTUATION_state4_state1_000(self):
        """
        CNL corrispondente:
         {   se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T10 è attivo commento: {36,} o  se il timer MainClass_C1_timer_T4 non è attivo, Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  uguale a  False 
        
         }
        """
        return db((db(not db((db((db((db(self.get_consdef() == False, self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[9].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t10().isAttivato(), self.dbs[9].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t4().isAttivato(), self.dbs[9].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c1() == False, self.dbs[9].subs[0].subs[1]), self.dbs[9].subs[0])), self.dbs[9])
    
    def guard_NOMINAL_ACTUATION_state4_state3_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[10])
    
    def guard_PERMANENCE_state5_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna  commento: {80,}
        }
        """
        return db((True), self.dbs[11])
    
    def guard_PERMANENCE_state7_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna  commento: {80,}
        }
        """
        return db((True), self.dbs[12])
    
    def guard_NORMALIZATION_state7_state4_000(self):
        """
        CNL corrispondente:
         {  commento: {34,}  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {36,} o  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
        
         }
        """
        return db((db(not db((db((db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[13].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[13].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[13].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[13].subs[0].subs[0].subs[0].subs[1])), self.dbs[13].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isAttivato(), self.dbs[13].subs[0].subs[0].subs[1].subs[0]), self.dbs[13].subs[0].subs[0].subs[1])), self.dbs[13].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[13].subs[0].subs[1].subs[0].subs[0]), self.dbs[13].subs[0].subs[1].subs[0]), self.dbs[13].subs[0].subs[1]), self.dbs[13].subs[0])), self.dbs[13])
    
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
        
         commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 4 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 12, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 3
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) commento: {73,}
        
        
        
        }
        """
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 12, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 3
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )
        if db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[14].subs[0].subs[0].subs[0].subs[0]), self.dbs[14].subs[0].subs[0].subs[0]), self.dbs[14].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p3() == 4, self.dbs[14].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[14].subs[0].subs[1].subs[0].subs[1])), self.dbs[14].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 12, self.dbs[14].subs[0].subs[1].subs[1].subs[0]), self.dbs[14].subs[0].subs[1].subs[1])), self.dbs[14].subs[0].subs[1])), self.dbs[14].subs[0]):
            self.set_mainclass_c1_variabile_v4(3)
        else:
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.gialloverde,True, self.dbs[14].subs[1])
    
    def effect_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 5,  Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 9
        
        
         commento: {36,}  se il timer MainClass_C1_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 3
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
        
          se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )  non  è  uguale a RossoGialloGiallo commento: {40,}  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  maggiore di  commento: {54,} 10 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  commento: {56,} 5,  Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
        
           
        
        }
        """
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 5,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 9
        if db((db(not db(self.get_mainclass_c1_restoreti_ti3_restore().isScaduto(), self.dbs[15].subs[0].subs[0].subs[0]), self.dbs[15].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() == 5, self.dbs[15].subs[0].subs[1].subs[0]), self.dbs[15].subs[0].subs[1])), self.dbs[15].subs[0]):
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.gialloverde,True, self.dbs[15].subs[1])
        else:
            self.set_mainclass_c1_variabile_v9(9)
        #  /*36,*/  se il timer MainClass_C1_timer_T4 è disattivo e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 3
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db((db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[16].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[16].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[16].subs[0].subs[1])), self.dbs[16].subs[0]):
            self.set_mainclass_c1_variabile_v2(3)
        else:
            self.macroMainclass_c1_macroef_m8(self.dbs[16].subs[1])
        #  /*73,*/
        #   /*35,*/  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) /*73,*/
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[17].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isAttivato(), self.dbs[17].subs[0].subs[1])), self.dbs[17].subs[0]):
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.avvio,True, self.dbs[17].subs[1])
        else:
            self.macroMainclass_c1_macroef_m8(self.dbs[17].subs[2])
        #  /*73,*/
        #    se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )  non  è  uguale a RossoGialloGiallo /*40,*/  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  /*56,*/ 5,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )
        if db((db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.c270x,GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.rossogiallogiallo,True,GlobalEnumeration.rossogiallo,GlobalEnumeration.gialloverde, self.dbs[18].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[18].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, self.dbs[18].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[18].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[18].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[18].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v9() > 10, self.dbs[18].subs[0].subs[0].subs[0].subs[1])), self.dbs[18].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[18].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[18].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[18].subs[0].subs[0].subs[1].subs[1])), self.dbs[18].subs[0].subs[0].subs[1])), self.dbs[18].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v9() == 5, self.dbs[18].subs[0].subs[1].subs[0].subs[0]), self.dbs[18].subs[0].subs[1].subs[0]), self.dbs[18].subs[0].subs[1])), self.dbs[18].subs[0]):
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.avvio,True, self.dbs[18].subs[1])
    
    def effect_NORMALIZATION_state2_state1_000(self):
        """
        CNL corrispondente:
         { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} o  se il timer MainClass_C1_timer_T4 non è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 1 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
        
         }
        """
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) /*73,*/
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[19].subs[0].subs[0].subs[0].subs[0]), self.dbs[19].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[19].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[19].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[19].subs[0].subs[0].subs[1].subs[1])), self.dbs[19].subs[0].subs[0].subs[1])), self.dbs[19].subs[0].subs[0]) or db((db(self.get_mainclass_c1_variabile_v4() < 1, self.dbs[19].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[19].subs[0].subs[1].subs[1])), self.dbs[19].subs[0].subs[1])), self.dbs[19].subs[0]):
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.avvio,True, self.dbs[19].subs[1])
        else:
            self.set_mainclass_c1_comando_c4(True)
    
    def effect_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  commento: {56,} 9 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 1
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
        
        
        
        }
        """
        #  /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 1
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False
        if db((db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == 9, self.dbs[20].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[20].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[20].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[1])), self.dbs[20].subs[0]):
            self.set_mainclass_c1_variabile_v9(1)
        else:
            self.set_mainclass_c1_comando_c4(False)
    
    def effect_PERMANENCE_state4_000(self):
        """
        CNL corrispondente:
        
        {
        
          se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo commento: {36,} o  se il timer MainClass_C1_timer_T4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T9 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T4 non è disattivo, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
        
           
          se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 1
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 15423 commento: {35,} o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 13 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
           
        
        }
        """
        #  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T4 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo, /*72,*/Azzera il contatore MainClass_C1_contatore_Co8
        if db((db((db((db((db(self.get_consdef() == False, self.dbs[21].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogiallogiallo, self.dbs[21].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[21].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[21].subs[0].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[21].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t9().isDisattivato(), self.dbs[21].subs[0].subs[0].subs[1].subs[1])), self.dbs[21].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[21].subs[0].subs[1].subs[0]), self.dbs[21].subs[0].subs[1])), self.dbs[21].subs[0]):
            self.get_mainclass_c1_contatore_co8().resetta()
        #  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 1
        if db((db(self.get_consdef() == False, self.dbs[22].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[22].subs[0].subs[1])), self.dbs[22].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[22].subs[1])
        else:
            self.set_mainclass_c1_variabile_v2(1)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 15423 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 13 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c8() == True, self.dbs[23].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[23].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[23].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 15423, self.dbs[23].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[23].subs[0].subs[0].subs[0].subs[1])), self.dbs[23].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogiallogiallo, self.dbs[23].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[23].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 13, self.dbs[23].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[23].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[23].subs[0].subs[0].subs[1].subs[1])), self.dbs[23].subs[0].subs[0].subs[1])), self.dbs[23].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[23].subs[0].subs[1].subs[0].subs[0]), self.dbs[23].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[23].subs[0].subs[1].subs[1].subs[0]), self.dbs[23].subs[0].subs[1].subs[1])), self.dbs[23].subs[0].subs[1])), self.dbs[23].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[23].subs[1])
    
    def effect_NOMINAL_ACTUATION_state4_state2_000(self):
        """
        CNL corrispondente:
         { commento: {36,}  se il timer MainClass_C1_timer_T4 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co8
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 1
        
        
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  commento: {54,} 8, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 5
        
           
          se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 2 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 11150 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 1542 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 10 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , commento: {68,}Attiva il timer MainClass_C1_timer_T4
        
           
         }
        """
        #  /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co8
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 1
        if db((db((db((db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[24].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[24].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c8() == True, self.dbs[24].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[24].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[24].subs[0].subs[0].subs[0].subs[1])), self.dbs[24].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[24].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[24].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[24].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), self.dbs[24].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[24].subs[0].subs[0].subs[1].subs[1])), self.dbs[24].subs[0].subs[0].subs[1])), self.dbs[24].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[24].subs[0].subs[1])), self.dbs[24].subs[0]):
            self.get_mainclass_c1_contatore_co8().decrementa()
        else:
            self.set_mainclass_c1_variabile_v4(1)
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  maggiore di  /*54,*/ 8, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 5
        if db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[25].subs[0].subs[0].subs[0]), self.dbs[25].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() > 8, self.dbs[25].subs[0].subs[1].subs[0]), self.dbs[25].subs[0].subs[1])), self.dbs[25].subs[0]):
            self.set_mainclass_c1_variabile_v9(5)
        #  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 11150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1542 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 10 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , /*68,*/Attiva il timer MainClass_C1_timer_T4
        if db((db((db((db(self.get_consdef() == False, self.dbs[26].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p3() == 2, self.dbs[26].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[26].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[26].subs[0].subs[0].subs[0].subs[1])), self.dbs[26].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 11150, self.dbs[26].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[26].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 1542, self.dbs[26].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[26].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[26].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() < 10, self.dbs[26].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[26].subs[0].subs[0].subs[1].subs[1])), self.dbs[26].subs[0].subs[0].subs[1])), self.dbs[26].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c1() == False, self.dbs[26].subs[0].subs[1])), self.dbs[26].subs[0]):
            self.get_mainclass_c1_timer_t4().attiva()
    
    def effect_NOMINAL_ACTUATION_state4_state7_000(self):
        """
        CNL corrispondente:
         { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  uguale a  commento: {53,} 7, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T10
        
        
         }
        """
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a  /*53,*/ 7, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T10
        if db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() > 5, self.dbs[27].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[27].subs[0].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[0].subs[1])), self.dbs[27].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v2() == 7, self.dbs[27].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[1])), self.dbs[27].subs[0]):
            self.get_mainclass_c1_contatore_co8().incrementa()
        else:
            self.get_mainclass_c1_timer_t10().attiva()
    
    def effect_NOMINAL_ACTUATION_state4_state5_000(self):
        """
        CNL corrispondente:
         {  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo commento: {40,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 14150, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
           
         commento: {38,}  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  commento: {54,} 15423 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 4 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 9,  Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde ) commento: {73,}
        
           
         }
        """
        #  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8
        if db((db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.c270x,True,GlobalEnumeration.giallogiallo,GlobalEnumeration.gialloverde, self.dbs[28].subs[0].subs[0].subs[0]), self.dbs[28].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, self.dbs[28].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[28].subs[0].subs[1].subs[0].subs[0]), self.dbs[28].subs[0].subs[1].subs[0]), self.dbs[28].subs[0].subs[1])), self.dbs[28].subs[0]):
            self.get_mainclass_c1_contatore_co8().incrementa()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 14150, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), self.dbs[29].subs[0].subs[0].subs[0].subs[0]), self.dbs[29].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c1() == True, self.dbs[29].subs[0].subs[0].subs[1].subs[0]), self.dbs[29].subs[0].subs[0].subs[1])), self.dbs[29].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 14150, self.dbs[29].subs[0].subs[1].subs[0]), self.dbs[29].subs[0].subs[1])), self.dbs[29].subs[0]):
            self.set_mainclass_c1_comando_c4(True)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  maggiore di  /*54,*/ 15423 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 4 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a GialloVerde )
        if db((db(self.get_mainclass_c1_contatore_co8().get_valore() > 15423, self.dbs[30].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v9() == 4, self.dbs[30].subs[0].subs[1].subs[0].subs[0]), self.dbs[30].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p3() < 9, self.dbs[30].subs[0].subs[1].subs[1])), self.dbs[30].subs[0].subs[1])), self.dbs[30].subs[0]):
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.gialloverde,True, self.dbs[30].subs[1])
    
    def effect_NOMINAL_ACTUATION_state4_state1_000(self):
        """
        CNL corrispondente:
         {  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 14, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
        
           
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  commento: {56,} 8, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
        
           
          se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co8
        
           
         commento: {36,}  se il timer MainClass_C1_timer_T10 è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 14150 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 6 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo,  Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 7 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a  commento: {53,} 3, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
        
           
         }
        """
        #  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 14, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 7
        if db((db((db((db(self.get_consdef() == False, self.dbs[31].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[31].subs[0].subs[0].subs[0].subs[1])), self.dbs[31].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_timer_t4().isScaduto(), self.dbs[31].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[31].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[31].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[31].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[31].subs[0].subs[0].subs[1].subs[1])), self.dbs[31].subs[0].subs[0].subs[1])), self.dbs[31].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 14, self.dbs[31].subs[0].subs[1].subs[0]), self.dbs[31].subs[0].subs[1])), self.dbs[31].subs[0]):
            self.set_mainclass_c1_variabile_v2(7)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  /*56,*/ 8, /*69,*/Disattiva il timer MainClass_C1_timer_T4
        if db(not db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == 8, self.dbs[32].subs[0].subs[0].subs[0]), self.dbs[32].subs[0].subs[0]), self.dbs[32].subs[0]):
            self.get_mainclass_c1_timer_t4().disattiva()
        #  se il controllo ConsDef è uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co8
        if db((db(self.get_consdef() == False, self.dbs[33].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[33].subs[0].subs[1])), self.dbs[33].subs[0]):
            self.get_mainclass_c1_contatore_co8().decrementa()
        #  /*36,*/  se il timer MainClass_C1_timer_T10 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 14150 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 6 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )
        if db((db((db((db((db(self.get_mainclass_c1_timer_t10().isAttivato(), self.dbs[34].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() < 3, self.dbs[34].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[34].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[34].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() < 14150, self.dbs[34].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[34].subs[0].subs[0].subs[0].subs[1])), self.dbs[34].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v4() < 6, self.dbs[34].subs[0].subs[0].subs[1])), self.dbs[34].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[34].subs[0].subs[1])), self.dbs[34].subs[0]):
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.avvio,True, self.dbs[34].subs[1])
        #  /*73,*/
        #     
        #   /*37,*/  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 7 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 3, /*69,*/Disattiva il timer MainClass_C1_timer_T4
        if db((db(not db(self.get_mainclass_c1_variabile_v9() < 7, self.dbs[35].subs[0].subs[0].subs[0]), self.dbs[35].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v9() == 3, self.dbs[35].subs[0].subs[1])), self.dbs[35].subs[0]):
            self.get_mainclass_c1_timer_t4().disattiva()
    
    def effect_NOMINAL_ACTUATION_state4_state3_000(self):
        """
        CNL corrispondente:
         { commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  maggiore di  commento: {54,} 6 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 commento: {36,} o  se il timer MainClass_C1_timer_T9 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
        
        
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da  commento: {56,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 11, commento: {69,}Disattiva il timer MainClass_C1_timer_T10
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  minore di  commento: {55,} 5 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  commento: {54,} 3 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  commento: {56,} 9 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 8, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
        
           
         }
        """
        #  /*37,*/  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 6 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  diverso da c270 /*36,*/ o  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db((db((db((db((db(self.get_mainclass_c1_variabile_v9() > 6, self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[36].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t9().isDisattivato(), self.dbs[36].subs[0].subs[0].subs[0].subs[1])), self.dbs[36].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t9().isAttivato(), self.dbs[36].subs[0].subs[0].subs[1])), self.dbs[36].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[36].subs[0].subs[1])), self.dbs[36].subs[0]):
            self.get_mainclass_c1_contatore_co8().incrementa()
        else:
            self.set_mainclass_c1_comando_c4(True)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
        if db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), self.dbs[37].subs[0].subs[0]), self.dbs[37].subs[0]):
            self.set_mainclass_c1_comando_c4(False)
        else:
            self.set_mainclass_c1_variabile_v9(10)
        #  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11, /*69,*/Disattiva il timer MainClass_C1_timer_T10
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co8
        if db((db((db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[38].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[38].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[38].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[38].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == 1, self.dbs[38].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[38].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[38].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p9() > 9, self.dbs[38].subs[0].subs[0].subs[0].subs[1])), self.dbs[38].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[38].subs[0].subs[0].subs[1])), self.dbs[38].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co8().get_valore() < 11, self.dbs[38].subs[0].subs[1])), self.dbs[38].subs[0]):
            self.get_mainclass_c1_timer_t10().disattiva()
        else:
            self.get_mainclass_c1_contatore_co8().resetta()
        #  /*37,*/  se la variabile MainClass_C1_variabile_V9 è  minore di  /*55,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  maggiore di  /*54,*/ 3 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da  /*56,*/ 9 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 8, /*69,*/Disattiva il timer MainClass_C1_timer_T4
        if db((db((db(self.get_mainclass_c1_variabile_v9() < 5, self.dbs[39].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c1() == False, self.dbs[39].subs[0].subs[0].subs[1].subs[0]), self.dbs[39].subs[0].subs[0].subs[1])), self.dbs[39].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p9() > 3, self.dbs[39].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[39].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v2() == 9, self.dbs[39].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), self.dbs[39].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[39].subs[0].subs[1].subs[0].subs[1])), self.dbs[39].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == 8, self.dbs[39].subs[0].subs[1].subs[1].subs[0]), self.dbs[39].subs[0].subs[1].subs[1])), self.dbs[39].subs[0].subs[1])), self.dbs[39].subs[0]):
            self.get_mainclass_c1_timer_t4().disattiva()
    
    def effect_PERMANENCE_state5_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  commento: {54,} 5,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  commento: {53,} 7 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 11 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 12 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 9, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 9,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T4
        
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 4, commento: {69,}Disattiva il timer MainClass_C1_timer_T10
        
           
        
        }
        """
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 5,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db(self.get_mainclass_c1_restoreva_rv1_restore() > 5, self.dbs[40].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[40].subs[1])
        #  /*73,*/
        #     
        #   /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 12 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 9, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
        if db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[41].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() == 7, self.dbs[41].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[41].subs[0].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co8().get_valore() == 11, self.dbs[41].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 12, self.dbs[41].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[41].subs[0].subs[0].subs[1].subs[1])), self.dbs[41].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v9() < 9, self.dbs[41].subs[0].subs[1].subs[0]), self.dbs[41].subs[0].subs[1])), self.dbs[41].subs[0]):
            self.set_mainclass_c1_comando_c4(True)
        else:
            self.set_mainclass_c1_variabile_v4(6)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo, /*72,*/Azzera il contatore MainClass_C1_contatore_Co8
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), self.dbs[42].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[42].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[42].subs[0].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isScaduto(), self.dbs[42].subs[0].subs[0].subs[1])), self.dbs[42].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[42].subs[0].subs[1])), self.dbs[42].subs[0]):
            self.get_mainclass_c1_contatore_co8().resetta()
        else:
            self.set_mainclass_c1_comando_c4(True)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 9,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8  /*73,*/
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T4
        if db(self.get_mainclass_c1_variabile_v4() < 9, self.dbs[43].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[43].subs[1])
        else:
            self.get_mainclass_c1_timer_t4().attiva()
        #  /*34,*/  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 4, /*69,*/Disattiva il timer MainClass_C1_timer_T10
        if db((db(self.get_mainclass_c1_parametro_p9() > 8, self.dbs[44].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == 4, self.dbs[44].subs[0].subs[1].subs[0].subs[0]), self.dbs[44].subs[0].subs[1].subs[0]), self.dbs[44].subs[0].subs[1])), self.dbs[44].subs[0]):
            self.get_mainclass_c1_timer_t10().disattiva()
    
    def effect_PERMANENCE_state7_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 9 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 1323 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 11150 commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 10, commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore  False 
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
        
        
        }
        """
        #  /*34,*/  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 1323 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 11150 /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 10, /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore  False 
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db((db((db((db((db(self.get_mainclass_c1_parametro_p3() < 9, self.dbs[45].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 1323, self.dbs[45].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[45].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 11150, self.dbs[45].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[45].subs[0].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v9() == 10, self.dbs[45].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[1])), self.dbs[45].subs[0]):
            self.set_mainclass_c1_comando_c3(False)
        else:
            self.set_mainclass_c1_comando_c4(True)
    
    def effect_NORMALIZATION_state7_state4_000(self):
        """
        CNL corrispondente:
         { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo,  Applica gli effetti
               della macro MainClass_C1_macroef_M8  commento: {73,}
        
           
         commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 3 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo,  Applica gli effetti
               della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio ) commento: {73,}
        
           
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore  True 
        
        
         }
        """
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  diverso da RossoGiallo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db(not db(self.get_mainclass_c1_restoreti_ti3_restore().isScaduto(), self.dbs[46].subs[0].subs[0].subs[0]), self.dbs[46].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, self.dbs[46].subs[0].subs[1].subs[0]), self.dbs[46].subs[0].subs[1])), self.dbs[46].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[46].subs[1])
        #  /*73,*/
        #     
        #   /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  uguale a c270 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 3 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  diverso da RossoGialloGiallo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4( con argomento_af9   uguale a True ,argomento_af5   uguale a avvio )
        if db((db((db((db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, self.dbs[47].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[47].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == 3, self.dbs[47].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[47].subs[0].subs[0].subs[0].subs[1])), self.dbs[47].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[47].subs[0].subs[0].subs[1])), self.dbs[47].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c8() == False, self.dbs[47].subs[0].subs[1].subs[0].subs[0]), self.dbs[47].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogiallogiallo, self.dbs[47].subs[0].subs[1].subs[1].subs[0]), self.dbs[47].subs[0].subs[1].subs[1])), self.dbs[47].subs[0].subs[1])), self.dbs[47].subs[0]):
            self.macroMainclass_c1_macroef_m4(GlobalEnumeration.avvio,True, self.dbs[47].subs[1])
        #  /*73,*/
        #     
        #    se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore  True
        if db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[48].subs[0].subs[0]), self.dbs[48].subs[0]):
            self.get_mainclass_c1_contatore_co8().incrementa()
        else:
            self.set_mainclass_c1_comando_c3(True)
    
    # effect macros
    def macroMainclass_c1_macroef_m4(self, argomento_af5, argomento_af9, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  commento: {56,} 5 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 2 commento: {36,} e  se il timer MainClass_C1_timer_T10 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 15 commento: {36,} e  se il timer MainClass_C1_timer_T4 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 122, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_variabile_v9)  è uguale a  (5))) )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v9)  è uguale a  (5)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 15 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 122, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 15 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 122""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((mainclass_c1_variabile_v9)  è minore di  (2)) )  e  ( il timer 'mainclass_c1_timer_t10' è inattivo ) )  e  
( il timer 'mainclass_c1_timer_t4' è scaduto ) )  o  
( ( (mainclass_c1_contatore_co8)  è minore di  (15) )  e  
( il timer 'mainclass_c1_timer_t4' è attivo ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_variabile_v9)  è minore di  (2)) )  e  ( il timer 'mainclass_c1_timer_t10' è inattivo ) )  e  
( il timer 'mainclass_c1_timer_t4' è scaduto )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v9)  è minore di  (2)) )  e  ( il timer 'mainclass_c1_timer_t10' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è minore di  (2))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v9)  è minore di  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co8)  è minore di  (15) )  e  
( il timer 'mainclass_c1_timer_t4' è attivo )""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (15)""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (122))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (122)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da c270, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore 6
        if db((db((db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.c270x,GlobalEnumeration.c270x,GlobalEnumeration.rossogiallogiallo,True,GlobalEnumeration.giallogiallo,GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v9() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v4(6)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 15 /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 122, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co8
        if db((db((db((db((db(not db(self.get_mainclass_c1_variabile_v9() < 2, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co8().get_valore() < 15, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 122, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c4(False)
        else:
            self.get_mainclass_c1_contatore_co8().resetta()
    
    def macroMainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  diverso da RossoGialloGiallo commento: {40,} ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 8 commento: {67,}
        
           
         commento: {36,}  se il timer MainClass_C1_timer_T9 è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  True 
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  diverso da  commento: {56,} 6, commento: {69,}Disattiva il timer MainClass_C1_timer_T10
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore 9
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  diverso da RossoGialloGiallo /*40,*/ ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 8""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*67,*/

   
 /*36,*/  se il timer MainClass_C1_timer_T9 è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T9 è disattivo""", [
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 6, /*69,*/Disattiva il timer MainClass_C1_timer_T10

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 9""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  diverso da RossoGialloGiallo /*40,*/ ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 8
        if db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.c270x,True,GlobalEnumeration.giallogiallo,GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v9(8)
        #  /*67,*/
        #     
        #   /*36,*/  se il timer MainClass_C1_timer_T9 è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  True
        if db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c4(True)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V2 è  diverso da  /*56,*/ 6, /*69,*/Disattiva il timer MainClass_C1_timer_T10
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore 9
        if db(not db(self.get_mainclass_c1_variabile_v2() == 6, di_ctx.subs[2].subs[0].subs[0]), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t10().disattiva()
        else:
            self.set_mainclass_c1_variabile_v2(9)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 150 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 9, Tutte le seguenti { 
         commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T10 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 1542, Solo una delle seguenti { 
          se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo commento: {40,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 6, Verifica che   commento: {50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 123
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  maggiore di  commento: {54,} 7
        
        
         } Verifica che   commento: {47,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  diverso da  commento: {56,} 3
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T9 sia attivo
        
        
         } Verifica che   commento: {48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a  commento: {53,} 10
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  commento: {54,} 15150
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 sia  maggiore di  commento: {54,} 7
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1542, Solo una delle seguenti { 
  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 6, Verifica che   /*50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 123
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 15150
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1542, Solo una delle seguenti { 
  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 6, Verifica che   /*50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 123
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 150 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 150""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C5 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 150""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (150)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 9""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1542, Solo una delle seguenti { 
  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 6, Verifica che   /*50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 123
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1542, Solo una delle seguenti { 
  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 6, Verifica che   /*50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 123
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 7


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1542""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1542""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (1542)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 6, Verifica che   /*50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 123
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nla macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a GialloGiallo  e argomento_a1   uguale a RossoGialloGiallo )   è  uguale a RossoGialloGiallo""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C1 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 123
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 123""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 7""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T9 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 15150
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  /*53,*/ 10
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 15150""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 15150""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (15150)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  maggiore di  /*54,*/ 7""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 150, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p3() == 9, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 1542, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.c270x,GlobalEnumeration.c270x,True,GlobalEnumeration.giallogiallo,GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p3() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_contatore_co8().get_valore() > 123, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v9() > 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db(not db(self.get_mainclass_c1_parametro_p3() == 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t9().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(self.get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == 10, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 15150, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v4() > 7, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m10")
    def macroMainclass_c1_macrove_m10(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,}, Almeno una delle seguenti { 
         commento: {61,}  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 8, Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 8, Solo una delle seguenti { 
         commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {61,} commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 1242, Tutte le seguenti { 
         commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
          se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T9 sia attivo
        
        
         } Verifica che   commento: {47,48,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  minore di  commento: {55,} 13
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  maggiore di  commento: {54,} 6
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  minore di  commento: {55,} 3
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  diverso da  commento: {56,} 10
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  minore di  commento: {55,} 1
        
        
         } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a  commento: {53,} 2
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  uguale a RossoGiallo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242, Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 1242""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia attivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T9 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  maggiore di  /*54,*/ 6""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 3""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a  /*53,*/ 2
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a  /*53,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() > 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p3() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() < 1242, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(not db(self.get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t9().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() < 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p9() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v9() < 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v9() < 1, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_mainclass_c1_parametro_p3() == 2, di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m5")
    def macroMainclass_c1_macrove_m5(self, argomento_ave3, argomento_ave4, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 14150, Solo una delle seguenti { 
         commento: {62,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde commento: {39,}  e  se l'argomento argomento_ave3 non  è  uguale a  True  commento: {39,} , Almeno una delle seguenti { 
         commento: {62,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde commento: {39,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
         commento: {61,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 7 commento: {36,} o  se il timer MainClass_C1_timer_T9 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
         commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  uguale a  commento: {53,} 1 commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  minore di  commento: {55,} 11423 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  minore di  commento: {55,} 5 commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  minore di  commento: {55,} 2 commento: {36,} e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   commento: {50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  maggiore di  commento: {54,} 6
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 121
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a  commento: {53,} 6
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 sia  minore di  commento: {55,} 2
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 sia  uguale a  commento: {53,} 5
        
        
         } Verifica che   commento: {49,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  diverso da  commento: {56,} 115
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia scaduto
         commento: {104,} o  che   l'argomento argomento_ave3 sia  uguale a  False  commento: {,} 
        
        
         } Verifica che   commento: {47,48,49,50,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  uguale a  commento: {53,} 150
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  diverso da  commento: {56,} 9
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  commento: {53,} 3
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia scaduto
         commento: {104,} o  che   l'argomento argomento_ave3 non  sia  diverso da  False  commento: {,} 
        
        
         } Verifica che   commento: {47,48,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
         commento: {104,} o  che   l'argomento argomento_ave3 sia  diverso da  False  commento: {,} 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  maggiore di  commento: {54,} 1
        
        
         } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  il timer MainClass_C1_timer_T10 non sia attivo
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  diverso da  commento: {56,} 6
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  diverso da  commento: {56,} 115
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T10 sia scaduto
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  diverso da RossoGiallo commento: {,} 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 14150, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  e  se l'argomento argomento_ave3 non  è  uguale a  True  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 } Verifica che   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*,*/ 


 } Verifica che   /*47,48,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave3 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 1


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da  /*56,*/ 6
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T10 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 14150, Solo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  e  se l'argomento argomento_ave3 non  è  uguale a  True  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 } Verifica che   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*,*/ 


 } Verifica che   /*47,48,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave3 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 14150""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI2 è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 14150""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  e  se l'argomento argomento_ave3 non  è  uguale a  True  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 } Verifica che   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*,*/ 


 } Verifica che   /*47,48,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave3 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  e  se l'argomento argomento_ave3 non  è  uguale a  True  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 } Verifica che   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  e  se l'argomento argomento_ave3 non  è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a GialloVerde ,argomento_a10   uguale a c270x ,argomento_a2   uguale a c270x ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P6 è  uguale a c270""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  e  se l'argomento argomento_ave3 non  è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 non  è  diverso da GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave3 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 } Verifica che   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo, Almeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 } Verifica che   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12 o  se l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV2 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (12)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave8 non  è  diverso da GialloVerde /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 non  è  diverso da GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T9 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 } Verifica che   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T9 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T9 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P6 è  uguale a c270""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423""", [
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V9 è  uguale a  /*53,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co8 è  minore di  /*55,*/ 11423""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V4 non è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v4)  è minore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2 /*36,*/ e  se il timer MainClass_C1_timer_T10 non è attivo""", [
                            DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V4 è  minore di  /*55,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 121""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  minore di  /*55,*/ 2""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V2 sia  uguale a  /*53,*/ 5""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (115)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave3 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 150""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T4 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave3 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave3 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V2 sia  maggiore di  /*54,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da  /*56,*/ 6
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T10 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,52,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da  /*56,*/ 6
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,52,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,51,52,*/  /*,*/  il timer MainClass_C1_timer_T10 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 115""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (115)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer MainClass_C1_timer_T10 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer MainClass_C1_timer_T10 sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T10 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave4)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_mainclass_c1_restoreti_ti2_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() == 14150, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.c270x,GlobalEnumeration.c270x,GlobalEnumeration.c270x,True,GlobalEnumeration.rossogiallo,GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(not db(argomento_ave8 == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave3 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() < 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(argomento_ave8 == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t9().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(self.get_mainclass_c1_variabile_v9() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() < 11423, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() < 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_variabile_v4() < 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t10().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_variabile_v2() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_contatore_co8().get_valore() > 121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v2() < 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v2() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 115, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(argomento_ave3 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_contatore_co8().get_valore() == 150, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v2() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(argomento_ave3 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(argomento_ave3 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v2() > 1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(self.get_mainclass_c1_timer_t10().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v9() == 6, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 115, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t10().isScaduto(), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(argomento_ave4 == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m6")
    def macroMainclass_c1_macrove_m6(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave5, argomento_ave6, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 123 o  se l'argomento argomento_ave2 non  è  uguale a c270 commento: {39,}  commento: {37,} o  se la variabile MainClass_C1_variabile_V2 è  minore di  commento: {55,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 non è  diverso da  False , Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 13150
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  commento: {54,} 7
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloGiallo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 123 o  se l'argomento argomento_ave2 non  è  uguale a c270 /*39,*/  /*37,*/ o  se la variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  diverso da  False , Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 13150
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 123 o  se l'argomento argomento_ave2 non  è  uguale a c270 /*39,*/  /*37,*/ o  se la variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  diverso da  False , Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 13150
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 123 o  se l'argomento argomento_ave2 non  è  uguale a c270 /*39,*/  /*37,*/ o  se la variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 123 o  se l'argomento argomento_ave2 non  è  uguale a c270 /*39,*/  /*37,*/ o  se la variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 123 o  se l'argomento argomento_ave2 non  è  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 123""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C3 è  uguale a RossoGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 123""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (123)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V2 è  minore di  /*55,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C1 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 13150
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 13150
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 13150
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 13150
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 13150""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9)  è maggiore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c3() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 123, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave2 == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v2() < 5, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db((db(self.get_mainclass_c1_contatore_co8().get_valore() > 13150, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() > 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m7")
    def macroMainclass_c1_macrove_m7(self, argomento_ave3, argomento_ave5, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,}  se il controllo ConsDef è uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  minore di  commento: {55,} 2 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , Tutte le seguenti { 
          se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  maggiore di  commento: {54,} 4, Verifica che   commento: {50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a  commento: {53,} 4
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  minore di  commento: {55,} 1
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 13
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 151
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  commento: {53,} 104
        
        
         } Verifica che   commento: {49,52,}  commento: {,}  il timer MainClass_C1_timer_T9 non sia scaduto
         commento: {104,} o  che   l'argomento argomento_ave5 sia  uguale a RossoGialloGiallo commento: {,} 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 4, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 151
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 104


 } Verifica che   /*49,52,*/  /*,*/  il timer MainClass_C1_timer_T9 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 4, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 151
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 104


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v9)  è minore di  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 4, Verifica che   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 151
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 104""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M3 ( con argomento_a4   uguale a True ,argomento_a7   uguale a avvio ,argomento_a10   uguale a c270x ,argomento_a2   uguale a RossoGialloGiallo ,argomento_a6   uguale a RossoGiallo  e argomento_a1   uguale a c270x )   è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (rossogiallogiallo)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile MainClass_C1_variabile_V9 è  maggiore di  /*54,*/ 4""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 151
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 104""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 151""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 104""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (104)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,52,*/  /*,*/  il timer MainClass_C1_timer_T9 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,52,*/  /*,*/  il timer MainClass_C1_timer_T9 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave5 sia  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v9() < 2, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.c270x,GlobalEnumeration.c270x,GlobalEnumeration.rossogiallogiallo,True,GlobalEnumeration.rossogiallo,GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v9() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v9() == 4, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_contatore_co8().get_valore() < 1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() > 151, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 104, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db(argomento_ave5 == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a1, argomento_a10, argomento_a2, argomento_a4, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGialloGiallo
        return GlobalEnumeration.rossogiallogiallo
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm2DaSenderb6f8ffb3(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm2DaSenderb6f8ffb3')
    
    def eventMainclass_c1_command_comm3(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm3')
    
    def eventMainclass_c1_command_comm6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm6')
    
    def eventMainclass_c1_command_comm8DaSender1a75134(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm8DaSender1a75134')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm1(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm1')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c10_prev(self.get_mainclass_c1_previousco_c10())
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c6_prev(self.get_mainclass_c1_previousco_c6())
        self.set_mainclass_c1_previousco_c9_prev(self.get_mainclass_c1_previousco_c9())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())
        self.set_mainclass_c1_previousva_pv5_prev(self.get_mainclass_c1_previousva_pv5())

