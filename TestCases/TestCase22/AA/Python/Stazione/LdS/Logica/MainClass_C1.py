# Codice del modello 'TestCase22', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(0)
        self.set_mainclass_c1_restoreva_rv3(False)
        self.set_mainclass_c1_restoreva_rv4(0)
        self.set_mainclass_c1_variabile_v1(False)
        self.set_mainclass_c1_variabile_v4(False)
        self.set_mainclass_c1_variabile_v5(GlobalEnumeration.rossogialloverde)
        self.set_mainclass_c1_variabile_v7(0)
        self.set_mainclass_c1_variabile_v8(GlobalEnumeration.avviox)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
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

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p3, mainclass_c1_parametro_p5, mainclass_c1_parametro_p8, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p5(mainclass_c1_parametro_p5)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(30000)
        self.set_mainclass_c1_restoreti_ti1_restore(30000)
        self.set_mainclass_c1_restoreti_ti2(23000)
        self.set_mainclass_c1_restoreti_ti2_restore(23000)
        self.set_mainclass_c1_timer_t10(2000)
        self.set_mainclass_c1_timer_t2(41000)
        self.set_mainclass_c1_timer_t4(2000)
        self.set_mainclass_c1_timer_t5(1000)
        self.set_mainclass_c1_timer_t9(3452000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_timer_t10,self.mainclass_c1_timer_t2,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t5,self.mainclass_c1_timer_t9,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co5(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p5(self, mainclass_c1_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5",mainclass_c1_parametro_p5)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c3")

    def get_mainclass_c1_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c4")

    def get_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c6")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1")

    def get_mainclass_c1_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7")


    # setters for state variables
    def set_mainclass_c1_previousco_c1_prev(self, mainclass_c1_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev",mainclass_c1_previousco_c1_prev)
    def set_mainclass_c1_previousco_c10_prev(self, mainclass_c1_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev",mainclass_c1_previousco_c10_prev)
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c7_prev(self, mainclass_c1_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7_prev",mainclass_c1_previousco_c7_prev)
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
    def set_mainclass_c1_restoreva_rv4(self, mainclass_c1_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4",mainclass_c1_restoreva_rv4)
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v4(self, mainclass_c1_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4",mainclass_c1_variabile_v4)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v7(self, mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7",mainclass_c1_variabile_v7)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

    # getters for state variables
    def get_mainclass_c1_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev")

    def get_mainclass_c1_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev")

    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7_prev")

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

    def get_mainclass_c1_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4")

    def get_mainclass_c1_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4_restore")

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

    def get_mainclass_c1_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

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

    def set_mainclass_c1_timer_t10(self, timerDuration):
        self.mainclass_c1_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t10", self.memory)

    def set_mainclass_c1_timer_t2(self, timerDuration):
        self.mainclass_c1_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t2", self.memory)

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)

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

    def get_mainclass_c1_timer_t10(self):
        return self.mainclass_c1_timer_t10

    def get_mainclass_c1_timer_t2(self):
        return self.mainclass_c1_timer_t2

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5

    def get_mainclass_c1_timer_t9(self):
        return self.mainclass_c1_timer_t9


    # setters for counters
    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5



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

        self.set_mainclass_c1_previousco_c1_prev(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_previousco_c10_prev(False)
        self.set_mainclass_c1_previousco_c2_prev(GlobalEnumeration.spento)
        self.set_mainclass_c1_previousco_c7_prev(GlobalEnumeration.rossoverde)
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
    def macroMainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 15145, commento: {72,}Azzera il contatore MainClass_C1_contatore_Co5
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co5
        
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  minore di  commento: {55,} 6 commento: {36,} o  se il timer MainClass_C1_timer_T5 è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T10
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  commento: {56,} 3 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 15145, /*72,*/Azzera il contatore MainClass_C1_contatore_Co5

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 15145""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (15145)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 6 /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 6 /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è minore di  (6))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p8)  è minore di  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T10

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  /*56,*/ 3 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  /*56,*/ 3 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (3))) )  o  
( negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (3)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 15145, /*72,*/Azzera il contatore MainClass_C1_contatore_Co5
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co5
        if db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 15145, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co5().resetta()
        else:
            self.get_mainclass_c1_contatore_co5().resetta()
        #  /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 6 /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        if db((db(not db(self.get_mainclass_c1_parametro_p8() < 6, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c5(GlobalEnumeration.rossogialloxverdex)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T10
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        if db((db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t10().disattiva()
        else:
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.rossogialloxverdex)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  /*56,*/ 3 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        if db((db((db(not db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == 3, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.rossogialloxverdex)
    
    def macroMainclass_c1_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer MainClass_C1_timer_T9 non è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  commento: {53,} 13, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        
         ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore RossoVerde commento: {67,}
        
        
          se la macro  MainClass_C1_macrova_M3 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a2   uguale a Verde ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a RossoGialloxVerdex )  non  è  diverso da Verde commento: {40,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 1114 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  commento: {55,} 11520, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
        
        
          se il controllo ConsDef è uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  maggiore di  commento: {54,} 4, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T9 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  /*53,*/ 13, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex

 ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T9 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t9' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex)) )  e  
( negazione di ((mainclass_c1_contatore_co5)  è uguale a  (13)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*67,*/


  se la macro  MainClass_C1_macrova_M3 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a2   uguale a Verde ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a RossoGialloxVerdex )  non  è  diverso da Verde /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 1114 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11520, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/


  se la macro  MainClass_C1_macrova_M3 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a2   uguale a Verde ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a RossoGialloxVerdex )  non  è  diverso da Verde /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 1114 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11520""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (verde))) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))) ) )  o  
