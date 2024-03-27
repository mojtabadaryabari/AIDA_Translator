# Codice del modello 'TestCase4', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_previousva_pv3(GlobalEnumeration.c270xx)
        self.set_mainclass_c1_previousva_pv4(False)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.gialloaverdea)
        self.set_mainclass_c1_restoreva_rv3(GlobalEnumeration.c180x)
        self.set_mainclass_c1_restoreva_rv4(0)
        self.set_mainclass_c1_restoreva_rv5(False)
        self.set_mainclass_c1_variabile_v4(GlobalEnumeration.c270x)
        self.set_mainclass_c1_variabile_v5(0)
        self.set_mainclass_c1_variabile_v6(False)
        self.set_mainclass_c1_variabile_v7(0)

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
    def init_configuration(self, mainclass_c1_parametro_p3):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(201000)
        self.set_mainclass_c1_restoreti_ti1_restore(201000)
        self.set_mainclass_c1_timer_t1(453000)
        self.set_mainclass_c1_timer_t6(44000)
        self.set_mainclass_c1_timer_t8(312000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_timer_t1,self.mainclass_c1_timer_t6,self.mainclass_c1_timer_t8,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co4(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c1")

    def get_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c2")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6")


    # setters for state variables
    def set_mainclass_c1_previousco_c6_prev(self, mainclass_c1_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev",mainclass_c1_previousco_c6_prev)
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
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_restoreva_rv4(self, mainclass_c1_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4",mainclass_c1_restoreva_rv4)
    def set_mainclass_c1_restoreva_rv5(self, mainclass_c1_restoreva_rv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5",mainclass_c1_restoreva_rv5)
    def set_mainclass_c1_variabile_v4(self, mainclass_c1_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4",mainclass_c1_variabile_v4)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v6(self, mainclass_c1_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6",mainclass_c1_variabile_v6)
    def set_mainclass_c1_variabile_v7(self, mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7",mainclass_c1_variabile_v7)

    # getters for state variables
    def get_mainclass_c1_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev")

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

    def get_mainclass_c1_restoreva_rv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5")

    def get_mainclass_c1_restoreva_rv5_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5_restore")

    def get_mainclass_c1_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

    def get_mainclass_c1_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6")

    def get_mainclass_c1_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_mainclass_c1_restoreti_ti1(self, timerDuration):
        self.mainclass_c1_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1", self.memory)

    def set_mainclass_c1_restoreti_ti1_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1_restore", self.memory)

    def set_mainclass_c1_timer_t1(self, timerDuration):
        self.mainclass_c1_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t1", self.memory)

    def set_mainclass_c1_timer_t6(self, timerDuration):
        self.mainclass_c1_timer_t6 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t6", self.memory)

    def set_mainclass_c1_timer_t8(self, timerDuration):
        self.mainclass_c1_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t8", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_timer_t1(self):
        return self.mainclass_c1_timer_t1

    def get_mainclass_c1_timer_t6(self):
        return self.mainclass_c1_timer_t6

    def get_mainclass_c1_timer_t8(self):
        return self.mainclass_c1_timer_t8


    # setters for counters
    def set_mainclass_c1_contatore_co4(self, counterInitValue):
        self.mainclass_c1_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co4", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co4(self):
        return self.mainclass_c1_contatore_co4



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

        self.set_mainclass_c1_previousco_c6_prev(True)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

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
        
        { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGialloVerde commento: {36,} e  se il timer MainClass_C1_timer_T1 non è disattivo commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  False , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co4
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T8 non è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGialloVerde commento: {37,} e  se la variabile MainClass_C1_variabile_V5 non è  minore di  commento: {55,} 9, commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        
           
         commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  uguale a  commento: {53,} 8 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  uguale a  commento: {53,} 10 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  commento: {36,} o  se il timer MainClass_C1_timer_T8 è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C3 il valore  True 
        
           
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} o  se la variabile MainClass_C1_variabile_V5 è  maggiore di  commento: {54,} 10 commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 123 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 11 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  commento: {54,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 5
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 7
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T1 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  False , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T1 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è attivo) )  o  
( ( negazione di (negazione di ((mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde))) )  e  
( negazione di (il timer 'mainclass_c1_timer_t1' è inattivo) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde))) )  e  
( negazione di (il timer 'mainclass_c1_timer_t1' è inattivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t1' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGialloVerde /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  minore di  /*55,*/ 9, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGialloVerde /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c8)  è uguale a  (rossogialloxverdex) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (False)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t8' è inattivo) ) )  e  ( negazione di ((mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde)) ) )  e  
( negazione di ((mainclass_c1_variabile_v5)  è minore di  (9)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (False)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t8' è inattivo) ) )  e  ( negazione di ((mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (False)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t8' è inattivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t8' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è minore di  (9))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v5)  è minore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P3 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a  /*53,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a  /*53,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*36,*/ o  se il timer MainClass_C1_timer_T8 è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P3 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a  /*53,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a  /*53,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*36,*/ o  se il timer MainClass_C1_timer_T8 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (True))) )  o  
( (mainclass_c1_variabile_v5)  è uguale a  (8) ) )  o  
( ( (mainclass_c1_variabile_v5)  è uguale a  (10) )  e  
( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (False)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (True))) )  o  
( (mainclass_c1_variabile_v5)  è uguale a  (8) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (8)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_variabile_v5)  è uguale a  (10) )  e  
( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (False)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (10)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  maggiore di  /*54,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 123 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore 5

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  maggiore di  /*54,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 123 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( (mainclass_c1_variabile_v5)  è maggiore di  (10) ) )  o  
( ( ( (mainclass_c1_contatore_co4)  è maggiore di  (123) )  e  ( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (11)) ) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è maggiore di  (15)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( (mainclass_c1_variabile_v5)  è maggiore di  (10) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v5)  è maggiore di  (10)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_contatore_co4)  è maggiore di  (123) )  e  ( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (11)) ) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è maggiore di  (15)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co4)  è maggiore di  (123) )  e  ( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (11)) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (123)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è maggiore di  (15))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (giallox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (giallox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  diverso da RossoGialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T1 non è disattivo /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da  False , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co4
        if db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co4().incrementa()
        #  /*35,*/  se il controllo MainClass_C1_controllo_C8 è  uguale a RossoGialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V4 è  diverso da RossoGialloVerde /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  minore di  /*55,*/ 9, /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        if db((db((db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_controllo_c9() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() < 9, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c5(GlobalEnumeration.rossogialloxverdex)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a  /*53,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  uguale a  /*53,*/ 10 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*36,*/ o  se il timer MainClass_C1_timer_T8 è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C3 il valore  True
        if db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p3() == True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v5() == 8, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_variabile_v5() == 10, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_comando_c3(True)
        #  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V5 è  maggiore di  /*54,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 123 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 11 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore 5
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore 7
        if db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v5() > 10, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_contatore_co4().get_valore() > 123, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 11, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co4().get_valore() > 15, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.giallox, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v5(5)
        else:
            self.set_mainclass_c1_variabile_v5(7)
    
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 110124 commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  minore di  commento: {55,} 7, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  False 
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co4
        
        
         commento: {36,}  se il timer MainClass_C1_timer_T8 è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V5 è  diverso da  commento: {56,} 5 commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  commento: {54,} 145, commento: {68,}Attiva il timer MainClass_C1_timer_T6
        
           
          se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , commento: {66,} Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 110124 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  minore di  /*55,*/ 7, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  False 

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 110124 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( (mainclass_c1_contatore_co4)  è maggiore di  (110124) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (110124)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è minore di  (7))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v5)  è minore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*36,*/  se il timer MainClass_C1_timer_T8 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  diverso da  /*56,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 145, /*68,*/Attiva il timer MainClass_C1_timer_T6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T8 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  diverso da  /*56,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 145""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'mainclass_c1_timer_t8' è inattivo )  o  
( ( ( (mainclass_c1_controllo_c9)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (True)) ) )  e  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (5)) ) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_controllo_c9)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (True)) ) )  e  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (5)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c9)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (True)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è maggiore di  (145))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (145)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto, /*69,*/Disattiva il timer MainClass_C1_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c1)  è uguale a  (True) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 110124 /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  minore di  /*55,*/ 7, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  False 
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co4
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() > 110124, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v5() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c10(False)
        else:
            self.get_mainclass_c1_contatore_co4().resetta()
        #  /*36,*/  se il timer MainClass_C1_timer_T8 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 è  diverso da  /*56,*/ 5 /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 145, /*68,*/Attiva il timer MainClass_C1_timer_T6
        if db((db((db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_controllo_c9() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() == 5, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co4().get_valore() > 145, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_timer_t6().attiva()
        #  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , /*66,*/ Assegna al comando MainClass_C1_comando_C5 il valore RossoGialloxVerdex
        if db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v6() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_comando_c5(GlobalEnumeration.rossogialloxverdex)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto, /*69,*/Disattiva il timer MainClass_C1_timer_T8
        if db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_mainclass_c1_timer_t8().disattiva()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {63,}  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True , Solo una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 150 commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   commento: {47,48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
        
        
         } Verifica che   commento: {47,48,49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 13
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia disattivo
        
        
         } Verifica che   commento: {47,48,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a  False 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da Giallox
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo


 } Verifica che   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Giallox""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo


 }""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox, Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 150""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (150))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (150)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P3 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C9 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da Giallox""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 è  diverso da Giallox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (giallox)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V4 non sia  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,48,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 13""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V4 sia  uguale a RossoGialloVerde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Giallox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da Giallox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (giallox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (giallox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 150, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.giallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db(self.get_mainclass_c1_contatore_co4().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_variabile_v4() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c2() == GlobalEnumeration.giallox, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m8")
    def macroMainclass_c1_macrove_m8(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
         commento: {62,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  commento: {54,} 124, Almeno una delle seguenti { 
         commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} 125, Solo una delle seguenti { 
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 12 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  minore di  commento: {55,} 7 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {47,48,49,51,}  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 15301
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia attivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
        
        
         } Verifica che   commento: {47,48,49,}  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia disattivo
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  commento: {54,} 11
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T8 non sia disattivo
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co4 sia  uguale a  commento: {53,} 1324
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 non sia scaduto
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  commento: {56,} 115
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T1 sia attivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 124, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 


 } Verifica che   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T8 non sia disattivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 1324
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 non sia scaduto
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 115
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T1 sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 124, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 


 } Verifica che   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T8 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 124, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 


 } Verifica che   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T8 non sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 124, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 124""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V6 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co4 è  maggiore di  /*54,*/ 124""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ 125""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (125)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 12""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V7 è  minore di  /*55,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C1 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,51,*/  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 15301""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T1 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t1' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  maggiore di  /*54,*/ 11""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 1324
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 non sia scaduto
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 115
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T1 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 1324
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 non sia scaduto
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 115""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 1324
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 1324""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co4 non sia  diverso da  /*56,*/ 115""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (115))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (115)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T1 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T1 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() > 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 125, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co4().get_valore() < 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v7() < 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() > 15301, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db((db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_mainclass_c1_contatore_co4().get_valore() == 1324, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t1().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 115, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t1().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m10")
    def macroMainclass_c1_macrova_m10(self, argomento_a10, argomento_a3, argomento_a4, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore Giallox commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore Giallox
        return GlobalEnumeration.giallox
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c6_prev(self.get_mainclass_c1_previousco_c6())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

