# Codice del modello 'TestCase10', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_restoreva_rv1(False)
        self.set_mainclass_c1_restoreva_rv2(0)
        self.set_mainclass_c1_variabile_v10(0)
        self.set_mainclass_c1_variabile_v3(GlobalEnumeration.c270xx)
        self.set_mainclass_c1_variabile_v5(False)
        self.set_mainclass_c1_variabile_v8(GlobalEnumeration.c180x)
        self.set_mainclass_c1_variabile_v9(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm1'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm1',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm1',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm10'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm10',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm10',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p4):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p4(mainclass_c1_parametro_p4)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(43000)
        self.set_mainclass_c1_restoreti_ti1_restore(43000)
        self.set_mainclass_c1_restoreti_ti2(3000)
        self.set_mainclass_c1_restoreti_ti2_restore(3000)
        self.set_mainclass_c1_timer_t3(5403000)
        self.set_mainclass_c1_timer_t4(240000)
        self.set_mainclass_c1_timer_t7(3215000)
        self.set_mainclass_c1_timer_t8(4215000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_timer_t3,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t7,self.mainclass_c1_timer_t8,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p4(self, mainclass_c1_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4",mainclass_c1_parametro_p4)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)

    def set_mainclass_c1_comando_c8(self, mainclass_c1_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c8",mainclass_c1_comando_c8)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c6")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")


    # setters for state variables
    def set_mainclass_c1_previousco_c1_prev(self, mainclass_c1_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev",mainclass_c1_previousco_c1_prev)
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousva_pv1(self, mainclass_c1_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1",mainclass_c1_previousva_pv1)
    def set_mainclass_c1_previousva_pv1_prev(self, mainclass_c1_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev",mainclass_c1_previousva_pv1_prev)
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v3(self, mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3",mainclass_c1_variabile_v3)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
    def get_mainclass_c1_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev")

    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1")

    def get_mainclass_c1_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev")

    def get_mainclass_c1_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1")

    def get_mainclass_c1_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1_restore")

    def get_mainclass_c1_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2")

    def get_mainclass_c1_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2_restore")

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

    def get_mainclass_c1_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8")

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

    def set_mainclass_c1_timer_t3(self, timerDuration):
        self.mainclass_c1_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t3", self.memory)

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)

    def set_mainclass_c1_timer_t7(self, timerDuration):
        self.mainclass_c1_timer_t7 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t7", self.memory)

    def set_mainclass_c1_timer_t8(self, timerDuration):
        self.mainclass_c1_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t8", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_restoreti_ti2(self):
        return self.mainclass_c1_restoreti_ti2

    def get_mainclass_c1_restoreti_ti2_restore(self):
        return self.mainclass_c1_restoreti_ti2_restore

    def get_mainclass_c1_timer_t3(self):
        return self.mainclass_c1_timer_t3

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t7(self):
        return self.mainclass_c1_timer_t7

    def get_mainclass_c1_timer_t8(self):
        return self.mainclass_c1_timer_t8


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1



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

        self.set_mainclass_c1_previousco_c1_prev(True)
        self.set_mainclass_c1_previousco_c2_prev(False)
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
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {35,}  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC commento: {36,} o  se il timer MainClass_C1_timer_T3 è scaduto, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
        
         ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore avviox commento: {67,}
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 13403 commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da avviox commento: {36,} e  se il timer MainClass_C1_timer_T8 è attivo, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
        
        
          se il controllo ConsDef è uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x commento: {36,} o  se il timer MainClass_C1_timer_T3 è scaduto,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore c270x commento: {67,}
        
           
          se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox, commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore  True 
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C8 il valore c270x
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1

 ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore avviox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (ac)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*67,*/


 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 13403 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da avviox /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/


 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 13403 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da avviox /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co1)  è uguale a  (13403)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t3' è inattivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (13403))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (13403)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (mainclass_c1_controllo_c7)  è uguale a  (False) )  e  ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) ) )  e  ( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (avviox)) ) )  e  
( il timer 'mainclass_c1_timer_t8' è attivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_controllo_c7)  è uguale a  (False) )  e  ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) ) )  e  ( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (avviox)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c7)  è uguale a  (False) )  e  ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (avviox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_variabile_v3)  è uguale a  (c270x) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270x)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*67,*/

   
  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  True 

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/

   
  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac)) )  e  
