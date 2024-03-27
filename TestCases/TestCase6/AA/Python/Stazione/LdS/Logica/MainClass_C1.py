# Codice del modello 'TestCase6', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_previousva_pv2(0)
        self.set_mainclass_c1_restoreva_rv1(GlobalEnumeration.rosso)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.c75giallo)
        self.set_mainclass_c1_restoreva_rv3(0)
        self.set_mainclass_c1_variabile_v1(GlobalEnumeration.verde)
        self.set_mainclass_c1_variabile_v10(False)
        self.set_mainclass_c1_variabile_v2(False)
        self.set_mainclass_c1_variabile_v7(GlobalEnumeration.rossogialloverde)
        self.set_mainclass_c1_variabile_v8(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm8'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm8',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm8',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p2, mainclass_c1_parametro_p7, mainclass_c1_parametro_p8, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p2(mainclass_c1_parametro_p2)
        self.set_mainclass_c1_parametro_p7(mainclass_c1_parametro_p7)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(4000)
        self.set_mainclass_c1_restoreti_ti1_restore(4000)
        self.set_mainclass_c1_restoreti_ti2(4302000)
        self.set_mainclass_c1_restoreti_ti2_restore(4302000)
        self.set_mainclass_c1_timer_t1(151000)
        self.set_mainclass_c1_timer_t2(4000)
        self.set_mainclass_c1_timer_t5(3024000)
        self.set_mainclass_c1_timer_t9(113000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_timer_t1,self.mainclass_c1_timer_t2,self.mainclass_c1_timer_t5,self.mainclass_c1_timer_t9,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co7(0)
        self.set_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p2(self, mainclass_c1_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p2",mainclass_c1_parametro_p2)

    def set_mainclass_c1_parametro_p7(self, mainclass_c1_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7",mainclass_c1_parametro_p7)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p2")

    def get_mainclass_c1_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)

    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c6(self, mainclass_c1_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c6",mainclass_c1_comando_c6)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c2")

    def get_mainclass_c1_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c4")

    def get_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c6")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3")

    def get_mainclass_c1_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5")

    def get_mainclass_c1_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8")


    # setters for state variables
    def set_mainclass_c1_previousco_c3_prev(self, mainclass_c1_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev",mainclass_c1_previousco_c3_prev)
    def set_mainclass_c1_previousco_c5_prev(self, mainclass_c1_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev",mainclass_c1_previousco_c5_prev)
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
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v7(self, mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7",mainclass_c1_variabile_v7)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

    # getters for state variables
    def get_mainclass_c1_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev")

    def get_mainclass_c1_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev")

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

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7")

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

    def set_mainclass_c1_timer_t1(self, timerDuration):
        self.mainclass_c1_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t1", self.memory)

    def set_mainclass_c1_timer_t2(self, timerDuration):
        self.mainclass_c1_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t2", self.memory)

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

    def get_mainclass_c1_timer_t1(self):
        return self.mainclass_c1_timer_t1

    def get_mainclass_c1_timer_t2(self):
        return self.mainclass_c1_timer_t2

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5

    def get_mainclass_c1_timer_t9(self):
        return self.mainclass_c1_timer_t9


    # setters for counters
    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)

    def set_mainclass_c1_contatore_co9(self, counterInitValue):
        self.mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co9", self.memory)


    # getters for counters
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

        self.set_mainclass_c1_previousco_c3_prev(True)
        self.set_mainclass_c1_previousco_c5_prev(True)
        self.set_mainclass_c1_previousco_c8_prev(GlobalEnumeration.c270)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())

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
         
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  commento: {56,} 125 o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T9
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  False 
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a GialloGiallo commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T2 non è attivo o  se il controllo ConsDef  è  uguale a FALSE ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  FALSE commento: {67,}
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamento commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T9 non è scaduto,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore  True  commento: {67,}
        
           
          se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C4 è  diverso da c270 commento: {36,} o  se il timer MainClass_C1_timer_T5 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 11130, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore c270
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 125 o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T9

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 125 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co7)  è uguale a  (125)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (125))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (125)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a GialloGiallo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo o  se il controllo ConsDef  è  uguale a FALSE ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a GialloGiallo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_restoreva_rv1_restore)  è uguale a  (giallogiallo) )  o  
( ( (mainclass_c1_controllo_c6)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t2' è attivo) ) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c6)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t2' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t2' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*67,*/

   
 /*35,*/  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamento /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/

   
 /*35,*/  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamento /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamento)) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (True) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamento)) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (True) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t9' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*67,*/

   
  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C4 è  diverso da c270 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 11130, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore c270

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/

   
  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C4 è  diverso da c270 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 11130""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((stato_restore)  è uguale a  (state1))) )  o  
( negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((stato_restore)  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (il timer 'mainclass_c1_timer_t5' è attivo) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( (mainclass_c1_contatore_co9)  è uguale a  (11130) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'mainclass_c1_timer_t5' è attivo) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t5' è attivo) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t5' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (11130)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 125 o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T9
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  False
        if db((db(not db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 125, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t9().disattiva()
        else:
            self.set_mainclass_c1_variabile_v10(False)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a GialloGiallo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T2 non è attivo o  se il controllo ConsDef  è  uguale a FALSE ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  FALSE
        if db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() == GlobalEnumeration.giallogiallo, di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v10(False)
        #  /*67,*/
        #     
        #   /*35,*/  se il controllo MainClass_C1_controllo_C2 è  diverso da avanzamento /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T9 non è scaduto,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore  True
        if db((db((db((db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamento, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v2(True)
        #  /*67,*/
        #     
        #    se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C4 è  diverso da c270 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è attivo e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 11130, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore c270
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co7
        if db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c4() == GlobalEnumeration.c270, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co9().get_valore() == 11130, di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_comando_c4(GlobalEnumeration.c270)
        else:
            self.get_mainclass_c1_contatore_co7().resetta()
    
    def macroMainclass_c1_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  True 
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  uguale a  True , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co7
        
           
          se il controllo ConsDef è uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a  commento: {53,} 6 commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  diverso da c270 commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  uguale a c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamento commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGiallo, commento: {68,}Attiva il timer MainClass_C1_timer_T9
        
           
         commento: {34,}  se il parametro MainClass_C1_parametro_P7 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 132, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore c270
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v10)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  uguale a  True , /*72,*/Azzera il contatore MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_restoreti_ti2_restore' è inattivo )  e  
( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (True)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270)) )  e  
( negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamento /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGiallo, /*68,*/Attiva il timer MainClass_C1_timer_T9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamento /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( (consdef)  è uguale a  (False) )  e  ( (mainclass_c1_variabile_v8)  è uguale a  (6) ) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270))) ) )  e  ( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270)) ) )  e  ( (mainclass_c1_controllo_c2)  è uguale a  (avanzamento) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (consdef)  è uguale a  (False) )  e  ( (mainclass_c1_variabile_v8)  è uguale a  (6) ) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270))) ) )  e  ( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( (mainclass_c1_variabile_v8)  è uguale a  (6) ) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( (mainclass_c1_variabile_v8)  è uguale a  (6) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (6)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (avanzamento)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P7 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 132, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P7 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 132""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (negazione di ((mainclass_c1_parametro_p7)  è uguale a  (False))) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))) ) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((mainclass_c1_parametro_p7)  è uguale a  (False))) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))) ) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_parametro_p7)  è uguale a  (False))) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p7)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c4)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è minore di  (132))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co9)  è minore di  (132)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  True
        if db((db(not db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c4() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c10(True)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C4 non è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  uguale a  True , /*72,*/Azzera il contatore MainClass_C1_contatore_Co7
        if db((db((db(self.get_mainclass_c1_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == True, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c4() == GlobalEnumeration.c270, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co7().resetta()
        #  se il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a  /*53,*/ 6 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a avanzamento /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGiallo, /*68,*/Attiva il timer MainClass_C1_timer_T9
        if db((db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == 6, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.c270, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.c270, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamento, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.rossogiallo, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t9().attiva()
        #  /*34,*/  se il parametro MainClass_C1_parametro_P7 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C4 non è  diverso da c270 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 132, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore c270
        if db((db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p7() == False, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c4() == GlobalEnumeration.c270, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c4() == GlobalEnumeration.c270, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co9().get_valore() < 132, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v1(GlobalEnumeration.c270)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m4")
    def macroMainclass_c1_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 6, Almeno una delle seguenti { 
         commento: {37,}  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  minore di  commento: {55,} 1302, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T9 sia scaduto
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T2 non sia attivo
        
        
         } Verifica che   commento: {48,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  diverso da  commento: {56,} 154
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  diverso da c270
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 1302, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 non sia attivo


 } Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da c270""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 1302, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 non sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 6""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 1302, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 1302""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 1302""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T2 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T9 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T2 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da c270""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 154
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 154""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 154""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (154)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_parametro_p8() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p8() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p9() > 6, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co9().get_valore() < 1302, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 154, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m5")
    def macroMainclass_c1_macrove_m5(self, argomento_ave1, argomento_ave3, argomento_ave5, argomento_ave6, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 commento: {40,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  commento: {54,} 7 e  se l'argomento argomento_ave8 non  è  diverso da RossoGiallo commento: {39,} , Almeno una delle seguenti { 
          se la macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo commento: {40,}  o  se l'argomento argomento_ave1 è  uguale a  True  commento: {39,} , Verifica che   commento: {48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 12
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia scaduto
        
        
         } Verifica che   commento: {48,49,52,}   l'argomento argomento_ave1 sia  uguale a  True  commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T9 sia disattivo
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T9 sia scaduto
         commento: {104,} e  che   l'argomento argomento_ave1 sia  diverso da  False  commento: {39,} 
         commento: {104,} o  che   l'argomento argomento_ave1 non  sia  diverso da  False  commento: {39,} 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamento
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 7 e  se l'argomento argomento_ave8 non  è  diverso da RossoGiallo /*39,*/ , Almeno una delle seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo /*40,*/  o  se l'argomento argomento_ave1 è  uguale a  True  /*39,*/ , Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia scaduto


 } Verifica che   /*48,49,52,*/   l'argomento argomento_ave1 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamento""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 7 e  se l'argomento argomento_ave8 non  è  diverso da RossoGiallo /*39,*/ , Almeno una delle seguenti { 
  se la macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo /*40,*/  o  se l'argomento argomento_ave1 è  uguale a  True  /*39,*/ , Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 7 e  se l'argomento argomento_ave8 non  è  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270 /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M3 ( con argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a Rosso ,argomento_a8   uguale a c75Giallo ,argomento_a6   uguale a c75Giallo  e argomento_a2   uguale a Verde )  non  è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (c270)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C6 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro MainClass_C1_parametro_P9 è  maggiore di  /*54,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 non  è  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo /*40,*/  o  se l'argomento argomento_ave1 è  uguale a  True  /*39,*/ , Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo /*40,*/  o  se l'argomento argomento_ave1 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M6 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a4   uguale a RossoGialloVerde  e argomento_a10   uguale a RossoGiallo )  non  è  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (rossogiallo)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave1 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C4 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 12""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T1 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,52,*/   l'argomento argomento_ave1 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,52,*/   l'argomento argomento_ave1 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,52,*/   l'argomento argomento_ave1 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T9 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,52,*/   l'argomento argomento_ave1 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T9 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T9 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T9 sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T9 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T9 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a avanzamento""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.verde,GlobalEnumeration.c75giallo,GlobalEnumeration.c75giallo,GlobalEnumeration.c75giallo,GlobalEnumeration.rosso, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p9() > 7, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave8 == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db(not db(db(self.macroMainclass_c1_macrova_m6(GlobalEnumeration.rossogiallo,GlobalEnumeration.rossogialloverde,GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(argomento_ave1 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_controllo_c4() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co7().get_valore() > 12, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(argomento_ave1 == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t9().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave1 == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(argomento_ave1 == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a2, argomento_a5, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  commento: {34,} o  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 153  , assegna alla macro il valore c270
        
         commento: {46,} assegna alla macro il valore c270 commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  /*34,*/ o  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 153  , assegna alla macro il valore c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  /*34,*/ o  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 153""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c6)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (False)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  
( negazione di ((mainclass_c1_contatore_co7)  è uguale a  (153)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (153))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (153)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False  /*34,*/ o  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 153  , assegna alla macro il valore c270
        if db((db((db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 153, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c270
        #  /*46,*/ assegna alla macro il valore c270
        return GlobalEnumeration.c270
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a10, argomento_a4, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGiallo
        return GlobalEnumeration.rossogiallo
    
    @srf_value_macro("macroMainclass_c1_macrova_m9")
    def macroMainclass_c1_macrova_m9(self, argomento_a1, argomento_a2, argomento_a3, argomento_a5, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se l'argomento argomento_a1 è  uguale a  False  commento: {39,}  , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se l'argomento argomento_a1 è  uguale a  False  /*39,*/  , assegna alla macro il valore  False""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_a1 è  uguale a  False""", [
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se l'argomento argomento_a1 è  uguale a  False  /*39,*/  , assegna alla macro il valore  False
        if db(argomento_a1 == False, di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm8(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm8')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm6(self, notifying_process, argomento_ave5, argomento_ave8, argomento_ave9):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm6', argomento_ave5=argomento_ave5, argomento_ave8=argomento_ave8, argomento_ave9=argomento_ave9)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c3_prev(self.get_mainclass_c1_previousco_c3())
        self.set_mainclass_c1_previousco_c5_prev(self.get_mainclass_c1_previousco_c5())
        self.set_mainclass_c1_previousco_c8_prev(self.get_mainclass_c1_previousco_c8())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())

