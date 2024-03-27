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

class LDS_SubClass_C2(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(LDS_SubClass_C2, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_lds_subclass_c2_variabile_v1(False)
        self.set_lds_subclass_c2_variabile_v10(GlobalEnumeration.rossogiallox)
        self.set_lds_subclass_c2_variabile_v2(GlobalEnumeration.rossogiallox)
        self.set_lds_subclass_c2_variabile_v3(0)
        self.set_lds_subclass_c2_variabile_v7(GlobalEnumeration.c180x)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of LDS_SubClass_C2
        if self.is_triggered('eventLds_subclass_c2_command_comm6'):
            IS_STATE_ACCEPTING_eventLds_subclass_c2_command_comm6 = false # no state is accepting this command!
            self.set_man_cmd_response('eventLds_subclass_c2_command_comm6',self.ManCmdResponse.BLOCKED if IS_STATE_ACCEPTING_eventLds_subclass_c2_command_comm6 else self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventLds_subclass_c2_command_comm6',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventLds_subclass_c2_command_comm7DaSender8d9d9a68'):
            IS_STATE_ACCEPTING_eventLds_subclass_c2_command_comm7DaSender8d9d9a68 = false # no state is accepting this command!
            self.set_man_cmd_response('eventLds_subclass_c2_command_comm7DaSender8d9d9a68',self.ManCmdResponse.BLOCKED if IS_STATE_ACCEPTING_eventLds_subclass_c2_command_comm7DaSender8d9d9a68 else self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventLds_subclass_c2_command_comm7DaSender8d9d9a68',self.ManCmdResponse.NOOP)


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
    def init_configuration(self, lds_subclass_c2_lista_l1, lds_subclass_c2_lista_l4, lds_subclass_c2_lista_l7, consdef, lds_subclass_c2_parametro_p4):
        # initialize the record type parameters
        self.set_lds_subclass_c2_lista_l1(lds_subclass_c2_lista_l1)
        self.set_lds_subclass_c2_lista_l4(lds_subclass_c2_lista_l4)
        self.set_lds_subclass_c2_lista_l7(lds_subclass_c2_lista_l7)
        # initialize the simple type parameters
        self.set_consdef(consdef)
        self.set_lds_subclass_c2_parametro_p4(lds_subclass_c2_parametro_p4)

        # initialize the timers
        self.set_lds_subclass_c2_timer_t4(45000)

        self.timers = [self.lds_subclass_c2_timer_t4,]

        # initialize the counters
        self.set_lds_subclass_c2_contatore_co10(0)
        self.set_lds_subclass_c2_contatore_co2(0)
        self.set_lds_subclass_c2_contatore_co3(0)
        self.set_lds_subclass_c2_contatore_co8(0)
        self.set_lds_subclass_c2_contatore_co9(0)

    # setters for record type parameters
    def set_lds_subclass_c2_lista_l1(self, lds_subclass_c2_lista_l1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_lista_l1",lds_subclass_c2_lista_l1)

    def set_lds_subclass_c2_lista_l4(self, lds_subclass_c2_lista_l4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_lista_l4",lds_subclass_c2_lista_l4)

    def set_lds_subclass_c2_lista_l7(self, lds_subclass_c2_lista_l7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_lista_l7",lds_subclass_c2_lista_l7)


    # getters for record type parameters
    def get_lds_subclass_c2_lista_l1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_lista_l1")

    def get_lds_subclass_c2_lista_l4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_lista_l4")

    def get_lds_subclass_c2_lista_l7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_lista_l7")


    # setters for simple type parameters
    def set_consdef(self, consdef):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"consdef",consdef)

    def set_lds_subclass_c2_parametro_p4(self, lds_subclass_c2_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_parametro_p4",lds_subclass_c2_parametro_p4)


    # getters for simple type parameters
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_lds_subclass_c2_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_parametro_p4")


    # setters for comandi al piazzale
    def set_lds_subclass_c2_comando_c10(self, lds_subclass_c2_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_comando_c10",lds_subclass_c2_comando_c10)

    def set_lds_subclass_c2_comando_c2(self, lds_subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_comando_c2",lds_subclass_c2_comando_c2)

    def set_lds_subclass_c2_comando_c4(self, lds_subclass_c2_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_comando_c4",lds_subclass_c2_comando_c4)

    def set_lds_subclass_c2_comando_c5(self, lds_subclass_c2_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_comando_c5",lds_subclass_c2_comando_c5)

    def set_lds_subclass_c2_comando_c7(self, lds_subclass_c2_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_comando_c7",lds_subclass_c2_comando_c7)


    # getters for controlli dal piazzale
    def get_lds_subclass_c2_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_controllo_c1")

    def get_lds_subclass_c2_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_controllo_c6")

    def get_lds_subclass_c2_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_controllo_c9")


    # setters for state variables
    def set_lds_subclass_c2_variabile_v1(self, lds_subclass_c2_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v1",lds_subclass_c2_variabile_v1)
    def set_lds_subclass_c2_variabile_v10(self, lds_subclass_c2_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v10",lds_subclass_c2_variabile_v10)
    def set_lds_subclass_c2_variabile_v2(self, lds_subclass_c2_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v2",lds_subclass_c2_variabile_v2)
    def set_lds_subclass_c2_variabile_v3(self, lds_subclass_c2_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v3",lds_subclass_c2_variabile_v3)
    def set_lds_subclass_c2_variabile_v7(self, lds_subclass_c2_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v7",lds_subclass_c2_variabile_v7)

    # getters for state variables
    def get_lds_subclass_c2_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v1")

    def get_lds_subclass_c2_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v10")

    def get_lds_subclass_c2_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v2")

    def get_lds_subclass_c2_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v3")

    def get_lds_subclass_c2_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"lds_subclass_c2_variabile_v7")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_lds_subclass_c2_timer_t4(self, timerDuration):
        self.lds_subclass_c2_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "lds_subclass_c2_timer_t4", self.memory)


    # getters for timers
    def get_lds_subclass_c2_timer_t4(self):
        return self.lds_subclass_c2_timer_t4


    # setters for counters
    def set_lds_subclass_c2_contatore_co10(self, counterInitValue):
        self.lds_subclass_c2_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_subclass_c2_contatore_co10", self.memory)

    def set_lds_subclass_c2_contatore_co2(self, counterInitValue):
        self.lds_subclass_c2_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_subclass_c2_contatore_co2", self.memory)

    def set_lds_subclass_c2_contatore_co3(self, counterInitValue):
        self.lds_subclass_c2_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_subclass_c2_contatore_co3", self.memory)

    def set_lds_subclass_c2_contatore_co8(self, counterInitValue):
        self.lds_subclass_c2_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_subclass_c2_contatore_co8", self.memory)

    def set_lds_subclass_c2_contatore_co9(self, counterInitValue):
        self.lds_subclass_c2_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "lds_subclass_c2_contatore_co9", self.memory)


    # getters for counters
    def get_lds_subclass_c2_contatore_co10(self):
        return self.lds_subclass_c2_contatore_co10

    def get_lds_subclass_c2_contatore_co2(self):
        return self.lds_subclass_c2_contatore_co2

    def get_lds_subclass_c2_contatore_co3(self):
        return self.lds_subclass_c2_contatore_co3

    def get_lds_subclass_c2_contatore_co8(self):
        return self.lds_subclass_c2_contatore_co8

    def get_lds_subclass_c2_contatore_co9(self):
        return self.lds_subclass_c2_contatore_co9



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
                    DIBoolExpr("""NAryLogicOP (AND)\nVerifica che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x""", [
                    DIBoolExpr("""EqualImpl\nche il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x""", [
                    ]),#0
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\nVerifica che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x""", [
                    DIBoolExpr("""EqualImpl\nche il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x""", [
                    ]),#0
                    ]),#2
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[2], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1,
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1)
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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1):
                if(self.guard_NOMINAL_ACTUATION_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1)
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
        Verifica che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
        }
        """
        return db((db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, self.dbs[1].subs[0])), self.dbs[1])
    
    def guard_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {
        	Verifica che il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
        }
        """
        return db((db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, self.dbs[2].subs[0])), self.dbs[2])
    
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
         	Incrementa il contatore LDS_SubClass_C2_contatore_Co10
         }
        """
        #  Incrementa il contatore LDS_SubClass_C2_contatore_Co10
        self.get_lds_subclass_c2_contatore_co10().incrementa()
    
    # effect macros
    def macroLds_subclass_c2_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {43,}  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 è attivo commento: {37,} e  se la variabile LDS_SubClass_C2_variabile_V3 non è  maggiore di  commento: {54,} 4 commento: {36,} o  se il timer LDS_SubClass_C2_timer_T4 è disattivo, commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
        
           
         commento: {41,}  se LDS_MainClass_C1_parametro_P5 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da  False  commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co8 non è  uguale a  commento: {53,} 135 o  se il parametro ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
        
           
         commento: {37,}  se la variabile LDS_SubClass_C2_variabile_V3 è  maggiore di  commento: {54,} 3 e  se il parametro ConsDef è uguale a FALSE  commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 122 commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x commento: {37,} o  se la variabile LDS_SubClass_C2_variabile_V7 è  diverso da c270x, commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
        
           
        
        }
        """
        def populate_macroLds_subclass_c2_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*43,*/  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 è attivo /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 4 /*36,*/ o  se il timer LDS_SubClass_C2_timer_T4 è disattivo, /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 è attivo /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 4 /*36,*/ o  se il timer LDS_SubClass_C2_timer_T4 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(il timer 'lds_mainclass_c1_timer_t3 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1' è attivo)} )  e  
( negazione di ((lds_subclass_c2_variabile_v3)  è maggiore di  (4)) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'lds_mainclass_c1_timer_t3 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1' è attivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t3 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_variabile_v3)  è maggiore di  (4))""", [
                            DIBoolExpr("""GreaterThanImpl\n(lds_subclass_c2_variabile_v3)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_subclass_c2_timer_t4' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*41,*/  se LDS_MainClass_C1_parametro_P5 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 135 o  se il parametro ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se LDS_MainClass_C1_parametro_P5 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 135 o  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((lds_mainclass_c1_parametro_p5 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (False)))} )  e  
( negazione di ((lds_subclass_c2_contatore_co8)  è uguale a  (135)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((lds_mainclass_c1_parametro_p5 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (False)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_parametro_p5 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p5 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_contatore_co8)  è uguale a  (135))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_contatore_co8)  è uguale a  (135)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*37,*/  se la variabile LDS_SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 3 e  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 122 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x /*37,*/ o  se la variabile LDS_SubClass_C2_variabile_V7 è  diverso da c270x, /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile LDS_SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 3 e  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 122 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x /*37,*/ o  se la variabile LDS_SubClass_C2_variabile_V7 è  diverso da c270x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (lds_subclass_c2_variabile_v3)  è maggiore di  (3) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (lds_subclass_c2_contatore_co10)  è uguale a  (122) ) )  e  
( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (lds_subclass_c2_variabile_v3)  è maggiore di  (3) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (lds_subclass_c2_contatore_co10)  è uguale a  (122) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lds_subclass_c2_variabile_v3)  è maggiore di  (3) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(lds_subclass_c2_variabile_v3)  è maggiore di  (3)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_contatore_co10)  è uguale a  (122)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_variabile_v7)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_variabile_v7)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroLds_subclass_c2_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*43,*/  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 è attivo /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 4 /*36,*/ o  se il timer LDS_SubClass_C2_timer_T4 è disattivo, /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
        if db((db((db(all(db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l1())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_variabile_v3() > 4, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_lds_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_lds_subclass_c2_comando_c10(GlobalEnumeration.c120x)
        #  /*41,*/  se LDS_MainClass_C1_parametro_P5 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 135 o  se il parametro ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
        if db((db((db(all_notempty(db(not db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_parametro_p5() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l7())), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_contatore_co8().get_valore() == 135, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_lds_subclass_c2_comando_c2(GlobalEnumeration.spento)
        #  /*37,*/  se la variabile LDS_SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 3 e  se il parametro ConsDef è uguale a FALSE  /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 122 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x /*37,*/ o  se la variabile LDS_SubClass_C2_variabile_V7 è  diverso da c270x, /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C10 il valore c120x
        if db((db((db((db((db(self.get_lds_subclass_c2_variabile_v3() > 3, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(self.get_lds_subclass_c2_contatore_co10().get_valore() == 122, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_lds_subclass_c2_variabile_v7() == GlobalEnumeration.c270x, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_lds_subclass_c2_comando_c10(GlobalEnumeration.c120x)
    
    def macroLds_subclass_c2_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore LDS_SubClass_C2_contatore_Co2 è  uguale a  commento: {53,} 14 commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è attivo commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è attivo o  se il parametro ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore LDS_SubClass_C2_contatore_Co2
        
         ,altrimenti  commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C7 il valore  True 
        
        
         commento: {44,}  se  LDS_MainClass_C1_variabile_V1 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  commento: {105,} è  diverso da c120 commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 1543 commento: {37,} e  se la variabile LDS_SubClass_C2_variabile_V1 è  uguale a  True  o  se il parametro ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x, commento: {67,} Assegna alla variabile LDS_SubClass_C2_variabile_V7 il valore c270x
        
         ,altrimenti  commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
        
        
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile LDS_SubClass_C2_variabile_V2 non è  diverso da c120x commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x e  se il parametro ConsDef è uguale a FALSE  commento: {38,} o  se il contatore LDS_SubClass_C2_contatore_Co10 è  minore di  commento: {55,} contatore LDS_SubClass_C2_contatore_Co8, commento: {67,} Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 6
        
           
         commento: {44,}  se  LDS_MainClass_C1_variabile_V7 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  commento: {105,} è  uguale a RossoVerde commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, commento: {72,}Azzera il contatore LDS_SubClass_C2_contatore_Co2
        
         ,altrimenti  commento: {70,}Incrementa il contatore LDS_SubClass_C2_contatore_Co10
        
        
         commento: {38,}  se il contatore LDS_SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 13 commento: {38,} o  se il contatore LDS_SubClass_C2_contatore_Co2 non è  uguale a  commento: {53,} 1215 e  se il parametro ConsDef è uguale a FALSE  commento: {34,} o  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x, commento: {67,} Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 1
        
         ,altrimenti  commento: {69,}Disattiva il timer LDS_SubClass_C2_timer_T4
        
        
        
        }
        """
        def populate_macroLds_subclass_c2_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore LDS_SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo o  se il parametro ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore LDS_SubClass_C2_contatore_Co2

 ,altrimenti  /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C7 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore LDS_SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo o  se il parametro ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (lds_subclass_c2_contatore_co2)  è uguale a  (14) )  e  ( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) ) )  e  ( negazione di (il timer 'lds_subclass_c2_timer_t4' è attivo) ) )  e  
( negazione di (il timer 'lds_subclass_c2_timer_t4' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (lds_subclass_c2_contatore_co2)  è uguale a  (14) )  e  ( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) ) )  e  ( negazione di (il timer 'lds_subclass_c2_timer_t4' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lds_subclass_c2_contatore_co2)  è uguale a  (14) )  e  ( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_contatore_co2)  è uguale a  (14)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'lds_subclass_c2_timer_t4' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'lds_subclass_c2_timer_t4' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*44,*/  se  LDS_MainClass_C1_variabile_V1 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da c120 /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 1543 /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V1 è  uguale a  True  o  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x, /*67,*/ Assegna alla variabile LDS_SubClass_C2_variabile_V7 il valore c270x

 ,altrimenti  /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  LDS_MainClass_C1_variabile_V1 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da c120 /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 1543 /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V1 è  uguale a  True  o  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti con lista non vuota {(negazione di ((lds_mainclass_c1_variabile_v1 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (c120)))} )  e  ( negazione di ((lds_subclass_c2_contatore_co10)  è uguale a  (1543)) ) )  e  
( (lds_subclass_c2_variabile_v1)  è uguale a  (True) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((lds_mainclass_c1_variabile_v1 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (c120)))} )  e  ( negazione di ((lds_subclass_c2_contatore_co10)  è uguale a  (1543)) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((lds_mainclass_c1_variabile_v1 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (c120)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_mainclass_c1_variabile_v1 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (c120))""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v1 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l7)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_contatore_co10)  è uguale a  (1543))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_contatore_co10)  è uguale a  (1543)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_variabile_v1)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V2 non è  diverso da c120x /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x e  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co10 è  minore di  /*55,*/ contatore LDS_SubClass_C2_contatore_Co8, /*67,*/ Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V2 non è  diverso da c120x /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x e  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co10 è  minore di  /*55,*/ contatore LDS_SubClass_C2_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (lo stato di 'self')  è uguale a  (state1) )  e  ( negazione di (negazione di ((lds_subclass_c2_variabile_v2)  è uguale a  (c120x))) ) )  e  ( negazione di (negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (lo stato di 'self')  è uguale a  (state1) )  e  ( negazione di (negazione di ((lds_subclass_c2_variabile_v2)  è uguale a  (c120x))) ) )  e  ( negazione di (negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lo stato di 'self')  è uguale a  (state1) )  e  ( negazione di (negazione di ((lds_subclass_c2_variabile_v2)  è uguale a  (c120x))) )""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lds_subclass_c2_variabile_v2)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_variabile_v2)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_variabile_v2)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(lds_subclass_c2_contatore_co10)  è minore di  (lds_subclass_c2_contatore_co8)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*44,*/  se  LDS_MainClass_C1_variabile_V7 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  /*105,*/ è  uguale a RossoVerde /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, /*72,*/Azzera il contatore LDS_SubClass_C2_contatore_Co2

 ,altrimenti  /*70,*/Incrementa il contatore LDS_SubClass_C2_contatore_Co10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*44,*/  se  LDS_MainClass_C1_variabile_V7 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  /*105,*/ è  uguale a RossoVerde /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((lds_mainclass_c1_variabile_v7 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1)  è uguale a  (rossoverde))}""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_variabile_v7 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore LDS_SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 13 /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co2 non è  uguale a  /*53,*/ 1215 e  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x, /*67,*/ Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 1

 ,altrimenti  /*69,*/Disattiva il timer LDS_SubClass_C2_timer_T4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore LDS_SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 13 /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co2 non è  uguale a  /*53,*/ 1215 e  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((lds_subclass_c2_contatore_co10)  è maggiore di  (13)) )  o  