( (mainclass_c1_contatore_co5)  è uguale a  (1114) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t4' è attivo) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (verde))) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))) ) )  o  
( (mainclass_c1_contatore_co5)  è uguale a  (1114) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (verde))) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (verde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (verde)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (1114)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t4' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è minore di  (11520))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (11520)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  maggiore di  /*54,*/ 4, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p5)  è maggiore di  (4)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer MainClass_C1_timer_T9 non è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  /*53,*/ 13, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        #   ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore RossoVerde
        if db((db(not db(self.get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c5(GlobalEnumeration.rossogialloxverdex)
        else:
            self.set_mainclass_c1_variabile_v8(GlobalEnumeration.rossoverde)
        #  /*67,*/
        #    se la macro  MainClass_C1_macrova_M3 ( con argomento_a7   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a2   uguale a Verde ,argomento_a5   uguale a RossoGialloVerde  e argomento_a6   uguale a RossoGialloxVerdex )  non  è  diverso da Verde /*40,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 1114 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 11520, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5
        if db((db((db((db((db(not db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.verde,GlobalEnumeration.rossogialloverde,GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.rossogialloverde,GlobalEnumeration.avvio, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co5().get_valore() == 1114, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co5().get_valore() < 11520, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.rossogialloxverdex)
        else:
            self.get_mainclass_c1_contatore_co5().decrementa()
        #  se il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  maggiore di  /*54,*/ 4, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore RossoGialloxVerdex
        if db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p5() > 4, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co5().incrementa()
        else:
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.rossogialloxverdex)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m10")
    def macroMainclass_c1_macrove_m10(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a True ,argomento_a2   uguale a spento ,argomento_a5   uguale a spento ,argomento_a6   uguale a RossoGialloxVerdex ,argomento_a3   uguale a avviox ,argomento_a9   uguale a avviox  e argomento_a1   uguale a avvio )   è  uguale a  False  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
         commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
          se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
        
        
         } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 8
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloxVerdex
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C6 sia  uguale a  True 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a True ,argomento_a2   uguale a spento ,argomento_a5   uguale a spento ,argomento_a6   uguale a RossoGialloxVerdex ,argomento_a3   uguale a avviox ,argomento_a9   uguale a avviox  e argomento_a1   uguale a avvio )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a True ,argomento_a2   uguale a spento ,argomento_a5   uguale a spento ,argomento_a6   uguale a RossoGialloxVerdex ,argomento_a3   uguale a avviox ,argomento_a9   uguale a avviox  e argomento_a1   uguale a avvio )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a True ,argomento_a2   uguale a spento ,argomento_a5   uguale a spento ,argomento_a6   uguale a RossoGialloxVerdex ,argomento_a3   uguale a avviox ,argomento_a9   uguale a avviox  e argomento_a1   uguale a avvio )   è  uguale a  False  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nla macro  MainClass_C1_macrova_M6 ( con argomento_a8   uguale a True ,argomento_a2   uguale a spento ,argomento_a5   uguale a spento ,argomento_a6   uguale a RossoGialloxVerdex ,argomento_a3   uguale a avviox ,argomento_a9   uguale a avviox  e argomento_a1   uguale a avvio )   è  uguale a  False""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6'"""),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è scaduto, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloxVerdex
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C6 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(db(self.macroMainclass_c1_macrova_m6(GlobalEnumeration.avvio,GlobalEnumeration.spento,GlobalEnumeration.avviox,GlobalEnumeration.spento,GlobalEnumeration.rossogialloxverdex,True,GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(self.get_mainclass_c1_parametro_p8() == 8, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T5 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T5 è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex commento: {36,} e  se il timer MainClass_C1_timer_T2 è disattivo, Almeno una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  commento: {53,} 152, Verifica che   commento: {47,48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 non sia  uguale a  commento: {53,} 9
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 4
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  uguale a RossoGialloxVerdex
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  minore di  commento: {55,} 11
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex /*36,*/ e  se il timer MainClass_C1_timer_T2 è disattivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  /*53,*/ 152, Verifica che   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  /*53,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex /*36,*/ e  se il timer MainClass_C1_timer_T2 è disattivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  /*53,*/ 152, Verifica che   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  /*53,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex /*36,*/ e  se il timer MainClass_C1_timer_T2 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T5 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T5 è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T5 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T5 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex /*36,*/ e  se il timer MainClass_C1_timer_T2 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V5 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  uguale a  /*53,*/ 152, Verifica che   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  /*53,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  uguale a  /*53,*/ 152""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (152)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  /*53,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a RossoVerde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  uguale a RossoGialloxVerdex
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C3 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 152, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p5() == 9, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(self.get_mainclass_c1_parametro_p8() > 4, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co5().get_valore() < 11, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a2, argomento_a5, argomento_a6, argomento_a7, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  diverso da RossoGialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T10 non è disattivo o  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} e  se l'argomento argomento_a7 è  uguale a RossoGialloxVerdex commento: {39,}  , assegna alla macro il valore Verde
        
         commento: {46,} assegna alla macro il valore Verde commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  diverso da RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo o  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ e  se l'argomento argomento_a7 è  uguale a RossoGialloxVerdex /*39,*/  , assegna alla macro il valore Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  diverso da RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo o  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ e  se l'argomento argomento_a7 è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex)) ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t10' è inattivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t10' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  
( (argomento_a7)  è uguale a  (rossogialloxverdex) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(argomento_a7)  è uguale a  (rossogialloxverdex)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  diverso da RossoGialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T10 non è disattivo o  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ e  se l'argomento argomento_a7 è  uguale a RossoGialloxVerdex /*39,*/  , assegna alla macro il valore Verde
        if db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(argomento_a7 == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.verde
        #  /*46,*/ assegna alla macro il valore Verde
        return GlobalEnumeration.verde
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a1, argomento_a2, argomento_a3, argomento_a5, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T4 non è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 4  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  commento: {54,} 6 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 4  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 6 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 4  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 6 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'mainclass_c1_timer_t4' è scaduto) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (4))) ) )  e  ( negazione di ((mainclass_c1_parametro_p8)  è maggiore di  (6)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t4' è scaduto) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (4))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (4)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è maggiore di  (6))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 4  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  maggiore di  /*54,*/ 6 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex , assegna alla macro il valore  True
        if db((db((db((db(not db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p8() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() > 6, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm3(self, notifying_process, argomento_ave3, argomento_ave9):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm3', argomento_ave3=argomento_ave3, argomento_ave9=argomento_ave9)
    
    def eventMainclass_c1_command_comm6(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm6')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c1_prev(self.get_mainclass_c1_previousco_c1())
        self.set_mainclass_c1_previousco_c10_prev(self.get_mainclass_c1_previousco_c10())
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c7_prev(self.get_mainclass_c1_previousco_c7())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())

