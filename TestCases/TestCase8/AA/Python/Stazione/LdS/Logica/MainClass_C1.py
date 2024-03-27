# Codice del modello 'TestCase8', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(False)
        self.set_mainclass_c1_previousva_pv2(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_previousva_pv3(0)
        self.set_mainclass_c1_previousva_pv4(GlobalEnumeration.c120x)
        self.set_mainclass_c1_previousva_pv5(0)
        self.set_mainclass_c1_restoreva_rv1(False)
        self.set_mainclass_c1_restoreva_rv2(0)
        self.set_mainclass_c1_restoreva_rv3(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_variabile_v1(0)
        self.set_mainclass_c1_variabile_v3(False)
        self.set_mainclass_c1_variabile_v4(False)
        self.set_mainclass_c1_variabile_v9(0)

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
    def init_configuration(self, mainclass_c1_parametro_p4, mainclass_c1_parametro_p6, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p4(mainclass_c1_parametro_p4)
        self.set_mainclass_c1_parametro_p6(mainclass_c1_parametro_p6)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(42000)
        self.set_mainclass_c1_restoreti_ti1_restore(42000)
        self.set_mainclass_c1_restoreti_ti2(51000)
        self.set_mainclass_c1_restoreti_ti2_restore(51000)
        self.set_mainclass_c1_restoreti_ti3(3453000)
        self.set_mainclass_c1_restoreti_ti3_restore(3453000)
        self.set_mainclass_c1_timer_t5(230000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_timer_t5,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co5(0)
        self.set_mainclass_c1_contatore_co8(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p4(self, mainclass_c1_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4",mainclass_c1_parametro_p4)

    def set_mainclass_c1_parametro_p6(self, mainclass_c1_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6",mainclass_c1_parametro_p6)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4")

    def get_mainclass_c1_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c8(self, mainclass_c1_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c8",mainclass_c1_comando_c8)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4")


    # setters for state variables
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c4_prev(self, mainclass_c1_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev",mainclass_c1_previousco_c4_prev)
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
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v3(self, mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3",mainclass_c1_variabile_v3)
    def set_mainclass_c1_variabile_v4(self, mainclass_c1_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4",mainclass_c1_variabile_v4)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev")

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

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

    def get_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3")

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

    def set_mainclass_c1_timer_t5(self, timerDuration):
        self.mainclass_c1_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t5", self.memory)


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

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5


    # setters for counters
    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)

    def set_mainclass_c1_contatore_co8(self, counterInitValue):
        self.mainclass_c1_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co8", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5

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

        self.set_mainclass_c1_previousco_c2_prev(False)
        self.set_mainclass_c1_previousco_c4_prev(GlobalEnumeration.ac)
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
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 13 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 13 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore AC
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 2
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} 13214, commento: {68,}Attiva il timer MainClass_C1_timer_T5
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  maggiore di  commento: {54,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  minore di  commento: {55,} 2 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {37,} o  se la variabile MainClass_C1_variabile_V9 non è  uguale a  commento: {53,} 3, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        
           
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore AC
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore 3
        
        
          se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a avanzamento ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )  non  è  diverso da RossoGialloaVerdea commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  maggiore di  commento: {54,} 10 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        
         ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co8
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore AC

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_contatore_co5)  è uguale a  (13) )  o  
( ( ( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (13)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t5' è scaduto) ) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (13)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (13)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t5' è scaduto) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (13)) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t5' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 13214, /*68,*/Attiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 13214""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (13214))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (13214)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V1 è  maggiore di  /*54,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 2 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  uguale a  /*53,*/ 3, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V1 è  maggiore di  /*54,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 2 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (mainclass_c1_variabile_v1)  è maggiore di  (9) )  e  
( (mainclass_c1_parametro_p4)  è minore di  (2) ) )  o  
( il timer 'mainclass_c1_timer_t5' è inattivo ) )  o  
( (mainclass_c1_parametro_p6)  è uguale a  (c270xx) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (mainclass_c1_variabile_v1)  è maggiore di  (9) )  e  
( (mainclass_c1_parametro_p4)  è minore di  (2) ) )  o  
( il timer 'mainclass_c1_timer_t5' è inattivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_variabile_v1)  è maggiore di  (9) )  e  
( (mainclass_c1_parametro_p4)  è minore di  (2) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v1)  è maggiore di  (9)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p4)  è minore di  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270xx)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore AC

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a avanzamento ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )  non  è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 10 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 

 ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a avanzamento ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )  non  è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 10 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogialloaverdea))) )  o  