( ( negazione di ((lds_subclass_c2_contatore_co2)  è uguale a  (1215)) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_contatore_co10)  è maggiore di  (13))""", [
                            DIBoolExpr("""GreaterThanImpl\n(lds_subclass_c2_contatore_co10)  è maggiore di  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lds_subclass_c2_contatore_co2)  è uguale a  (1215)) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_contatore_co2)  è uguale a  (1215))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_contatore_co2)  è uguale a  (1215)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroLds_subclass_c2_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore LDS_SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo o  se il parametro ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore LDS_SubClass_C2_contatore_Co2
        #   ,altrimenti  /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C7 il valore  True
        if db((db((db((db((db(self.get_lds_subclass_c2_contatore_co2().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_lds_subclass_c2_contatore_co2().resetta()
        else:
            self.set_lds_subclass_c2_comando_c7(True)
        #  /*44,*/  se  LDS_MainClass_C1_variabile_V1 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L7 esiste e  /*105,*/ è  diverso da c120 /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 1543 /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V1 è  uguale a  True  o  se il parametro ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x, /*67,*/ Assegna alla variabile LDS_SubClass_C2_variabile_V7 il valore c270x
        #   ,altrimenti  /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C2 il valore spento
        if db((db((db((db(all_notempty(db(not db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_variabile_v1() == GlobalEnumeration.c120, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l7())), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_contatore_co10().get_valore() == 1543, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_lds_subclass_c2_variabile_v1() == True, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_lds_subclass_c2_variabile_v7(GlobalEnumeration.c270x)
        else:
            self.set_lds_subclass_c2_comando_c2(GlobalEnumeration.spento)
        #  /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile LDS_SubClass_C2_variabile_V2 non è  diverso da c120x /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x e  se il parametro ConsDef è uguale a FALSE  /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co10 è  minore di  /*55,*/ contatore LDS_SubClass_C2_contatore_Co8, /*67,*/ Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 6
        if db((db((db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_lds_subclass_c2_variabile_v2() == GlobalEnumeration.c120x, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_lds_subclass_c2_contatore_co10().get_valore() < self.get_lds_subclass_c2_contatore_co8().get_valore(), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_lds_subclass_c2_variabile_v3(6)
        #  /*44,*/  se  LDS_MainClass_C1_variabile_V7 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  /*105,*/ è  uguale a RossoVerde /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, /*72,*/Azzera il contatore LDS_SubClass_C2_contatore_Co2
        #   ,altrimenti  /*70,*/Incrementa il contatore LDS_SubClass_C2_contatore_Co10
        if db((db(all_notempty(db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_variabile_v7() == GlobalEnumeration.rossoverde, di_ctx.subs[3].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l1())), di_ctx.subs[3].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_lds_subclass_c2_contatore_co2().resetta()
        else:
            self.get_lds_subclass_c2_contatore_co10().incrementa()
        #  /*38,*/  se il contatore LDS_SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 13 /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co2 non è  uguale a  /*53,*/ 1215 e  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x, /*67,*/ Assegna alla variabile LDS_SubClass_C2_variabile_V3 il valore 1
        #   ,altrimenti  /*69,*/Disattiva il timer LDS_SubClass_C2_timer_T4
        if db((db((db(not db(self.get_lds_subclass_c2_contatore_co10().get_valore() > 13, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db((db(not db(self.get_lds_subclass_c2_contatore_co2().get_valore() == 1215, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_lds_subclass_c2_variabile_v3(1)
        else:
            self.get_lds_subclass_c2_timer_t4().disattiva()
    
    def macroLds_subclass_c2_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a variabile LDS_SubClass_C2_variabile_V10 commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x commento: {38,} o  se il contatore LDS_SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 12 commento: {34,} o  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x o  se il parametro ConsDef è uguale a FALSE  commento: {34,} o  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, commento: {66,} Assegna al comando LDS_SubClass_C2_comando_C4 il valore  False 
        
           
        
        }
        """
        def populate_macroLds_subclass_c2_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a variabile LDS_SubClass_C2_variabile_V10 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x o  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C4 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a variabile LDS_SubClass_C2_variabile_V10 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x o  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( (lds_subclass_c2_parametro_p4)  è uguale a  (lds_subclass_c2_variabile_v10) )  e  
( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) ) )  o  
( (lds_subclass_c2_contatore_co2)  è minore di  (12) ) )  o  
( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (lds_subclass_c2_parametro_p4)  è uguale a  (lds_subclass_c2_variabile_v10) )  e  
( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) ) )  o  
( (lds_subclass_c2_contatore_co2)  è minore di  (12) ) )  o  
( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (lds_subclass_c2_parametro_p4)  è uguale a  (lds_subclass_c2_variabile_v10) )  e  
( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) ) )  o  
( (lds_subclass_c2_contatore_co2)  è minore di  (12) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lds_subclass_c2_parametro_p4)  è uguale a  (lds_subclass_c2_variabile_v10) )  e  
( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (lds_subclass_c2_variabile_v10)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(lds_subclass_c2_contatore_co2)  è minore di  (12)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_subclass_c2_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a variabile LDS_SubClass_C2_variabile_V10 /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ o  se il contatore LDS_SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 12 /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x o  se il parametro ConsDef è uguale a FALSE  /*34,*/ o  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x, /*66,*/ Assegna al comando LDS_SubClass_C2_comando_C4 il valore  False
        if db((db((db((db((db((db(self.get_lds_subclass_c2_parametro_p4() == self.get_lds_subclass_c2_variabile_v10(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_lds_subclass_c2_contatore_co2().get_valore() < 12, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_lds_subclass_c2_comando_c4(False)
    
    # verify macros
    @srf_value_macro("macroLds_subclass_c2_macrove_m1")
    def macroLds_subclass_c2_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se la macro  LDS_SubClass_C2_macrova_M8   non  è  diverso da spento commento: {40,}  e  se il parametro ConsDef è uguale a FALSE , Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} o  se il parametro ConsDef è uguale a FALSE , Tutte le seguenti { 
         commento: {34,}  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x commento: {38,} e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  commento: {56,} 1501, Verifica che   commento: {47,}   il parametro ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
        
        
         } Verifica che   commento: {47,}   il parametro ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x
        
        
         } Verifica che   commento: {47,49,50,}   il parametro ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che  commento: {,}  la variabile LDS_SubClass_C2_variabile_V3 sia  diverso da  commento: {56,} 10
         commento: {104,} o  che  commento: {,}  il timer LDS_SubClass_C2_timer_T4 non sia attivo
         commento: {104,} e  che  commento: {36,}  il timer LDS_SubClass_C2_timer_T4 sia attivo
        
        
        }
        """
        def populate_macroLds_subclass_c2_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  LDS_SubClass_C2_macrova_M8   non  è  diverso da spento /*40,*/  e  se il parametro ConsDef è uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il parametro ConsDef è uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 1501, Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x


 } Verifica che   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile LDS_SubClass_C2_variabile_V3 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*,*/  il timer LDS_SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer LDS_SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  LDS_SubClass_C2_macrova_M8   non  è  diverso da spento /*40,*/  e  se il parametro ConsDef è uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il parametro ConsDef è uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 1501, Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  LDS_SubClass_C2_macrova_M8   non  è  diverso da spento /*40,*/  e  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  LDS_SubClass_C2_macrova_M8   non  è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroLds_subclass_c2_macrova_m8')  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroLds_subclass_c2_macrova_m8')  è uguale a  (spento)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroLds_subclass_c2_macrova_m8'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il parametro ConsDef è uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 1501, Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 } Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il parametro ConsDef è uguale a FALSE , Tutte le seguenti { 
 /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 1501, Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ o  se il parametro ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro ConsDef è uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 1501, Verifica che   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x /*38,*/ e  se il contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 1501""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro LDS_SubClass_C2_parametro_P4 è  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore LDS_SubClass_C2_contatore_Co2 non è  diverso da  /*56,*/ 1501""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_contatore_co2)  è uguale a  (1501))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_contatore_co2)  è uguale a  (1501)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,*/   il parametro ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,*/   il parametro ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile LDS_SubClass_C2_variabile_V3 sia  diverso da  /*56,*/ 10
 /*104,*/ o  che  /*,*/  il timer LDS_SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer LDS_SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*,*/  la variabile LDS_SubClass_C2_variabile_V3 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il parametro ConsDef sia uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,*/   il parametro ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile LDS_SubClass_C2_variabile_V3 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_variabile_v3)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer LDS_SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer LDS_SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer LDS_SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer LDS_SubClass_C2_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroLds_subclass_c2_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(not db(db(self.macroLds_subclass_c2_macrova_m8(di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_lds_subclass_c2_contatore_co2().get_valore() == 1501, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_variabile_v3() == 10, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_lds_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_lds_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroLds_subclass_c2_macrove_m3")
    def macroLds_subclass_c2_macrove_m3(self, argomento_ave3, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 è  diverso da  commento: {56,}  state1 , Verifica che   commento: {47,52,}   l'argomento argomento_ave6 sia  uguale a c270x commento: {,} 
         commento: {104,} e  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
         commento: {104,} o  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x
         commento: {104,} e  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x
        
        
        }
        """
        def populate_macroLds_subclass_c2_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*111,*/  se lo stato del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 è  diverso da  /*56,*/  state1 , Verifica che   /*47,52,*/   l'argomento argomento_ave6 sia  uguale a c270x /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*111,*/  se lo stato del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 è  diverso da  /*56,*/  state1 , Verifica che   /*47,52,*/   l'argomento argomento_ave6 sia  uguale a c270x /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x""", [
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'lds_mainclass_c1 della lista lds_subclass_c2_lista_l4')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'lds_mainclass_c1 della lista lds_subclass_c2_lista_l4')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,52,*/   l'argomento argomento_ave6 sia  uguale a c270x /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,52,*/   l'argomento argomento_ave6 sia  uguale a c270x /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,52,*/   l'argomento argomento_ave6 sia  uguale a c270x""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_subclass_c2_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db(all(db(not db(it.get_lds_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.LDS_MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(argomento_ave6 == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(not db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroLds_subclass_c2_macrove_m9")
    def macroLds_subclass_c2_macrove_m9(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave4, argomento_ave5, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        {
        	
        	 commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile LDS_SubClass_C2_variabile_V3 è  minore di  commento: {55,} 5 commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è scaduto, Verifica che   commento: {47,49,50,52,}  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
         commento: {104,} o  che   l'argomento argomento_ave5 sia  diverso da  False  commento: {,} 
         commento: {104,} o  che   il parametro ConsDef sia uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10
         commento: {104,} o  che  commento: {,}  il timer LDS_SubClass_C2_timer_T4 sia disattivo
        
        
        }
        """
        def populate_macroLds_subclass_c2_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile LDS_SubClass_C2_variabile_V3 è  minore di  /*55,*/ 5 /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è scaduto, Verifica che   /*47,49,50,52,*/  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave5 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10
 /*104,*/ o  che  /*,*/  il timer LDS_SubClass_C2_timer_T4 sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile LDS_SubClass_C2_variabile_V3 è  minore di  /*55,*/ 5 /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è scaduto, Verifica che   /*47,49,50,52,*/  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave5 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10
 /*104,*/ o  che  /*,*/  il timer LDS_SubClass_C2_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile LDS_SubClass_C2_variabile_V3 è  minore di  /*55,*/ 5 /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile LDS_SubClass_C2_variabile_V3 è  minore di  /*55,*/ 5 /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""LessThanImpl\nla variabile LDS_SubClass_C2_variabile_V3 è  minore di  /*55,*/ 5""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer LDS_SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave5 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10
 /*104,*/ o  che  /*,*/  il timer LDS_SubClass_C2_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave5 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave5 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,52,*/  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 sia  uguale a c120x""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave5 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il parametro ConsDef sia uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10""", [
                            DIBoolExpr("""EqualImpl\nche   il parametro ConsDef sia uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro LDS_SubClass_C2_parametro_P4 non sia  uguale a variabile LDS_SubClass_C2_variabile_V10""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (lds_subclass_c2_variabile_v10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer LDS_SubClass_C2_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_subclass_c2_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.LDS_SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_lds_subclass_c2_variabile_v3() < 5, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_lds_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(argomento_ave5 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_lds_subclass_c2_parametro_p4() == self.get_lds_subclass_c2_variabile_v10(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(self.get_lds_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroLds_subclass_c2_macrova_m4")
    def macroLds_subclass_c2_macrova_m4(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[} commento: {41,}  se LDS_MainClass_C1_parametro_P3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a  False  commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x commento: {36,} o  se il timer LDS_SubClass_C2_timer_T4 è disattivo commento: {34,} e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x commento: {36,} e  se il timer LDS_SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore RossoGiallo
        
         commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
        }
        """
        def populate_macroLds_subclass_c2_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*41,*/  se LDS_MainClass_C1_parametro_P3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a  False  /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x /*36,*/ o  se il timer LDS_SubClass_C2_timer_T4 è disattivo /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*41,*/  se LDS_MainClass_C1_parametro_P3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a  False  /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x /*36,*/ o  se il timer LDS_SubClass_C2_timer_T4 è disattivo /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {((lds_mainclass_c1_parametro_p3 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l4)  è uguale a  (False))} )  e  
( (lds_subclass_c2_parametro_p4)  è uguale a  (c120x) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((lds_mainclass_c1_parametro_p3 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l4)  è uguale a  (False))}""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p3 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'lds_subclass_c2_timer_t4' è inattivo )  e  ( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) ) )  e  
( negazione di (il timer 'lds_subclass_c2_timer_t4' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'lds_subclass_c2_timer_t4' è inattivo )  e  ( negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'lds_subclass_c2_timer_t4' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_subclass_c2_macrova_m4_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*41,*/  se LDS_MainClass_C1_parametro_P3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a  False  /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 è  uguale a c120x /*36,*/ o  se il timer LDS_SubClass_C2_timer_T4 è disattivo /*34,*/ e  se il parametro LDS_SubClass_C2_parametro_P4 non è  uguale a c120x /*36,*/ e  se il timer LDS_SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore RossoGiallo
        if db((db((db(all_notempty(db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_parametro_p3() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(self.get_lds_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_lds_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogiallo
        #  /*46,*/ assegna alla macro il valore RossoGiallo
        return GlobalEnumeration.rossogiallo
    
    @srf_value_macro("macroLds_subclass_c2_macrova_m5")
    def macroLds_subclass_c2_macrova_m5(self, argomento_a1, argomento_a3, argomento_a4, argomento_a5, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGiallo commento: {],}
        }
        """
        def populate_macroLds_subclass_c2_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroLds_subclass_c2_macrova_m5_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGiallo
        return GlobalEnumeration.rossogiallo
    
    @srf_value_macro("macroLds_subclass_c2_macrova_m6")
    def macroLds_subclass_c2_macrova_m6(self, argomento_a10, argomento_a2, argomento_a3, argomento_a6, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        {
        	 commento: {[} commento: {34,}  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x,  commento: {43,}   se LDS_MainClass_C1_timer_T8 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  commento: {105,} è attivo, commento: {88,} quando  commento: {41,}   LDS_MainClass_C1_parametro_P2 del campo LDS_MainClass_C1      commento: {105,} è  uguale a  commento: {53,} 5 , assegna alla macro il valore  True  
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroLds_subclass_c2_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x,  /*43,*/   se LDS_MainClass_C1_timer_T8 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*41,*/   LDS_MainClass_C1_parametro_P2 del campo LDS_MainClass_C1      /*105,*/ è  uguale a  /*53,*/ 5 , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x,  /*43,*/   se LDS_MainClass_C1_timer_T8 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*41,*/   LDS_MainClass_C1_parametro_P2 del campo LDS_MainClass_C1      /*105,*/ è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lds_subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(lds_subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((lds_mainclass_c1_parametro_p2 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1)  è uguale a  (5)) allora (il timer 'lds_mainclass_c1_timer_t8 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1' è attivo)}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lds_mainclass_c1_parametro_p2 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1)  è uguale a  (5)) allora (il timer 'lds_mainclass_c1_timer_t8 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1' è attivo)""", [
                            DIBoolExpr("""EqualImpl\n(lds_mainclass_c1_parametro_p2 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1)  è uguale a  (5)""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t8 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l1' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_subclass_c2_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se il parametro LDS_SubClass_C2_parametro_P4 non è  diverso da c120x,  /*43,*/   se LDS_MainClass_C1_timer_T8 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L1 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*41,*/   LDS_MainClass_C1_parametro_P2 del campo LDS_MainClass_C1      /*105,*/ è  uguale a  /*53,*/ 5 , assegna alla macro il valore  True
        if db((db(not db(not db(self.get_lds_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l1()) if db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_parametro_p2() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroLds_subclass_c2_macrova_m8")
    def macroLds_subclass_c2_macrova_m8(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[} commento: {43,}  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4  è disattivo , assegna alla macro il valore spento
        
         commento: {46,} assegna alla macro il valore spento commento: {],}
        }
        """
        def populate_macroLds_subclass_c2_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*43,*/  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4  è disattivo , assegna alla macro il valore spento""", [
                            DIBoolExpr("""Predicato ForAll\nLDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4  è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'lds_mainclass_c1_timer_t3 del campo lds_mainclass_c1 della lista lds_subclass_c2_lista_l4' è inattivo""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroLds_subclass_c2_macrova_m8_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*43,*/  se LDS_MainClass_C1_timer_T3 del campo LDS_MainClass_C1  di LDS_SubClass_C2_lista_L4  è disattivo , assegna alla macro il valore spento
        if db(all(db(it.get_lds_mainclass_c1().get_lds_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_lds_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.spento
        #  /*46,*/ assegna alla macro il valore spento
        return GlobalEnumeration.spento
    
    # for each manual command, the corresponding method is created
    def eventLds_subclass_c2_command_comm6(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventLds_subclass_c2_command_comm6')
    
    def eventLds_subclass_c2_command_comm7DaSender8d9d9a68(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventLds_subclass_c2_command_comm7DaSender8d9d9a68')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        pass

class LDS_SubClass_C2_RecordHeaderR2(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, lds_mainclass_c1, recordfiled13, recordfiled2, recordfiled18, recordfiled1):
        self.set_lds_mainclass_c1(lds_mainclass_c1)
        self.set_recordfiled13(recordfiled13)
        self.set_recordfiled2(recordfiled2)
        self.set_recordfiled18(recordfiled18)
        self.set_recordfiled1(recordfiled1)

    # setters for the fields of record
    def set_lds_mainclass_c1(self, lds_mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "lds_mainclass_c1"), lds_mainclass_c1)

    def set_recordfiled13(self, recordfiled13):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"), recordfiled13)

    def set_recordfiled2(self, recordfiled2):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"), recordfiled2)

    def set_recordfiled18(self, recordfiled18):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"), recordfiled18)

    def set_recordfiled1(self, recordfiled1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled1"), recordfiled1)


    # getters for the fields of record
    def get_lds_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "lds_mainclass_c1"))

    def get_recordfiled13(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"))

    def get_recordfiled2(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"))

    def get_recordfiled18(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"))

    def get_recordfiled1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled1"))



class LDS_SubClass_C2_RecordHeaderR9(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, lds_mainclass_c1, recordfiled4, recordfiled6, recordfiled17):
        self.set_lds_mainclass_c1(lds_mainclass_c1)
        self.set_recordfiled4(recordfiled4)
        self.set_recordfiled6(recordfiled6)
        self.set_recordfiled17(recordfiled17)

    # setters for the fields of record
    def set_lds_mainclass_c1(self, lds_mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "lds_mainclass_c1"), lds_mainclass_c1)

    def set_recordfiled4(self, recordfiled4):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"), recordfiled4)

    def set_recordfiled6(self, recordfiled6):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"), recordfiled6)

    def set_recordfiled17(self, recordfiled17):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled17"), recordfiled17)


    # getters for the fields of record
    def get_lds_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "lds_mainclass_c1"))

    def get_recordfiled4(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"))

    def get_recordfiled6(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled6"))

    def get_recordfiled17(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled17"))



