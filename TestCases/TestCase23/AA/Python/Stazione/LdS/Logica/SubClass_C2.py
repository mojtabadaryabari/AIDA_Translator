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

class SubClass_C2(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C2, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c2_previousva_pv1(0)
        self.set_subclass_c2_previousva_pv2(False)
        self.set_subclass_c2_previousva_pv3(GlobalEnumeration.c120)
        self.set_subclass_c2_previousva_pv4(0)
        self.set_subclass_c2_restoreva_rv1(False)
        self.set_subclass_c2_restoreva_rv2(False)
        self.set_subclass_c2_restoreva_rv3(False)
        self.set_subclass_c2_variabile_v1(0)
        self.set_subclass_c2_variabile_v6(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
        if self.is_triggered('eventSubclass_c2_command_comm10'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm10',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm10',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, subclass_c2_lista_l3, subclass_c2_parametro_p2, subclass_c2_parametro_p3, subclass_c2_parametro_p6):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l3(subclass_c2_lista_l3)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p2(subclass_c2_parametro_p2)
        self.set_subclass_c2_parametro_p3(subclass_c2_parametro_p3)
        self.set_subclass_c2_parametro_p6(subclass_c2_parametro_p6)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(55000)
        self.set_subclass_c2_restoreti_ti1_restore(55000)
        self.set_subclass_c2_timer_t4(330000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_timer_t4,]

        # initialize the counters
        self.set_subclass_c2_contatore_co5(0)
        self.set_subclass_c2_contatore_co8(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l3(self, subclass_c2_lista_l3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3",subclass_c2_lista_l3)


    # getters for record type parameters
    def get_subclass_c2_lista_l3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p2(self, subclass_c2_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2",subclass_c2_parametro_p2)

    def set_subclass_c2_parametro_p3(self, subclass_c2_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p3",subclass_c2_parametro_p3)

    def set_subclass_c2_parametro_p6(self, subclass_c2_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6",subclass_c2_parametro_p6)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2")

    def get_subclass_c2_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p3")

    def get_subclass_c2_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c2(self, subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c2",subclass_c2_comando_c2)

    def set_subclass_c2_comando_c8(self, subclass_c2_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c8",subclass_c2_comando_c8)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c3")

    def get_subclass_c2_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5")


    # setters for state variables
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
    def set_subclass_c2_previousva_pv3(self, subclass_c2_previousva_pv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3",subclass_c2_previousva_pv3)
    def set_subclass_c2_previousva_pv3_prev(self, subclass_c2_previousva_pv3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3_prev",subclass_c2_previousva_pv3_prev)
    def set_subclass_c2_previousva_pv4(self, subclass_c2_previousva_pv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4",subclass_c2_previousva_pv4)
    def set_subclass_c2_previousva_pv4_prev(self, subclass_c2_previousva_pv4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4_prev",subclass_c2_previousva_pv4_prev)
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_restoreva_rv3(self, subclass_c2_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3",subclass_c2_restoreva_rv3)
    def set_subclass_c2_variabile_v1(self, subclass_c2_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v1",subclass_c2_variabile_v1)
    def set_subclass_c2_variabile_v6(self, subclass_c2_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6",subclass_c2_variabile_v6)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

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

    def get_subclass_c2_previousva_pv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3")

    def get_subclass_c2_previousva_pv3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv3_prev")

    def get_subclass_c2_previousva_pv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4")

    def get_subclass_c2_previousva_pv4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4_prev")

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

    def get_subclass_c2_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v1")

    def get_subclass_c2_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_timer_t4(self, timerDuration):
        self.subclass_c2_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t4", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_timer_t4(self):
        return self.subclass_c2_timer_t4


    # setters for counters
    def set_subclass_c2_contatore_co5(self, counterInitValue):
        self.subclass_c2_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co5", self.memory)

    def set_subclass_c2_contatore_co8(self, counterInitValue):
        self.subclass_c2_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co8", self.memory)


    # getters for counters
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

        self.set_subclass_c2_previousco_c5_prev(GlobalEnumeration.rossogiallogiallo)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())

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
    def macroSubclass_c2_macroef_m1(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 151 commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  commento: {55,} 13 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  minore di  commento: {55,} 6, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 4
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M7  commento: {73,}
        
        
          se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )   è  diverso da c180 commento: {40,} ,  commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  commento: {55,} 1, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  maggiore di  commento: {54,} 2 commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo commento: {36,} e  se il timer SubClass_C2_timer_T4 è attivo, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co5
        
         ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co5
        
        
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  commento: {53,} 13, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 7
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  True 
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 151 /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 13 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  minore di  /*55,*/ 6, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 4

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 151 /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 13 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'subclass_c2_restoreti_ti1_restore' è inattivo) )  o  
( ( ( negazione di ((subclass_c2_contatore_co5)  è maggiore di  (151)) )  e  ( (subclass_c2_variabile_v6)  è uguale a  (False) ) )  e  
( negazione di ((subclass_c2_contatore_co5)  è minore di  (13)) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_restoreti_ti1_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_contatore_co5)  è maggiore di  (151)) )  e  ( (subclass_c2_variabile_v6)  è uguale a  (False) ) )  e  
( negazione di ((subclass_c2_contatore_co5)  è minore di  (13)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co5)  è maggiore di  (151)) )  e  ( (subclass_c2_variabile_v6)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è maggiore di  (151))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (151)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è minore di  (13))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co5)  è minore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p6)  è minore di  (6)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M7"""),#1
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*73,*/


  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )   è  diverso da c180 /*40,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 1, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  maggiore di  /*54,*/ 2 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co5

 ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/


  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )   è  diverso da c180 /*40,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 1, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  maggiore di  /*54,*/ 2 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (c180)) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (2)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (1))} ) )  e  ( (subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (c180)) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (2)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (c180)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (2)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (1))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (2)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (1))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (2)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 13, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 7

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_contatore_co5)  è uguale a  (13)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 151 /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 13 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  minore di  /*55,*/ 6, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 4
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M7
        if db((db((db(not db(self.get_subclass_c2_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 151, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() < 13, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p6() < 6, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v1(4)
        else:
            self.macroSubclass_c2_macroef_m7(di_ctx.subs[0].subs[1])
        #  /*73,*/
        #    se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )   è  diverso da c180 /*40,*/ ,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 1, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  maggiore di  /*54,*/ 2 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo /*36,*/ e  se il timer SubClass_C2_timer_T4 è attivo, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co5
        #   ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co5
        if db((db((db((db(not db(db(self.macroSubclass_c2_macrova_m9(GlobalEnumeration.avvio,True,GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.rossogialloxverdex, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.c180, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v7() < 1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_variabile_v7() > 2, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co5().incrementa()
        else:
            self.get_subclass_c2_contatore_co5().resetta()
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  uguale a  /*53,*/ 13, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 7
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  True
        if db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[2].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 13, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_variabile_v1(7)
        else:
            self.set_subclass_c2_variabile_v6(True)
    
    def macroSubclass_c2_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 1 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo commento: {37,} o  se la variabile SubClass_C2_variabile_V1 è  minore di  commento: {55,} 3 commento: {34,} o  se il parametro SubClass_C2_parametro_P3 non è  uguale a RossoGialloGiallo, commento: {68,}Attiva il timer SubClass_C2_timer_T4
        
           
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 1442 commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  commento: {55,} 14130 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  commento: {53,} 3, commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
        
           
         commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  uguale a  commento: {53,} 10, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co8
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V1 è  minore di  /*55,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 non è  uguale a RossoGialloGiallo, /*68,*/Attiva il timer SubClass_C2_timer_T4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V1 è  minore di  /*55,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (lo stato di 'self')  è uguale a  (state1) )  e  ( (subclass_c2_parametro_p6)  è uguale a  (1) ) )  e  
( (subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo) ) )  o  
( (subclass_c2_variabile_v1)  è minore di  (3) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (lo stato di 'self')  è uguale a  (state1) )  e  ( (subclass_c2_parametro_p6)  è uguale a  (1) ) )  e  
( (subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lo stato di 'self')  è uguale a  (state1) )  e  ( (subclass_c2_parametro_p6)  è uguale a  (1) )""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v1)  è minore di  (3)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 1442 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 14130 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  /*53,*/ 3, /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 1442 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 14130 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)))} )  e  
( (consdef)  è uguale a  (False) ) )  o  
( ( negazione di ((subclass_c2_contatore_co8)  è maggiore di  (1442)) )  e  
( negazione di ((subclass_c2_contatore_co5)  è minore di  (14130)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)))} )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co8)  è maggiore di  (1442)) )  e  
( negazione di ((subclass_c2_contatore_co5)  è minore di  (14130)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co8)  è maggiore di  (1442))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co8)  è maggiore di  (1442)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è minore di  (14130))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co5)  è minore di  (14130)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (3))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 10, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co8

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (10)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroSubclass_c2_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V1 è  minore di  /*55,*/ 3 /*34,*/ o  se il parametro SubClass_C2_parametro_P3 non è  uguale a RossoGialloGiallo, /*68,*/Attiva il timer SubClass_C2_timer_T4
        if db((db((db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p6() == 1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v1() < 3, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t4().attiva()
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 1442 /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  minore di  /*55,*/ 14130 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  uguale a  /*53,*/ 3, /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
        if db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co8().get_valore() > 1442, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() < 14130, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() == 3, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_comando_c8(GlobalEnumeration.rossogiallogiallo)
        #  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 10, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co8
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
        if db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[2].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[2].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p2() == 10, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_contatore_co8().incrementa()
        else:
            self.set_subclass_c2_variabile_v1(8)
    
    def macroSubclass_c2_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
        
           
         commento: {36,}  se il timer SubClass_C2_timer_T4 non è scaduto,  commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  commento: {54,} 1, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co2 del campo  MainClass_C1     commento: {105,} è  maggiore di  commento: {54,} 142 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co5
        
           
         commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  uguale a  False ,  commento: {41,}  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P8 del campo  MainClass_C1     commento: {105,} è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
        
           
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  diverso da  True , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V1 il valore 10
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M7  commento: {73,}
        
        
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*41,*/  se MainClass_C1_parametro_P5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_parametro_p5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p5 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  /*54,*/ 1, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co2 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 142 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore SubClass_C2_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  /*54,*/ 1, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co2 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 142 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c2_timer_t4' è scaduto) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (142)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (1))} ) )  e  
( (subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t4' è scaduto) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (142)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (142)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (1))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (142)) allora ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (1))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (142)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a  False ,  /*41,*/  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a  False ,  /*41,*/  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex)) allora ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex)) allora ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  True , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 10

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_variabile_v6)  è uguale a  (True)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M7"""),#1
                            ]),#3
                            DIStatement("""ITStatement\n/*73,*/


 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*41,*/  se MainClass_C1_parametro_P5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
        if db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p5() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c8(GlobalEnumeration.rossogiallogiallo)
        #  /*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto,  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  maggiore di  /*54,*/ 1, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co2 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 142 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore SubClass_C2_contatore_Co5
        if db((db((db((db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v7() > 1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co2().get_valore() > 142, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co5().incrementa()
        #  /*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a  False ,  /*41,*/  se MainClass_C1_parametro_P8 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 8
        if db((db(self.get_subclass_c2_variabile_v6() == False, di_ctx.subs[2].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_variabile_v1(8)
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  True , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V1 il valore 10
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M7
        if db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == True, di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_variabile_v1(10)
        else:
            self.macroSubclass_c2_macroef_m7(di_ctx.subs[3].subs[1])
        #  /*73,*/
        #   /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
        if db((db(self.get_subclass_c2_restoreva_rv1_restore() == True, di_ctx.subs[4].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_subclass_c2_comando_c2(GlobalEnumeration.giallogiallo)
    
    def macroSubclass_c2_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro SubClass_C2_parametro_P2 non è  minore di  commento: {55,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  commento: {56,} 4 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  minore di  commento: {55,} 4 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è scaduto, commento: {68,}Attiva il timer SubClass_C2_timer_T4
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
        
        
         commento: {45,}  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  maggiore di  commento: {54,} 122, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co5
        
           
         commento: {37,}  se la variabile SubClass_C2_variabile_V1 è  uguale a  commento: {53,} 10 commento: {36,} o  se il timer SubClass_C2_timer_T4 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V1 non è  maggiore di  commento: {54,} 5,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  True  commento: {67,}
        
           
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {34,} o  se il parametro SubClass_C2_parametro_P2 non è  uguale a  commento: {53,} 6 commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 151 commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  commento: {53,} 113054, commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T4
        
        
          se il controllo ConsDef  è  uguale a FALSE ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  False commento: {67,}
        
         ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore  True  commento: {67,}
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  minore di  /*55,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  /*56,*/ 4 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto, /*68,*/Attiva il timer SubClass_C2_timer_T4

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  minore di  /*55,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  /*56,*/ 4 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_parametro_p2)  è minore di  (5)) )  e  ( negazione di ((subclass_c2_parametro_p6)  è uguale a  (4)) ) )  e  ( negazione di ((subclass_c2_parametro_p6)  è minore di  (4)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p2)  è minore di  (5)) )  e  ( negazione di ((subclass_c2_parametro_p6)  è uguale a  (4)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è minore di  (5))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p2)  è minore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è minore di  (4))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p6)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 122, /*72,*/Azzera il contatore SubClass_C2_contatore_Co5""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 122""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è maggiore di  (122)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  maggiore di  /*54,*/ 5,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_variabile_v1)  è uguale a  (10) )  o  
( il timer 'subclass_c2_timer_t4' è attivo ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c2_variabile_v1)  è uguale a  (10) )  o  
( il timer 'subclass_c2_timer_t4' è attivo )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v1)  è uguale a  (10)""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v1)  è maggiore di  (5))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v1)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*67,*/

   
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 113054, /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo

 ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/

   
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 113054""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( negazione di ((subclass_c2_parametro_p2)  è uguale a  (6)) ) )  o  
( negazione di ((subclass_c2_contatore_co5)  è maggiore di  (151)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( negazione di ((subclass_c2_parametro_p2)  è uguale a  (6)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è maggiore di  (151))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (151)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (113054)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  False /*67,*/

 ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  True""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            ]),#4
                ])

        populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P2 non è  minore di  /*55,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  /*56,*/ 4 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  minore di  /*55,*/ 4 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto, /*68,*/Attiva il timer SubClass_C2_timer_T4
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore GialloGiallo
        if db((db((db((db(not db(self.get_subclass_c2_parametro_p2() < 5, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() < 4, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t4().attiva()
        else:
            self.set_subclass_c2_comando_c2(GlobalEnumeration.giallogiallo)
        #  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  maggiore di  /*54,*/ 122, /*72,*/Azzera il contatore SubClass_C2_contatore_Co5
        if db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co2().get_valore() > 122, di_ctx.subs[1].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co5().resetta()
        #  /*37,*/  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 10 /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  maggiore di  /*54,*/ 5,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  True
        if db((db((db((db(self.get_subclass_c2_variabile_v1() == 10, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v1() > 5, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_variabile_v6(True)
        #  /*67,*/
        #     
        #    se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 151 /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 113054, /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore RossoGialloGiallo
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T4
        if db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == 6, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 151, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co5().get_valore() == 113054, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_comando_c8(GlobalEnumeration.rossogiallogiallo)
        else:
            self.get_subclass_c2_timer_t4().attiva()
        #  se il controllo ConsDef  è  uguale a FALSE ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  False /*67,*/
        #   ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore  True
        if db(self.get_consdef() == False, di_ctx.subs[4].subs[0]):
            self.set_subclass_c2_variabile_v6(False)
        else:
            self.set_subclass_c2_variabile_v6(True)
    
    def macroSubclass_c2_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {44,}  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  commento: {55,} 8 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 2 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
        
           
         commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  diverso da  True ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C3 del campo  MainClass_C1     commento: {105,} è  uguale a  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  minore di  commento: {55,} 155,  Applica gli effetti
               della macro SubClass_C2_macroef_M1  commento: {73,}
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (8))} )  e  
( (subclass_c2_parametro_p6)  è maggiore di  (2) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (8))}""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è minore di  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V6 è  diverso da  True ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C3 del campo  MainClass_C1     /*105,*/ è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 155,  Applica gli effetti
       della macro SubClass_C2_macroef_M1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V6 è  diverso da  True ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C3 del campo  MainClass_C1     /*105,*/ è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 155""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v6)  è uguale a  (True)) )  e  
( per ognuna delle seguenti {se ((mainclass_c1_controllo_c3 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (True)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_controllo_c3 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (True)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_controllo_c3 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (True)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co8)  è minore di  (155))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co8)  è minore di  (155)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M1"""),#1
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*44,*/  se  MainClass_C1_variabile_V7 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v7() < 8, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p6() > 2, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co8().decrementa()
        #  /*37,*/  se la variabile SubClass_C2_variabile_V6 è  diverso da  True ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C3 del campo  MainClass_C1     /*105,*/ è  uguale a  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 155,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M1
        if db((db((db(not db(self.get_subclass_c2_variabile_v6() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_controllo_c3() == True, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() < 155, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.macroSubclass_c2_macroef_m1(di_ctx.subs[1].subs[1])
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m10")
    def macroSubclass_c2_macrove_m10(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave4, argomento_ave6, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,}  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  commento: {53,} 144, Solo una delle seguenti { 
         commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 3, Solo una delle seguenti { 
         commento: {62,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  commento: {53,} 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,} , Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  commento: {54,} 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo commento: {39,} , Tutte le seguenti { 
         commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo commento: {39,}  commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  commento: {54,} 153054, Tutte le seguenti { 
         commento: {63,} commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
         commento: {63,} commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  commento: {39,}  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo commento: {39,}  commento: {36,} o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
         commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da GialloxVerdex commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo commento: {38,} o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  commento: {53,} 122 commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   commento: {47,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  commento: {54,} 2
         commento: {104,} e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  commento: {54,} 11
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo
        
        
         } Verifica che   commento: {49,52,}   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo commento: {39,} 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
        
        
         } Verifica che   commento: {47,48,50,52,}  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  commento: {54,} 9
         commento: {104,} o  che   l'argomento argomento_ave4 non  sia  diverso da avviox commento: {,} 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a  commento: {53,} 8
        
        
         } Verifica che   commento: {49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
         commento: {104,} e  che   l'argomento argomento_ave1 sia  diverso da  False  commento: {,} 
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 non sia disattivo
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 14
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia attivo
        
        
         } Verifica che   commento: {51,52,}   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo commento: {,} 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  uguale a  commento: {53,} 12130
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co8 sia  minore di  commento: {55,} 1254
        
        
         } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  diverso da  commento: {56,} 10
         commento: {104,} e  che   l'argomento argomento_ave10 non  sia  diverso da  False  commento: {,} 
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 non sia disattivo
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  diverso da  commento: {56,} 152
        
        
         } Verifica che   commento: {47,48,49,52,}  commento: {,}  il timer SubClass_C2_timer_T4 non sia scaduto
         commento: {104,} o  che   l'argomento argomento_ave10 sia  diverso da  False  commento: {,} 
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia attivo
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo
         commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a  True  commento: {39,} 
        
        
         } Verifica che   commento: {47,48,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  uguale a  commento: {53,} 10
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  diverso da RossoGialloGiallo
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 144, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/ , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 } Verifica che   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 152


 } Verifica che   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*39,*/ 


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a  /*53,*/ 10
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 144, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/ , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 } Verifica che   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 152


 } Verifica che   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*39,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 144""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C2_restoreTI_TI1 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 144""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  uguale a  /*53,*/ 144""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (144)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/ , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 } Verifica che   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 152


 } Verifica che   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*39,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/ , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 } Verifica che   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 152


 }""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/ , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 } Verifica che   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 152


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/ , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 } Verifica che   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  SubClass_C2_restoreva_RV2 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8 e  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V1 non è  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v1)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 } Verifica che   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 è  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421 e  se l'argomento argomento_ave2 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co5 non è  maggiore di  /*54,*/ 1421""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (1421)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 } Verifica che   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054, Tutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto o  se l'argomento argomento_ave2 non  è  uguale a GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (3)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  uguale a GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co5 è  maggiore di  /*54,*/ 153054""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 } Verifica che   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  diverso da  False""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 } Verifica che   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo, Solo una delle seguenti { 
 /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo /*39,*/  /*36,*/ o  se il timer SubClass_C2_timer_T4 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo o  se l'argomento argomento_ave6 è  uguale a  False""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave6 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Verifica che   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*38,*/ o  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 122""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v1)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave2 sia  uguale a GialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  maggiore di  /*54,*/ 11""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,52,*/   l'argomento argomento_ave2 non  sia  diverso da GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave2 sia  diverso da GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da avviox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V1 non sia  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v1)  è maggiore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  diverso da avviox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave4)  è uguale a  (avviox))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  /*53,*/ 8""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 14""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*51,52,*/   l'argomento argomento_ave2 non  sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 12130""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1254""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 152""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v1)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  diverso da  /*56,*/ 152""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (152)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,52,*/  /*,*/  il timer SubClass_C2_timer_T4 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a  /*53,*/ 10
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a  /*53,*/ 10
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a  /*53,*/ 10""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_subclass_c2_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 144, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db(self.get_subclass_c2_parametro_p6() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(self.get_subclass_c2_restoreva_rv2_restore() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v1() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 1421, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p6() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co5().get_valore() > 153054, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave6 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co5().get_valore() == 122, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v1() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co5().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(not db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v1() > 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(argomento_ave4 == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_parametro_p6() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(not db(self.get_subclass_c2_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave1 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(argomento_ave2 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co8().get_valore() == 12130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_contatore_co8().get_valore() < 1254, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(not db(self.get_subclass_c2_variabile_v1() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave10 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 152, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db((db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave10 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(argomento_ave10 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_subclass_c2_parametro_p2() == 10, di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m2")
    def macroSubclass_c2_macrove_m2(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T4 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 151, Verifica che   commento: {47,48,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  diverso da  commento: {56,} 4
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  uguale a  commento: {53,} 1130
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 151, Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 151, Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P3 è  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co8)  è maggiore di  (151)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  uguale a  /*53,*/ 1130
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  uguale a  /*53,*/ 1130""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  diverso da  /*56,*/ 4
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  uguale a  /*53,*/ 1130""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(not db(self.get_subclass_c2_parametro_p6() == 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co8().get_valore() > 151, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db((db(not db(self.get_subclass_c2_parametro_p6() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co5().get_valore() == 1130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m4")
    def macroSubclass_c2_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V1 è  minore di  commento: {55,} 4, Solo una delle seguenti { 
         commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V1 è  uguale a  commento: {53,} 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
         commento: {62,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T4 non è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  commento: {53,} 125 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 2, Almeno una delle seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T4 è scaduto commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  uguale a  commento: {53,} 7, Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co8 non sia  minore di  commento: {55,} 11
        
        
         } Verifica che   commento: {47,48,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  maggiore di  commento: {54,} 2
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  commento: {54,} 1
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  minore di  commento: {55,} 8
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il timer SubClass_C2_timer_T4 sia scaduto
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 non sia attivo
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 sia scaduto
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  minore di  /*55,*/ 4, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  /*54,*/ 1


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  minore di  /*55,*/ 8


 } Verifica che   /*48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  minore di  /*55,*/ 4, Solo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  /*54,*/ 1


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  minore di  /*55,*/ 8


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V1 è  minore di  /*55,*/ 4""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  /*54,*/ 1


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  minore di  /*55,*/ 8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo, Solo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  /*54,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V1 è  uguale a  /*53,*/ 3""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  /*54,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  SubClass_C2_restoreva_RV3 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T4 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (1))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co5 è  uguale a  /*53,*/ 125""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7, Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T4 è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P2 è  uguale a  /*53,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co8)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  maggiore di  /*54,*/ 2""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co8)  è maggiore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  minore di  /*55,*/ 8""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,*/  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v1() < 4, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db((db((db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v1() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_subclass_c2_restoreva_rv3_restore() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p6() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co5().get_valore() == 125, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p2() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p6() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db(self.get_subclass_c2_variabile_v1() < 8, di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m8")
    def macroSubclass_c2_macrove_m8(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo e  se l'argomento argomento_ave6 non  è  uguale a c180 commento: {39,} , Solo una delle seguenti { 
         commento: {61,}  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 commento: {40,} ,  commento: {45,}  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,} 1121, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  commento: {53,} 4 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 1 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 1 o  se l'argomento argomento_ave2 non  è  uguale a  True  commento: {39,} , Tutte le seguenti { 
         commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 5, Tutte le seguenti { 
         commento: {38,}  se il contatore SubClass_C2_contatore_Co8 non è  minore di  commento: {55,} 1330,  commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P8 del campo  MainClass_C1     commento: {105,} è  diverso da GialloxVerdex, Verifica che   commento: {47,52,}   l'argomento argomento_ave2 sia  diverso da  False  commento: {,} 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a  commento: {53,} 10
        
        
         } Verifica che   commento: {48,50,52,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  maggiore di  commento: {54,} 1
         commento: {104,} e  che   l'argomento argomento_ave4 sia  diverso da  True  commento: {,} 
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
        
        
         } Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V1 sia  diverso da  commento: {56,} 6
         commento: {104,} o  che   l'argomento argomento_ave4 non  sia  diverso da  True  commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave2 sia  uguale a  True  commento: {39,} 
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V1 non sia  diverso da  commento: {56,} 2
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  commento: {54,} 1554
        
        
         } Verifica che   commento: {47,49,50,51,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  minore di  commento: {55,} 8
         commento: {104,} o  che   l'argomento argomento_ave1 sia  diverso da  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co5 sia  minore di  commento: {55,} 132
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T4 sia scaduto
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo e  se l'argomento argomento_ave6 non  è  uguale a c180 /*39,*/ , Solo una delle seguenti { 
 /*61,*/  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 o  se l'argomento argomento_ave2 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5, Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex, Verifica che   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 1554


 } Verifica che   /*47,49,50,51,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  minore di  /*55,*/ 132
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo e  se l'argomento argomento_ave6 non  è  uguale a c180 /*39,*/ , Solo una delle seguenti { 
 /*61,*/  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 o  se l'argomento argomento_ave2 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5, Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex, Verifica che   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 1554


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo e  se l'argomento argomento_ave6 non  è  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a RossoGialloGiallo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave6 non  è  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 o  se l'argomento argomento_ave2 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5, Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex, Verifica che   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo


 } Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 1554


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 o  se l'argomento argomento_ave2 non  è  uguale a  True  /*39,*/ , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5, Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex, Verifica che   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 o  se l'argomento argomento_ave2 non  è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se la macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180 /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  SubClass_C2_macrova_M9 ( con argomento_a5   uguale a True ,argomento_a3   uguale a avvio ,argomento_a8   uguale a RossoGialloxVerdex  e argomento_a7   uguale a RossoGialloGiallo )  non  è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (c180)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co2 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/ 1121, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_variabile_v7 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (4)) allora ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1121))""", [
                            DIBoolExpr("""EqualImpl\n/*44,*/    MainClass_C1_variabile_V7 del campo  MainClass_C1     è  uguale a  /*53,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (1121)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5, Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex, Verifica che   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5, Tutte le seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex, Verifica che   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex, Verifica che   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1330""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co8)  è minore di  (1330)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è disattivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex))) allora (il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)""", [
                            DIBoolExpr("""Operatore Logico Not\n/*41,*/   MainClass_C1_parametro_P8 del campo  MainClass_C1     /*105,*/ è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,52,*/   l'argomento argomento_ave2 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V1 sia  maggiore di  /*54,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 1554""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V1 sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v1)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave2 sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave2 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a RossoGialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 1554""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V1 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v1)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v1)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 non sia  maggiore di  /*54,*/ 1554""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co5)  è maggiore di  (1554)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 8
 /*104,*/ o  che   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  minore di  /*55,*/ 132
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 8""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p2)  è minore di  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  minore di  /*55,*/ 132
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  minore di  /*55,*/ 132""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave1 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co5 sia  minore di  /*55,*/ 132""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T4 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave6 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(not db(db(self.macroSubclass_c2_macrova_m9(GlobalEnumeration.avvio,True,GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co2().get_valore() == 1121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_variabile_v7() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p6() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p6() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(argomento_ave2 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_parametro_p6() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(self.get_subclass_c2_contatore_co8().get_valore() < 1330, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(argomento_ave2 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v1() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_subclass_c2_variabile_v1() == 6, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(argomento_ave2 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c3() == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_subclass_c2_variabile_v1() == 2, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co5().get_valore() > 1554, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_subclass_c2_parametro_p2() < 8, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db((db((db((db(not db(argomento_ave1 == True, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == True, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co5().get_valore() < 132, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m9")
    def macroSubclass_c2_macrova_m9(self, argomento_a3, argomento_a5, argomento_a7, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c180 commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c180
        return GlobalEnumeration.c180
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c2_command_comm10(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm10')
    
    # for each automatic command, the corresponding method is created
    def eventSubclass_c2_command_comm2(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm2')
    
    def eventSubclass_c2_command_comm7(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm7')
    
    def eventSubclass_c2_command_comm8(self, notifying_process, argomento_ave3, argomento_ave5, argomento_ave6, argomento_ave9):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm8', argomento_ave3=argomento_ave3, argomento_ave5=argomento_ave5, argomento_ave6=argomento_ave6, argomento_ave9=argomento_ave9)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c5_prev(self.get_subclass_c2_previousco_c5())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())

class SubClass_C2_RecordHeaderR2(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled7, recordfiled8, recordfiled13):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled7(recordfiled7)
        self.set_recordfiled8(recordfiled8)
        self.set_recordfiled13(recordfiled13)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled7(self, recordfiled7):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"), recordfiled7)

    def set_recordfiled8(self, recordfiled8):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"), recordfiled8)

    def set_recordfiled13(self, recordfiled13):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"), recordfiled13)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled7(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"))

    def get_recordfiled8(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"))

    def get_recordfiled13(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"))



