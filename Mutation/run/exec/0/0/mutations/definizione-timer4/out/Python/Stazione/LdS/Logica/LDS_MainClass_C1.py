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

class LDS_MainClass_C1(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(LDS_MainClass_C1, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_lds_mainclass_c1_variabile_v1(GlobalEnumeration.rosso)
        self.set_lds_mainclass_c1_variabile_v7(GlobalEnumeration.giallox)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of LDS_MainClass_C1
        if self.is_triggered('eventLds_mainclass_c1_command_comm10'):
            IS_STATE_ACCEPTING_eventLds_mainclass_c1_command_comm10 = false # no state is accepting this command!
            self.set_man_cmd_response('eventLds_mainclass_c1_command_comm10',self.ManCmdResponse.BLOCKED if IS_STATE_ACCEPTING_eventLds_mainclass_c1_command_comm10 else self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventLds_mainclass_c1_command_comm10',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventLds_mainclass_c1_command_comm11'):
            IS_STATE_ACCEPTING_eventLds_mainclass_c1_command_comm11 = false # no state is accepting this command!
            self.set_man_cmd_response('eventLds_mainclass_c1_command_comm11',self.ManCmdResponse.BLOCKED if IS_STATE_ACCEPTING_eventLds_mainclass_c1_command_comm11 else self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventLds_mainclass_c1_command_comm11',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventLds_mainclass_c1_command_comm9DaSender4db07f5e'):
            IS_STATE_ACCEPTING_eventLds_mainclass_c1_command_comm9DaSender4db07f5e = false # no state is accepting this command!
            self.set_man_cmd_response('eventLds_mainclass_c1_command_comm9DaSender4db07f5e',self.ManCmdResponse.BLOCKED if IS_STATE_ACCEPTING_eventLds_mainclass_c1_command_comm9DaSender4db07f5e else self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventLds_mainclass_c1_command_comm9DaSender4db07f5e',self.ManCmdResponse.NOOP)


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
    def init_configuration(self, consdef, lds_mainclass_c1_parametro_p2, lds_mainclass_c1_parametro_p3, lds_mainclass_c1_parametro_p5):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_consdef(consdef)
        self.set_lds_mainclass_c1_parametro_p2(lds_mainclass_c1_parametro_p2)
        self.set_lds_mainclass_c1_parametro_p3(lds_mainclass_c1_parametro_p3)
        self.set_lds_mainclass_c1_parametro_p5(lds_mainclass_c1_parametro_p5)

        # initialize the timers
        self.set_lds_mainclass_c1_timer_t1(3000)
        self.set_lds_mainclass_c1_timer_t2(3152000)
        self.set_lds_mainclass_c1_timer_t3(1000)
        self.set_lds_mainclass_c1_timer_t8(1430000)
        self.set_nabcc_mainclass_c1_timer_t5(31000)

        self.timers = [self.lds_mainclass_c1_timer_t1,self.lds_mainclass_c1_timer_t2,self.lds_mainclass_c1_timer_t3,self.lds_mainclass_c1_timer_t8,self.nabcc_mainclass_c1_timer_t5,]

        # initialize the counters
        self.set_lds_mainclass_c1_contatore_co5(0)
        self.set_lds_mainclass_c1_contatore_co6(0)
        self.set_lds_mainclass_c1_contatore_co8(0)
        self.set_lds_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_consdef(self, consdef):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"consdef",consdef)

    def set_lds_mainclass_c1_parametro_p2(self, lds_mainclass_c1_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_parametro_p2",lds_mainclass_c1_parametro_p2)

    def set_lds_mainclass_c1_parametro_p3(self, lds_mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_parametro_p3",lds_mainclass_c1_parametro_p3)

    def set_lds_mainclass_c1_parametro_p5(self, lds_mainclass_c1_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_parametro_p5",lds_mainclass_c1_parametro_p5)


    # getters for simple type parameters
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_lds_mainclass_c1_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_parametro_p2")

    def get_lds_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_parametro_p3")

    def get_lds_mainclass_c1_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_parametro_p5")


    # setters for comandi al piazzale
    def set_lds_mainclass_c1_comando_c4(self, lds_mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_comando_c4",lds_mainclass_c1_comando_c4)

    def set_lds_mainclass_c1_comando_c5(self, lds_mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_comando_c5",lds_mainclass_c1_comando_c5)

    def set_lds_mainclass_c1_comando_c7(self, lds_mainclass_c1_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_comando_c7",lds_mainclass_c1_comando_c7)


    # getters for controlli dal piazzale
    def get_lds_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_controllo_c10")

    def get_lds_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_controllo_c2")

    def get_lds_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_controllo_c6")

    def get_lds_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_controllo_c9")


    # setters for state variables
    def set_lds_mainclass_c1_variabile_v1(self, lds_mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_variabile_v1",lds_mainclass_c1_variabile_v1)
    def set_lds_mainclass_c1_variabile_v7(self, lds_mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_variabile_v7",lds_mainclass_c1_variabile_v7)

    # getters for state variables
    def get_lds_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_variabile_v1")

    def get_lds_mainclass_c1_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_mainclass_c1_variabile_v7")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_lds_mainclass_c1_timer_t1(self, timerDuration):
        self.lds_mainclass_c1_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_timer_t1", self.memory)

    def set_lds_mainclass_c1_timer_t2(self, timerDuration):
        self.lds_mainclass_c1_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_timer_t2", self.memory)

    def set_lds_mainclass_c1_timer_t3(self, timerDuration):
        self.lds_mainclass_c1_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_timer_t3", self.memory)

    def set_lds_mainclass_c1_timer_t8(self, timerDuration):
        self.lds_mainclass_c1_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_timer_t8", self.memory)

    def set_nabcc_mainclass_c1_timer_t5(self, timerDuration):
        self.nabcc_mainclass_c1_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "nabcc_mainclass_c1_timer_t5", self.memory)


    # getters for timers
    def get_lds_mainclass_c1_timer_t1(self):
        return self.lds_mainclass_c1_timer_t1

    def get_lds_mainclass_c1_timer_t2(self):
        return self.lds_mainclass_c1_timer_t2

    def get_lds_mainclass_c1_timer_t3(self):
        return self.lds_mainclass_c1_timer_t3

    def get_lds_mainclass_c1_timer_t8(self):
        return self.lds_mainclass_c1_timer_t8

    def get_nabcc_mainclass_c1_timer_t5(self):
        return self.nabcc_mainclass_c1_timer_t5


    # setters for counters
    def set_lds_mainclass_c1_contatore_co5(self, counterInitValue):
        self.lds_mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_contatore_co5", self.memory)

    def set_lds_mainclass_c1_contatore_co6(self, counterInitValue):
        self.lds_mainclass_c1_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_contatore_co6", self.memory)

    def set_lds_mainclass_c1_contatore_co8(self, counterInitValue):
        self.lds_mainclass_c1_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_contatore_co8", self.memory)

    def set_lds_mainclass_c1_contatore_co9(self, counterInitValue):
        self.lds_mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_mainclass_c1_contatore_co9", self.memory)


    # getters for counters
    def get_lds_mainclass_c1_contatore_co5(self):
        return self.lds_mainclass_c1_contatore_co5

    def get_lds_mainclass_c1_contatore_co6(self):
        return self.lds_mainclass_c1_contatore_co6

    def get_lds_mainclass_c1_contatore_co8(self):
        return self.lds_mainclass_c1_contatore_co8

    def get_lds_mainclass_c1_contatore_co9(self):
        return self.lds_mainclass_c1_contatore_co9



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
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1,
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1)
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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1)
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
        Azzera il contatore LDS_MainClass_C1_contatore_Co5
        }
        """
        #  Azzera il contatore LDS_MainClass_C1_contatore_Co5
        self.get_lds_mainclass_c1_contatore_co5().resetta()
    
    # effect macros
    def macroLds_mainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il parametro ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile LDS_MainClass_C1_variabile_V1 non è  diverso da c120 commento: {38,} e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 145,  commento: {67,} Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde commento: {67,}
        
         ,altrimenti  commento: {72,}Azzera il contatore LDS_MainClass_C1_contatore_Co5
        
        
          se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a Verde )   è  diverso da avanzamento commento: {40,}  commento: {38,} o  se il contatore LDS_MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6 commento: {38,} e  se il contatore LDS_MainClass_C1_contatore_Co8 non è  diverso da  commento: {56,} contatore LDS_MainClass_C1_contatore_Co8 o  se il parametro ConsDef  è  uguale a FALSE ,  commento: {67,} Assegna alla variabile LDS_MainClass_C1_variabile_V1 il valore c120 commento: {67,}
        
         ,altrimenti  commento: {66,} Assegna al comando LDS_MainClass_C1_comando_C5 il valore GialloxVerdex
        
        
         commento: {38,}  se il contatore LDS_MainClass_C1_contatore_Co9 è  diverso da  commento: {56,} contatore LDS_MainClass_C1_contatore_Co6 o  se il parametro ConsDef  è  uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE ,  commento: {67,} Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde commento: {67,}
        
         ,altrimenti  commento: {69,}Disattiva il timer LDS_MainClass_C1_timer_T8 
        
         commento: {34,}  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True  commento: {38,} e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 13430 commento: {37,} o  se la variabile LDS_MainClass_C1_variabile_V7 non è  diverso da RossoVerde e  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer LDS_MainClass_C1_timer_T3
        
         ,altrimenti  commento: {66,} Assegna al comando LDS_MainClass_C1_comando_C4 il valore  False 
        
        
          se il parametro ConsDef è uguale a FALSE  commento: {37,} e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a variabile LDS_MainClass_C1_variabile_V1, commento: {68,}Attiva il timer LDS_MainClass_C1_timer_T3
        
         ,altrimenti  commento: {68,}Attiva il timer LDS_MainClass_C1_timer_T3
        
        
        
        }
        """
        def populate_macroLds_mainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il parametro ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 non è  diverso da c120 /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 145,  /*67,*/ Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde /*67,*/

 ,altrimenti  /*72,*/Azzera il contatore LDS_MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 non è  diverso da c120 /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 145""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di (negazione di ((lds_mainclass_c1_variabile_v1)  è uguale a  (c120))) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lds_mainclass_c1_variabile_v1)  è uguale a  (c120)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_variabile_v1)  è uguale a  (c120))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_contatore_co9)  è uguale a  (145)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a Verde )   è  diverso da avanzamento /*40,*/  /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ contatore LDS_MainClass_C1_contatore_Co8 o  se il parametro ConsDef  è  uguale a FALSE ,  /*67,*/ Assegna alla variabile LDS_MainClass_C1_variabile_V1 il valore c120 /*67,*/

 ,altrimenti  /*66,*/ Assegna al comando LDS_MainClass_C1_comando_C5 il valore GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a Verde )   è  diverso da avanzamento /*40,*/  /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ contatore LDS_MainClass_C1_contatore_Co8 o  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((chiamata alla macro valorizzata 'macroLds_mainclass_c1_macrova_m10')  è uguale a  (avanzamento)) )  o  