( (mainclass_c1_variabile_v8)  è uguale a  (avviox) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (avviox)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1
        #   ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore avviox
        if db((db(not db(not db(self.get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co1().decrementa()
        else:
            self.set_mainclass_c1_variabile_v8(GlobalEnumeration.avviox)
        #  /*67,*/
        #   /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 13403 /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da avviox /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1
        if db((db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 13403, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db((db((db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.avviox, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_mainclass_c1_contatore_co1().decrementa()
        else:
            self.get_mainclass_c1_contatore_co1().decrementa()
        #  se il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore c270x
        if db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v3(GlobalEnumeration.c270x)
        #  /*67,*/
        #     
        #    se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox, /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore  True 
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C8 il valore c270x
        if db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.avviox, di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_comando_c10(True)
        else:
            self.set_mainclass_c1_comando_c8(GlobalEnumeration.c270x)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox commento: {34,} o  se il parametro MainClass_C1_parametro_P4 è  diverso da AC commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 14 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 14 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T7 è disattivo commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 13154, Verifica che   commento: {48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  commento: {53,} 110
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*34,*/ o  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T7 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 13154, Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*34,*/ o  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T7 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 13154, Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*34,*/ o  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*34,*/ o  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V8 è  uguale a avviox""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P4 è  diverso da AC /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 è  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T7 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 13154, Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T7 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 13154""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 14""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T7 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 13154""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T7 è disattivo /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a avviox""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T7 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V8 è  uguale a avviox""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 13154""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 110""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (110)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db(self.get_mainclass_c1_contatore_co1().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() == 13154, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 110, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, argomento_ave2, argomento_ave3, argomento_ave6, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
         commento: {61,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 11 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False  commento: {39,} , Tutte le seguenti { 
          se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  commento: {54,} 5 commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   commento: {47,48,49,50,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
         commento: {104,} e  che   l'argomento argomento_ave9 non  sia  diverso da  False  commento: {,} 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T7 non sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia scaduto
        
        
         } Verifica che   commento: {47,48,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
         commento: {104,} e  che   l'argomento argomento_ave9 sia  diverso da  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C6 sia  diverso da AC
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  commento: {54,} 7
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T8 non sia scaduto
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da  False 
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  diverso da  commento: {56,} 5
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/ , Tutte le seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia scaduto


 } Verifica che   /*47,48,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True , Tutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/ , Tutte le seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia scaduto


 } Verifica che   /*47,48,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/ , Tutte le seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia scaduto


 } Verifica che   /*47,48,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/ , Tutte le seguenti { 
  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C7 è  uguale a  True  e  se l'argomento argomento_ave8 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C7 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC, Verifica che   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5 /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T7 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave9 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V3 sia  diverso da c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T7 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave9 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C6 sia  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v9)  è maggiore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T8 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(not db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave9 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave9 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() > 7, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t8().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v10() == 5, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m4")
    def macroMainclass_c1_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 15 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC, Almeno una delle seguenti { 
         commento: {62,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 11 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False , Almeno una delle seguenti { 
         commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T4 non è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T3 è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {61,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 14 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 123, Tutte le seguenti { 
         commento: {62,} commento: {36,}  se il timer MainClass_C1_timer_T7 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 12215 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 114, Almeno una delle seguenti { 
          se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 1103 commento: {36,} e  se il timer MainClass_C1_timer_T7 è scaduto commento: {36,} e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   commento: {47,48,49,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T7 non sia attivo
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  minore di  commento: {55,} 13215
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  commento: {54,} 12
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P4 sia  uguale a AC
        
        
         } Verifica che   commento: {47,48,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  uguale a  commento: {53,} 1
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox
        
        
         } Verifica che   commento: {47,48,49,}  commento: {,}  il timer MainClass_C1_timer_T7 sia attivo
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 sia disattivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC, Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  uguale a  /*53,*/ 1


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox


 } Verifica che   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T7 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC, Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  uguale a  /*53,*/ 1


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P4 non è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  diverso da c270x""", [
                            DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 non è  diverso da c270x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 non è  diverso da c270x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  uguale a  /*53,*/ 1


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  uguale a  /*53,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V5 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC


 } Verifica che   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  uguale a  /*53,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T4 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T4 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a c270x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P4 è  diverso da AC""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T3 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 è  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C6 non è  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V3 è  uguale a c270x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123, Tutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 14""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P4 non è  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P4 non è  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (123)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*36,*/  se il timer MainClass_C1_timer_T7 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T7 è attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C6 è  diverso da AC /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C6 è  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 12215""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (12215)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 114""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (114)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo, Verifica che   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1103""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T7 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T7 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  minore di  /*55,*/ 13215""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  maggiore di  /*54,*/ 12""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (12)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P4 sia  uguale a AC""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  uguale a  /*53,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V3 non sia  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a avviox""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T7 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T7 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T7 sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,48,49,*/  /*,*/  il timer MainClass_C1_timer_T7 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P4 non sia  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_contatore_co1().get_valore() > 15, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db((db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db(self.get_mainclass_c1_contatore_co1().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 123, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 12215, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 114, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() < 1103, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() < 13215, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a10, argomento_a2, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  commento: {56,} 152 commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo e  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a c120x  e argomento_a3   uguale a AC )  non  è  uguale a  True  commento: {40,}  o  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a AC  e argomento_a3   uguale a AC )  non  è  uguale a  True  commento: {40,}  , assegna alla macro il valore avviox
        
         commento: {46,} assegna alla macro il valore avviox commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 152 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo e  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a c120x  e argomento_a3   uguale a AC )  non  è  uguale a  True  /*40,*/  o  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a AC  e argomento_a3   uguale a AC )  non  è  uguale a  True  /*40,*/  , assegna alla macro il valore avviox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 152 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo e  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a c120x  e argomento_a3   uguale a AC )  non  è  uguale a  True  /*40,*/  o  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a AC  e argomento_a3   uguale a AC )  non  è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_contatore_co1)  è uguale a  (152)) ) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (ac))) ) )  o  
( ( il timer 'mainclass_c1_restoreti_ti1_restore' è attivo )  e  
( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (True)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_contatore_co1)  è uguale a  (152)) ) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (ac))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_contatore_co1)  è uguale a  (152)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (152))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (152)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c6)  è uguale a  (ac)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_restoreti_ti1_restore' è attivo )  e  
( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (True)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7'"""),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m7'"""),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se il controllo ConsDef è uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  diverso da  /*56,*/ 152 /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da AC /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo e  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a c120x  e argomento_a3   uguale a AC )  non  è  uguale a  True  /*40,*/  o  se la macro  MainClass_C1_macrova_M7 ( con argomento_a9   uguale a AC  e argomento_a3   uguale a AC )  non  è  uguale a  True  /*40,*/  , assegna alla macro il valore avviox
        if db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 152, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c6() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(db(self.macroMainclass_c1_macrova_m7(GlobalEnumeration.ac,GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(db(self.macroMainclass_c1_macrova_m7(GlobalEnumeration.ac,GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.avviox
        #  /*46,*/ assegna alla macro il valore avviox
        return GlobalEnumeration.avviox
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a3, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm1(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm1')
    
    def eventMainclass_c1_command_comm10(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm10')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm2(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm2')
    
    def eventMainclass_c1_command_comm6(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm6')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c1_prev(self.get_mainclass_c1_previousco_c1())
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())