( ( (mainclass_c1_parametro_p8)  è maggiore di  (10) )  e  
( (consdef)  è uguale a  (False) ) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogialloaverdea))) )  o  
( ( (mainclass_c1_parametro_p8)  è maggiore di  (10) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogialloaverdea)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogialloaverdea)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_parametro_p8)  è maggiore di  (10) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (10)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 13 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 13 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore AC
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 2
        if db((db((db(self.get_mainclass_c1_contatore_co5().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c8(GlobalEnumeration.ac)
        else:
            self.set_mainclass_c1_variabile_v9(2)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ 13214, /*68,*/Attiva il timer MainClass_C1_timer_T5
        if db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 13214, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_timer_t5().attiva()
        #  /*37,*/  se la variabile MainClass_C1_variabile_V1 è  maggiore di  /*54,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 2 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*37,*/ o  se la variabile MainClass_C1_variabile_V9 non è  uguale a  /*53,*/ 3, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True
        if db((db((db((db((db(self.get_mainclass_c1_variabile_v1() > 9, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p4() < 2, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270xx, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v9() == 3, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v4(True)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore AC
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore 3
        if db((db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == False, di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_comando_c8(GlobalEnumeration.ac)
        else:
            self.set_mainclass_c1_variabile_v1(3)
        #  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a avanzamento ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )  non  è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 10 e  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        #   ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co8
        if db((db((db((db(not db(not db(db(self.macroMainclass_c1_macrova_m7(GlobalEnumeration.avanzamento,True,GlobalEnumeration.ac,GlobalEnumeration.c270,GlobalEnumeration.c270, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_parametro_p8() > 10, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v4(True)
        else:
            self.get_mainclass_c1_contatore_co8().incrementa()
    
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da  True , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
        
         ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
        
        
          se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 12 commento: {34,} o  se il parametro MainClass_C1_parametro_P4 è  maggiore di  commento: {54,} 1 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 121453 commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        
        
          se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {36,} o  se il timer MainClass_C1_timer_T5 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 150, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  False 
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da  True , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5

 ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx)) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (10))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (10)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro MainClass_C1_parametro_P4 è  maggiore di  /*54,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 121453 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 10

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro MainClass_C1_parametro_P4 è  maggiore di  /*54,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 121453 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_contatore_co5)  è minore di  (12) ) )  o  
( (mainclass_c1_parametro_p4)  è maggiore di  (1) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_contatore_co5)  è minore di  (12) ) )  o  
( (mainclass_c1_parametro_p4)  è maggiore di  (1) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_contatore_co5)  è minore di  (12) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (12)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p4)  è maggiore di  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (121453)) )  e  
( il timer 'mainclass_c1_timer_t5' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (121453))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (121453)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 150, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 150""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_parametro_p6)  è uguale a  (c270xx) ) ) )  o  
( il timer 'mainclass_c1_timer_t5' è attivo ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_parametro_p6)  è uguale a  (c270xx) ) ) )  o  
( il timer 'mainclass_c1_timer_t5' è attivo )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_parametro_p6)  è uguale a  (c270xx) ) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_parametro_p6)  è uguale a  (c270xx) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270xx)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è maggiore di  (150))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (150)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da  True , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5
        #   ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5
        if db((db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p8() == 10, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co5().incrementa()
        else:
            self.get_mainclass_c1_contatore_co5().incrementa()
        #  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro MainClass_C1_parametro_P4 è  maggiore di  /*54,*/ 1 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 121453 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore 10
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True
        if db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() < 12, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p4() > 1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 121453, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v9(10)
        else:
            self.set_mainclass_c1_variabile_v4(True)
        #  se il controllo ConsDef è uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 150, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  False
        if db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270xx, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 150, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v4(True)
        else:
            self.set_mainclass_c1_variabile_v4(False)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m10")
    def macroMainclass_c1_macrove_m10(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  uguale a  False , Tutte le seguenti { 
         commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  commento: {53,} 1302 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  commento: {54,} 8 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T5 non è disattivo, Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  commento: {54,} 5 commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 131, Solo una delle seguenti { 
         commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 13453, Solo una delle seguenti { 
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, Verifica che   commento: {48,49,50,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T5 sia attivo
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a  commento: {53,} 7
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  minore di  commento: {55,} 2
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  minore di  commento: {55,} 11
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da  commento: {56,} 6
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  False , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131, Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 2
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  False , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131, Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V4 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131, Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131, Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  uguale a  /*53,*/ 1302""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (1302)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro MainClass_C1_parametro_P8 è  maggiore di  /*54,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131, Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131, Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p4)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 131""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453, Solo una delle seguenti { 
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 13453""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è uguale a  (13453))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (13453)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T5 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
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
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 2
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 2
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 2
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 6
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 1302, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() > 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_parametro_p4() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co8().get_valore() == 131, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(not db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 13453, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_parametro_p8() < 2, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() < 11, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == 6, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, argomento_ave10, argomento_ave4, argomento_ave6, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 11 commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 11 e  se l'argomento argomento_ave6 è  uguale a c270xx commento: {39,} , Tutte le seguenti { 
         commento: {61,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto, Tutte le seguenti { 
         commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 è  uguale a  commento: {53,} 1 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 140 e  se l'argomento argomento_ave6 è  diverso da c270xx commento: {39,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
         commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx commento: {39,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
         commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
         commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 152 commento: {36,} o  se il timer MainClass_C1_timer_T5 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
         commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
          se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  diverso da  commento: {56,} 1 o  se l'argomento argomento_ave8 è  uguale a  False  commento: {39,} , Verifica che   commento: {47,48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a  commento: {53,} 5
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  commento: {54,} 15
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a  commento: {53,} 1
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  commento: {54,} 1513
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx
        
        
         } Verifica che   commento: {48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia disattivo
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  uguale a  commento: {53,} 1302
        
        
         } Verifica che   commento: {48,49,52,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
         commento: {104,} o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx commento: {,} 
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
        
        
         } Verifica che   commento: {50,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  commento: {54,} 1314
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a  commento: {53,} 5
         commento: {104,} o  che   l'argomento argomento_ave8 non  sia  diverso da  True  commento: {,} 
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  uguale a  commento: {53,} 13
        
        
         } Verifica che   commento: {48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V9 sia  diverso da  commento: {56,} 8
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 15
        
        
         } Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  diverso da  commento: {56,} 1502
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V1 sia  diverso da  commento: {56,} 7
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  False  commento: {,} 
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
        
        
         } Verifica che   commento: {51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  minore di  commento: {55,} 14
         commento: {104,} e  che   l'argomento argomento_ave6 sia  diverso da c270xx commento: {,} 
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  commento: {54,} 131
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a  commento: {53,} 5
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 è  uguale a c270xx /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx


 } Verifica che   /*51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*,*/ 


 } Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 131
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 è  uguale a c270xx /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx


 } Verifica che   /*51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 è  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T5 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 è  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave6 è  uguale a c270xx""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx


 } Verifica che   /*51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx


 }""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI3 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P4 è  uguale a  /*53,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P6 è  uguale a c270xx""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140 e  se l'argomento argomento_ave6 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 140""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave6 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 } Verifica che   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx, Tutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx o  se l'argomento argomento_ave6 è  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave6 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 } Verifica che   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx, Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152 /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 152""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è uguale a  (152))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (152)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx, Solo una delle seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C7 è  uguale a c270xx""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False  /*39,*/ , Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1 o  se l'argomento argomento_ave8 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 è  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave8 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a  /*53,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 15""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 1513""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (1513)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P6 sia  uguale a c270xx""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 1302""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave6 non  sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  maggiore di  /*54,*/ 1314""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (1314)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave8 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  uguale a  /*53,*/ 13""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (15))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 1502""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (1502)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c270xx""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14
 /*104,*/ e  che   l'argomento argomento_ave6 sia  diverso da c270xx""", [
                            DIBoolExpr("""LessThanImpl\nche   /*51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  minore di  /*55,*/ 14""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave6 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 131
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 131
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 131""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  maggiore di  /*54,*/ 131""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 11, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v3() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 11, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(argomento_ave6 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_restoreti_ti3_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_mainclass_c1_parametro_p4() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(self.get_mainclass_c1_contatore_co8().get_valore() == 140, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave6 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave6 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 152, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p4() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() > 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 1513, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() == 1302, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(argomento_ave6 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 1314, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(argomento_ave8 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co8().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db((db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db(not db(self.get_mainclass_c1_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 1502, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v1() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db(self.get_mainclass_c1_contatore_co8().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(argomento_ave6 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() > 131, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p4() == 5, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m5")
    def macroMainclass_c1_macrove_m5(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave7, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,}  se l'argomento argomento_ave1 è  diverso da  False  commento: {39,}  commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  commento: {56,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  commento: {53,} 6, Almeno una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 non è  diverso da  commento: {56,} 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  minore di  commento: {55,} 7 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 12453 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  minore di  commento: {55,} 7, Almeno una delle seguenti { 
         commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 144 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
          se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  commento: {54,} 5 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 11, Verifica che   commento: {47,49,50,52,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da  commento: {56,} 8
         commento: {104,} o  che   l'argomento argomento_ave3 non  sia  diverso da  True  commento: {,} 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T5 non sia disattivo
        
        
         } Verifica che   commento: {47,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  commento: {54,} 6
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V1 non sia  minore di  commento: {55,} 7
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia attivo
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx
        
        
         } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  commento: {53,} 12
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a  commento: {53,} 7
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da  commento: {56,} 6
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se l'argomento argomento_ave1 è  diverso da  False  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 7, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11, Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo


 } Verifica che   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo


 } Verifica che   /*47,48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se l'argomento argomento_ave1 è  diverso da  False  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 7, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11, Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo


 } Verifica che   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo


 } Verifica che   /*47,48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se l'argomento argomento_ave1 è  diverso da  False  /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T5 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T5 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T5 non è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P6 è  uguale a c270xx""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 7, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11, Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo


 } Verifica che   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo


 } Verifica che   /*47,48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 7, Almeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11, Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo


 } Verifica che   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 5 o  se l'argomento argomento_ave7 è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453""", [
                            DIBoolExpr("""LessThanImpl\nil parametro MainClass_C1_parametro_P8 è  minore di  /*55,*/ 7""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 12453""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (12453)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro MainClass_C1_parametro_P4 è  minore di  /*55,*/ 7""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11, Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo


 } Verifica che   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx, Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11, Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da c270xx /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 144""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11, Verifica che   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M7 ( con argomento_a10   uguale a True ,argomento_a1   uguale a AC ,argomento_a3   uguale a AC ,argomento_a7   uguale a c270  e argomento_a9   uguale a c270 )   è  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (rossogialloaverdea)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p4)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V4 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T5 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 11""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave3 non  sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p4)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v1)  è minore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T5 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  uguale a  /*53,*/ 12""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (12)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(argomento_ave1 == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == 8, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == 6, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(not db(not db(self.get_mainclass_c1_parametro_p4() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave7 == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p8() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 12453, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p4() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co5().get_valore() == 144, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m7(GlobalEnumeration.ac,True,GlobalEnumeration.ac,GlobalEnumeration.c270,GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p4() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co8().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave3 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p4() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v1() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(not db(self.get_mainclass_c1_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 12, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == 7, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == 6, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m6")
    def macroMainclass_c1_macrove_m6(self, argomento_ave1, argomento_ave10, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 5, Tutte le seguenti { 
         commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx commento: {39,} , Almeno una delle seguenti { 
         commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 132 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 12145 commento: {36,} e  se il timer MainClass_C1_timer_T5 è disattivo commento: {37,} o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx commento: {39,} , Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  commento: {54,} 12
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 13
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  minore di  commento: {55,} 2
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  diverso da  commento: {56,} 123
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  maggiore di  commento: {54,} 7
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  maggiore di  commento: {54,} 5
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 12
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co5 sia  diverso da  commento: {56,} 151
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 9
        
        
         } Verifica che   commento: {49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  commento: {56,} 15302
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V9 sia  uguale a  commento: {53,} 8
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  commento: {53,} 151
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 non sia  minore di  commento: {55,} 124
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  commento: {54,} 3
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  commento: {54,} 1153
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 5, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx /*39,*/ , Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 9


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15302
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  /*53,*/ 151
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 124
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1153
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 5, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx /*39,*/ , Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 9


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15302
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 5, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx /*39,*/ , Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 9


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15302
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 5, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx /*39,*/ , Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 9


 }""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 5""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx /*39,*/ , Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7


 } Verifica che   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 9


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx /*39,*/ , Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx o  se l'argomento argomento_ave1 non  è  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V4 è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V4 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 non  è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave1)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 132""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (132)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T5 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False  o  se l'argomento argomento_ave1 non  è  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI3 è attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145 /*36,*/ e  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 12145""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T5 è disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V4 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 non  è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  maggiore di  /*54,*/ 12""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (12)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  minore di  /*55,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (123)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  maggiore di  /*54,*/ 7""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V9 sia  maggiore di  /*54,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 12""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co5 sia  diverso da  /*56,*/ 151""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (151)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15302
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15302
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15302""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V4 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co8 non sia  diverso da  /*56,*/ 15302""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (15302))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (15302)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  uguale a  /*53,*/ 8""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  /*53,*/ 151
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 124
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1153
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  /*53,*/ 151
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 124
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1153""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  /*53,*/ 151""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co5 non sia  uguale a  /*53,*/ 151""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (151)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 124
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1153""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 124
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ 124""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (124)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p8)  è maggiore di  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co8 sia  maggiore di  /*54,*/ 1153""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p8() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_mainclass_c1_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave1 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 132, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(self.get_mainclass_c1_restoreti_ti3_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co8().get_valore() == 12145, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v4() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(argomento_ave1 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_mainclass_c1_parametro_p4() < 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 123, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_parametro_p4() > 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v9() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co8().get_valore() > 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 151, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() > 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 15302, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v9() == 8, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(not db(self.get_mainclass_c1_variabile_v3() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 151, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() < 124, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() > 3, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() > 1153, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a1, argomento_a10, argomento_a3, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGialloaVerdea commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGialloaVerdea
        return GlobalEnumeration.rossogialloaverdea
    
    @srf_value_macro("macroMainclass_c1_macrova_m8")
    def macroMainclass_c1_macrova_m8(self, argomento_a10, argomento_a2, argomento_a4, argomento_a5, argomento_a6, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c4_prev(self.get_mainclass_c1_previousco_c4())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())
        self.set_mainclass_c1_previousva_pv5_prev(self.get_mainclass_c1_previousva_pv5())

