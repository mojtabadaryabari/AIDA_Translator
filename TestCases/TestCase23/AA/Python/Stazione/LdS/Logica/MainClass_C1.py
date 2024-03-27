# Codice del modello 'TestCase23', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_previousva_pv3(0)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_variabile_v7(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm1'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm1',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm1',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm9DaSender1f7f1f8e'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm9DaSender1f7f1f8e',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm9DaSender1f7f1f8e',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p5, mainclass_c1_parametro_p7, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p5(mainclass_c1_parametro_p5)
        self.set_mainclass_c1_parametro_p7(mainclass_c1_parametro_p7)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(130000)
        self.set_mainclass_c1_restoreti_ti1_restore(130000)
        self.set_mainclass_c1_restoreti_ti2(4542000)
        self.set_mainclass_c1_restoreti_ti2_restore(4542000)
        self.set_mainclass_c1_restoreti_ti3(113000)
        self.set_mainclass_c1_restoreti_ti3_restore(113000)
        self.set_mainclass_c1_restoreti_ti4(40542000)
        self.set_mainclass_c1_restoreti_ti4_restore(40542000)
        self.set_mainclass_c1_restoreti_ti5(5000)
        self.set_mainclass_c1_restoreti_ti5_restore(5000)
        self.set_mainclass_c1_timer_t3(1000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_restoreti_ti5,self.mainclass_c1_restoreti_ti5_restore,self.mainclass_c1_timer_t3,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co2(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p5(self, mainclass_c1_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5",mainclass_c1_parametro_p5)

    def set_mainclass_c1_parametro_p7(self, mainclass_c1_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7",mainclass_c1_parametro_p7)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5")

    def get_mainclass_c1_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


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

    def get_mainclass_c1_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c3")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5")

    def get_mainclass_c1_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c7")

    def get_mainclass_c1_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8")


    # setters for state variables
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c5_prev(self, mainclass_c1_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev",mainclass_c1_previousco_c5_prev)
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
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_variabile_v7(self, mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7",mainclass_c1_variabile_v7)

    # getters for state variables
    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev")

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

    def get_mainclass_c1_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1")

    def get_mainclass_c1_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1_restore")

    def get_mainclass_c1_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7")

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

    def set_mainclass_c1_restoreti_ti5(self, timerDuration):
        self.mainclass_c1_restoreti_ti5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti5", self.memory)

    def set_mainclass_c1_restoreti_ti5_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti5_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti5_restore", self.memory)

    def set_mainclass_c1_timer_t3(self, timerDuration):
        self.mainclass_c1_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t3", self.memory)


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

    def get_mainclass_c1_restoreti_ti5(self):
        return self.mainclass_c1_restoreti_ti5

    def get_mainclass_c1_restoreti_ti5_restore(self):
        return self.mainclass_c1_restoreti_ti5_restore

    def get_mainclass_c1_timer_t3(self):
        return self.mainclass_c1_timer_t3


    # setters for counters
    def set_mainclass_c1_contatore_co2(self, counterInitValue):
        self.mainclass_c1_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co2", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co2(self):
        return self.mainclass_c1_contatore_co2



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

        self.set_mainclass_c1_previousco_c2_prev(True)
        self.set_mainclass_c1_previousco_c5_prev(True)
        self.set_mainclass_c1_previousco_c7_prev(GlobalEnumeration.gialloxverdex)
        self.set_mainclass_c1_previousco_c8_prev(False)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())

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
    def macroMainclass_c1_macroef_m10(self, argomento_af6, argomento_af9, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 1442 commento: {34,} e  se il parametro MainClass_C1_parametro_P5 non è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        
           
         commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 13 commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  diverso da  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  diverso da GialloxVerdex, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
        
           
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} e  se l'argomento argomento_af6 è  diverso da GialloVerde commento: {39,}  o  se l'argomento argomento_af6 non  è  uguale a GialloVerde commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T3
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  commento: {54,} 12 commento: {36,} o  se il timer MainClass_C1_timer_T3 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da GialloxVerdex, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 1442 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 1442 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (1442))) )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p5)  è uguale a  (False))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co2)  è uguale a  (1442)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (1442))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (1442)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p5)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 13 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  diverso da GialloxVerdex, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 13 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (13)) ) )  e  
( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (13)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_parametro_p5)  è uguale a  (True))) )  e  
( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p5)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ e  se l'argomento argomento_af6 è  diverso da GialloVerde /*39,*/  o  se l'argomento argomento_af6 non  è  uguale a GialloVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ e  se l'argomento argomento_af6 è  diverso da GialloVerde /*39,*/  o  se l'argomento argomento_af6 non  è  uguale a GialloVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (lo stato di 'self')  è uguale a  (state1) )  e  
( negazione di ((argomento_af6)  è uguale a  (gialloverde)) ) )  o  
( negazione di ((argomento_af6)  è uguale a  (gialloverde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lo stato di 'self')  è uguale a  (state1) )  e  
( negazione di ((argomento_af6)  è uguale a  (gialloverde)) )""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af6)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af6)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af6)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af6)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 12 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da GialloxVerdex, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 12 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (mainclass_c1_contatore_co2)  è maggiore di  (12) )  o  
( negazione di (il timer 'mainclass_c1_timer_t3' è scaduto) ) )  o  
( (mainclass_c1_variabile_v7)  è maggiore di  (5) ) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (mainclass_c1_contatore_co2)  è maggiore di  (12) )  o  
( negazione di (il timer 'mainclass_c1_timer_t3' è scaduto) ) )  o  
( (mainclass_c1_variabile_v7)  è maggiore di  (5) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_contatore_co2)  è maggiore di  (12) )  o  
( negazione di (il timer 'mainclass_c1_timer_t3' è scaduto) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (12)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v7)  è maggiore di  (5)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 1442 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        if db((db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 1442, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c1(GlobalEnumeration.c270xx)
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 13 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  diverso da GialloxVerdex, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
        if db((db((db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 13, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p5() == True, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.gialloxverdex)
        #  /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ e  se l'argomento argomento_af6 è  diverso da GialloVerde /*39,*/  o  se l'argomento argomento_af6 non  è  uguale a GialloVerde /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T3
        if db((db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_af6 == GlobalEnumeration.gialloverde, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(not db(argomento_af6 == GlobalEnumeration.gialloverde, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co2().decrementa()
        else:
            self.get_mainclass_c1_timer_t3().attiva()
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co2 è  maggiore di  /*54,*/ 12 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da GialloxVerdex, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
        if db((db((db((db((db(self.get_mainclass_c1_contatore_co2().get_valore() > 12, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v7() > 5, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.gialloxverdex)
    
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V7 il valore 8
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        
        
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 11, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V7 il valore 3
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M9  commento: {73,}
        
        
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 14 commento: {36,} e  se il timer MainClass_C1_timer_T3 è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 1442, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co2
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M9  commento: {73,}
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V7 il valore 6
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T3
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V7 il valore 8

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 11, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V7 il valore 3

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) ) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è maggiore di  (11))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M9"""),#1
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*73,*/


 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 14 /*36,*/ e  se il timer MainClass_C1_timer_T3 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 1442, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co2

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 14 /*36,*/ e  se il timer MainClass_C1_timer_T3 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 1442""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è maggiore di  (14)) ) )  e  ( il timer 'mainclass_c1_timer_t3' è attivo ) )  e  
( negazione di ((mainclass_c1_contatore_co2)  è maggiore di  (1442)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è maggiore di  (14)) ) )  e  ( il timer 'mainclass_c1_timer_t3' è attivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è maggiore di  (14)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è maggiore di  (14))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è maggiore di  (1442))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (1442)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M9"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*73,*/


 /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V7 il valore 6

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T3""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V7 il valore 8
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        if db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v7(8)
        else:
            self.set_mainclass_c1_comando_c1(GlobalEnumeration.c270xx)
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 11, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V7 il valore 3
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M9
        if db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 11, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v7(3)
        else:
            self.macroMainclass_c1_macroef_m9(di_ctx.subs[1].subs[1])
        #  /*73,*/
        #   /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 14 /*36,*/ e  se il timer MainClass_C1_timer_T3 è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 1442, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co2
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M9
        if db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0]) or db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 14, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 1442, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co2().incrementa()
        else:
            self.macroMainclass_c1_macroef_m9(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #   /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V7 il valore 6
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T3
        if db(not db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v7(6)
        else:
            self.get_mainclass_c1_timer_t3().disattiva()
    
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  diverso da  commento: {56,} 10, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  maggiore di  commento: {54,} 1 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 12305 commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  commento: {56,} 10,  Applica gli effetti
               della macro MainClass_C1_macroef_M10( con argomento_af6   uguale a GialloVerde ,argomento_af9   uguale a avanzamento ) commento: {73,}
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da  /*56,*/ 10, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t3' è inattivo) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t3' è inattivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p5)  è uguale a  (False)) )  e  
( negazione di (negazione di ((mainclass_c1_variabile_v7)  è uguale a  (10))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v7)  è uguale a  (10)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v7)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  maggiore di  /*54,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 12305 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  /*56,*/ 10,  Applica gli effetti
       della macro MainClass_C1_macroef_M10( con argomento_af6   uguale a GialloVerde ,argomento_af9   uguale a avanzamento )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  maggiore di  /*54,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 12305 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( (mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex) )  e  ( negazione di ((mainclass_c1_variabile_v7)  è maggiore di  (1)) ) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è minore di  (12305)) ) )  e  ( negazione di ((mainclass_c1_parametro_p5)  è uguale a  (True)) ) )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p10)  è uguale a  (10))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex) )  e  ( negazione di ((mainclass_c1_variabile_v7)  è maggiore di  (1)) ) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è minore di  (12305)) ) )  e  ( negazione di ((mainclass_c1_parametro_p5)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex) )  e  ( negazione di ((mainclass_c1_variabile_v7)  è maggiore di  (1)) ) )  e  ( negazione di ((mainclass_c1_contatore_co2)  è minore di  (12305)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex) )  e  ( negazione di ((mainclass_c1_variabile_v7)  è maggiore di  (1)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v7)  è maggiore di  (1))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v7)  è maggiore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è minore di  (12305))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co2)  è minore di  (12305)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p10)  è uguale a  (10)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M10( con argomento_af6   uguale a GialloVerde ,argomento_af9   uguale a avanzamento )"""),#1
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da  /*56,*/ 10, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloxVerdex
        if db((db((db(not db(not db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v7() == 10, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.gialloxverdex)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  uguale a  True , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2
        if db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co2().decrementa()
        #  /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  maggiore di  /*54,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 12305 /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  diverso da  /*56,*/ 10,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M10( con argomento_af6   uguale a GialloVerde ,argomento_af9   uguale a avanzamento )
        if db((db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db((db((db((db((db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v7() > 1, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() < 12305, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p5() == True, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p10() == 10, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.macroMainclass_c1_macroef_m10(GlobalEnumeration.gialloverde,GlobalEnumeration.avanzamento, di_ctx.subs[2].subs[1])
    
    def macroMainclass_c1_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 13 commento: {37,} o  se la variabile MainClass_C1_variabile_V7 non è  minore di  commento: {55,} 10 commento: {36,} e  se il timer MainClass_C1_timer_T3 è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, commento: {69,}Disattiva il timer MainClass_C1_timer_T3
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  minore di  /*55,*/ 10 /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, /*69,*/Disattiva il timer MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  minore di  /*55,*/ 10 /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_contatore_co2)  è uguale a  (13)) )  o  
( ( ( negazione di ((mainclass_c1_variabile_v7)  è minore di  (10)) )  e  ( il timer 'mainclass_c1_timer_t3' è inattivo ) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_variabile_v7)  è minore di  (10)) )  e  ( il timer 'mainclass_c1_timer_t3' è inattivo ) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v7)  è minore di  (10)) )  e  ( il timer 'mainclass_c1_timer_t3' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v7)  è minore di  (10))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v7)  è minore di  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c3)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  minore di  /*55,*/ 10 /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C3 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, /*69,*/Disattiva il timer MainClass_C1_timer_T3
        if db((db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v7() < 10, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t3().disattiva()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave4, argomento_ave7, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T3 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True  commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex commento: {36,} o  se il timer MainClass_C1_timer_T3 non è disattivo, Solo una delle seguenti { 
         commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  uguale a  commento: {53,} 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  commento: {39,}  o  se l'argomento argomento_ave7 è  uguale a  False  commento: {39,}  e  se l'argomento argomento_ave7 non  è  diverso da  False  commento: {39,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False , Almeno una delle seguenti { 
         commento: {61,}  se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 155 commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
         commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx commento: {39,}  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
         commento: {63,} commento: {35,}  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 13 commento: {36,} o  se il timer MainClass_C1_timer_T3 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P7 è  diverso da  commento: {56,} 9 commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
         commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T3 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  commento: {56,} 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  commento: {39,}  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 155 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  uguale a  commento: {53,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  commento: {53,} 1342 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  commento: {54,} 151 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 14305, Verifica che   commento: {47,49,52,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia attivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T3 sia scaduto
         commento: {104,} o  che   l'argomento argomento_ave7 sia  uguale a  False  commento: {,} 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  maggiore di  commento: {54,} 5
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia scaduto
        
        
         } Verifica che   commento: {47,48,49,50,52,}   l'argomento argomento_ave7 non  sia  uguale a  False  commento: {,} 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T3 sia attivo
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  diverso da  commento: {56,} 7
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex
        
        
         } Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V7 sia  maggiore di  commento: {54,} 3
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 sia  uguale a  commento: {53,} 14
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V7 non sia  minore di  commento: {55,} 5
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co2 sia  minore di  commento: {55,} 1305
         commento: {104,} o  che   l'argomento argomento_ave7 sia  diverso da  True  commento: {,} 
        
        
         } Verifica che   commento: {48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V7 sia  maggiore di  commento: {54,} 4
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V7 sia  minore di  commento: {55,} 10
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V7 sia  uguale a  commento: {53,} 1
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 1
        
        
         } Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P7 non sia  minore di  commento: {55,} 4
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T3 sia attivo
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex
        
        
         } Verifica che   commento: {48,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T3 sia attivo
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  commento: {54,} 1321
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 10
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  maggiore di  commento: {54,} 5
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da GialloxVerdex
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  o  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False , Almeno una delle seguenti { 
 /*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 1


 } Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P7 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex


 } Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  /*54,*/ 1321
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  o  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False , Almeno una delle seguenti { 
 /*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 1


 } Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P7 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex e  se l'argomento argomento_ave10 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T3 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave10 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  o  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False , Almeno una delle seguenti { 
 /*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 1


 } Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P7 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  o  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False , Almeno una delle seguenti { 
 /*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  o  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C3 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/  o  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  e  se l'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1 e  se l'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave7 è  uguale a  False  /*39,*/  e  se l'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave7 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C3 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P5 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 155""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (155)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P5 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 } Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 o  se l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (1342)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave2 è  diverso da c270xx /*39,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 è  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p7)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True  /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C3 non è  diverso da  False  e  se l'argomento argomento_ave10 non  è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C3 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave10 non  è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co2)  è minore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9 /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P7 è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p7)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C9 è  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130 o  se l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T3 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 è  diverso da  /*56,*/ 12130""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (12130)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave7 non  è  diverso da  True  /*39,*/  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 non  è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305, Verifica che   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 155""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (155)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 3""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  uguale a  /*53,*/ 1342""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (1342)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (151)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 14305""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (14305))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (14305)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,52,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T3 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave7 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  maggiore di  /*54,*/ 5""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,52,*/   l'argomento argomento_ave7 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T3 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v7)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*48,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C3 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co2 sia  uguale a  /*53,*/ 14""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V7 non sia  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v7)  è minore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co2 sia  minore di  /*55,*/ 1305""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 sia  maggiore di  /*54,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""LessThanImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  minore di  /*55,*/ 10""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  /*53,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (1))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P7 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P7 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T3 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P7 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p7)  è minore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T3 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C9 sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  /*54,*/ 1321
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  /*54,*/ 1321
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  /*54,*/ 1321""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T3 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  /*54,*/ 1321""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a GialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  maggiore di  /*54,*/ 1321""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2)  è maggiore di  (1321)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v7)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(argomento_ave10 == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_variabile_v7() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 155, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 1342, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(argomento_ave2 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p7() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave10 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co2().get_valore() < 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p7() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 12130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(argomento_ave7 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 155, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v7() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 1342, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 151, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 14305, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p10() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v7() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db(self.get_mainclass_c1_variabile_v7() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co2().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v7() < 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co2().get_valore() < 1305, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(argomento_ave7 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(self.get_mainclass_c1_variabile_v7() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_variabile_v7() < 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v7() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db(not db(self.get_mainclass_c1_parametro_p7() < 4, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() > 1321, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 10, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v7() > 5, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m6")
    def macroMainclass_c1_macrove_m6(self, argomento_ave3, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è attivo o  se l'argomento argomento_ave3 non  è  diverso da  True  commento: {39,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  uguale a  commento: {53,} 6, Verifica che   commento: {47,52,}   l'argomento argomento_ave3 non  sia  uguale a  False  commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave3 non  sia  uguale a  True  commento: {39,} 
         commento: {104,} e  che   l'argomento argomento_ave3 sia  uguale a  False  commento: {39,} 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a GialloxVerdex
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è attivo o  se l'argomento argomento_ave3 non  è  diverso da  True  /*39,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 6, Verifica che   /*47,52,*/   l'argomento argomento_ave3 non  sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è attivo o  se l'argomento argomento_ave3 non  è  diverso da  True  /*39,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 6, Verifica che   /*47,52,*/   l'argomento argomento_ave3 non  sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI5 non è attivo o  se l'argomento argomento_ave3 non  è  diverso da  True  /*39,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI5 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti5_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave3 non  è  diverso da  True  /*39,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave3 non  è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V7 è  uguale a  /*53,*/ 6""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,52,*/   l'argomento argomento_ave3 non  sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 sia  uguale a  False  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,52,*/   l'argomento argomento_ave3 non  sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,52,*/   l'argomento argomento_ave3 non  sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,52,*/   l'argomento argomento_ave3 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave3 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_mainclass_c1_restoreti_ti5_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(argomento_ave3 == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v7() == 6, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(not db(argomento_ave3 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave3 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(argomento_ave3 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a10, argomento_a2, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c270xx commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c270xx
        return GlobalEnumeration.c270xx
    
    @srf_value_macro("macroMainclass_c1_macrova_m5")
    def macroMainclass_c1_macrova_m5(self, argomento_a1, argomento_a4, argomento_a5, argomento_a6, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore Rosso commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore Rosso
        return GlobalEnumeration.rosso
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm1(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm1')
    
    def eventMainclass_c1_command_comm9DaSender1f7f1f8e(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm9DaSender1f7f1f8e')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm6(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm6')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c5_prev(self.get_mainclass_c1_previousco_c5())
        self.set_mainclass_c1_previousco_c7_prev(self.get_mainclass_c1_previousco_c7())
        self.set_mainclass_c1_previousco_c8_prev(self.get_mainclass_c1_previousco_c8())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())

