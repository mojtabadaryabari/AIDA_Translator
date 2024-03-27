# Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_subclass_c2_previousva_pv2(False)
        self.set_subclass_c2_restoreva_rv1(GlobalEnumeration.spento)
        self.set_subclass_c2_restoreva_rv2(False)
        self.set_subclass_c2_restoreva_rv3(GlobalEnumeration.avvio)
        self.set_subclass_c2_variabile_v2(False)
        self.set_subclass_c2_variabile_v9(0)

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
    def init_configuration(self, subclass_c2_lista_l3, subclass_c2_lista_l9, subclass_c2_parametro_p3, subclass_c2_parametro_p6):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l3(subclass_c2_lista_l3)
        self.set_subclass_c2_lista_l9(subclass_c2_lista_l9)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p3(subclass_c2_parametro_p3)
        self.set_subclass_c2_parametro_p6(subclass_c2_parametro_p6)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(1000)
        self.set_subclass_c2_restoreti_ti1_restore(1000)
        self.set_subclass_c2_restoreti_ti2(34000)
        self.set_subclass_c2_restoreti_ti2_restore(34000)
        self.set_subclass_c2_restoreti_ti3(3000)
        self.set_subclass_c2_restoreti_ti3_restore(3000)
        self.set_subclass_c2_timer_t1(1213000)
        self.set_subclass_c2_timer_t2(3000)
        self.set_subclass_c2_timer_t6(3000)
        self.set_subclass_c2_timer_t8(5000)
        self.set_subclass_c2_timer_t9(1450000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_restoreti_ti3,self.subclass_c2_restoreti_ti3_restore,self.subclass_c2_timer_t1,self.subclass_c2_timer_t2,self.subclass_c2_timer_t6,self.subclass_c2_timer_t8,self.subclass_c2_timer_t9,]

        # initialize the counters
        self.set_subclass_c2_contatore_co2(0)
        self.set_subclass_c2_contatore_co5(0)
        self.set_subclass_c2_contatore_co8(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l3(self, subclass_c2_lista_l3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3",subclass_c2_lista_l3)

    def set_subclass_c2_lista_l9(self, subclass_c2_lista_l9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9",subclass_c2_lista_l9)


    # getters for record type parameters
    def get_subclass_c2_lista_l3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3")

    def get_subclass_c2_lista_l9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p3(self, subclass_c2_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p3",subclass_c2_parametro_p3)

    def set_subclass_c2_parametro_p6(self, subclass_c2_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6",subclass_c2_parametro_p6)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p3")

    def get_subclass_c2_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c10(self, subclass_c2_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c10",subclass_c2_comando_c10)

    def set_subclass_c2_comando_c2(self, subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c2",subclass_c2_comando_c2)

    def set_subclass_c2_comando_c8(self, subclass_c2_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c8",subclass_c2_comando_c8)

    def set_subclass_c2_comando_c9(self, subclass_c2_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c9",subclass_c2_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c1")

    def get_subclass_c2_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c3")

    def get_subclass_c2_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c6")

    def get_subclass_c2_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c7")

    def get_subclass_c2_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c8")

    def get_subclass_c2_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4")

    def get_subclass_c2_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5")


    # setters for state variables
    def set_subclass_c2_previousco_c4_prev(self, subclass_c2_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev",subclass_c2_previousco_c4_prev)
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
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_restoreva_rv3(self, subclass_c2_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3",subclass_c2_restoreva_rv3)
    def set_subclass_c2_variabile_v2(self, subclass_c2_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2",subclass_c2_variabile_v2)
    def set_subclass_c2_variabile_v9(self, subclass_c2_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9",subclass_c2_variabile_v9)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev")

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

    def get_subclass_c2_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2")

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

    def set_subclass_c2_timer_t1(self, timerDuration):
        self.subclass_c2_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t1", self.memory)

    def set_subclass_c2_timer_t2(self, timerDuration):
        self.subclass_c2_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t2", self.memory)

    def set_subclass_c2_timer_t6(self, timerDuration):
        self.subclass_c2_timer_t6 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t6", self.memory)

    def set_subclass_c2_timer_t8(self, timerDuration):
        self.subclass_c2_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t8", self.memory)

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

    def get_subclass_c2_timer_t1(self):
        return self.subclass_c2_timer_t1

    def get_subclass_c2_timer_t2(self):
        return self.subclass_c2_timer_t2

    def get_subclass_c2_timer_t6(self):
        return self.subclass_c2_timer_t6

    def get_subclass_c2_timer_t8(self):
        return self.subclass_c2_timer_t8

    def get_subclass_c2_timer_t9(self):
        return self.subclass_c2_timer_t9


    # setters for counters
    def set_subclass_c2_contatore_co2(self, counterInitValue):
        self.subclass_c2_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co2", self.memory)

    def set_subclass_c2_contatore_co5(self, counterInitValue):
        self.subclass_c2_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co5", self.memory)

    def set_subclass_c2_contatore_co8(self, counterInitValue):
        self.subclass_c2_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co8", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co2(self):
        return self.subclass_c2_contatore_co2

    def get_subclass_c2_contatore_co5(self):
        return self.subclass_c2_contatore_co5

    def get_subclass_c2_contatore_co8(self):
        return self.subclass_c2_contatore_co8



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

        self.set_subclass_c2_previousco_c4_prev(GlobalEnumeration.c120)
        self.set_subclass_c2_previousco_c5_prev(False)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())

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
        
        { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  diverso da Rosso commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 155021 commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  commento: {54,} 1134, commento: {69,}Disattiva il timer SubClass_C2_timer_T8
        
           
         commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,}, commento: {68,}Attiva il timer SubClass_C2_timer_T8
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore  False 
        
        
         commento: {36,}  se il timer SubClass_C2_timer_T8 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T2 non è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  commento: {56,} 8, commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  True 
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  diverso da Rosso /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 155021 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 1134, /*69,*/Disattiva il timer SubClass_C2_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  diverso da Rosso /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 155021 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 1134""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_restoreva_rv3_restore)  è uguale a  (rosso))) )  e  ( negazione di ((subclass_c2_contatore_co5)  è maggiore di  (155021)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_restoreva_rv3_restore)  è uguale a  (rosso)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv3_restore)  è uguale a  (rosso))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv3_restore)  è uguale a  (rosso)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è maggiore di  (155021))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (155021)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (1134)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/, /*68,*/Attiva il timer SubClass_C2_timer_T8

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore  False""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T8 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 8, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T8 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'subclass_c2_timer_t8' è inattivo) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t8' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t2' è attivo) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (8))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t2' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (8)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 non è  diverso da Rosso /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 155021 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 1134, /*69,*/Disattiva il timer SubClass_C2_timer_T8
        if db((db((db(not db(not db(self.get_subclass_c2_restoreva_rv3_restore() == GlobalEnumeration.rosso, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 155021, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co5().get_valore() > 1134, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t8().disattiva()
        #  /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/, /*68,*/Attiva il timer SubClass_C2_timer_T8
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore  False
        if db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_timer_t8().attiva()
        else:
            self.set_subclass_c2_comando_c8(False)
        #  /*36,*/  se il timer SubClass_C2_timer_T8 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 8, /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  True
        if db((db((db(not db(self.get_subclass_c2_timer_t8().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t2().isAttivato(), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v9() == 8, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_comando_c2(True)
    
    def macroSubclass_c2_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {42,}  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  True  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 7 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True ,  Applica gli effetti
               della macro SubClass_C2_macroef_M9( con argomento_af10   uguale a True ,argomento_af6   uguale a c270x ,argomento_af1   uguale a avvio ,argomento_af3   uguale a c75Giallo ,argomento_af2   uguale a c270x ,argomento_af4   uguale a c270x ,argomento_af9   uguale a Rosso ) commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore 4
        
        
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a  True , commento: {69,}Disattiva il timer SubClass_C2_timer_T8
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True ,  Applica gli effetti
       della macro SubClass_C2_macroef_M9( con argomento_af10   uguale a True ,argomento_af6   uguale a c270x ,argomento_af1   uguale a avvio ,argomento_af3   uguale a c75Giallo ,argomento_af2   uguale a c270x ,argomento_af4   uguale a c270x ,argomento_af9   uguale a Rosso ) /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore 4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_parametro_p6)  è maggiore di  (7) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((subclass_c2_controllo_c8)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_parametro_p6)  è maggiore di  (7) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (7)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M9( con argomento_af10   uguale a True ,argomento_af6   uguale a c270x ,argomento_af1   uguale a avvio ,argomento_af3   uguale a c75Giallo ,argomento_af2   uguale a c270x ,argomento_af4   uguale a c270x ,argomento_af9   uguale a Rosso )"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a  True , /*69,*/Disattiva il timer SubClass_C2_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (c270x))) )  e  ( negazione di (negazione di ((subclass_c2_parametro_p6)  è uguale a  (2))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (c270x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p6)  è uguale a  (2)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M9( con argomento_af10   uguale a True ,argomento_af6   uguale a c270x ,argomento_af1   uguale a avvio ,argomento_af3   uguale a c75Giallo ,argomento_af2   uguale a c270x ,argomento_af4   uguale a c270x ,argomento_af9   uguale a Rosso ) /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore 4
        if db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_parametro_p6() > 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c2_macroef_m9(GlobalEnumeration.avvio,True,GlobalEnumeration.c270x,GlobalEnumeration.c75giallo,GlobalEnumeration.c270x,GlobalEnumeration.c270x,GlobalEnumeration.rosso, di_ctx.subs[0].subs[1])
        else:
            self.set_subclass_c2_variabile_v9(4)
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a  True , /*69,*/Disattiva il timer SubClass_C2_timer_T8
        if db((db((db(not db(not db(self.get_subclass_c2_restoreva_rv1_restore() == GlobalEnumeration.c270x, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p6() == 2, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c1() == True, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_timer_t8().disattiva()
    
    def macroSubclass_c2_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  minore di  commento: {55,} 9, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
        
        
         commento: {37,}  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 3, commento: {69,}Disattiva il timer SubClass_C2_timer_T1
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T2
        
        
         commento: {35,}  se il controllo SubClass_C2_controllo_C6 non è  uguale a  False , commento: {69,}Disattiva il timer SubClass_C2_timer_T8
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  minore di  /*55,*/ 9, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 3, /*69,*/Disattiva il timer SubClass_C2_timer_T1

 ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p6)  è uguale a  (3)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C2_controllo_C6 non è  uguale a  False , /*69,*/Disattiva il timer SubClass_C2_timer_T8""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#2
                ])

        populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  minore di  /*55,*/ 9, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8
        if db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v6() < 9, di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v2(False)
        else:
            self.get_subclass_c2_contatore_co8().decrementa()
        #  /*37,*/  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 3, /*69,*/Disattiva il timer SubClass_C2_timer_T1
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T2
        if db((db(not db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p6() == 3, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_timer_t1().disattiva()
        else:
            self.get_subclass_c2_timer_t2().attiva()
        #  /*35,*/  se il controllo SubClass_C2_controllo_C6 non è  uguale a  False , /*69,*/Disattiva il timer SubClass_C2_timer_T8
        if db(not db(self.get_subclass_c2_controllo_c6() == False, di_ctx.subs[2].subs[0].subs[0]), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_timer_t8().disattiva()
    
    def macroSubclass_c2_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  uguale a  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  commento: {53,} 15213, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore 9
        
           
         commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 5 commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a Rosso, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
        
           
         commento: {41,}  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,} 6 o  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        
         ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co2
        
        
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  commento: {53,} 144 commento: {36,} o  se il timer SubClass_C2_timer_T2 non è attivo commento: {36,} e  se il timer SubClass_C2_timer_T2 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T2 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 15213, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 15213""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (False))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c3)  è uguale a  (True)) )  e  
( (subclass_c2_contatore_co8)  è uguale a  (15213) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (15213)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a Rosso, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a Rosso""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo)} )  o  
( negazione di ((subclass_c2_parametro_p6)  è maggiore di  (5)) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è maggiore di  (5))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (rosso)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 

 ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (6))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 144 /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 144 /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'subclass_c2_restoreti_ti1_restore' è attivo )  e  
( negazione di ((subclass_c2_contatore_co5)  è uguale a  (144)) ) )  o  
( ( negazione di (il timer 'subclass_c2_timer_t2' è attivo) )  e  
( negazione di (il timer 'subclass_c2_timer_t2' è scaduto) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_restoreti_ti1_restore' è attivo )  e  
( negazione di ((subclass_c2_contatore_co5)  è uguale a  (144)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è uguale a  (144))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (144)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t2' è attivo) )  e  
( negazione di (il timer 'subclass_c2_timer_t2' è scaduto) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t2' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t2' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'subclass_c2_timer_t2' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t2' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 15213, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore 9
        if db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co8().get_valore() == 15213, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v9(9)
        #  /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L9 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5 /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a Rosso, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() > 5, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c7() == GlobalEnumeration.rosso, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v2(False)
        #  /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        #   ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co2
        if db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p2() == 6, di_ctx.subs[2].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
        else:
            self.get_subclass_c2_contatore_co2().incrementa()
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 144 /*36,*/ o  se il timer SubClass_C2_timer_T2 non è attivo /*36,*/ e  se il timer SubClass_C2_timer_T2 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
        if db((db((db((db(self.get_subclass_c2_restoreti_ti1_restore().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 144, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t2().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t2().isScaduto(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t2().isAttivato(), di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
        else:
            self.set_subclass_c2_variabile_v2(False)
    
    def macroSubclass_c2_macroef_m9(self, argomento_af1, argomento_af10, argomento_af2, argomento_af3, argomento_af4, argomento_af6, argomento_af9, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se l'argomento argomento_af10 è  uguale a  True  commento: {39,} ,  commento: {45,}  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  maggiore di  commento: {54,} 144, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  diverso da  commento: {56,} 1350 commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  minore di  commento: {55,} 2 e  se l'argomento argomento_af10 è  diverso da  False  commento: {39,} ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True  commento: {67,}
        
           
          se l'argomento argomento_af1 è  diverso da Rosso commento: {39,} , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co2
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C10 il valore GialloGiallo
        
        
         commento: {42,}  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  True  o  se l'argomento argomento_af3 non  è  uguale a c120 commento: {39,} , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore  True 
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 3,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False commento: {67,}
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 non è scaduto commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True  commento: {67,}
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse l'argomento argomento_af10 è  uguale a  True  /*39,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 144, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  diverso da  /*56,*/ 1350 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 2 e  se l'argomento argomento_af10 è  diverso da  False  /*39,*/ ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse l'argomento argomento_af10 è  uguale a  True  /*39,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 144, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  diverso da  /*56,*/ 1350 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 2 e  se l'argomento argomento_af10 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (argomento_af10)  è uguale a  (True) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1350))) allora ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (144))} ) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (False))) ) )  o  
( negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (argomento_af10)  è uguale a  (True) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1350))) allora ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (144))} ) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (False))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (argomento_af10)  è uguale a  (True) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1350))) allora ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (144))} )""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af10)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1350))) allora ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (144))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1350))) allora ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (144))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1350))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1350)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (144)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_controllo_c1)  è uguale a  (False)) )  e  ( (subclass_c2_variabile_v9)  è minore di  (2) ) )  e  
( negazione di ((argomento_af10)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c1)  è uguale a  (False)) )  e  ( (subclass_c2_variabile_v9)  è minore di  (2) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v9)  è minore di  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*67,*/

   
  se l'argomento argomento_af1 è  diverso da Rosso /*39,*/ , /*72,*/Azzera il contatore SubClass_C2_contatore_Co2

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C10 il valore GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_af1 è  diverso da Rosso""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af1)  è uguale a  (rosso)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  True  o  se l'argomento argomento_af3 non  è  uguale a c120 /*39,*/ , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  True  o  se l'argomento argomento_af3 non  è  uguale a c120""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af3)  è uguale a  (c120))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af3)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 3,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False""", [
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 3""", [
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*67,*/

   
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 non è scaduto /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/

   
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 non è scaduto /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_restoreti_ti3_restore' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti3_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  se l'argomento argomento_af10 è  uguale a  True  /*39,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 144, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  diverso da  /*56,*/ 1350 /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 2 e  se l'argomento argomento_af10 è  diverso da  False  /*39,*/ ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
        if db((db((db((db((db(argomento_af10 == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co7().get_valore() > 144, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() == 1350, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v9() < 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_af10 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
        #  /*67,*/
        #     
        #    se l'argomento argomento_af1 è  diverso da Rosso /*39,*/ , /*72,*/Azzera il contatore SubClass_C2_contatore_Co2
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C10 il valore GialloGiallo
        if db(not db(argomento_af1 == GlobalEnumeration.rosso, di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co2().resetta()
        else:
            self.set_subclass_c2_comando_c10(GlobalEnumeration.giallogiallo)
        #  /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  True  o  se l'argomento argomento_af3 non  è  uguale a c120 /*39,*/ , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore  True
        if db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c1() == True, di_ctx.subs[2].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[2].subs[0].subs[0]) or db(not db(argomento_af3 == GlobalEnumeration.c120, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_variabile_v2(False)
        else:
            self.set_subclass_c2_comando_c2(True)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 3,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
        if db(self.get_subclass_c2_parametro_p3() < 3, di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_variabile_v2(False)
        #  /*67,*/
        #     
        #   /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 non è scaduto /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
        if db((db(not db(self.get_subclass_c2_restoreti_ti3_restore().isScaduto(), di_ctx.subs[4].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[4].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m1")
    def macroSubclass_c2_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  minore di  commento: {55,} 6 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 14 commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 non è  maggiore di  commento: {54,} 1334 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  commento: {53,} 3, Verifica che   commento: {47,48,50,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  uguale a  commento: {53,} 3
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  minore di  commento: {55,} 7
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  uguale a  False 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 14 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  maggiore di  /*54,*/ 1334 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  /*53,*/ 3, Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 14 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  maggiore di  /*54,*/ 1334 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  /*53,*/ 3, Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 14 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  maggiore di  /*54,*/ 1334 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  True""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 6""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co8)  è uguale a  (14))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co2 non è  maggiore di  /*54,*/ 1334 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co2 non è  maggiore di  /*54,*/ 1334""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co2)  è maggiore di  (1334)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p3)  è minore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v9() < 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co2().get_valore() > 1334, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() == 3, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p3() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p3() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m10")
    def macroSubclass_c2_macrove_m10(self, argomento_ave1, argomento_ave10, argomento_ave3, argomento_ave6, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P3 è  maggiore di  commento: {54,} 2, Solo una delle seguenti { 
         commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 non è  minore di  commento: {55,} 9 commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  commento: {56,} 1313 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  commento: {54,} 8, Tutte le seguenti { 
         commento: {62,} commento: {42,}  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  commento: {55,} 154 commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  commento: {39,}  commento: {36,} e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
         commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
         commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  True  commento: {36,} o  se il timer SubClass_C2_timer_T9 non è scaduto commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
         commento: {35,}  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  commento: {55,} 155021 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 4, Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  uguale a  commento: {53,} 9
         commento: {104,} e  che   l'argomento argomento_ave6 sia  uguale a  True  commento: {,} 
        
        
         } Verifica che   commento: {47,49,50,}  commento: {,}  il timer SubClass_C2_timer_T2 sia disattivo
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 9
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T2 non sia disattivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T2 sia scaduto
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V9 non sia  diverso da  commento: {56,} 9
        
        
         } Verifica che   commento: {48,50,}  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  minore di  commento: {55,} 4
        
        
         } Verifica che   commento: {48,49,51,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T2 non sia scaduto
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  minore di  commento: {55,} 15
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  diverso da  True 
        
        
         } Verifica che   commento: {47,48,52,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
         commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a c120 commento: {,} 
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C8 sia  uguale a  False 
         commento: {104,} o  che   l'argomento argomento_ave10 sia  uguale a c120 commento: {39,} 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 8
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 è  maggiore di  /*54,*/ 2, Solo una delle seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 1313 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da  True 


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a c120 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave10 sia  uguale a c120 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 è  maggiore di  /*54,*/ 2, Solo una delle seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 1313 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P3 è  maggiore di  /*54,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 1313 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  minore di  /*55,*/ 15


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 1313 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  /*54,*/ 8, Tutte le seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  minore di  /*55,*/ 15


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 1313 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 1313""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p3)  è minore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 1313""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è uguale a  (1313))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (1313)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C2_variabile_V9 è  maggiore di  /*54,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4


 } Verifica che   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  minore di  /*55,*/ 15


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*42,*/  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da  True""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 154""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co5)  è minore di  (154)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True  /*39,*/  /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11 e  se l'argomento argomento_ave6 non  è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave6 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 } Verifica che   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto, Almeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C2_timer_T6 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T6 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 } Verifica che   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True , Almeno una delle seguenti { 
 /*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4, Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 155021""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co2)  è minore di  (155021)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a  /*53,*/ 9""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave6 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,49,50,*/  /*,*/  il timer SubClass_C2_timer_T2 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 9""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T2 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C2_timer_T2 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,50,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v9)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co5)  è minore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a c120 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave10 sia  uguale a c120 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a c120 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave10 non  sia  uguale a c120 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  uguale a c120""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave10 sia  uguale a c120 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave10 sia  uguale a c120""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 8""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db(self.get_subclass_c2_parametro_p3() > 2, di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p3() < 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 1313, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v9() > 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() < 154, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(argomento_ave6 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(self.get_subclass_c2_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co2().get_valore() < 155021, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c2_parametro_p3() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(argomento_ave6 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(self.get_subclass_c2_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p6() > 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v9() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_subclass_c2_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() < 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(not db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db(not db(argomento_ave10 == GlobalEnumeration.c120, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c8() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(argomento_ave10 == GlobalEnumeration.c120, di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p6() > 8, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m4")
    def macroSubclass_c2_macrove_m4(self, argomento_ave4, argomento_ave5, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  minore di  commento: {55,} 1 commento: {36,} e  se il timer SubClass_C2_timer_T2 è scaduto, Verifica che   commento: {50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  diverso da  True 
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a GialloGiallo commento: {,} 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 1 /*36,*/ e  se il timer SubClass_C2_timer_T2 è scaduto, Verifica che   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 1 /*36,*/ e  se il timer SubClass_C2_timer_T2 è scaduto, Verifica che   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 1 /*36,*/ e  se il timer SubClass_C2_timer_T2 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V9 è  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T2 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v9() < 1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave4 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m8")
    def macroSubclass_c2_macrove_m8(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave4, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  maggiore di  commento: {54,} 11 e  se l'argomento argomento_ave3 è  diverso da Rosso commento: {39,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 7 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Tutte le seguenti { 
         commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  commento: {54,} 4 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True , Tutte le seguenti { 
         commento: {61,} commento: {37,}  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  commento: {56,} 14 commento: {36,} e  se il timer SubClass_C2_timer_T6 è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  commento: {54,} 15450, Tutte le seguenti { 
         commento: {61,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  commento: {53,} 15 commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 14213 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 124 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  commento: {56,} 5 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
         commento: {63,}  se l'argomento argomento_ave4 è  diverso da c120 commento: {39,}  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  commento: {53,} 145 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  commento: {54,} 5 e  se l'argomento argomento_ave1 è  diverso da  True  commento: {39,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 3 commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 7, Solo una delle seguenti { 
         commento: {63,} commento: {45,}  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  maggiore di  commento: {54,} 1402, Solo una delle seguenti { 
         commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  uguale a  commento: {53,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P3 non è  minore di  commento: {55,} 4 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
         commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
         commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 6, Verifica che   commento: {47,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  uguale a  commento: {53,} 9
         commento: {104,} e  che   l'argomento argomento_ave2 non  sia  uguale a  False  commento: {,} 
         commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {39,} 
         commento: {104,} o  che   l'argomento argomento_ave1 sia  uguale a  False  commento: {39,} 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  minore di  commento: {55,} 5
        
        
         } Verifica che   commento: {50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  commento: {54,} 1513
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  commento: {56,} 11
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  diverso da  commento: {56,} 4
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  commento: {53,} 11
        
        
         } Verifica che   commento: {50,52,}   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
        
        
         } Verifica che   commento: {47,48,49,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T2 non sia scaduto
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  diverso da  commento: {56,} 1
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 134
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  commento: {56,} 135
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  diverso da  commento: {56,} 1302
        
        
         } Verifica che   commento: {47,49,50,51,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  commento: {54,} 13
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 10
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T2 sia attivo
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  minore di  commento: {55,} 13
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T2 sia scaduto
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co2 sia  diverso da  commento: {56,} 154
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  minore di  commento: {55,} 8
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T2 non sia disattivo
        
        
         } Verifica che   commento: {47,51,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  diverso da  commento: {56,} 4
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 115021
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a c120 commento: {,} 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 11 e  se l'argomento argomento_ave3 è  diverso da Rosso /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450, Tutte le seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T2 sia scaduto


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 154
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  minore di  /*55,*/ 8
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T2 non sia disattivo


 } Verifica che   /*47,51,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  diverso da  /*56,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 115021
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a c120""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 11 e  se l'argomento argomento_ave3 è  diverso da Rosso /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450, Tutte le seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T2 sia scaduto


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 154
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  minore di  /*55,*/ 8
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T2 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 11 e  se l'argomento argomento_ave3 è  diverso da Rosso /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 11 e  se l'argomento argomento_ave3 è  diverso da Rosso /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 11 e  se l'argomento argomento_ave3 è  diverso da Rosso /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 11 e  se l'argomento argomento_ave3 è  diverso da Rosso""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave3 è  diverso da Rosso""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (rosso)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C8 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450, Tutte le seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T2 sia scaduto


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 154
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  minore di  /*55,*/ 8
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T2 non sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450, Tutte le seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T2 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p3)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V2 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450, Tutte le seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T2 sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450, Tutte le seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*36,*/ e  se il timer SubClass_C2_timer_T6 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V2 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T6 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co8 è  maggiore di  /*54,*/ 15450""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True , Tutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 14213""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (14213)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 124""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (124)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V2 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7, Solo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True  /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5 e  se l'argomento argomento_ave1 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se l'argomento argomento_ave4 è  diverso da c120 /*39,*/  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 è  diverso da c120""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 145""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (145)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v9)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 3""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 }""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 1402""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (1402)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da c270x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 non è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p3)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V2 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo, Tutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 }""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI2 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T2 non è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T2 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6, Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  uguale a  /*53,*/ 9""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave2 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave1 sia  uguale a  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave1 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  minore di  /*55,*/ 5""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  maggiore di  /*54,*/ 1513""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,52,*/   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 134""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (134)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co5 non sia  diverso da  /*56,*/ 135""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è uguale a  (135))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (135)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 1302""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (1302)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T2 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 13""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 10""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T2 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 13""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T2 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 154
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  minore di  /*55,*/ 8
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T2 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 154
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  minore di  /*55,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co2 sia  diverso da  /*56,*/ 154""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (154)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  minore di  /*55,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  minore di  /*55,*/ 8""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T2 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t2' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  diverso da  /*56,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 115021
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a c120""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p3)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 115021
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a c120""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 115021""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (115021)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a c120""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() > 11, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave3 == GlobalEnumeration.rosso, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p3() == 7, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(self.get_subclass_c2_parametro_p3() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co8().get_valore() > 15450, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 14213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v9() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db((db(not db(argomento_ave4 == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 145, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave1 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p6() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p3() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co7().get_valore() > 1402, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db(not db(not db(self.get_subclass_c2_restoreva_rv1_restore() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p3() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p3() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c2_parametro_p6() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p3() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_subclass_c2_variabile_v9() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave2 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(argomento_ave1 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(argomento_ave1 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p3() < 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(self.get_subclass_c2_contatore_co2().get_valore() > 1513, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db((db(not db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(not db(argomento_ave1 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_parametro_p3() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 134, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 135, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 1302, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(not db(self.get_subclass_c2_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co5().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p6() > 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co8().get_valore() < 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 154, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p6() < 8, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(not db(self.get_subclass_c2_parametro_p3() == 4, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 115021, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(argomento_ave4 == GlobalEnumeration.c120, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m3")
    def macroSubclass_c2_macrova_m3(self, argomento_a4, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {37,}  se la variabile SubClass_C2_variabile_V9 non è  minore di  commento: {55,} 2 commento: {36,} e  se il timer SubClass_C2_timer_T8 non è disattivo o  se l'argomento argomento_a4 non  è  uguale a c270x commento: {39,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  minore di  commento: {55,} 134 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è attivo e  se la macro  SubClass_C2_macrova_M5 ( con argomento_a10   uguale a c270x ,argomento_a6   uguale a avvio ,argomento_a1   uguale a Rosso ,argomento_a3   uguale a c75Giallo  e argomento_a2   uguale a c120 )  non  è  diverso da  True  commento: {40,}  , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 non è  minore di  /*55,*/ 2 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è disattivo o  se l'argomento argomento_a4 non  è  uguale a c270x /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  minore di  /*55,*/ 134 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo e  se la macro  SubClass_C2_macrova_M5 ( con argomento_a10   uguale a c270x ,argomento_a6   uguale a avvio ,argomento_a1   uguale a Rosso ,argomento_a3   uguale a c75Giallo  e argomento_a2   uguale a c120 )  non  è  diverso da  True  /*40,*/  , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 non è  minore di  /*55,*/ 2 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è disattivo o  se l'argomento argomento_a4 non  è  uguale a c270x /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  minore di  /*55,*/ 134 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo e  se la macro  SubClass_C2_macrova_M5 ( con argomento_a10   uguale a c270x ,argomento_a6   uguale a avvio ,argomento_a1   uguale a Rosso ,argomento_a3   uguale a c75Giallo  e argomento_a2   uguale a c120 )  non  è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_variabile_v9)  è minore di  (2)) )  e  
( negazione di (il timer 'subclass_c2_timer_t8' è inattivo) ) )  o  
( ( negazione di ((argomento_a4)  è uguale a  (c270x)) )  e  
( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (134)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))} ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v9)  è minore di  (2)) )  e  
( negazione di (il timer 'subclass_c2_timer_t8' è inattivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è minore di  (2))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v9)  è minore di  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t8' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((argomento_a4)  è uguale a  (c270x)) )  e  
( per ognuna delle seguenti con lista non vuota {se ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (134)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a4)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a4)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (134)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (134)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (134)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t1' è attivo) )  e  
( negazione di (negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m5')  è uguale a  (True))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m5')  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m5')  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m5')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m5'"""),#0
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m3_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 non è  minore di  /*55,*/ 2 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è disattivo o  se l'argomento argomento_a4 non  è  uguale a c270x /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co7 del campo  MainClass_C1     è  minore di  /*55,*/ 134 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo e  se la macro  SubClass_C2_macrova_M5 ( con argomento_a10   uguale a c270x ,argomento_a6   uguale a avvio ,argomento_a1   uguale a Rosso ,argomento_a3   uguale a c75Giallo  e argomento_a2   uguale a c120 )  non  è  diverso da  True  /*40,*/  , assegna alla macro il valore  False
        if db((db((db((db(not db(self.get_subclass_c2_variabile_v9() < 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(argomento_a4 == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co7().get_valore() < 134, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(db(self.macroSubclass_c2_macrova_m5(GlobalEnumeration.rosso,GlobalEnumeration.c270x,GlobalEnumeration.c120,GlobalEnumeration.c75giallo,GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m5")
    def macroSubclass_c2_macrova_m5(self, argomento_a1, argomento_a10, argomento_a2, argomento_a3, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m5_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c2_macrova_m6")
    def macroSubclass_c2_macrova_m6(self, argomento_a10, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da avanzamento commento: {41,} o  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  commento: {55,} 4 commento: {34,} o  se il parametro SubClass_C2_parametro_P3 non è  uguale a  commento: {53,} 8 commento: {42,} o  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  True  , assegna alla macro il valore GialloGiallo
        
         commento: {46,} assegna alla macro il valore GialloGiallo commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da avanzamento /*41,*/ o  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 non è  uguale a  /*53,*/ 8 /*42,*/ o  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True  , assegna alla macro il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da avanzamento /*41,*/ o  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 non è  uguale a  /*53,*/ 8 /*42,*/ o  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (avanzamento)))} )  o  
( per ognuna delle seguenti {((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (4))} ) )  o  
( negazione di ((subclass_c2_parametro_p3)  è uguale a  (8)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (avanzamento)))} )  o  
( per ognuna delle seguenti {((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (4))} )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (avanzamento)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (4))}""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p3)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da avanzamento /*41,*/ o  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 non è  uguale a  /*53,*/ 8 /*42,*/ o  se  MainClass_C1_controllo_C1 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True  , assegna alla macro il valore GialloGiallo
        if db((db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p2() < 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p3() == 8, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.giallogiallo
        #  /*46,*/ assegna alla macro il valore GialloGiallo
        return GlobalEnumeration.giallogiallo
    
    @srf_value_macro("macroSubclass_c2_macrova_m7")
    def macroSubclass_c2_macrova_m7(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c4_prev(self.get_subclass_c2_previousco_c4())
        self.set_subclass_c2_previousco_c5_prev(self.get_subclass_c2_previousco_c5())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())

class SubClass_C2_RecordHeaderR2(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled7, recordfiled4):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled7(recordfiled7)
        self.set_recordfiled4(recordfiled4)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled7(self, recordfiled7):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"), recordfiled7)

    def set_recordfiled4(self, recordfiled4):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"), recordfiled4)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled7(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"))

    def get_recordfiled4(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"))



class SubClass_C2_RecordHeaderR4(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled13, recordfiled6, recordfiled11):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled13(recordfiled13)
        self.set_recordfiled6(recordfiled6)
        self.set_recordfiled11(recordfiled11)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled13(self, recordfiled13):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"), recordfiled13)

    def set_recordfiled6(self, recordfiled6):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"), recordfiled6)

    def set_recordfiled11(self, recordfiled11):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"), recordfiled11)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled13(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"))

    def get_recordfiled6(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"))

    def get_recordfiled11(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"))



