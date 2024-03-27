from enum import IntEnum
from GlobalEnums import GlobalEnumeration
from core.lds.acc_class import ParamRecord, srf_value_macro
from core.lds.process_impl import ProcessImpl
from core.runtime.scheduler import ERROR, DISCARDED
from core.runtime.utils import all_notempty
from core.lds.Timer import Timer
from core.lds.Counter import Counter
import Stazione.LdV.Logica.Enumeratives
import os
from core.debugger.debinfo import (  # noqa: F401
    DIBoolExpr, DIExpr, DIStatement, EventDebInfo, TransPhase,
    TransDebInfo, CdLDebInfo, DIVerifyMacro, DIEffectMacro, DIValueMacro,
    add_instance_deb_info, db)

class LDV_MainClass_C1(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(LDV_MainClass_C1, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_ldv_mainclass_c1_variabile_v3(0)
        self.set_ldv_mainclass_c1_variabile_v8(False)
        self.set_ldv_mainclass_c1_variabile_v9(GlobalEnumeration.c270)

        self._expected_commands_map = {
            Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of LDV_MainClass_C1
        if self.is_triggered('eventLdv_mainclass_c1_command_comm1DaSender59cfb9d8'):
            IS_STATE_ACCEPTING_eventLdv_mainclass_c1_command_comm1DaSender59cfb9d8 = false # no state is accepting this command!
            self.set_man_cmd_response('eventLdv_mainclass_c1_command_comm1DaSender59cfb9d8',self.ManCmdResponse.BLOCKED if IS_STATE_ACCEPTING_eventLdv_mainclass_c1_command_comm1DaSender59cfb9d8 else self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventLdv_mainclass_c1_command_comm1DaSender59cfb9d8',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventLdv_mainclass_c1_command_comm2'):
            IS_STATE_ACCEPTING_eventLdv_mainclass_c1_command_comm2 = false # no state is accepting this command!
            self.set_man_cmd_response('eventLdv_mainclass_c1_command_comm2',self.ManCmdResponse.BLOCKED if IS_STATE_ACCEPTING_eventLdv_mainclass_c1_command_comm2 else self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventLdv_mainclass_c1_command_comm2',self.ManCmdResponse.NOOP)


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
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_0 = 2

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, consdef, ldv_mainclass_c1_parametro_p1, ldv_mainclass_c1_parametro_p7, ldv_mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_consdef(consdef)
        self.set_ldv_mainclass_c1_parametro_p1(ldv_mainclass_c1_parametro_p1)
        self.set_ldv_mainclass_c1_parametro_p7(ldv_mainclass_c1_parametro_p7)
        self.set_ldv_mainclass_c1_parametro_p9(ldv_mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_ldv_mainclass_c1_timer_t3(10000)

        self.timers = [self.ldv_mainclass_c1_timer_t3,]

        # initialize the counters
        self.set_ldv_mainclass_c1_contatore_co1(0)
        self.set_ldv_mainclass_c1_contatore_co4(0)
        self.set_ldv_mainclass_c1_contatore_co6(0)
        self.set_ldv_mainclass_c1_contatore_co7(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_consdef(self, consdef):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"consdef",consdef)

    def set_ldv_mainclass_c1_parametro_p1(self, ldv_mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_parametro_p1",ldv_mainclass_c1_parametro_p1)

    def set_ldv_mainclass_c1_parametro_p7(self, ldv_mainclass_c1_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_parametro_p7",ldv_mainclass_c1_parametro_p7)

    def set_ldv_mainclass_c1_parametro_p9(self, ldv_mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_parametro_p9",ldv_mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_ldv_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_parametro_p1")

    def get_ldv_mainclass_c1_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_parametro_p7")

    def get_ldv_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_ldv_mainclass_c1_output_1(self, ldv_mainclass_c1_output_1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_output_1",ldv_mainclass_c1_output_1)


    # getters for controlli dal piazzale

    # setters for state variables
    def set_ldv_mainclass_c1_variabile_v3(self, ldv_mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_variabile_v3",ldv_mainclass_c1_variabile_v3)
    def set_ldv_mainclass_c1_variabile_v8(self, ldv_mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_variabile_v8",ldv_mainclass_c1_variabile_v8)
    def set_ldv_mainclass_c1_variabile_v9(self, ldv_mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_variabile_v9",ldv_mainclass_c1_variabile_v9)

    # getters for state variables
    def get_ldv_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_variabile_v3")

    def get_ldv_mainclass_c1_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_variabile_v8")

    def get_ldv_mainclass_c1_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"ldv_mainclass_c1_variabile_v9")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_ldv_mainclass_c1_timer_t3(self, timerDuration):
        self.ldv_mainclass_c1_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "ldv_mainclass_c1_timer_t3", self.memory)


    # getters for timers
    def get_ldv_mainclass_c1_timer_t3(self):
        return self.ldv_mainclass_c1_timer_t3


    # setters for counters
    def set_ldv_mainclass_c1_contatore_co1(self, counterInitValue):
        self.ldv_mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "ldv_mainclass_c1_contatore_co1", self.memory)

    def set_ldv_mainclass_c1_contatore_co4(self, counterInitValue):
        self.ldv_mainclass_c1_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "ldv_mainclass_c1_contatore_co4", self.memory)

    def set_ldv_mainclass_c1_contatore_co6(self, counterInitValue):
        self.ldv_mainclass_c1_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "ldv_mainclass_c1_contatore_co6", self.memory)

    def set_ldv_mainclass_c1_contatore_co7(self, counterInitValue):
        self.ldv_mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "ldv_mainclass_c1_contatore_co7", self.memory)


    # getters for counters
    def get_ldv_mainclass_c1_contatore_co1(self):
        return self.ldv_mainclass_c1_contatore_co1

    def get_ldv_mainclass_c1_contatore_co4(self):
        return self.ldv_mainclass_c1_contatore_co4

    def get_ldv_mainclass_c1_contatore_co6(self):
        return self.ldv_mainclass_c1_contatore_co6

    def get_ldv_mainclass_c1_contatore_co7(self):
        return self.ldv_mainclass_c1_contatore_co7



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
                    DIBoolExpr("""NAryLogicOP (AND)\nVerifica che il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a False""", [
                    DIBoolExpr("""EqualImpl\nche il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a False""", [
                    ]),#0
                    ]),#2
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.StatoIniziale, Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1,Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[2], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1,Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1,
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
            self.set_fsmState(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()


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
            if self.is_current_state(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1):
                if(self.guard_NOMINAL_ACTUATION_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state1_000()
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
    
    def guard_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {
        	Verifica che il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a False
        }
        """
        return db((db(self.get_ldv_mainclass_c1_parametro_p1() == False, self.dbs[2].subs[0])), self.dbs[2])
    
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
    
    def effect_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {
         	Nessuno
         }
        """
        pass
    
    # effect macros
    def macroLdv_mainclass_c1_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer LDV_MainClass_C1_timer_T3 è scaduto e  se il parametro ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è scaduto commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo, commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        
         ,altrimenti  commento: {70,}Incrementa il contatore LDV_MainClass_C1_contatore_Co6
        
        
          se il parametro ConsDef è uguale a FALSE ,  Applica gli effetti
               della macro LDV_MainClass_C1_macroef_M3   commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True 
        
        
          se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co7 commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 1452 commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P9 è  uguale a RossoGialloGiallo commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V3 non è  uguale a  commento: {53,} 10, commento: {72,}Azzera il contatore LDV_MainClass_C1_contatore_Co6
        
           
         commento: {38,}  se il contatore LDV_MainClass_C1_contatore_Co6 non è  maggiore di  commento: {54,} contatore LDV_MainClass_C1_contatore_Co7 commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  uguale a  commento: {53,} contatore LDV_MainClass_C1_contatore_Co1 o  se il parametro ConsDef è uguale a FALSE , commento: {68,}Attiva il timer LDV_MainClass_C1_timer_T3
        
         ,altrimenti   Applica gli effetti
               della macro LDV_MainClass_C1_macroef_M7  commento: {73,}
        
        
         commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} contatore LDV_MainClass_C1_contatore_Co4 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True ,  Applica gli effetti
               della macro LDV_MainClass_C1_macroef_M8  commento: {73,}
        
         ,altrimenti  commento: {70,}Incrementa il contatore LDV_MainClass_C1_contatore_Co6
        
        
        
        }
        """
        def populate_macroLdv_mainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto e  se il parametro ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è scaduto /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo, /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx

 ,altrimenti  /*70,*/Incrementa il contatore LDV_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto e  se il parametro ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è scaduto /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'ldv_mainclass_c1_timer_t3' è scaduto )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di (il timer 'ldv_mainclass_c1_timer_t3' è scaduto) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'ldv_mainclass_c1_timer_t3' è scaduto )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'ldv_mainclass_c1_timer_t3' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'ldv_mainclass_c1_timer_t3' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il parametro ConsDef è uguale a FALSE ,  Applica gli effetti
       della macro LDV_MainClass_C1_macroef_M3   /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro LDV_MainClass_C1_macroef_M3"""),#1
                            ]),#1
                            DIStatement("""ITStatement\nse il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co7 /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 1452 /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 è  uguale a RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V3 non è  uguale a  /*53,*/ 10, /*72,*/Azzera il contatore LDV_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co7 /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 1452 /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 è  uguale a RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V3 non è  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co6)  è minore di  (ldv_mainclass_c1_contatore_co7)) ) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co7)  è uguale a  (1452)) ) )  o  
( (ldv_mainclass_c1_parametro_p9)  è uguale a  (rossogiallogiallo) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co6)  è minore di  (ldv_mainclass_c1_contatore_co7)) ) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co7)  è uguale a  (1452)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co6)  è minore di  (ldv_mainclass_c1_contatore_co7)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co6)  è minore di  (ldv_mainclass_c1_contatore_co7))""", [
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_contatore_co6)  è minore di  (ldv_mainclass_c1_contatore_co7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co7)  è uguale a  (1452))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co7)  è uguale a  (1452)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p9)  è uguale a  (rossogiallogiallo)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v3)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v3)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7 /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co1 o  se il parametro ConsDef è uguale a FALSE , /*68,*/Attiva il timer LDV_MainClass_C1_timer_T3

 ,altrimenti   Applica gli effetti
       della macro LDV_MainClass_C1_macroef_M7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7 /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co1 o  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((ldv_mainclass_c1_contatore_co6)  è maggiore di  (ldv_mainclass_c1_contatore_co7)) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co6)  è uguale a  (ldv_mainclass_c1_contatore_co1)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co6)  è maggiore di  (ldv_mainclass_c1_contatore_co7))""", [
                            DIBoolExpr("""GreaterThanImpl\n(ldv_mainclass_c1_contatore_co6)  è maggiore di  (ldv_mainclass_c1_contatore_co7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co6)  è uguale a  (ldv_mainclass_c1_contatore_co1))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co6)  è uguale a  (ldv_mainclass_c1_contatore_co1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro LDV_MainClass_C1_macroef_M7"""),#1
                            ]),#3
                            DIStatement("""ITEStatementImpl\n/*73,*/


 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co4 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True ,  Applica gli effetti
       della macro LDV_MainClass_C1_macroef_M8  /*73,*/

 ,altrimenti  /*70,*/Incrementa il contatore LDV_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co4 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((ldv_mainclass_c1_contatore_co1)  è uguale a  (ldv_mainclass_c1_contatore_co4)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((ldv_mainclass_c1_contatore_co1)  è uguale a  (ldv_mainclass_c1_contatore_co4)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True)) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co1)  è uguale a  (ldv_mainclass_c1_contatore_co4))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co1)  è uguale a  (ldv_mainclass_c1_contatore_co4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (ldv_mainclass_c1_parametro_p1)  è uguale a  (True) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro LDV_MainClass_C1_macroef_M8"""),#1
                            ]),#4
                ])

        populate_macroLdv_mainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto e  se il parametro ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è scaduto /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo, /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        #   ,altrimenti  /*70,*/Incrementa il contatore LDV_MainClass_C1_contatore_Co6
        if db((db((db((db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_ldv_mainclass_c1_variabile_v9(GlobalEnumeration.c270xx)
        else:
            self.get_ldv_mainclass_c1_contatore_co6().incrementa()
        #  se il parametro ConsDef è uguale a FALSE ,  Applica gli effetti
        #         della macro LDV_MainClass_C1_macroef_M3   /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True
        if db(self.get_consdef() == False, di_ctx.subs[1].subs[0]):
            self.macroLdv_mainclass_c1_macroef_m3(di_ctx.subs[1].subs[1])
        else:
            self.set_ldv_mainclass_c1_variabile_v8(True)
        #  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co7 /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 1452 /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 è  uguale a RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V3 non è  uguale a  /*53,*/ 10, /*72,*/Azzera il contatore LDV_MainClass_C1_contatore_Co6
        if db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() < self.get_ldv_mainclass_c1_contatore_co7().get_valore(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_contatore_co7().get_valore() == 1452, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_ldv_mainclass_c1_parametro_p9() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_variabile_v3() == 10, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_ldv_mainclass_c1_contatore_co6().resetta()
        #  /*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7 /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co1 o  se il parametro ConsDef è uguale a FALSE , /*68,*/Attiva il timer LDV_MainClass_C1_timer_T3
        #   ,altrimenti   Applica gli effetti
        #         della macro LDV_MainClass_C1_macroef_M7
        if db((db((db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() > self.get_ldv_mainclass_c1_contatore_co7().get_valore(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() == self.get_ldv_mainclass_c1_contatore_co1().get_valore(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_ldv_mainclass_c1_timer_t3().attiva()
        else:
            self.macroLdv_mainclass_c1_macroef_m7(di_ctx.subs[3].subs[1])
        #  /*73,*/
        #   /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co4 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True ,  Applica gli effetti
        #         della macro LDV_MainClass_C1_macroef_M8  /*73,*/
        #   ,altrimenti  /*70,*/Incrementa il contatore LDV_MainClass_C1_contatore_Co6
        if db((db((db((db((db(not db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_contatore_co1().get_valore() == self.get_ldv_mainclass_c1_contatore_co4().get_valore(), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[4].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.macroLdv_mainclass_c1_macroef_m8(di_ctx.subs[4].subs[1])
        else:
            self.get_ldv_mainclass_c1_contatore_co6().incrementa()
    
    def macroLdv_mainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        {  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE , commento: {71,}Decrementa il contatore LDV_MainClass_C1_contatore_Co6
        
           
         commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  False , commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        
           
          se il parametro ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True 
        
         ,altrimenti  commento: {68,}Attiva il timer LDV_MainClass_C1_timer_T3
        
        
        
        }
        """
        def populate_macroLdv_mainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE , /*71,*/Decrementa il contatore LDV_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  False , /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx""", [
                            DIBoolExpr("""EqualImpl\nil parametro LDV_MainClass_C1_parametro_P1 è  uguale a  False""", [
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\nse il parametro ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True 

 ,altrimenti  /*68,*/Attiva il timer LDV_MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il parametro ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'ldv_mainclass_c1_timer_t3' è inattivo) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'ldv_mainclass_c1_timer_t3' è inattivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'ldv_mainclass_c1_timer_t3' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroLdv_mainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE , /*71,*/Decrementa il contatore LDV_MainClass_C1_contatore_Co6
        if db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_ldv_mainclass_c1_contatore_co6().decrementa()
        #  /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  False , /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        if db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[1].subs[0]):
            self.set_ldv_mainclass_c1_variabile_v9(GlobalEnumeration.c270xx)
        #  se il parametro ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  True 
        #   ,altrimenti  /*68,*/Attiva il timer LDV_MainClass_C1_timer_T3
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_ldv_mainclass_c1_variabile_v8(True)
        else:
            self.get_ldv_mainclass_c1_timer_t3().attiva()
    
    def macroLdv_mainclass_c1_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {37,}  se la variabile LDV_MainClass_C1_variabile_V3 è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V3 non è  minore di  commento: {55,} 8 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef è uguale a FALSE , commento: {68,}Attiva il timer LDV_MainClass_C1_timer_T3
        
           
          se il parametro ConsDef è uguale a FALSE  commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True , commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        
         ,altrimenti  commento: {70,}Incrementa il contatore LDV_MainClass_C1_contatore_Co6
        
        
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 è scaduto commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P7 è  minore di  commento: {55,} 10 commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx, commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  False 
        
           
        
        }
        """
        def populate_macroLdv_mainclass_c1_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*37,*/  se la variabile LDV_MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 8 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef è uguale a FALSE , /*68,*/Attiva il timer LDV_MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile LDV_MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 8 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((ldv_mainclass_c1_variabile_v3)  è uguale a  (9)) )  o  
