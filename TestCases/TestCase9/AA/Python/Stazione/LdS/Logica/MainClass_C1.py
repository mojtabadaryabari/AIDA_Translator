# Codice del modello 'TestCase9', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_restoreva_rv1(GlobalEnumeration.spento)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.rossogiallox)
        self.set_mainclass_c1_restoreva_rv3(0)
        self.set_mainclass_c1_restoreva_rv4(GlobalEnumeration.spento)
        self.set_mainclass_c1_variabile_v10(False)
        self.set_mainclass_c1_variabile_v7(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm2DaSenderab077139'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm2DaSenderab077139',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm2DaSenderab077139',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm3DaSender2cbf5cfa'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm3DaSender2cbf5cfa',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm3DaSender2cbf5cfa',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm7'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p1, mainclass_c1_parametro_p5, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p1(mainclass_c1_parametro_p1)
        self.set_mainclass_c1_parametro_p5(mainclass_c1_parametro_p5)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(120000)
        self.set_mainclass_c1_restoreti_ti1_restore(120000)
        self.set_mainclass_c1_restoreti_ti2(23000)
        self.set_mainclass_c1_restoreti_ti2_restore(23000)
        self.set_mainclass_c1_timer_t4(11000)
        self.set_mainclass_c1_timer_t5(545000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t5,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)
        self.set_mainclass_c1_contatore_co10(0)
        self.set_mainclass_c1_contatore_co4(0)
        self.set_mainclass_c1_contatore_co7(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p1(self, mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1",mainclass_c1_parametro_p1)

    def set_mainclass_c1_parametro_p5(self, mainclass_c1_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5",mainclass_c1_parametro_p5)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1")

    def get_mainclass_c1_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p5")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)

    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)

    def set_mainclass_c1_comando_c6(self, mainclass_c1_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c6",mainclass_c1_comando_c6)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c2")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10")


    # setters for state variables
    def set_mainclass_c1_previousco_c10_prev(self, mainclass_c1_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev",mainclass_c1_previousco_c10_prev)
    def set_mainclass_c1_previousva_pv1(self, mainclass_c1_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1",mainclass_c1_previousva_pv1)
    def set_mainclass_c1_previousva_pv1_prev(self, mainclass_c1_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev",mainclass_c1_previousva_pv1_prev)
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_restoreva_rv4(self, mainclass_c1_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4",mainclass_c1_restoreva_rv4)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v7(self, mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7",mainclass_c1_variabile_v7)

    # getters for state variables
    def get_mainclass_c1_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev")

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

    def get_mainclass_c1_restoreva_rv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3")

    def get_mainclass_c1_restoreva_rv3_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3_restore")

    def get_mainclass_c1_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4")

    def get_mainclass_c1_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4_restore")

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

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

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)

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

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)

    def set_mainclass_c1_contatore_co10(self, counterInitValue):
        self.mainclass_c1_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co10", self.memory)

    def set_mainclass_c1_contatore_co4(self, counterInitValue):
        self.mainclass_c1_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co4", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1

    def get_mainclass_c1_contatore_co10(self):
        return self.mainclass_c1_contatore_co10

    def get_mainclass_c1_contatore_co4(self):
        return self.mainclass_c1_contatore_co4

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

        self.set_mainclass_c1_previousco_c10_prev(GlobalEnumeration.rossogialloverde)
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
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  commento: {53,} 13120, commento: {68,}Attiva il timer MainClass_C1_timer_T4
        
         ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True  commento: {67,}
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 13120, /*68,*/Attiva il timer MainClass_C1_timer_T4

 ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 13120""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (13120)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 13120, /*68,*/Attiva il timer MainClass_C1_timer_T4
        #   ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True
        if db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 13120, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t4().attiva()
        else:
            self.set_mainclass_c1_variabile_v10(True)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {35,}  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True , Almeno una delle seguenti { 
         commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180, Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, Almeno una delle seguenti { 
         commento: {63,} commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T4 non è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
         commento: {34,}  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  commento: {55,} 130 commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
        
        
         } Verifica che   commento: {47,49,51,}  commento: {,}  il timer MainClass_C1_timer_T5 sia scaduto
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  uguale a  commento: {53,} 133
        
        
         } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 11
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 non sia  diverso da c180
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True , Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 133


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  diverso da c180
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True , Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 133


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 non è  uguale a  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo


 } Verifica che   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 133


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V7 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P5 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T4 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P5 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox, Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  uguale a avviox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130 /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P5 è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P5 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V10 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 130""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10)  è minore di  (130)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P1 è  uguale a avviox""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V7 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V10 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 133""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,49,51,*/  /*,*/  il timer MainClass_C1_timer_T5 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 133""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 133""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  diverso da c180
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 11""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C9 non sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  diverso da c180
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P5 non sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p5() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p5() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db((db(not db(self.get_mainclass_c1_parametro_p5() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co10().get_valore() < 130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(not db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co7().get_valore() == 133, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_mainclass_c1_contatore_co7().get_valore() > 11, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.c180, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p5() == GlobalEnumeration.c180, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m5")
    def macroMainclass_c1_macrove_m5(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,}  se il controllo ConsDef è uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False , Tutte le seguenti { 
         commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 1212 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False , Almeno una delle seguenti { 
         commento: {63,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
         commento: {63,}  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  commento: {54,} 130 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
         commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 15345, Solo una delle seguenti { 
         commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 1312, Tutte le seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
         commento: {37,}  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   commento: {47,48,50,51,52,}   l'argomento argomento_ave2 sia  diverso da GialloaVerdea commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 1303
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  minore di  commento: {55,} 15
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co10 sia  uguale a  commento: {53,} 111203
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T4 non sia attivo
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  commento: {56,} 15
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
        
        
         } Verifica che   commento: {47,48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  commento: {53,} 1312
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T5 non sia scaduto
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True 
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 sia disattivo
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T5 non sia scaduto
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False , Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1212 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True 


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False , Tutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1212 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T4 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T4 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 15""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C9 non è  diverso da c180 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1212 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1212 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False , Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1212 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1212""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1212""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 


 } Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False , Solo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True , Solo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True""", [
                            DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co10 è  maggiore di  /*54,*/ 130""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C2 è  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 15345""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (15345)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P5 non è  diverso da c180 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P5 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 1312""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (1312)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 } Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Tutte le seguenti { 
 /*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto, Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V10 non è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave2 sia  diverso da GialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P5 sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1303""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10)  è minore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co10 sia  uguale a  /*53,*/ 111203""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (15))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloaVerdea""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C9 sia  uguale a c180""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  uguale a  /*53,*/ 1312""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (1312)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a avviox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C2 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T5 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T5 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() == 15, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_mainclass_c1_variabile_v7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co7().get_valore() == 1212, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co10().get_valore() > 130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() > 15345, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p5() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co10().get_valore() > 1312, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(argomento_ave2 == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p5() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() < 1303, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() < 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co10().get_valore() == 111203, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 1312, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v7() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t5().isScaduto(), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m2")
    def macroMainclass_c1_macrova_m2(self, argomento_a1, argomento_a4, argomento_a5, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  commento: {109,} e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a RossoGialloVerde commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  commento: {54,} 155 , assegna alla macro il valore c180
        
         commento: {46,} assegna alla macro il valore c180 commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m2_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*109,*/ e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a RossoGialloVerde /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 155 , assegna alla macro il valore c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*109,*/ e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a RossoGialloVerde /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 155""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (True)) )  e  ( negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde)) ) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è maggiore di  (155)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (True)) )  e  ( negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è maggiore di  (155))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co4)  è maggiore di  (155)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m2_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*109,*/ e  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a RossoGialloVerde /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  maggiore di  /*54,*/ 155 , assegna alla macro il valore c180
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co4().get_valore() > 155, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c180
        #  /*46,*/ assegna alla macro il valore c180
        return GlobalEnumeration.c180
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a5, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore avviox commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore avviox
        return GlobalEnumeration.avviox
    
    @srf_value_macro("macroMainclass_c1_macrova_m8")
    def macroMainclass_c1_macrova_m8(self, argomento_a10, argomento_a5, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C2 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  diverso da avviox commento: {110,} e  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde commento: {35,} e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  , assegna alla macro il valore c180
        
         commento: {46,} assegna alla macro il valore c180 commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da avviox /*110,*/ e  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  , assegna alla macro il valore c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da avviox /*110,*/ e  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_controllo_c2)  è uguale a  (False)) )  o  
( ( negazione di ((mainclass_c1_parametro_p1)  è uguale a  (avviox)) )  e  
( il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p1)  è uguale a  (avviox)) )  e  
( il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è uguale a  (avviox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde))) )  e  
( (mainclass_c1_controllo_c2)  è uguale a  (True) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C2 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da avviox /*110,*/ e  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da RossoGialloVerde /*35,*/ e  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  , assegna alla macro il valore c180
        if db((db((db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c180
        #  /*46,*/ assegna alla macro il valore c180
        return GlobalEnumeration.c180
    
    @srf_value_macro("macroMainclass_c1_macrova_m9")
    def macroMainclass_c1_macrova_m9(self, argomento_a10, argomento_a2, argomento_a3, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c180 commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c180
        return GlobalEnumeration.c180
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm2DaSenderab077139(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm2DaSenderab077139')
    
    def eventMainclass_c1_command_comm3DaSender2cbf5cfa(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm3DaSender2cbf5cfa')
    
    def eventMainclass_c1_command_comm7(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm7')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm6(self, notifying_process, argomento_ave4, argomento_ave5, argomento_ave6):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm6', argomento_ave4=argomento_ave4, argomento_ave5=argomento_ave5, argomento_ave6=argomento_ave6)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c10_prev(self.get_mainclass_c1_previousco_c10())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())