( ( negazione di ((lds_mainclass_c1_contatore_co8)  è minore di  (lds_mainclass_c1_contatore_co6)) )  e  
( negazione di (negazione di ((lds_mainclass_c1_contatore_co8)  è uguale a  (lds_mainclass_c1_contatore_co8))) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroLds_mainclass_c1_macrova_m10')  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroLds_mainclass_c1_macrova_m10')  è uguale a  (avanzamento)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroLds_mainclass_c1_macrova_m10'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lds_mainclass_c1_contatore_co8)  è minore di  (lds_mainclass_c1_contatore_co6)) )  e  
( negazione di (negazione di ((lds_mainclass_c1_contatore_co8)  è uguale a  (lds_mainclass_c1_contatore_co8))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_contatore_co8)  è minore di  (lds_mainclass_c1_contatore_co6))""", [
                            DIBoolExpr("""LessThanImpl\n(lds_mainclass_c1_contatore_co8)  è minore di  (lds_mainclass_c1_contatore_co6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lds_mainclass_c1_contatore_co8)  è uguale a  (lds_mainclass_c1_contatore_co8)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_contatore_co8)  è uguale a  (lds_mainclass_c1_contatore_co8))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_contatore_co8)  è uguale a  (lds_mainclass_c1_contatore_co8)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ contatore LDS_MainClass_C1_contatore_Co6 o  se il parametro ConsDef  è  uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE ,  /*67,*/ Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde /*67,*/

 ,altrimenti  /*69,*/Disattiva il timer LDS_MainClass_C1_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ contatore LDS_MainClass_C1_contatore_Co6 o  se il parametro ConsDef  è  uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_contatore_co9)  è uguale a  (lds_mainclass_c1_contatore_co6))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_contatore_co9)  è uguale a  (lds_mainclass_c1_contatore_co6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True  /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 13430 /*37,*/ o  se la variabile LDS_MainClass_C1_variabile_V7 non è  diverso da RossoVerde e  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer LDS_MainClass_C1_timer_T3

 ,altrimenti  /*66,*/ Assegna al comando LDS_MainClass_C1_comando_C4 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True  /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 13430 /*37,*/ o  se la variabile LDS_MainClass_C1_variabile_V7 non è  diverso da RossoVerde e  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (lds_mainclass_c1_parametro_p5)  è uguale a  (True) )  e  