( negazione di ((ldv_mainclass_c1_variabile_v3)  è minore di  (8)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((ldv_mainclass_c1_variabile_v3)  è uguale a  (9)) )  o  
( negazione di ((ldv_mainclass_c1_variabile_v3)  è minore di  (8)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v3)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v3)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v3)  è minore di  (8))""", [
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_variabile_v3)  è minore di  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il parametro ConsDef è uguale a FALSE  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True , /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx

 ,altrimenti  /*70,*/Incrementa il contatore LDV_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il parametro ConsDef è uguale a FALSE  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((ldv_mainclass_c1_variabile_v8)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P7 è  minore di  /*55,*/ 10 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx, /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P7 è  minore di  /*55,*/ 10 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'ldv_mainclass_c1_timer_t3' è scaduto )  e  ( (ldv_mainclass_c1_parametro_p7)  è minore di  (10) ) )  e  
( (ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'ldv_mainclass_c1_timer_t3' è scaduto )  e  ( (ldv_mainclass_c1_parametro_p7)  è minore di  (10) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_parametro_p7)  è minore di  (10)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroLdv_mainclass_c1_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*37,*/  se la variabile LDV_MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 8 o  se il parametro ConsDef  è  uguale a FALSE  o  se il parametro ConsDef è uguale a FALSE , /*68,*/Attiva il timer LDV_MainClass_C1_timer_T3
        if db((db((db((db(not db(self.get_ldv_mainclass_c1_variabile_v3() == 9, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_variabile_v3() < 8, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_ldv_mainclass_c1_timer_t3().attiva()
        #  se il parametro ConsDef è uguale a FALSE  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True , /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        #   ,altrimenti  /*70,*/Incrementa il contatore LDV_MainClass_C1_contatore_Co6
        if db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0]) or db(not db(not db(self.get_ldv_mainclass_c1_variabile_v8() == True, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_ldv_mainclass_c1_variabile_v9(GlobalEnumeration.c270xx)
        else:
            self.get_ldv_mainclass_c1_contatore_co6().incrementa()
        #  /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P7 è  minore di  /*55,*/ 10 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx, /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V8 il valore  False
        if db((db(self.get_fsmState() == Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0]) or db((db((db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_parametro_p7() < 10, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v9() == GlobalEnumeration.c270xx, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_ldv_mainclass_c1_variabile_v8(False)
    
    def macroLdv_mainclass_c1_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il parametro ConsDef è uguale a FALSE  commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V9 non è  uguale a c270xx commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} contatore LDV_MainClass_C1_contatore_Co1, commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
        
         ,altrimenti  commento: {67,} Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        
        
         commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  True  commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  commento: {53,} 2 commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False , commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
        
         ,altrimenti   Applica gli effetti
               della macro LDV_MainClass_C1_macroef_M3   commento: {73,}
        
        
          se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 11 commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 è scaduto commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 2 commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE , commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
        
           
         commento: {38,}  se il contatore LDV_MainClass_C1_contatore_Co6 è  uguale a  commento: {53,} contatore LDV_MainClass_C1_contatore_Co7, commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
        
           
        
        }
        """
        def populate_macroLdv_mainclass_c1_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il parametro ConsDef è uguale a FALSE  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V9 non è  uguale a c270xx /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co1, /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3

 ,altrimenti  /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il parametro ConsDef è uguale a FALSE  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V9 non è  uguale a c270xx /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di ((ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((ldv_mainclass_c1_contatore_co4)  è uguale a  (ldv_mainclass_c1_contatore_co1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co4)  è uguale a  (ldv_mainclass_c1_contatore_co1))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co4)  è uguale a  (ldv_mainclass_c1_contatore_co1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  True  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False , /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3

 ,altrimenti   Applica gli effetti
       della macro LDV_MainClass_C1_macroef_M3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  True  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True)) )  e  
