# Codice del modello 'TestCase7', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.gialloxverdex)
        self.set_mainclass_c1_previousva_pv2(False)
        self.set_mainclass_c1_previousva_pv3(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_previousva_pv4(False)
        self.set_mainclass_c1_previousva_pv5(0)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(GlobalEnumeration.spento)
        self.set_mainclass_c1_restoreva_rv4(GlobalEnumeration.gialloxverdex)
        self.set_mainclass_c1_variabile_v1(0)
        self.set_mainclass_c1_variabile_v5(False)
        self.set_mainclass_c1_variabile_v8(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm1DaSenderd480970a'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm1DaSenderd480970a',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm1DaSenderd480970a',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm3DaSender4ae38da5'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm3DaSender4ae38da5',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm3DaSender4ae38da5',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm8DaSender66ff29ab'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm8DaSender66ff29ab',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm8DaSender66ff29ab',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p3, mainclass_c1_parametro_p5, mainclass_c1_parametro_p7, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p5(mainclass_c1_parametro_p5)
        self.set_mainclass_c1_parametro_p7(mainclass_c1_parametro_p7)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(14000)
        self.set_mainclass_c1_restoreti_ti1_restore(14000)
        self.set_mainclass_c1_restoreti_ti2(11000)
        self.set_mainclass_c1_restoreti_ti2_restore(11000)
        self.set_mainclass_c1_timer_t5(3530000)
        self.set_mainclass_c1_timer_t9(5000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_timer_t5,self.mainclass_c1_timer_t9,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)
        self.set_mainclass_c1_contatore_co7(0)
        self.set_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p5(self, mainclass_c1_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5",mainclass_c1_parametro_p5)

    def set_mainclass_c1_parametro_p7(self, mainclass_c1_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7",mainclass_c1_parametro_p7)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5")

    def get_mainclass_c1_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)

    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)

    def set_mainclass_c1_comando_c6(self, mainclass_c1_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c6",mainclass_c1_comando_c6)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3")


    # setters for state variables
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c3_prev(self, mainclass_c1_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev",mainclass_c1_previousco_c3_prev)
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
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_restoreva_rv4(self, mainclass_c1_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4",mainclass_c1_restoreva_rv4)
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

    # getters for state variables
    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev")

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

    def get_mainclass_c1_restoreva_rv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3")

    def get_mainclass_c1_restoreva_rv3_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3_restore")

    def get_mainclass_c1_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4")

    def get_mainclass_c1_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4_restore")

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

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

    def set_mainclass_c1_timer_t5(self, timerDuration):
        self.mainclass_c1_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t5", self.memory)

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

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5

    def get_mainclass_c1_timer_t9(self):
        return self.mainclass_c1_timer_t9


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)

    def set_mainclass_c1_contatore_co9(self, counterInitValue):
        self.mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co9", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1

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

        self.set_mainclass_c1_previousco_c2_prev(GlobalEnumeration.rossogialloaverdea)
        self.set_mainclass_c1_previousco_c3_prev(GlobalEnumeration.c180x)
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
        
        { commento: {36,}  se il timer MainClass_C1_timer_T5 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 1525 commento: {36,} o  se il timer MainClass_C1_timer_T9 è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  minore di  commento: {55,} 2 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  diverso da  True , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*36,*/  se il timer MainClass_C1_timer_T5 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1525 /*36,*/ o  se il timer MainClass_C1_timer_T9 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  diverso da  True , /*72,*/Azzera il contatore MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T5 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1525 /*36,*/ o  se il timer MainClass_C1_timer_T9 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (il timer 'mainclass_c1_timer_t5' è attivo) )  o  
( (mainclass_c1_contatore_co1)  è maggiore di  (1525) ) )  o  
( ( il timer 'mainclass_c1_timer_t9' è scaduto )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))) ) ) )  o  
( (mainclass_c1_variabile_v1)  è minore di  (2) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'mainclass_c1_timer_t5' è attivo) )  o  
( (mainclass_c1_contatore_co1)  è maggiore di  (1525) ) )  o  
( ( il timer 'mainclass_c1_timer_t9' è scaduto )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'mainclass_c1_timer_t5' è attivo) )  o  
( (mainclass_c1_contatore_co1)  è maggiore di  (1525) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t5' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (1525)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t9' è scaduto )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v1)  è minore di  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer MainClass_C1_timer_T5 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1525 /*36,*/ o  se il timer MainClass_C1_timer_T9 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  diverso da  True , /*72,*/Azzera il contatore MainClass_C1_contatore_Co7
        if db((db((db((db((db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co1().get_valore() > 1525, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v1() < 2, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co7().resetta()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave5, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo commento: {36,} e  se il timer MainClass_C1_timer_T5 è attivo, Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloGiallo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 è attivo, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 è attivo, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T5 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da  True""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V5 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m6")
    def macroMainclass_c1_macrove_m6(self, argomento_ave10, argomento_ave2, argomento_ave3, argomento_ave5, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T9 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 14, Almeno una delle seguenti { 
         commento: {36,}  se il timer MainClass_C1_timer_T9 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo commento: {36,} e  se il timer MainClass_C1_timer_T9 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T5 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 11, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia attivo
        
        
         } Verifica che   commento: {50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  commento: {53,} 155304
         commento: {104,} o  che   l'argomento argomento_ave2 sia  diverso da  True  commento: {,} 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T9 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 14, Almeno una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T9 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T9 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo


 } Verifica che   /*50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 155304
 /*104,*/ o  che   l'argomento argomento_ave2 sia  diverso da  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T9 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 14, Almeno una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T9 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T9 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T9 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T9 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 14""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer MainClass_C1_timer_T9 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T9 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T9 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T9 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T9 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T9 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T9 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T9 è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T9 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T9 è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloGiallo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T9 è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 155304
 /*104,*/ o  che   l'argomento argomento_ave2 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 155304""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 155304""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (155304)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave2 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co7().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db((db(not db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(self.get_mainclass_c1_variabile_v5() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 155304, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(argomento_ave2 == True, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m7")
    def macroMainclass_c1_macrove_m7(self, argomento_ave10, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave6, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T9 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T9 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T5 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a  False , Verifica che   commento: {52,}   l'argomento argomento_ave8 sia  diverso da RossoGialloaVerdea commento: {,} 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T9 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  False , Verifica che   /*52,*/   l'argomento argomento_ave8 sia  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T9 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  False , Verifica che   /*52,*/   l'argomento argomento_ave8 sia  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T9 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T9 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T9 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T9 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nla macro  MainClass_C1_macrova_M9 ( con argomento_a10   uguale a avvio ,argomento_a3   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  uguale a  False""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9'"""),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T9 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T9 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T9 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P10 non è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V8 è  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*52,*/   l'argomento argomento_ave8 sia  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(db(self.macroMainclass_c1_macrova_m9(GlobalEnumeration.avvio,GlobalEnumeration.rossogialloaverdea,GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p10() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(argomento_ave8 == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m9")
    def macroMainclass_c1_macrova_m9(self, argomento_a10, argomento_a3, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se il controllo ConsDef è uguale a FALSE   commento: {36,} o  se il timer MainClass_C1_timer_T9 non è disattivo o  se l'argomento argomento_a10 non  è  diverso da avvio commento: {39,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se il controllo ConsDef è uguale a FALSE   /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo o  se l'argomento argomento_a10 non  è  diverso da avvio /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se il controllo ConsDef è uguale a FALSE   /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo o  se l'argomento argomento_a10 non  è  diverso da avvio /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di (il timer 'mainclass_c1_timer_t9' è inattivo) ) )  o  
( negazione di (negazione di ((argomento_a10)  è uguale a  (avvio))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di (il timer 'mainclass_c1_timer_t9' è inattivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t9' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((argomento_a10)  è uguale a  (avvio)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a10)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a10)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se il controllo ConsDef è uguale a FALSE   /*36,*/ o  se il timer MainClass_C1_timer_T9 non è disattivo o  se l'argomento argomento_a10 non  è  diverso da avvio /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloGiallo , assegna alla macro il valore  False
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_a10 == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm1DaSenderd480970a(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm1DaSenderd480970a')
    
    def eventMainclass_c1_command_comm3DaSender4ae38da5(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm3DaSender4ae38da5')
    
    def eventMainclass_c1_command_comm8DaSender66ff29ab(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm8DaSender66ff29ab')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c3_prev(self.get_mainclass_c1_previousco_c3())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())
        self.set_mainclass_c1_previousva_pv5_prev(self.get_mainclass_c1_previousva_pv5())

