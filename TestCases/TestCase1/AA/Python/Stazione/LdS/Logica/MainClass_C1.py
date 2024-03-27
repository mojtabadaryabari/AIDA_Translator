# Codice del modello 'TestCase1', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_previousva_pv3(False)
        self.set_mainclass_c1_restoreva_rv1(False)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.rossoverde)
        self.set_mainclass_c1_restoreva_rv3(False)
        self.set_mainclass_c1_variabile_v10(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm1DaSender1500ffbc'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm1DaSender1500ffbc',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm1DaSender1500ffbc',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm6'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm6',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm6',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p1, mainclass_c1_parametro_p3, mainclass_c1_parametro_p4, mainclass_c1_parametro_p6, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p1(mainclass_c1_parametro_p1)
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p4(mainclass_c1_parametro_p4)
        self.set_mainclass_c1_parametro_p6(mainclass_c1_parametro_p6)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(1000)
        self.set_mainclass_c1_restoreti_ti1_restore(1000)
        self.set_mainclass_c1_timer_t5(40000)
        self.set_mainclass_c1_timer_t7(55321000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_timer_t5,self.mainclass_c1_timer_t7,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)
        self.set_mainclass_c1_contatore_co10(0)
        self.set_mainclass_c1_contatore_co3(0)
        self.set_mainclass_c1_contatore_co4(0)
        self.set_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p1(self, mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1",mainclass_c1_parametro_p1)

    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p4(self, mainclass_c1_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4",mainclass_c1_parametro_p4)

    def set_mainclass_c1_parametro_p6(self, mainclass_c1_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6",mainclass_c1_parametro_p6)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1")

    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4")

    def get_mainclass_c1_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)

    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5")


    # setters for state variables
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c5_prev(self, mainclass_c1_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev",mainclass_c1_previousco_c5_prev)
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
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)

    # getters for state variables
    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev")

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

    def get_mainclass_c1_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2")

    def get_mainclass_c1_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2_restore")

    def get_mainclass_c1_restoreva_rv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3")

    def get_mainclass_c1_restoreva_rv3_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3_restore")

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_mainclass_c1_restoreti_ti1(self, timerDuration):
        self.mainclass_c1_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1", self.memory)

    def set_mainclass_c1_restoreti_ti1_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1_restore", self.memory)

    def set_mainclass_c1_timer_t5(self, timerDuration):
        self.mainclass_c1_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t5", self.memory)

    def set_mainclass_c1_timer_t7(self, timerDuration):
        self.mainclass_c1_timer_t7 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t7", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5

    def get_mainclass_c1_timer_t7(self):
        return self.mainclass_c1_timer_t7


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)

    def set_mainclass_c1_contatore_co10(self, counterInitValue):
        self.mainclass_c1_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co10", self.memory)

    def set_mainclass_c1_contatore_co3(self, counterInitValue):
        self.mainclass_c1_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co3", self.memory)

    def set_mainclass_c1_contatore_co4(self, counterInitValue):
        self.mainclass_c1_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co4", self.memory)

    def set_mainclass_c1_contatore_co9(self, counterInitValue):
        self.mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co9", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1

    def get_mainclass_c1_contatore_co10(self):
        return self.mainclass_c1_contatore_co10

    def get_mainclass_c1_contatore_co3(self):
        return self.mainclass_c1_contatore_co3

    def get_mainclass_c1_contatore_co4(self):
        return self.mainclass_c1_contatore_co4

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

        self.set_mainclass_c1_previousco_c2_prev(True)
        self.set_mainclass_c1_previousco_c5_prev(False)
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
    def macroMainclass_c1_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  minore di  commento: {55,} 7 commento: {36,} o  se il timer MainClass_C1_timer_T7 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  diverso da  commento: {56,} 115321, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 9
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  commento: {54,} 2 commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  minore di  commento: {55,} 1 commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  commento: {55,} 130, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
        
           
         commento: {34,}  se il parametro MainClass_C1_parametro_P4 è  diverso da RossoGialloGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  commento: {56,} 8 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 13 commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 11 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 134532, commento: {68,}Attiva il timer MainClass_C1_timer_T7
        
         ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 4 commento: {67,}
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 4, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 2
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 6
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  diverso da  /*56,*/ 115321, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  diverso da  /*56,*/ 115321""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_variabile_v10)  è minore di  (7) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v10)  è minore di  (7)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t7' è scaduto) )  e  
( negazione di ((mainclass_c1_contatore_co10)  è uguale a  (115321)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t7' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co10)  è uguale a  (115321))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (115321)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 2 /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 130, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 2 /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 130""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo) )  e  
( negazione di ((mainclass_c1_variabile_v10)  è maggiore di  (2)) ) )  o  
( (mainclass_c1_variabile_v10)  è minore di  (1) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo) )  e  
( negazione di ((mainclass_c1_variabile_v10)  è maggiore di  (2)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è maggiore di  (2))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v10)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v10)  è minore di  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è minore di  (130))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co4)  è minore di  (130)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P4 è  diverso da RossoGialloGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 8 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 11 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 134532, /*68,*/Attiva il timer MainClass_C1_timer_T7

 ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P4 è  diverso da RossoGialloGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 8 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 11 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 134532""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((mainclass_c1_parametro_p4)  è uguale a  (rossogiallogiallo)) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (8))) ) )  e  