( (ldv_mainclass_c1_variabile_v3)  è uguale a  (2) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v3)  è uguale a  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro LDV_MainClass_C1_macroef_M3"""),#1
                            ]),#1
                            DIStatement("""ITStatement\n/*73,*/


  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE , /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co6)  è minore di  (11)) ) )  o  
( ( ( il timer 'ldv_mainclass_c1_timer_t3' è scaduto )  e  ( negazione di ((ldv_mainclass_c1_parametro_p7)  è maggiore di  (2)) ) )  e  
( il timer 'ldv_mainclass_c1_timer_t3' è inattivo ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di ((ldv_mainclass_c1_contatore_co6)  è minore di  (11)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co6)  è minore di  (11))""", [
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_contatore_co6)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'ldv_mainclass_c1_timer_t3' è scaduto )  e  ( negazione di ((ldv_mainclass_c1_parametro_p7)  è maggiore di  (2)) ) )  e  
( il timer 'ldv_mainclass_c1_timer_t3' è inattivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'ldv_mainclass_c1_timer_t3' è scaduto )  e  ( negazione di ((ldv_mainclass_c1_parametro_p7)  è maggiore di  (2)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p7)  è maggiore di  (2))""", [
                            DIBoolExpr("""GreaterThanImpl\n(ldv_mainclass_c1_parametro_p7)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co7, /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3""", [
                            DIBoolExpr("""EqualImpl\nil contatore LDV_MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            ]),#0
                            ]),#3
                ])

        populate_macroLdv_mainclass_c1_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  se il parametro ConsDef è uguale a FALSE  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V9 non è  uguale a c270xx /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co1, /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3
        #   ,altrimenti  /*67,*/ Assegna alla variabile LDV_MainClass_C1_variabile_V9 il valore c270xx
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_variabile_v9() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_ldv_mainclass_c1_contatore_co4().get_valore() == self.get_ldv_mainclass_c1_contatore_co1().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_ldv_mainclass_c1_timer_t3().disattiva()
        else:
            self.set_ldv_mainclass_c1_variabile_v9(GlobalEnumeration.c270xx)
        #  /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  True  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 2 /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False , /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3
        #   ,altrimenti   Applica gli effetti
        #         della macro LDV_MainClass_C1_macroef_M3
        if db((db((db(not db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v3() == 2, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_ldv_mainclass_c1_timer_t3().disattiva()
        else:
            self.macroLdv_mainclass_c1_macroef_m3(di_ctx.subs[1].subs[1])
        #  /*73,*/
        #    se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 2 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE , /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() < 11, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db((db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_parametro_p7() > 2, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_ldv_mainclass_c1_timer_t3().disattiva()
        #  /*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ contatore LDV_MainClass_C1_contatore_Co7, /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3
        if db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() == self.get_ldv_mainclass_c1_contatore_co7().get_valore(), di_ctx.subs[3].subs[0]):
            self.get_ldv_mainclass_c1_timer_t3().disattiva()
    
    def macroLdv_mainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il parametro ConsDef è uguale a FALSE  commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 1215, commento: {69,}Disattiva il timer LDV_MainClass_C1_timer_T3
        
           
        
        }
        """
        def populate_macroLdv_mainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1215, /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1215""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co7)  è uguale a  (1215)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLdv_mainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 1215, /*69,*/Disattiva il timer LDV_MainClass_C1_timer_T3
        if db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_contatore_co7().get_valore() == 1215, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_ldv_mainclass_c1_timer_t3().disattiva()
    
    # verify macros
    @srf_value_macro("macroLdv_mainclass_c1_macrove_m10")
    def macroLdv_mainclass_c1_macrove_m10(self, argomento_ave1, argomento_ave10, argomento_ave4, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  commento: {39,}  commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  commento: {56,} 10 commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 111 e  se l'argomento argomento_ave4 non  è  uguale a  True  commento: {39,} , Verifica che   commento: {47,50,52,}  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
         commento: {104,} o  che   l'argomento argomento_ave1 sia  diverso da  True  commento: {,} 
         commento: {104,} o  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  commento: {55,} 4
         commento: {104,} e  che  commento: {37,}  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
         commento: {104,} e  che   l'argomento argomento_ave1 non  sia  diverso da  False  commento: {39,} 
         commento: {104,} o  che   l'argomento argomento_ave1 non  sia  uguale a  True  commento: {39,} 
        
        
        }
        """
        def populate_macroLdv_mainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  /*39,*/  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  /*56,*/ 10 /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 111 e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Verifica che   /*47,50,52,*/  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  /*39,*/  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  /*56,*/ 10 /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 111 e  se l'argomento argomento_ave4 non  è  uguale a  True  /*39,*/ , Verifica che   /*47,50,52,*/  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  /*39,*/  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  /*56,*/ 10 /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 111 e  se l'argomento argomento_ave4 non  è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  /*39,*/  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  /*56,*/ 10 /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 111""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False  /*39,*/  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer LDV_MainClass_C1_timer_T3 non è disattivo e  se l'argomento argomento_ave1 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer LDV_MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile LDV_MainClass_C1_variabile_V3 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v3)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v3)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore LDV_MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 111""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,52,*/  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ o  che   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,52,*/  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,52,*/  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che   l'argomento argomento_ave1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,50,52,*/  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*37,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_variabile_v3)  è minore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLdv_mainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave1 == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_ldv_mainclass_c1_variabile_v3() == 10, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_contatore_co4().get_valore() == 111, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(argomento_ave1 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_ldv_mainclass_c1_variabile_v3() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(argomento_ave1 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(argomento_ave1 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroLdv_mainclass_c1_macrove_m2")
    def macroLdv_mainclass_c1_macrove_m2(self, argomento_ave1, argomento_ave10, argomento_ave3, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è attivo commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se l'argomento argomento_ave5 è  diverso da avvio commento: {39,}  commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 non è scaduto, Almeno una delle seguenti { 
         commento: {63,} commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  commento: {55,} 4 commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è disattivo commento: {38,} o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co1 commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE , Solo una delle seguenti { 
         commento: {63,} commento: {36,}  se il timer LDV_MainClass_C1_timer_T3 è scaduto commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  commento: {56,} contatore LDV_MainClass_C1_contatore_Co7 commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  commento: {53,} 8, Solo una delle seguenti { 
         commento: {63,} commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  commento: {39,}  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo commento: {39,} , Solo una delle seguenti { 
         commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  commento: {53,} 1 commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   commento: {47,49,51,}  commento: {,}  il timer LDV_MainClass_C1_timer_T3 non sia attivo
         commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  commento: {56,} 140
         commento: {104,} e  che  commento: {36,}  il timer LDV_MainClass_C1_timer_T3 sia attivo
        
        
         } Verifica che   commento: {47,52,}   l'argomento argomento_ave8 non  sia  diverso da  False  commento: {,} 
         commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 
        
        
         } Verifica che   commento: {47,49,50,51,}  commento: {,}  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
         commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
         commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 non sia attivo
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  commento: {55,} 121
        
        
         } Verifica che   commento: {49,50,51,}  commento: {,}  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
         commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  commento: {56,} 1152
         commento: {104,} o  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia scaduto
         commento: {104,} e  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  commento: {54,} 13
         commento: {104,} o  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co4
        
        
         } Verifica che   commento: {47,49,50,52,}   l'argomento argomento_ave3 sia  uguale a  False  commento: {,} 
         commento: {104,} e  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 non sia disattivo
         commento: {104,} o  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
         commento: {104,} e  che  commento: {36,}  il timer LDV_MainClass_C1_timer_T3 non sia scaduto
         commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  True 
        
        
        }
        """
        def populate_macroLdv_mainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se l'argomento argomento_ave5 è  diverso da avvio /*39,*/  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co1 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 } Verifica che   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  /*55,*/ 121


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 1152
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia scaduto
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co4


 } Verifica che   /*47,49,50,52,*/   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se l'argomento argomento_ave5 è  diverso da avvio /*39,*/  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co1 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 } Verifica che   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  /*55,*/ 121


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 1152
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia scaduto
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co4


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se l'argomento argomento_ave5 è  diverso da avvio /*39,*/  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo o  se l'argomento argomento_ave5 è  diverso da avvio""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDV_MainClass_C1_timer_T3 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDV_MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave5 è  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDV_MainClass_C1_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co1 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 } Verifica che   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  /*55,*/ 121


 } Verifica che   /*49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 1152
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia scaduto
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co4


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co1 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE , Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 } Verifica che   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  /*55,*/ 121


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co1 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo /*38,*/ o  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil parametro LDV_MainClass_C1_parametro_P1 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P7 non è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_parametro_p7)  è minore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer LDV_MainClass_C1_timer_T3 è disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  e  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nla variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 } Verifica che   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  /*55,*/ 121


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 } Verifica che   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer LDV_MainClass_C1_timer_T3 è scaduto /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer LDV_MainClass_C1_timer_T3 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore LDV_MainClass_C1_contatore_Co4 è  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co4)  è uguale a  (ldv_mainclass_c1_contatore_co7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile LDV_MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 } Verifica che   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False  /*39,*/  e  se l'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False  e  se l'argomento argomento_ave8 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave6 non  è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False  o  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1 /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nil parametro LDV_MainClass_C1_parametro_P7 è  uguale a  /*53,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile LDV_MainClass_C1_variabile_V8 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,51,*/  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 140""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co6)  è uguale a  (140))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co6)  è uguale a  (140)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,52,*/   l'argomento argomento_ave8 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  /*55,*/ 121""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  minore di  /*55,*/ 121""", [
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_contatore_co6)  è minore di  (121)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 1152
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia scaduto
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 1152
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia scaduto
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 1152""", [
                            DIBoolExpr("""EqualImpl\nche   /*49,50,51,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 sia  uguale a variabile LDV_MainClass_C1_variabile_V9""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co1 sia  diverso da  /*56,*/ 1152""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co1)  è uguale a  (1152)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia scaduto
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""GreaterThanImpl\n(ldv_mainclass_c1_contatore_co6)  è maggiore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co4""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,52,*/   l'argomento argomento_ave3 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,52,*/   l'argomento argomento_ave3 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False 
 /*104,*/ e  che  /*36,*/  il timer LDV_MainClass_C1_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer LDV_MainClass_C1_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroLdv_mainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(self.get_fsmState() == Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave5 == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_ldv_mainclass_c1_parametro_p7() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() < self.get_ldv_mainclass_c1_contatore_co1().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_ldv_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_contatore_co4().get_valore() == self.get_ldv_mainclass_c1_contatore_co7().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v3() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(not db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave6 == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_ldv_mainclass_c1_parametro_p7() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_ldv_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() == 140, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(not db(not db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(not db(self.get_ldv_mainclass_c1_variabile_v9() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_ldv_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() < 121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_ldv_mainclass_c1_variabile_v9() == self.get_ldv_mainclass_c1_variabile_v9(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_contatore_co1().get_valore() == 1152, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() < self.get_ldv_mainclass_c1_contatore_co4().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(argomento_ave3 == False, di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_ldv_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroLdv_mainclass_c1_macrove_m4")
    def macroLdv_mainclass_c1_macrove_m4(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave6, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {38,}  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  commento: {55,} contatore LDV_MainClass_C1_contatore_Co7 commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  False , Almeno una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx commento: {39,} , Almeno una delle seguenti { 
         commento: {61,}  se il parametro ConsDef è uguale a FALSE  commento: {38,} e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  commento: {55,} 143 o  se il parametro ConsDef è uguale a FALSE  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  commento: {54,} 9, Tutte le seguenti { 
         commento: {62,}  se il parametro ConsDef è uguale a FALSE  commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo commento: {37,} e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  commento: {39,} , Almeno una delle seguenti { 
         commento: {62,}  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  commento: {40,}  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx commento: {39,}  commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  commento: {54,} 2, Almeno una delle seguenti { 
         commento: {62,}  se il parametro ConsDef è uguale a FALSE  commento: {34,} e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo commento: {37,} o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  commento: {36,} e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 10, Almeno una delle seguenti { 
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  commento: {36,} o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   commento: {47,51,}  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} 11
         commento: {104,} e  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  commento: {53,} 12
         commento: {104,} o  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  commento: {55,} 10
        
        
         } Verifica che   commento: {50,52,}   l'argomento argomento_ave1 sia  diverso da c270xx commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  commento: {53,} 8
        
        
         } Verifica che   commento: {47,}   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
        
        
         } Verifica che   commento: {47,}   il parametro ConsDef sia uguale a FALSE 
        
        
         } Verifica che   commento: {47,49,50,51,52,}   l'argomento argomento_ave10 sia  uguale a avvio commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia disattivo
         commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  commento: {54,} contatore LDV_MainClass_C1_contatore_Co7
         commento: {104,} e  che  commento: {,}  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  commento: {56,} 7
        
        
         } Verifica che   commento: {47,49,51,52,}   l'argomento argomento_ave10 non  sia  diverso da avvio commento: {,} 
         commento: {104,} e  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia attivo
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  commento: {53,} 121
        
        
         } Verifica che   commento: {49,50,51,52,}  commento: {,}  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx
         commento: {104,} o  che   l'argomento argomento_ave10 sia  diverso da avvio commento: {,} 
         commento: {104,} e  che  commento: {,}  il timer LDV_MainClass_C1_timer_T3 sia disattivo
         commento: {104,} o  che  commento: {,}  il contatore LDV_MainClass_C1_contatore_Co6 sia  diverso da  commento: {56,} 11
         commento: {104,} o  che  commento: {38,}  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  commento: {56,} contatore LDV_MainClass_C1_contatore_Co7
        
        
        }
        """
        def populate_macroLdv_mainclass_c1_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  False , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Almeno una delle seguenti { 
 /*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9, Tutte le seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave10 non  sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  /*53,*/ 121


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  diverso da  /*56,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  False , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Almeno una delle seguenti { 
 /*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9, Tutte le seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave10 non  sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  /*53,*/ 121


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co7 /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""LessThanImpl\nil contatore LDV_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Almeno una delle seguenti { 
 /*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9, Tutte le seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7


 } Verifica che   /*47,49,51,52,*/   l'argomento argomento_ave10 non  sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  /*53,*/ 121


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx /*39,*/ , Almeno una delle seguenti { 
 /*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9, Tutte le seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo e  se l'argomento argomento_ave1 non  è  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p9)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p9)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 non  è  uguale a c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9, Tutte le seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9, Tutte le seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo o  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143 o  se il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore LDV_MainClass_C1_contatore_Co6 non è  minore di  /*55,*/ 143""", [
                            DIBoolExpr("""LessThanImpl\n(ldv_mainclass_c1_contatore_co6)  è minore di  (143)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef è uguale a FALSE  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer LDV_MainClass_C1_timer_T3 è disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile LDV_MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 9""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False  /*39,*/ , Almeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se l'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P9 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p9)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile LDV_MainClass_C1_variabile_V9 è  uguale a c270xx""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer LDV_MainClass_C1_timer_T3 è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx /*39,*/  /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False  /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  LDV_MainClass_C1_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a7   uguale a c180 ,argomento_a6   uguale a RossoGialloGiallo  e argomento_a8   uguale a RossoGialloGiallo )  non  è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroLdv_mainclass_c1_macrova_m1')  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroLdv_mainclass_c1_macrova_m1')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroLdv_mainclass_c1_macrova_m1'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P1 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True  e  se l'argomento argomento_ave1 è  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile LDV_MainClass_C1_variabile_V8 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave1 è  uguale a c270xx""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro LDV_MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 } Verifica che   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10, Almeno una delle seguenti { 
 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo /*37,*/ o  se la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P9 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p9)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p9)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False  /*36,*/ e  se il timer LDV_MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile LDV_MainClass_C1_variabile_V8 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDV_MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'ldv_mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""GreaterThanImpl\n(ldv_mainclass_c1_parametro_p7)  è maggiore di  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE , Verifica che   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto o  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE  /*36,*/ o  se il timer LDV_MainClass_C1_timer_T3 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True  o  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDV_MainClass_C1_parametro_P1 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer LDV_MainClass_C1_timer_T3 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12
 /*104,*/ o  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,51,*/  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ 11""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co4 sia  uguale a  /*53,*/ 12""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 sia  minore di  /*55,*/ 10""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,52,*/   l'argomento argomento_ave1 sia  diverso da c270xx""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V3 sia  uguale a  /*53,*/ 8""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,*/   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*47,*/   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio /*,*/ 
 /*104,*/ o  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,51,52,*/   l'argomento argomento_ave10 sia  uguale a avvio""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7
 /*104,*/ e  che  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False""", [
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  maggiore di  /*54,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile LDV_MainClass_C1_variabile_V8 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P1 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDV_MainClass_C1_parametro_P7 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_parametro_p7)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_parametro_p7)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,52,*/   l'argomento argomento_ave10 non  sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  /*53,*/ 121""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,52,*/   l'argomento argomento_ave10 non  sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,52,*/   l'argomento argomento_ave10 non  sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,51,52,*/   l'argomento argomento_ave10 non  sia  diverso da avvio""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave10)  è uguale a  (avvio))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co4 non sia  uguale a  /*53,*/ 121""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co4)  è uguale a  (121)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,52,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  diverso da  /*56,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,52,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,52,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,51,52,*/  /*,*/  la variabile LDV_MainClass_C1_variabile_V9 non sia  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_variabile_v9)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave10 sia  diverso da avvio /*,*/ 
 /*104,*/ e  che  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 sia  diverso da avvio""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (avvio)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer LDV_MainClass_C1_timer_T3 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore LDV_MainClass_C1_contatore_Co6 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co6)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore LDV_MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ contatore LDV_MainClass_C1_contatore_Co7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((ldv_mainclass_c1_contatore_co6)  è uguale a  (ldv_mainclass_c1_contatore_co7))""", [
                            DIBoolExpr("""EqualImpl\n(ldv_mainclass_c1_contatore_co6)  è uguale a  (ldv_mainclass_c1_contatore_co7)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroLdv_mainclass_c1_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() < self.get_ldv_mainclass_c1_contatore_co7().get_valore(), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_ldv_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(not db(self.get_ldv_mainclass_c1_parametro_p9() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave1 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() < 143, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v3() > 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_ldv_mainclass_c1_parametro_p9() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v9() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(not db(db(self.macroLdv_mainclass_c1_macrova_m1(True,GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.c180,GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_ldv_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(argomento_ave1 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_ldv_mainclass_c1_parametro_p7() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_ldv_mainclass_c1_parametro_p9() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_ldv_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_parametro_p7() > 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(self.get_fsmState() == Stazione.LdV.Logica.Enumeratives.LDV_MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_ldv_mainclass_c1_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_ldv_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_contatore_co4().get_valore() == 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_ldv_mainclass_c1_parametro_p7() < 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(argomento_ave1 == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v3() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(argomento_ave10 == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db((db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() > self.get_ldv_mainclass_c1_contatore_co7().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_ldv_mainclass_c1_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_ldv_mainclass_c1_parametro_p7() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(not db(argomento_ave10 == GlobalEnumeration.avvio, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_ldv_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_ldv_mainclass_c1_contatore_co4().get_valore() == 121, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(not db(self.get_ldv_mainclass_c1_variabile_v9() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(argomento_ave10 == GlobalEnumeration.avvio, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_ldv_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() == 11, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(not db(self.get_ldv_mainclass_c1_contatore_co6().get_valore() == self.get_ldv_mainclass_c1_contatore_co7().get_valore(), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroLdv_mainclass_c1_macrova_m1")
    def macroLdv_mainclass_c1_macrova_m1(self, argomento_a2, argomento_a6, argomento_a7, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroLdv_mainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroLdv_mainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroLdv_mainclass_c1_macrova_m7")
    def macroLdv_mainclass_c1_macrova_m7(self, argomento_a3, argomento_a5, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroLdv_mainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroLdv_mainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventLdv_mainclass_c1_command_comm1DaSender59cfb9d8(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventLdv_mainclass_c1_command_comm1DaSender59cfb9d8')
    
    def eventLdv_mainclass_c1_command_comm2(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventLdv_mainclass_c1_command_comm2')
    
    # for each automatic command, the corresponding method is created
    def eventLdv_mainclass_c1_command_comm8(self, notifying_process, argomento_ave6, argomento_ave8):
        notifying_process.response_notify_auto_cmd(self, 'eventLdv_mainclass_c1_command_comm8', argomento_ave6=argomento_ave6, argomento_ave8=argomento_ave8)
    

    def update_precedente(self):
        # update the variables with previous value
        pass

