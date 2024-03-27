# Codice del modello 'TestCase21', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_variabile_v1(GlobalEnumeration.c270x)
        self.set_mainclass_c1_variabile_v10(0)
        self.set_mainclass_c1_variabile_v2(GlobalEnumeration.ac)
        self.set_mainclass_c1_variabile_v5(GlobalEnumeration.ac)
        self.set_mainclass_c1_variabile_v6(False)

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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(42000)
        self.set_mainclass_c1_restoreti_ti1_restore(42000)
        self.set_mainclass_c1_restoreti_ti2(205000)
        self.set_mainclass_c1_restoreti_ti2_restore(205000)
        self.set_mainclass_c1_restoreti_ti3(534000)
        self.set_mainclass_c1_restoreti_ti3_restore(534000)
        self.set_mainclass_c1_restoreti_ti4(4120000)
        self.set_mainclass_c1_restoreti_ti4_restore(4120000)
        self.set_mainclass_c1_restoreti_ti5(2000)
        self.set_mainclass_c1_restoreti_ti5_restore(2000)
        self.set_mainclass_c1_timer_t4(4341000)
        self.set_mainclass_c1_timer_t9(2000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_restoreti_ti5,self.mainclass_c1_restoreti_ti5_restore,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t9,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)
        self.set_mainclass_c1_contatore_co2(0)
        self.set_mainclass_c1_contatore_co6(0)
        self.set_mainclass_c1_contatore_co7(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c2(self, mainclass_c1_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c2",mainclass_c1_comando_c2)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)

    def set_mainclass_c1_comando_c6(self, mainclass_c1_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c6",mainclass_c1_comando_c6)

    def set_mainclass_c1_comando_c8(self, mainclass_c1_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c8",mainclass_c1_comando_c8)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c10")

    def get_mainclass_c1_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1")


    # setters for state variables
    def set_mainclass_c1_previousco_c1_prev(self, mainclass_c1_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev",mainclass_c1_previousco_c1_prev)
    def set_mainclass_c1_previousva_pv1(self, mainclass_c1_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1",mainclass_c1_previousva_pv1)
    def set_mainclass_c1_previousva_pv1_prev(self, mainclass_c1_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev",mainclass_c1_previousva_pv1_prev)
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v6(self, mainclass_c1_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6",mainclass_c1_variabile_v6)

    # getters for state variables
    def get_mainclass_c1_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev")

    def get_mainclass_c1_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1")

    def get_mainclass_c1_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev")

    def get_mainclass_c1_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1")

    def get_mainclass_c1_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1_restore")

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

    def get_mainclass_c1_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6")

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

    def get_mainclass_c1_restoreti_ti4(self):
        return self.mainclass_c1_restoreti_ti4

    def get_mainclass_c1_restoreti_ti4_restore(self):
        return self.mainclass_c1_restoreti_ti4_restore

    def get_mainclass_c1_restoreti_ti5(self):
        return self.mainclass_c1_restoreti_ti5

    def get_mainclass_c1_restoreti_ti5_restore(self):
        return self.mainclass_c1_restoreti_ti5_restore

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t9(self):
        return self.mainclass_c1_timer_t9


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)

    def set_mainclass_c1_contatore_co2(self, counterInitValue):
        self.mainclass_c1_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co2", self.memory)

    def set_mainclass_c1_contatore_co6(self, counterInitValue):
        self.mainclass_c1_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co6", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1

    def get_mainclass_c1_contatore_co2(self):
        return self.mainclass_c1_contatore_co2

    def get_mainclass_c1_contatore_co6(self):
        return self.mainclass_c1_contatore_co6

    def get_mainclass_c1_contatore_co7(self):
        return self.mainclass_c1_contatore_co7



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

        self.set_mainclass_c1_previousco_c1_prev(GlobalEnumeration.spento)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())

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
    def macroMainclass_c1_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore c120
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore  False 
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co7
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore c120
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c120

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore  False""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co7

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore c120""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore c120
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore  False
        if db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v5(GlobalEnumeration.c120)
        else:
            self.set_mainclass_c1_comando_c8(False)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co7
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore c120
        if db((db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.avvio, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co7().decrementa()
        else:
            self.set_mainclass_c1_variabile_v2(GlobalEnumeration.c120)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m7")
    def macroMainclass_c1_macrove_m7(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da spento commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  diverso da c180x, Almeno una delle seguenti { 
         commento: {35,}  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio, Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  diverso da  commento: {56,} 4
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T4 non sia attivo
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  minore di  commento: {55,} 3
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a avvio
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da spento /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  diverso da c180x, Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a avvio""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da spento /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  diverso da c180x, Almeno una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da spento /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  diverso da c180x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da spento""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 è  diverso da c180x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a avvio""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 non è  uguale a c180x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V1 non è  uguale a avvio""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c120""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C10 sia  uguale a c180x""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a avvio""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c180x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (c180x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a avvio""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db((db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v10() == 4, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() < 3, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v1() == GlobalEnumeration.avvio, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a1, argomento_a10, argomento_a2, argomento_a3, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore spento commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore spento
        return GlobalEnumeration.spento
    
    @srf_value_macro("macroMainclass_c1_macrova_m4")
    def macroMainclass_c1_macrova_m4(self, argomento_a1, argomento_a10, argomento_a2, argomento_a4, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se la macro  MainClass_C1_macrova_M3 ( con argomento_a2   uguale a c270x ,argomento_a3   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a9   uguale a AC ,argomento_a1   uguale a AC  e argomento_a10   uguale a AC )  non  è  diverso da spento commento: {40,}  e  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  commento: {53,} 3 commento: {34,} e  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} , assegna alla macro il valore c180x
        
         commento: {46,} assegna alla macro il valore c180x commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a2   uguale a c270x ,argomento_a3   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a9   uguale a AC ,argomento_a1   uguale a AC  e argomento_a10   uguale a AC )  non  è  diverso da spento /*40,*/  e  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  /*53,*/ 3 /*34,*/ e  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore c180x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a2   uguale a c270x ,argomento_a3   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a9   uguale a AC ,argomento_a1   uguale a AC  e argomento_a10   uguale a AC )  non  è  diverso da spento /*40,*/  e  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  /*53,*/ 3 /*34,*/ e  se lo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (spento))) )  e  
( negazione di ((stato_restore)  è uguale a  (state1)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (spento)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3')  è uguale a  (spento)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (3)) )  e  
( negazione di ((lo stato di 'self')  è uguale a  (state1)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se la macro  MainClass_C1_macrova_M3 ( con argomento_a2   uguale a c270x ,argomento_a3   uguale a c180x ,argomento_a8   uguale a spento ,argomento_a9   uguale a AC ,argomento_a1   uguale a AC  e argomento_a10   uguale a AC )  non  è  diverso da spento /*40,*/  e  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  /*53,*/ 3 /*34,*/ e  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ , assegna alla macro il valore c180x
        if db((db((db(not db(not db(db(self.macroMainclass_c1_macrova_m3(GlobalEnumeration.ac,GlobalEnumeration.ac,GlobalEnumeration.c270x,GlobalEnumeration.c180x,GlobalEnumeration.spento,GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c180x
        #  /*46,*/ assegna alla macro il valore c180x
        return GlobalEnumeration.c180x
    
    @srf_value_macro("macroMainclass_c1_macrova_m8")
    def macroMainclass_c1_macrova_m8(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  commento: {54,} 10 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 1153 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  /*54,*/ 10 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 1153 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  /*54,*/ 10 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 1153 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_restoreva_rv1_restore)  è maggiore di  (10)) )  e  ( negazione di ((mainclass_c1_contatore_co1)  è uguale a  (1153)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è maggiore di  (10))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_restoreva_rv1_restore)  è maggiore di  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (1153))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (1153)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (c180x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  /*54,*/ 10 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 1153 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c180x , assegna alla macro il valore  True
        if db((db((db(not db(self.get_mainclass_c1_restoreva_rv1_restore() > 10, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 1153, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroMainclass_c1_macrova_m9")
    def macroMainclass_c1_macrova_m9(self, argomento_a10, argomento_a4, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} o  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} e  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore spento
        
         commento: {46,} assegna alla macro il valore spento commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ o  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ o  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (stato_restore)  è uguale a  (state1) )  e  
( negazione di ((lo stato di 'self')  è uguale a  (state1)) )""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ o  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore spento
        if db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.spento
        #  /*46,*/ assegna alla macro il valore spento
        return GlobalEnumeration.spento
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm1(self, notifying_process, argomento_ave4, argomento_ave5, argomento_ave7):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm1', argomento_ave4=argomento_ave4, argomento_ave5=argomento_ave5, argomento_ave7=argomento_ave7)
    
    def eventMainclass_c1_command_comm10(self, notifying_process, argomento_ave2, argomento_ave3):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm10', argomento_ave2=argomento_ave2, argomento_ave3=argomento_ave3)
    
    def eventMainclass_c1_command_comm3(self, notifying_process, argomento_ave1, argomento_ave10, argomento_ave6):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm3', argomento_ave1=argomento_ave1, argomento_ave10=argomento_ave10, argomento_ave6=argomento_ave6)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c1_prev(self.get_mainclass_c1_previousco_c1())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())