( (lds_mainclass_c1_contatore_co9)  è uguale a  (13430) ) )  o  
( ( ( negazione di (negazione di ((lds_mainclass_c1_variabile_v7)  è uguale a  (rossoverde))) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lds_mainclass_c1_parametro_p5)  è uguale a  (True) )  e  
( (lds_mainclass_c1_contatore_co9)  è uguale a  (13430) )""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_contatore_co9)  è uguale a  (13430)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((lds_mainclass_c1_variabile_v7)  è uguale a  (rossoverde))) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((lds_mainclass_c1_variabile_v7)  è uguale a  (rossoverde))) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lds_mainclass_c1_variabile_v7)  è uguale a  (rossoverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_variabile_v7)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v7)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\nse il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a variabile LDS_MainClass_C1_variabile_V1, /*68,*/Attiva il timer LDS_MainClass_C1_timer_T3

 ,altrimenti  /*68,*/Attiva il timer LDS_MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a variabile LDS_MainClass_C1_variabile_V1""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1)  è uguale a  (lds_mainclass_c1_variabile_v1)""", [
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroLds_mainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  se il parametro ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 non è  diverso da c120 /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 145,  /*67,*/ Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde /*67,*/
        #   ,altrimenti  /*72,*/Azzera il contatore LDS_MainClass_C1_contatore_Co5
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_lds_mainclass_c1_contatore_co9().get_valore() == 145, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_lds_mainclass_c1_variabile_v7(GlobalEnumeration.rossoverde)
        else:
            self.get_lds_mainclass_c1_contatore_co5().resetta()
        #  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a Verde )   è  diverso da avanzamento /*40,*/  /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co8 non è  diverso da  /*56,*/ contatore LDS_MainClass_C1_contatore_Co8 o  se il parametro ConsDef  è  uguale a FALSE ,  /*67,*/ Assegna alla variabile LDS_MainClass_C1_variabile_V1 il valore c120 /*67,*/
        #   ,altrimenti  /*66,*/ Assegna al comando LDS_MainClass_C1_comando_C5 il valore GialloxVerdex
        if db((db((db(not db(db(self.macroLds_mainclass_c1_macrova_m10(True,GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.avanzamento, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_lds_mainclass_c1_contatore_co8().get_valore() < self.get_lds_mainclass_c1_contatore_co6().get_valore(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_lds_mainclass_c1_contatore_co8().get_valore() == self.get_lds_mainclass_c1_contatore_co8().get_valore(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_lds_mainclass_c1_variabile_v1(GlobalEnumeration.c120)
        else:
            self.set_lds_mainclass_c1_comando_c5(GlobalEnumeration.gialloxverdex)
        #  /*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ contatore LDS_MainClass_C1_contatore_Co6 o  se il parametro ConsDef  è  uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE ,  /*67,*/ Assegna alla variabile LDS_MainClass_C1_variabile_V7 il valore RossoVerde /*67,*/
        #   ,altrimenti  /*69,*/Disattiva il timer LDS_MainClass_C1_timer_T8
        if db((db(not db(self.get_lds_mainclass_c1_contatore_co9().get_valore() == self.get_lds_mainclass_c1_contatore_co6().get_valore(), di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_lds_mainclass_c1_variabile_v7(GlobalEnumeration.rossoverde)
        else:
            self.get_lds_mainclass_c1_timer_t8().disattiva()
        #  /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True  /*38,*/ e  se il contatore LDS_MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 13430 /*37,*/ o  se la variabile LDS_MainClass_C1_variabile_V7 non è  diverso da RossoVerde e  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef è uguale a FALSE  o  se il parametro ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer LDS_MainClass_C1_timer_T3
        #   ,altrimenti  /*66,*/ Assegna al comando LDS_MainClass_C1_comando_C4 il valore  False
        if db((db((db((db(self.get_lds_mainclass_c1_parametro_p5() == True, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) and db(self.get_lds_mainclass_c1_contatore_co9().get_valore() == 13430, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_lds_mainclass_c1_variabile_v7() == GlobalEnumeration.rossoverde, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_lds_mainclass_c1_timer_t3().attiva()
        else:
            self.set_lds_mainclass_c1_comando_c4(False)
        #  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a variabile LDS_MainClass_C1_variabile_V1, /*68,*/Attiva il timer LDS_MainClass_C1_timer_T3
        #   ,altrimenti  /*68,*/Attiva il timer LDS_MainClass_C1_timer_T3
        if db((db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0]) and db(self.get_lds_mainclass_c1_variabile_v1() == self.get_lds_mainclass_c1_variabile_v1(), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.get_lds_mainclass_c1_timer_t3().attiva()
        else:
            self.get_lds_mainclass_c1_timer_t3().attiva()
    
    # verify macros
    @srf_value_macro("macroLds_mainclass_c1_macrove_m2")
    def macroLds_mainclass_c1_macrove_m2(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento commento: {40,}  commento: {36,} e  se il timer LDS_MainClass_C1_timer_T3 è disattivo commento: {36,} e  se il timer LDS_MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True , Almeno una delle seguenti { 
          se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento commento: {40,} , Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
         commento: {104,} e  che  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
         commento: {104,} o  che  commento: {,}  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6
         commento: {104,} o  che   il parametro ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {50,51,}  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
         commento: {104,} e  che  commento: {37,}  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120
         commento: {104,} o  che  commento: {,}  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  commento: {55,} 12
         commento: {104,} e  che  commento: {38,}  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  commento: {53,} contatore LDS_MainClass_C1_contatore_Co8
        
        
         } Verifica che   commento: {47,50,51,}   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  commento: {56,} 10
         commento: {104,} e  che  commento: {,}  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6
         commento: {104,} o  che  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120
         commento: {104,} e  che   il parametro ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P3 sia  uguale a  True 
        
        
        }
        """
        def populate_macroLds_mainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/  /*36,*/ e  se il timer LDS_MainClass_C1_timer_T3 è disattivo /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True , Almeno una delle seguenti { 
  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/ , Verifica che   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che   il parametro ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,51,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  /*53,*/ contatore LDS_MainClass_C1_contatore_Co8


 } Verifica che   /*47,50,51,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/  /*36,*/ e  se il timer LDS_MainClass_C1_timer_T3 è disattivo /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True , Almeno una delle seguenti { 
  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/ , Verifica che   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che   il parametro ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,51,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  /*53,*/ contatore LDS_MainClass_C1_contatore_Co8


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/  /*36,*/ e  se il timer LDS_MainClass_C1_timer_T3 è disattivo /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/  /*36,*/ e  se il timer LDS_MainClass_C1_timer_T3 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nla macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroLds_mainclass_c1_macrova_m10'"""),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer LDS_MainClass_C1_timer_T3 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDS_MainClass_C1_timer_T8 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t8' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True , Almeno una delle seguenti { 
  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/ , Verifica che   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che   il parametro ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,51,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  /*53,*/ contatore LDS_MainClass_C1_contatore_Co8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True , Almeno una delle seguenti { 
  se la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/ , Verifica che   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che   il parametro ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""EqualImpl\nil parametro LDS_MainClass_C1_parametro_P5 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento /*40,*/ , Verifica che   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che   il parametro ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nla macro  LDS_MainClass_C1_macrova_M10 ( con argomento_a10   uguale a True  e argomento_a9   uguale a GialloxVerdex )   è  uguale a avanzamento""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroLds_mainclass_c1_macrova_m10'"""),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che   il parametro ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,51,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120
 /*104,*/ o  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  /*53,*/ contatore LDS_MainClass_C1_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120""", [
                            DIBoolExpr("""EqualImpl\nche   /*50,51,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  diverso da c120""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*38,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  /*53,*/ contatore LDS_MainClass_C1_contatore_Co8""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore LDS_MainClass_C1_contatore_Co9 non sia  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""LessThanImpl\n(lds_mainclass_c1_contatore_co9)  è minore di  (12)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*38,*/  il contatore LDS_MainClass_C1_contatore_Co9 sia  uguale a  /*53,*/ contatore LDS_MainClass_C1_contatore_Co8""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6
 /*104,*/ o  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,50,51,*/   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore LDS_MainClass_C1_contatore_Co8 non sia  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6""", [
                            DIBoolExpr("""LessThanImpl\n(lds_mainclass_c1_contatore_co8)  è minore di  (lds_mainclass_c1_contatore_co6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  uguale a c120""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroLds_mainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(db(self.macroLds_mainclass_c1_macrova_m10(True,GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_lds_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_lds_mainclass_c1_parametro_p5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(db(self.macroLds_mainclass_c1_macrova_m10(True,GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_lds_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_lds_mainclass_c1_contatore_co9().get_valore() < self.get_lds_mainclass_c1_contatore_co6().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_lds_mainclass_c1_contatore_co9().get_valore() < 12, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_lds_mainclass_c1_contatore_co9().get_valore() == self.get_lds_mainclass_c1_contatore_co8().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_lds_mainclass_c1_parametro_p2() == 10, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_lds_mainclass_c1_contatore_co8().get_valore() < self.get_lds_mainclass_c1_contatore_co6().get_valore(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_lds_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroLds_mainclass_c1_macrove_m4")
    def macroLds_mainclass_c1_macrove_m4(self, argomento_ave2, argomento_ave3, argomento_ave6, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { 
        
        commento: {38,}  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  commento: {56,} 11430 commento: {36,} e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo e  se l'argomento argomento_ave7 è  uguale a  False  commento: {39,}  commento: {34,} o  se il parametro LDS_MainClass_C1_parametro_P5 è  diverso da  True , Verifica che   commento: {50,}  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
        
        
        }
        """
        def populate_macroLds_mainclass_c1_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 11430 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo e  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  /*34,*/ o  se il parametro LDS_MainClass_C1_parametro_P5 è  diverso da  True , Verifica che   /*50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 11430 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo e  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  /*34,*/ o  se il parametro LDS_MainClass_C1_parametro_P5 è  diverso da  True , Verifica che   /*50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 11430 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo e  se l'argomento argomento_ave7 è  uguale a  False  /*39,*/  /*34,*/ o  se il parametro LDS_MainClass_C1_parametro_P5 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 11430 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo e  se l'argomento argomento_ave7 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 11430 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore LDS_MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 11430""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_contatore_co9)  è uguale a  (11430))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_contatore_co9)  è uguale a  (11430)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDS_MainClass_C1_timer_T8 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave7 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDS_MainClass_C1_parametro_P5 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_mainclass_c1_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(not db(self.get_lds_mainclass_c1_contatore_co9().get_valore() == 11430, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_lds_mainclass_c1_parametro_p5() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroLds_mainclass_c1_macrove_m5")
    def macroLds_mainclass_c1_macrove_m5(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
         commento: {63,} commento: {36,}  se il timer LDS_MainClass_C1_timer_T3 non è attivo commento: {38,} o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6 commento: {36,} e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {61,}  se il parametro ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {34,}  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  commento: {36,} o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  commento: {34,} e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   commento: {47,}   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} o  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  commento: {53,} 7
        
        
         } Verifica che   commento: {47,50,}  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che  commento: {37,}  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P5 sia  uguale a  True 
        
        
         } Verifica che   commento: {47,49,50,}   il parametro ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
         commento: {104,} e  che  commento: {,}  il timer LDS_MainClass_C1_timer_T3 sia disattivo
        
        
        }
        """
        def populate_macroLds_mainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDS_MainClass_C1_timer_T3 non è attivo /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7


 } Verifica che   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1


 } Verifica che   /*47,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 sia  uguale a  True 


 } Verifica che   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ e  che  /*,*/  il timer LDS_MainClass_C1_timer_T3 sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDS_MainClass_C1_timer_T3 non è attivo /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7


 } Verifica che   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1


 } Verifica che   /*47,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*36,*/  se il timer LDS_MainClass_C1_timer_T3 non è attivo /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7


 } Verifica che   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1


 } Verifica che   /*47,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer LDS_MainClass_C1_timer_T3 non è attivo /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7


 } Verifica che   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer LDS_MainClass_C1_timer_T3 non è attivo /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto o  se il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer LDS_MainClass_C1_timer_T3 non è attivo /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer LDS_MainClass_C1_timer_T3 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 /*36,*/ e  se il timer LDS_MainClass_C1_timer_T8 non è scaduto""", [
                            DIBoolExpr("""LessThanImpl\nil contatore LDS_MainClass_C1_contatore_Co9 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDS_MainClass_C1_timer_T8 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef è uguale a FALSE  e  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7


 } Verifica che   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True  e  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_parametro_p5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False , Verifica che   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto o  se il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False  /*36,*/ o  se il timer LDS_MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_parametro_p5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDS_MainClass_C1_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro ConsDef è uguale a FALSE  /*34,*/ e  se il parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDS_MainClass_C1_parametro_P5 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_parametro_p5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,*/   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,*/   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro LDS_MainClass_C1_parametro_P2 sia  uguale a  /*53,*/ 7""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,*/  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da c120""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_variabile_v1)  è uguale a  (c120))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile LDS_MainClass_C1_variabile_V1 non sia  diverso da variabile LDS_MainClass_C1_variabile_V1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_variabile_v1)  è uguale a  (lds_mainclass_c1_variabile_v1))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1)  è uguale a  (lds_mainclass_c1_variabile_v1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120
 /*104,*/ e  che  /*,*/  il timer LDS_MainClass_C1_timer_T3 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile LDS_MainClass_C1_variabile_V1 sia  uguale a c120""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer LDS_MainClass_C1_timer_T3 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroLds_mainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_lds_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_lds_mainclass_c1_contatore_co9().get_valore() < self.get_lds_mainclass_c1_contatore_co6().get_valore(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_lds_mainclass_c1_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_lds_mainclass_c1_parametro_p5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(not db(self.get_lds_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_lds_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_lds_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_lds_mainclass_c1_parametro_p2() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(not db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_lds_mainclass_c1_variabile_v1() == self.get_lds_mainclass_c1_variabile_v1(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(self.get_lds_mainclass_c1_parametro_p5() == True, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(self.get_lds_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroLds_mainclass_c1_macrove_m6")
    def macroLds_mainclass_c1_macrove_m6(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {38,}  se il contatore LDS_MainClass_C1_contatore_Co6 è  minore di  commento: {55,} contatore LDS_MainClass_C1_contatore_Co6 e  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
          se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 14, Verifica che   commento: {47,49,}  commento: {,}  il timer LDS_MainClass_C1_timer_T3 non sia attivo
         commento: {104,} e  che   il parametro ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {36,}  il timer LDS_MainClass_C1_timer_T1 sia attivo
         commento: {104,} o  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
         commento: {104,} e  che  commento: {34,}  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True 
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer LDS_MainClass_C1_timer_T2 sia attivo
        
        
        }
        """
        def populate_macroLds_mainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore LDS_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 e  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14, Verifica che   /*47,49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer LDS_MainClass_C1_timer_T1 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T2 sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore LDS_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 e  se il parametro ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14, Verifica che   /*47,49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer LDS_MainClass_C1_timer_T1 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore LDS_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6 e  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""LessThanImpl\nil contatore LDS_MainClass_C1_contatore_Co6 è  minore di  /*55,*/ contatore LDS_MainClass_C1_contatore_Co6""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14, Verifica che   /*47,49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer LDS_MainClass_C1_timer_T1 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore LDS_MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_contatore_co9)  è uguale a  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer LDS_MainClass_C1_timer_T1 sia attivo
 /*104,*/ o  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer LDS_MainClass_C1_timer_T1 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T3 non sia attivo
 /*104,*/ e  che   il parametro ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer LDS_MainClass_C1_timer_T1 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDS_MainClass_C1_parametro_P5 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_parametro_p5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDS_MainClass_C1_parametro_P3 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer LDS_MainClass_C1_timer_T2 sia attivo""", [
                            ]),#1
                            ]),#0
                ])

        populate_macroLds_mainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_lds_mainclass_c1_contatore_co6().get_valore() < self.get_lds_mainclass_c1_contatore_co6().get_valore(), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_lds_mainclass_c1_contatore_co9().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_lds_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_lds_mainclass_c1_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_lds_mainclass_c1_parametro_p5() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_lds_mainclass_c1_parametro_p3() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(self.get_lds_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroLds_mainclass_c1_macrova_m10")
    def macroLds_mainclass_c1_macrova_m10(self, argomento_a10, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se il parametro ConsDef è uguale a FALSE  commento: {37,} e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a c120 commento: {34,} o  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore avanzamento
        
         commento: {46,} assegna alla macro il valore avanzamento commento: {],}
        }
        """
        def populate_macroLds_mainclass_c1_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a c120 /*34,*/ o  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a c120 /*34,*/ o  se lo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (lds_mainclass_c1_variabile_v1)  è uguale a  (c120) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1)  è uguale a  (c120)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_mainclass_c1_macrova_m10_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se il parametro ConsDef è uguale a FALSE  /*37,*/ e  se la variabile LDS_MainClass_C1_variabile_V1 è  uguale a c120 /*34,*/ o  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore avanzamento
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.avanzamento
        #  /*46,*/ assegna alla macro il valore avanzamento
        return GlobalEnumeration.avanzamento
    
    # for each manual command, the corresponding method is created
    def eventLds_mainclass_c1_command_comm10(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventLds_mainclass_c1_command_comm10')
    
    def eventLds_mainclass_c1_command_comm11(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventLds_mainclass_c1_command_comm11')
    
    def eventLds_mainclass_c1_command_comm9DaSender4db07f5e(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventLds_mainclass_c1_command_comm9DaSender4db07f5e')
    
    # for each automatic command, the corresponding method is created
    def eventLds_mainclass_c1_command_comm5(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventLds_mainclass_c1_command_comm5')
    

    def update_precedente(self):
        # update the variables with previous value
        pass

