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

class SubClass_C2(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C2, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c2_previousva_pv1(False)
        self.set_subclass_c2_previousva_pv2(0)
        self.set_subclass_c2_previousva_pv3(0)
        self.set_subclass_c2_previousva_pv4(False)
        self.set_subclass_c2_restoreva_rv1(False)
        self.set_subclass_c2_restoreva_rv2(False)
        self.set_subclass_c2_variabile_v4(0)

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

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c2_lista_l3, subclass_c2_parametro_p1, subclass_c2_parametro_p5, subclass_c2_parametro_p7):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l3(subclass_c2_lista_l3)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p1(subclass_c2_parametro_p1)
        self.set_subclass_c2_parametro_p5(subclass_c2_parametro_p5)
        self.set_subclass_c2_parametro_p7(subclass_c2_parametro_p7)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(321000)
        self.set_subclass_c2_restoreti_ti1_restore(321000)
        self.set_subclass_c2_restoreti_ti2(5450000)
        self.set_subclass_c2_restoreti_ti2_restore(5450000)
        self.set_subclass_c2_timer_t1(103000)
        self.set_subclass_c2_timer_t10(332000)
        self.set_subclass_c2_timer_t3(314000)
        self.set_subclass_c2_timer_t7(45000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_timer_t1,self.subclass_c2_timer_t10,self.subclass_c2_timer_t3,self.subclass_c2_timer_t7,]

        # initialize the counters
        self.set_subclass_c2_contatore_co6(0)
        self.set_subclass_c2_contatore_co7(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l3(self, subclass_c2_lista_l3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3",subclass_c2_lista_l3)


    # getters for record type parameters
    def get_subclass_c2_lista_l3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p1(self, subclass_c2_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1",subclass_c2_parametro_p1)

    def set_subclass_c2_parametro_p5(self, subclass_c2_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5",subclass_c2_parametro_p5)

    def set_subclass_c2_parametro_p7(self, subclass_c2_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7",subclass_c2_parametro_p7)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p1")

    def get_subclass_c2_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5")

    def get_subclass_c2_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c3(self, subclass_c2_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c3",subclass_c2_comando_c3)

    def set_subclass_c2_comando_c6(self, subclass_c2_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c6",subclass_c2_comando_c6)

    def set_subclass_c2_comando_c7(self, subclass_c2_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c7",subclass_c2_comando_c7)

    def set_subclass_c2_comando_c8(self, subclass_c2_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c8",subclass_c2_comando_c8)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c2")

    def get_subclass_c2_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c3")

    def get_subclass_c2_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c4")

    def get_subclass_c2_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c6")

    def get_subclass_c2_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c7")

    def get_subclass_c2_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1")

    def get_subclass_c2_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10")

    def get_subclass_c2_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5")

    def get_subclass_c2_previousco_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c9")


    # setters for state variables
    def set_subclass_c2_previousco_c1_prev(self, subclass_c2_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1_prev",subclass_c2_previousco_c1_prev)
    def set_subclass_c2_previousco_c10_prev(self, subclass_c2_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev",subclass_c2_previousco_c10_prev)
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
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_variabile_v4(self, subclass_c2_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v4",subclass_c2_variabile_v4)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c1_prev")

    def get_subclass_c2_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev")

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

    def get_subclass_c2_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1")

    def get_subclass_c2_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1_restore")

    def get_subclass_c2_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2")

    def get_subclass_c2_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2_restore")

    def get_subclass_c2_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v4")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_restoreti_ti2(self, timerDuration):
        self.subclass_c2_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2", self.memory)

    def set_subclass_c2_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2_restore", self.memory)

    def set_subclass_c2_timer_t1(self, timerDuration):
        self.subclass_c2_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t1", self.memory)

    def set_subclass_c2_timer_t10(self, timerDuration):
        self.subclass_c2_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t10", self.memory)

    def set_subclass_c2_timer_t3(self, timerDuration):
        self.subclass_c2_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t3", self.memory)

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

    def get_subclass_c2_timer_t1(self):
        return self.subclass_c2_timer_t1

    def get_subclass_c2_timer_t10(self):
        return self.subclass_c2_timer_t10

    def get_subclass_c2_timer_t3(self):
        return self.subclass_c2_timer_t3

    def get_subclass_c2_timer_t7(self):
        return self.subclass_c2_timer_t7


    # setters for counters
    def set_subclass_c2_contatore_co6(self, counterInitValue):
        self.subclass_c2_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co6", self.memory)

    def set_subclass_c2_contatore_co7(self, counterInitValue):
        self.subclass_c2_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co7", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co6(self):
        return self.subclass_c2_contatore_co6

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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_subclass_c2_previousco_c1_prev(True)
        self.set_subclass_c2_previousco_c10_prev(False)
        self.set_subclass_c2_previousco_c5_prev(GlobalEnumeration.rossoverde)
        self.set_subclass_c2_previousco_c9_prev(GlobalEnumeration.rossogiallo)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())

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
        Nessuna
        }
        """
        pass
    
    # effect macros
    def macroSubclass_c2_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  uguale a  False , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  uguale a  False , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 5""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C2_restoreva_RV2 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv2_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 non è  uguale a  False , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
        if db(not db(self.get_subclass_c2_restoreva_rv2_restore() == False, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v4(5)
    
    def macroSubclass_c2_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {35,}  se il controllo SubClass_C2_controllo_C7 è  diverso da  False , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 9
        
           
          se il controllo ConsDef  è  uguale a FALSE ,  commento: {45,}  se  MainClass_C1_contatore_Co4 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  commento: {54,} 14, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V8 del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,} 7 commento: {38,} e  se il contatore SubClass_C2_contatore_Co6 è  minore di  commento: {55,} 1414 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
        
        
         commento: {37,}  se la variabile SubClass_C2_variabile_V4 non è  minore di  commento: {55,} 9 commento: {37,} e  se la variabile SubClass_C2_variabile_V4 non è  diverso da  commento: {56,} 10, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
        
           
          se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  commento: {55,} 1450 commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  diverso da RossoVerde, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C2_controllo_C7 è  diverso da  False , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 9""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE ,  /*45,*/  se  MainClass_C1_contatore_Co4 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  /*54,*/ 14, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/ 7 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  minore di  /*55,*/ 1414 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co6

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE ,  /*45,*/  se  MainClass_C1_contatore_Co4 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  /*54,*/ 14, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/ 7 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  minore di  /*55,*/ 1414 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (7)) allora ((mainclass_c1_contatore_co4 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (14))} ) )  e  ( (subclass_c2_contatore_co6)  è minore di  (1414) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (7)) allora ((mainclass_c1_contatore_co4 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (14))} )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (7)) allora ((mainclass_c1_contatore_co4 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (14))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (7)) allora ((mainclass_c1_contatore_co4 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (14))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (7)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (14)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co6)  è minore di  (1414)""", [
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
                            DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V4 non è  minore di  /*55,*/ 9 /*37,*/ e  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 10, /*72,*/Azzera il contatore SubClass_C2_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C2_variabile_V4 non è  minore di  /*55,*/ 9 /*37,*/ e  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è minore di  (9))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v4)  è minore di  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v4)  è uguale a  (10)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 1450 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  diverso da RossoVerde, /*72,*/Azzera il contatore SubClass_C2_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 1450 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (negazione di ((stato_restore)  è uguale a  (state1))) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t1' è scaduto) ) )  o  
( negazione di ((subclass_c2_contatore_co6)  è minore di  (1450)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((stato_restore)  è uguale a  (state1))) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t1' è scaduto) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((stato_restore)  è uguale a  (state1))) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((stato_restore)  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co6)  è minore di  (1450))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co6)  è minore di  (1450)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*35,*/  se il controllo SubClass_C2_controllo_C7 è  diverso da  False , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 9
        if db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v4(9)
        #  se il controllo ConsDef  è  uguale a FALSE ,  /*45,*/  se  MainClass_C1_contatore_Co4 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  /*54,*/ 14, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/ 7 /*38,*/ e  se il contatore SubClass_C2_contatore_Co6 è  minore di  /*55,*/ 1414 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co6
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 7
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co4().get_valore() > 14, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == 7, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co6().get_valore() < 1414, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co6().resetta()
        else:
            self.set_subclass_c2_variabile_v4(7)
        #  /*37,*/  se la variabile SubClass_C2_variabile_V4 non è  minore di  /*55,*/ 9 /*37,*/ e  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 10, /*72,*/Azzera il contatore SubClass_C2_contatore_Co6
        if db((db(not db(self.get_subclass_c2_variabile_v4() < 9, di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v4() == 10, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_contatore_co6().resetta()
        #  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  minore di  /*55,*/ 1450 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  diverso da RossoVerde, /*72,*/Azzera il contatore SubClass_C2_contatore_Co6
        if db((db((db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co6().get_valore() < 1450, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c2_contatore_co6().resetta()
    
    def macroSubclass_c2_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {43,}  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True , commento: {69,}Disattiva il timer SubClass_C2_timer_T7
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 4
        
        
         commento: {36,}  se il timer SubClass_C2_timer_T10 non è attivo,  commento: {43,}  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T8 del campo  MainClass_C1     commento: {105,} è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V4 non è  maggiore di  commento: {54,} 3, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co7
        
         ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co6
        
        
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 1345 commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 1303 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo,  Applica gli effetti
               della macro SubClass_C2_macroef_M10  commento: {73,}
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
        
         commento: {44,}  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a c270x commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  commento: {56,} 12450 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 14 commento: {34,} o  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  commento: {56,} 9 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T10
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 1332 commento: {34,} o  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde commento: {37,} o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  commento: {56,} 10 commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo commento: {36,} e  se il timer SubClass_C2_timer_T10 non è scaduto, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True , /*69,*/Disattiva il timer SubClass_C2_timer_T7

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è attivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer SubClass_C2_timer_T10 non è attivo,  /*43,*/  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T8 del campo  MainClass_C1     /*105,*/ è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  maggiore di  /*54,*/ 3, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co7

 ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T10 non è attivo,  /*43,*/  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T8 del campo  MainClass_C1     /*105,*/ è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( negazione di (il timer 'subclass_c2_timer_t10' è attivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo) allora (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)} ) )  e  
( negazione di ((subclass_c2_controllo_c6)  è uguale a  (rossogiallo)) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (il timer 'subclass_c2_timer_t10' è attivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo) allora (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)} ) )  e  
( negazione di ((subclass_c2_controllo_c6)  è uguale a  (rossogiallo)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c2_timer_t10' è attivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo) allora (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)} ) )  e  
( negazione di ((subclass_c2_controllo_c6)  è uguale a  (rossogiallo)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t10' è attivo) )  e  ( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo) allora (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t10' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo) allora (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo) allora (il timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è maggiore di  (3))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v4)  è maggiore di  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1345 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1303 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo,  Applica gli effetti
       della macro SubClass_C2_macroef_M10  /*73,*/

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1345 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1303 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( il timer 'subclass_c2_restoreti_ti2_restore' è inattivo )  o  
( ( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (1345)) )  e  
( negazione di ((subclass_c2_parametro_p1)  è uguale a  (rossoverde)) ) ) )  o  
( (subclass_c2_contatore_co7)  è minore di  (1303) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'subclass_c2_restoreti_ti2_restore' è inattivo )  o  
( ( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (1345)) )  e  
( negazione di ((subclass_c2_parametro_p1)  è uguale a  (rossoverde)) ) ) )  o  
( (subclass_c2_contatore_co7)  è minore di  (1303) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'subclass_c2_restoreti_ti2_restore' è inattivo )  o  
( ( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (1345)) )  e  
( negazione di ((subclass_c2_parametro_p1)  è uguale a  (rossoverde)) ) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti2_restore' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (1345)) )  e  
( negazione di ((subclass_c2_parametro_p1)  è uguale a  (rossoverde)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è maggiore di  (1345))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co7)  è maggiore di  (1345)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (1303)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (rossogiallo)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M10"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*44,*/  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a c270x /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  /*56,*/ 12450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 9 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 5

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a c270x /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  /*56,*/ 12450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 9 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270x))} )  o  
( ( negazione di (negazione di ((subclass_c2_contatore_co6)  è uguale a  (12450))) )  e  
( (subclass_c2_contatore_co7)  è minore di  (14) ) ) )  o  
( negazione di ((subclass_c2_parametro_p7)  è uguale a  (False)) ) )  o  
( negazione di (negazione di ((subclass_c2_variabile_v4)  è uguale a  (9))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270x))} )  o  
( ( negazione di (negazione di ((subclass_c2_contatore_co6)  è uguale a  (12450))) )  e  
( (subclass_c2_contatore_co7)  è minore di  (14) ) ) )  o  
( negazione di ((subclass_c2_parametro_p7)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270x))} )  o  
( ( negazione di (negazione di ((subclass_c2_contatore_co6)  è uguale a  (12450))) )  e  
( (subclass_c2_contatore_co7)  è minore di  (14) ) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270x))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_contatore_co6)  è uguale a  (12450))) )  e  
( (subclass_c2_contatore_co7)  è minore di  (14) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co6)  è uguale a  (12450)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co6)  è uguale a  (12450))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co6)  è uguale a  (12450)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (14)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v4)  è uguale a  (9)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 1332 /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 10 /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo /*36,*/ e  se il timer SubClass_C2_timer_T10 non è scaduto, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 1332 /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 10 /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo /*36,*/ e  se il timer SubClass_C2_timer_T10 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde)) )  o  
( (subclass_c2_contatore_co6)  è maggiore di  (1332) ) )  o  
( (subclass_c2_parametro_p1)  è uguale a  (rossoverde) ) )  o  
( negazione di (negazione di ((subclass_c2_variabile_v4)  è uguale a  (10))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde)) )  o  
( (subclass_c2_contatore_co6)  è maggiore di  (1332) ) )  o  
( (subclass_c2_parametro_p1)  è uguale a  (rossoverde) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde)) )  o  
( (subclass_c2_contatore_co6)  è maggiore di  (1332) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co6)  è maggiore di  (1332)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (rossoverde)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v4)  è uguale a  (10)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v4)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_controllo_c6)  è uguale a  (rossogiallo) )  e  
( negazione di (il timer 'subclass_c2_timer_t10' è scaduto) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t10' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*43,*/  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True , /*69,*/Disattiva il timer SubClass_C2_timer_T7
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 4
        if db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t7().disattiva()
        else:
            self.set_subclass_c2_variabile_v4(4)
        #  /*36,*/  se il timer SubClass_C2_timer_T10 non è attivo,  /*43,*/  se MainClass_C1_timer_T8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*43,*/   MainClass_C1_timer_T8 del campo  MainClass_C1     /*105,*/ è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da RossoVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  maggiore di  /*54,*/ 3, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co7
        #   ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co6
        if db((db((db((db((db((db(not db(self.get_subclass_c2_timer_t10().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.rossogiallo, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v4() > 3, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co7().decrementa()
        else:
            self.get_subclass_c2_contatore_co6().resetta()
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1345 /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1303 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M10  /*73,*/
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10
        if db((db((db((db((db(self.get_subclass_c2_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() > 1345, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co7().get_valore() < 1303, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.rossogiallo, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.macroSubclass_c2_macroef_m10(di_ctx.subs[2].subs[1])
        else:
            self.get_subclass_c2_timer_t10().disattiva()
        #  /*44,*/  se  MainClass_C1_variabile_V5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a c270x /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 non è  diverso da  /*56,*/ 12450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P7 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 9 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 5
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T10
        if db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v5() == GlobalEnumeration.c270x, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_contatore_co6().get_valore() == 12450, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co7().get_valore() < 14, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p7() == False, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v4() == 9, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_variabile_v4(5)
        else:
            self.get_subclass_c2_timer_t10().disattiva()
        #  /*34,*/  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 1332 /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde /*37,*/ o  se la variabile SubClass_C2_variabile_V4 non è  diverso da  /*56,*/ 10 /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a RossoGiallo /*36,*/ e  se il timer SubClass_C2_timer_T10 non è scaduto, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V4 il valore 1
        if db((db((db((db((db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co6().get_valore() > 1332, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v4() == 10, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db((db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.rossogiallo, di_ctx.subs[4].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t10().isScaduto(), di_ctx.subs[4].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_subclass_c2_variabile_v4(1)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m3")
    def macroSubclass_c2_macrove_m3(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde commento: {34,} e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T3 non è attivo, Solo una delle seguenti { 
         commento: {62,} commento: {38,}  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 15321 commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 15450 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 13, Almeno una delle seguenti { 
         commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  diverso da  commento: {56,} 7 commento: {37,} o  se la variabile SubClass_C2_variabile_V4 è  minore di  commento: {55,} 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  commento: {54,} 14321 commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
        
        
         } Verifica che   commento: {47,48,49,}  commento: {,}  il timer SubClass_C2_timer_T1 non sia attivo
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
        
        
         } Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T1 sia disattivo
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 sia  diverso da RossoGiallo
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è attivo, Solo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 13, Almeno una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 } Verifica che   /*47,48,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è attivo, Solo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 13, Almeno una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T3 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P1 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P5 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 13, Almeno una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 13, Almeno una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 15321""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 non è  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P1 è  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15450 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 15450""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (15450)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7 /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C2_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V4 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v4)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V4 è  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T10 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co6 è  maggiore di  /*54,*/ 14321""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T10 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p1)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia disattivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P1 sia  uguale a RossoVerde""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T1 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_subclass_c2_contatore_co6().get_valore() > 15321, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 15450, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_subclass_c2_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v4() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v4() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co6().get_valore() > 14321, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db(not db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t1().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m2")
    def macroSubclass_c2_macrova_m2(self, argomento_a10, argomento_a2, argomento_a3, argomento_a4, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {41,}  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da RossoGialloVerde commento: {34,} e  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {109,} o  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False ,  commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,} 4, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C1 del campo  MainClass_C1     è  diverso da RossoGialloxVerdex commento: {34,} e  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde commento: {42,} e  se  MainClass_C1_controllo_C10 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da RossoGialloxVerdex , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m2_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*41,*/  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da RossoGialloVerde /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*109,*/ o  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False ,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 4, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C1 del campo  MainClass_C1     è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde /*42,*/ e  se  MainClass_C1_controllo_C10 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da RossoGialloxVerdex , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*41,*/  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da RossoGialloVerde /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*109,*/ o  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False ,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 4, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C1 del campo  MainClass_C1     è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde /*42,*/ e  se  MainClass_C1_controllo_C10 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloverde)))} )  e  
( negazione di ((lo stato di 'self')  è uguale a  (state1)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloverde)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)) )  e  ( ( negazione di (negazione di ((subclass_c2_controllo_c7)  è uguale a  (False))) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))) allora ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4))} ) ) )  e  ( (subclass_c2_parametro_p1)  è uguale a  (rossoverde) ) )  e  
( per ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex)))} )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)) )  e  ( ( negazione di (negazione di ((subclass_c2_controllo_c7)  è uguale a  (False))) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))) allora ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4))} ) ) )  e  ( (subclass_c2_parametro_p1)  è uguale a  (rossoverde) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)) )  e  ( ( negazione di (negazione di ((subclass_c2_controllo_c7)  è uguale a  (False))) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))) allora ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4))} ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_controllo_c7)  è uguale a  (False))) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))) allora ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c7)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))) allora ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))) allora ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p1)  è uguale a  (rossoverde)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m2_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*41,*/  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da RossoGialloVerde /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*109,*/ o  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C7 non è  diverso da  False ,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 4, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C1 del campo  MainClass_C1     è  diverso da RossoGialloxVerdex /*34,*/ e  se il parametro SubClass_C2_parametro_P1 è  uguale a RossoVerde /*42,*/ e  se  MainClass_C1_controllo_C10 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da RossoGialloxVerdex , assegna alla macro il valore  False
        if db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_subclass_c2_restoreva_rv1_restore() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db((db(not db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c1() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p1() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c10() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m9")
    def macroSubclass_c2_macrova_m9(self, argomento_a1, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  commento: {53,}  state1  , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/  state1  , assegna alla macro il valore  True""", [
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/  state1  , assegna alla macro il valore  True
        if db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c1_prev(self.get_subclass_c2_previousco_c1())
        self.set_subclass_c2_previousco_c10_prev(self.get_subclass_c2_previousco_c10())
        self.set_subclass_c2_previousco_c5_prev(self.get_subclass_c2_previousco_c5())
        self.set_subclass_c2_previousco_c9_prev(self.get_subclass_c2_previousco_c9())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())

class SubClass_C2_RecordHeaderR6(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled6, recordfiled4, recordfiled7, recordfiled19):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled6(recordfiled6)
        self.set_recordfiled4(recordfiled4)
        self.set_recordfiled7(recordfiled7)
        self.set_recordfiled19(recordfiled19)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled6(self, recordfiled6):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"), recordfiled6)

    def set_recordfiled4(self, recordfiled4):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"), recordfiled4)

    def set_recordfiled7(self, recordfiled7):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"), recordfiled7)

    def set_recordfiled19(self, recordfiled19):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"), recordfiled19)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled6(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"))

    def get_recordfiled4(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"))

    def get_recordfiled7(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"))

    def get_recordfiled19(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"))