( (mainclass_c1_contatore_co4)  è maggiore di  (13) ) )  o  
( ( il timer 'mainclass_c1_timer_t5' è inattivo )  e  
( (mainclass_c1_contatore_co4)  è uguale a  (11) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_parametro_p4)  è uguale a  (rossogiallogiallo)) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (8))) ) )  e  
( (mainclass_c1_contatore_co4)  è maggiore di  (13) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p4)  è uguale a  (rossogiallogiallo)) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (8))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (8)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (13)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t5' è inattivo )  e  
( (mainclass_c1_contatore_co4)  è uguale a  (11) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (11)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (134532)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*67,*/


 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 4, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 2

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/


 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  minore di  /*55,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  diverso da  /*56,*/ 115321, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 9
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v10() < 7, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() == 115321, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v10(9)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  maggiore di  /*54,*/ 2 /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  minore di  /*55,*/ 1 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 130, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
        if db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() > 2, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v10() < 1, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co4().get_valore() < 130, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.giallogiallo)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P4 è  diverso da RossoGialloGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P8 non è  diverso da  /*56,*/ 8 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 11 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 134532, /*68,*/Attiva il timer MainClass_C1_timer_T7
        #   ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 4
        if db((db((db((db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p8() == 8, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co4().get_valore() > 13, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co4().get_valore() == 11, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co10().get_valore() > 134532, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t7().attiva()
        else:
            self.set_mainclass_c1_variabile_v10(4)
        #  /*67,*/
        #   /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 4, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 2
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 6
        if db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v10() == 4, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v10(2)
        else:
            self.set_mainclass_c1_variabile_v10(6)
    
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer MainClass_C1_timer_T7 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 11, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 15 commento: {36,} e  se il timer MainClass_C1_timer_T5 non è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  maggiore di  commento: {54,} 4, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
        
           
         commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 114532, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 11, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 8

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t7' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (11)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 15 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  maggiore di  /*54,*/ 4, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 15 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (15)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t5' è attivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (15))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t5' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v10)  è maggiore di  (4)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 114532, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 114532""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co10)  è maggiore di  (114532))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (114532)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 11, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
        if db((db(not db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v10(8)
        else:
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.giallogiallo)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 15 /*36,*/ e  se il timer MainClass_C1_timer_T5 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  maggiore di  /*54,*/ 4, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore GialloGiallo
        if db((db((db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 15, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v10() > 4, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.giallogiallo)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 114532, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        if db((db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co10().get_valore() > 114532, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_comando_c1(GlobalEnumeration.c270xx)
    
    def macroMainclass_c1_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        {  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 7
        
         ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co4
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  commento: {56,} 7 e  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co1
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 1310 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  minore di  commento: {55,} 9 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {36,} o  se il timer MainClass_C1_timer_T5 è disattivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M4  commento: {73,}
        
           
          se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 7 commento: {36,} o  se il timer MainClass_C1_timer_T7 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T7 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T7 è disattivo, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 3
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        
        
          se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto, commento: {68,}Attiva il timer MainClass_C1_timer_T5
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 7

 ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co4""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co1

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (9)) ) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (9))) ) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (7))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (9)) ) )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (9))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (9)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (9)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (7)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 1310 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 1310 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (1310))) )  e  ( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)) ) )  e  
( negazione di ((mainclass_c1_parametro_p1)  è minore di  (9)) ) )  o  
( (mainclass_c1_controllo_c7)  è uguale a  (giallogiallo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (1310))) )  e  ( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)) ) )  e  
( negazione di ((mainclass_c1_parametro_p1)  è minore di  (9)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (1310))) )  e  ( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (1310)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (1310))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (1310)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è minore di  (9))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p1)  è minore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*73,*/

   
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T7 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T7 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T7 è disattivo, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 3

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T7 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T7 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T7 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_parametro_p3)  è maggiore di  (7)) ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t7' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di ((mainclass_c1_parametro_p3)  è maggiore di  (7)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è maggiore di  (7))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3)  è maggiore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t7' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t7' è attivo )  e  
( il timer 'mainclass_c1_timer_t7' è inattivo )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, /*68,*/Attiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (stato_restore)  è uguale a  (state1) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)) ) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (stato_restore)  è uguale a  (state1) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (stato_restore)  è uguale a  (state1) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t5' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 7
        #   ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co4
        if db(self.get_consdef() == False, di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v10(7)
        else:
            self.get_mainclass_c1_contatore_co4().incrementa()
        #  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da  /*56,*/ 7 e  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co1
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        if db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == 9, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == 9, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == 7, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co1().incrementa()
        else:
            self.set_mainclass_c1_comando_c1(GlobalEnumeration.c270xx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 1310 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T5 è disattivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M4
        if db((db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 1310, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p1() < 9, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.macroMainclass_c1_macroef_m4(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #     
        #    se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 7 /*36,*/ o  se il timer MainClass_C1_timer_T7 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T7 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T7 è disattivo, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 3
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore c270xx
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() > 7, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v10(3)
        else:
            self.set_mainclass_c1_comando_c1(GlobalEnumeration.c270xx)
        #  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, /*68,*/Attiva il timer MainClass_C1_timer_T5
        if db((db((db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[4].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.get_mainclass_c1_timer_t5().attiva()
    
    def macroMainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 1310,  Applica gli effetti
               della macro MainClass_C1_macroef_M2  commento: {73,}
        
           
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
        
           
          se il controllo ConsDef è uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T5
        
           
         commento: {38,}  se il contatore MainClass_C1_contatore_Co3 è  diverso da  commento: {56,} 1145 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 133210 commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a RossoGialloGiallo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 9, commento: {66,} Assegna al comando MainClass_C1_comando_C4 il valore  False 
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T5
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloGiallo, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co10
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 1310,  Applica gli effetti
       della macro MainClass_C1_macroef_M2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 1310""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((stato_restore)  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è minore di  (1310))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (1310)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M2"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*73,*/

   
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 8""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co3 è  diverso da  /*56,*/ 1145 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 133210 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a RossoGialloGiallo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co3 è  diverso da  /*56,*/ 1145 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 133210 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a RossoGialloGiallo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_contatore_co3)  è uguale a  (1145)) )  o  
( ( ( (mainclass_c1_contatore_co10)  è uguale a  (133210) )  e  ( (mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo) ) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è uguale a  (1145))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3)  è uguale a  (1145)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_contatore_co10)  è uguale a  (133210) )  e  ( (mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co10)  è uguale a  (133210) )  e  ( (mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (133210)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (9)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloGiallo, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co10""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 1310,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M2
        if db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 1310, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroMainclass_c1_macroef_m2(di_ctx.subs[0].subs[1])
        #  /*73,*/
        #     
        #   /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore 8
        if db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v10(8)
        #  se il controllo ConsDef è uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T5
        if db(self.get_consdef() == False, di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t5().disattiva()
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co3 è  diverso da  /*56,*/ 1145 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 133210 /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a RossoGialloGiallo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 9, /*66,*/ Assegna al comando MainClass_C1_comando_C4 il valore  False 
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T5
        if db((db((db(not db(self.get_mainclass_c1_contatore_co3().get_valore() == 1145, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_contatore_co10().get_valore() == 133210, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p3() < 9, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_comando_c4(False)
        else:
            self.get_mainclass_c1_timer_t5().disattiva()
        #  /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloGiallo, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co10
        if db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[4].subs[0].subs[0]), di_ctx.subs[4].subs[0]):
            self.get_mainclass_c1_contatore_co10().decrementa()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, argomento_ave10, argomento_ave5, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo commento: {36,} o  se il timer MainClass_C1_timer_T5 non è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T7 non è scaduto commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  commento: {56,} 3, Verifica che   commento: {47,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  minore di  commento: {55,} 3
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  minore di  commento: {55,} 9
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 sia  diverso da  commento: {56,} 9
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 3, Verifica che   /*47,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  minore di  /*55,*/ 9
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 3, Verifica che   /*47,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  minore di  /*55,*/ 9
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T5 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T5 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T5 non è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T7 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  minore di  /*55,*/ 9
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  minore di  /*55,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V10 sia  minore di  /*55,*/ 9""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == 3, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p8() < 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v10() < 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v10() == 9, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m6")
    def macroMainclass_c1_macrove_m6(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 140 commento: {34,} o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 1, Tutte le seguenti { 
         commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 9 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1545321, Almeno una delle seguenti { 
          se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 150 o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T7 non sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia disattivo
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T5 sia scaduto
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia attivo
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  maggiore di  commento: {54,} 10
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  diverso da  commento: {56,} 2
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 140 /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 1, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1545321, Almeno una delle seguenti { 
  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo


 } Verifica che   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 140 /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 1, Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1545321, Almeno una delle seguenti { 
  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo


 } Verifica che   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 140 /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 140 /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 140 /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 140""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 140""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (140)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v10)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3)  è maggiore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1545321, Almeno una delle seguenti { 
  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo


 } Verifica che   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1545321, Almeno una delle seguenti { 
  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1545321""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v10)  è minore di  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1545321""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1545321""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (150))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (150)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  maggiore di  /*54,*/ 10
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloGiallo""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V10 sia  maggiore di  /*54,*/ 10""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co10().get_valore() > 140, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p6() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v10() < 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() > 1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_variabile_v10() < 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() == 1545321, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 150, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v10() > 10, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v10() == 2, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m7")
    def macroMainclass_c1_macrove_m7(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        {  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  commento: {40,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  commento: {54,} 10 commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  minore di  commento: {55,} 2 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo commento: {36,} e  se il timer MainClass_C1_timer_T5 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  uguale a  commento: {53,} 10, Verifica che   commento: {47,48,49,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  minore di  commento: {55,} 9
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  maggiore di  commento: {54,} 6
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T7 sia attivo
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  diverso da  commento: {56,} 134
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 2 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  uguale a  /*53,*/ 10, Verifica che   /*47,48,49,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 9
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 134""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 2 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  uguale a  /*53,*/ 10, Verifica che   /*47,48,49,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 9
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 134""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 2 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True  /*40,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a c270xx  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro MainClass_C1_parametro_P3 è  maggiore di  /*54,*/ 10""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo /*36,*/ e  se il timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V10 è  uguale a  /*53,*/ 10""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 9
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 134""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 9
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 sia attivo""", [
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  maggiore di  /*54,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T7 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 134""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 134""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (134)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(not db(db(self.macroMainclass_c1_macrova_m4(GlobalEnumeration.rossoverde,GlobalEnumeration.c270xx,True,GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p3() > 10, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() < 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v10() == 10, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() < 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_parametro_p1() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 134, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m9")
    def macroMainclass_c1_macrove_m9(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave6, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo, Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia disattivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo, Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C7 è  uguale a GialloGiallo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a10, argomento_a5, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 135321 o  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a avanzamento  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  False  commento: {40,}  , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 135321 o  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a avanzamento  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  False  /*40,*/  , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 135321 o  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a avanzamento  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogiallogiallo)) )  e  
( (mainclass_c1_contatore_co1)  è minore di  (135321) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (135321)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4'"""),#0
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 135321 o  se la macro  MainClass_C1_macrova_M4 ( con argomento_a5   uguale a True ,argomento_a6   uguale a c120 ,argomento_a4   uguale a avanzamento  e argomento_a3   uguale a RossoVerde )  non  è  diverso da  False  /*40,*/  , assegna alla macro il valore  False
        if db((db((db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() < 135321, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(db(self.macroMainclass_c1_macrova_m4(GlobalEnumeration.rossoverde,GlobalEnumeration.avanzamento,True,GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroMainclass_c1_macrova_m4")
    def macroMainclass_c1_macrova_m4(self, argomento_a3, argomento_a4, argomento_a5, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T7 è attivo , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo , assegna alla macro il valore  True
        if db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm1DaSender1500ffbc(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm1DaSender1500ffbc')
    
    def eventMainclass_c1_command_comm6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm6')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c5_prev(self.get_mainclass_c1_previousco_c5())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())

