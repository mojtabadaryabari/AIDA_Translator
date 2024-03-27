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

class SubClass_C2(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C2, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c2_previousva_pv1(0)
        self.set_subclass_c2_previousva_pv2(False)
        self.set_subclass_c2_previousva_pv3(0)
        self.set_subclass_c2_previousva_pv4(False)
        self.set_subclass_c2_restoreva_rv1(GlobalEnumeration.rosso)
        self.set_subclass_c2_variabile_v5(False)
        self.set_subclass_c2_variabile_v9(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6 : set(['eventSubclass_c2_command_comm4',]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
        if self.is_triggered('eventSubclass_c2_command_comm4'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm4',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm4',self.ManCmdResponse.NOOP)


        if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6):
        # for each manual command that can be received in Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6
            if self.is_triggered('eventSubclass_c2_command_comm4'):
                self.set_man_cmd_response('eventSubclass_c2_command_comm4',self.ManCmdResponse.BLOCKED)

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
        _State2__State2__stateSheet_1__permanence = 1
        _State1__State1__stateSheet_0__permanence = 2
        _State6__State6__stateSheet_3__permanence = 3
        _State6__State1__stateSheet_3__nominalActuation__transitionTo_0 = 4
        _State6__State2__stateSheet_3__nominalActuation__transitionTo_1 = 5
        _State6__State3__stateSheet_3__nominalActuation__transitionTo_2 = 6
        _State6__State6__stateSheet_3__nominalActuation__transitionTo_3 = 7
        _State3__State3__stateSheet_2__permanence = 8
        _State3__State6__stateSheet_2__nominalActuation__transitionTo_0 = 9
        _State3__State6__stateSheet_2__nominalActuation__transitionTo_1 = 10
        _State3__State1__stateSheet_2__nominalActuation__transitionTo_2 = 11
        _State3__State6__stateSheet_2__normalization__transitionTo_0 = 12

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c2_lista_l9, subclass_c2_parametro_p8):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l9(subclass_c2_lista_l9)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p8(subclass_c2_parametro_p8)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(4000)
        self.set_subclass_c2_restoreti_ti1_restore(4000)
        self.set_subclass_c2_timer_t3(3000)
        self.set_subclass_c2_timer_t5(45000)
        self.set_subclass_c2_timer_t7(4403000)
        self.set_subclass_c2_timer_t8(5215000)
        self.set_subclass_c2_timer_t9(3000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_timer_t3,self.subclass_c2_timer_t5,self.subclass_c2_timer_t7,self.subclass_c2_timer_t8,self.subclass_c2_timer_t9,]

        # initialize the counters
        self.set_subclass_c2_contatore_co10(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l9(self, subclass_c2_lista_l9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9",subclass_c2_lista_l9)


    # getters for record type parameters
    def get_subclass_c2_lista_l9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p8(self, subclass_c2_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p8",subclass_c2_parametro_p8)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p8")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c1(self, subclass_c2_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c1",subclass_c2_comando_c1)

    def set_subclass_c2_comando_c2(self, subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c2",subclass_c2_comando_c2)

    def set_subclass_c2_comando_c6(self, subclass_c2_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c6",subclass_c2_comando_c6)

    def set_subclass_c2_comando_c7(self, subclass_c2_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c7",subclass_c2_comando_c7)

    def set_subclass_c2_comando_c9(self, subclass_c2_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c9",subclass_c2_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c3")

    def get_subclass_c2_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c9")

    def get_subclass_c2_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10")

    def get_subclass_c2_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4")

    def get_subclass_c2_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5")

    def get_subclass_c2_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8")


    # setters for state variables
    def set_subclass_c2_previousco_c10_prev(self, subclass_c2_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev",subclass_c2_previousco_c10_prev)
    def set_subclass_c2_previousco_c4_prev(self, subclass_c2_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev",subclass_c2_previousco_c4_prev)
    def set_subclass_c2_previousco_c5_prev(self, subclass_c2_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev",subclass_c2_previousco_c5_prev)
    def set_subclass_c2_previousco_c8_prev(self, subclass_c2_previousco_c8_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8_prev",subclass_c2_previousco_c8_prev)
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
    def set_subclass_c2_variabile_v5(self, subclass_c2_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5",subclass_c2_variabile_v5)
    def set_subclass_c2_variabile_v9(self, subclass_c2_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9",subclass_c2_variabile_v9)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev")

    def get_subclass_c2_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev")

    def get_subclass_c2_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c5_prev")

    def get_subclass_c2_previousco_c8_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8_prev")

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

    def get_subclass_c2_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5")

    def get_subclass_c2_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_timer_t3(self, timerDuration):
        self.subclass_c2_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t3", self.memory)

    def set_subclass_c2_timer_t5(self, timerDuration):
        self.subclass_c2_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t5", self.memory)

    def set_subclass_c2_timer_t7(self, timerDuration):
        self.subclass_c2_timer_t7 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t7", self.memory)

    def set_subclass_c2_timer_t8(self, timerDuration):
        self.subclass_c2_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t8", self.memory)

    def set_subclass_c2_timer_t9(self, timerDuration):
        self.subclass_c2_timer_t9 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t9", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_timer_t3(self):
        return self.subclass_c2_timer_t3

    def get_subclass_c2_timer_t5(self):
        return self.subclass_c2_timer_t5

    def get_subclass_c2_timer_t7(self):
        return self.subclass_c2_timer_t7

    def get_subclass_c2_timer_t8(self):
        return self.subclass_c2_timer_t8

    def get_subclass_c2_timer_t9(self):
        return self.subclass_c2_timer_t9


    # setters for counters
    def set_subclass_c2_contatore_co10(self, counterInitValue):
        self.subclass_c2_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co10", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co10(self):
        return self.subclass_c2_contatore_co10



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 11215, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False , Tutte le seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 153


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 11215, Almeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False , Tutte le seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 153


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 11215""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*37,*/  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11215 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11215""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a  False""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11215""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (11215)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (13403))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (13403)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 11215""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (11215)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False , Tutte le seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 153


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False , Tutte le seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v5)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V5 è  uguale a  True""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V9 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 3""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (3))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (3)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 


 }""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è scaduto""", [
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T5 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T5 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (11)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 sia  uguale a  True""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 153""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (153)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (15))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (15)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 9 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 122


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T7 sia disattivo""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 9 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 122


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 9 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 9""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (9)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 122""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (9)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (5)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 122""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (122)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T7 sia disattivo""", [
                    ]),#1
                    ]),#3
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#4
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#5
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#6
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#7
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T3 non è scaduto, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#8
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#9
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12215 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 1""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12215 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12215 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12215 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12215""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è disattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12215""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (12215))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (12215)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T3 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13403""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (13403))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (13403)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 1""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (1)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#10
                    DIBoolExpr("""NAryLogicOP (AND)\n/*86,*/  Almeno una delle seguenti {
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 14, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 4


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 15


} /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 11215


} /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 124, Almeno una delle seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 


} /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215 /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 14, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 


}
}""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*86,*/  Almeno una delle seguenti {
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 14, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 4


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 15


} /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 11215


} /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 124, Almeno una delle seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 


} /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215 /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 14, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 


}
}""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 14, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 4


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 15


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   SubClass_C2_command_comm4"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
 /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 14, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 4


 }""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 14, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 4""", [
                    DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 14""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 4""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (4)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 15""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (15)""", [
                    ]),#0
                    ]),#2
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n/*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 11215


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   SubClass_C2_command_comm4"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V9 è  uguale a  True""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 }""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  /*36,*/ o  se il timer SubClass_C2_timer_T8 è scaduto""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a  True""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T5 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è attivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 sia attivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 13""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 11215""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (11215)""", [
                    ]),#0
                    ]),#2
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\n/*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*68,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 124, Almeno una delle seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   SubClass_C2_command_comm4"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*68,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 124, Almeno una delle seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*68,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 124""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*68,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*68,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è scaduto""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (2)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 12""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (12))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (12)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 124""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 124""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125, Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 non è  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v5)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False""", [
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 130""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a  False""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T5 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è attivo""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11321""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 125""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (125))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (125)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403, Almeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13403""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15, Solo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 13""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (13))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (13)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 15""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421 o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 14""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  uguale a  /*53,*/ 7""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (7)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 1421""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 }""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T7 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t7' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11540""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (11540)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11321""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (11321))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (11321)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è attivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T5 è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True""", [
                    DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 8""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 9""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403, Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T5 non è scaduto /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T5 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 6""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V9 non è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V9 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 135""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 11403""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (11403)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 non sia disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T5 sia disattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 10""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                    ]),#0
                    ]),#2
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\n/*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   SubClass_C2_command_comm4   /*77,*/
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215 /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 14, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   SubClass_C2_command_comm4"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215 /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 14, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215 /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 14""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                    DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 13""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215 /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 14""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215 /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo""", [
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13215""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è disattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 14""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (14)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è disattivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 14403""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (14403)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 1""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*35,*/  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 2""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V5 non è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v5)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T5 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T3 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è disattivo""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 }""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è scaduto""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215 /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (5)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 15215""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (15215)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T5 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T5 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co10 è  maggiore di  /*54,*/ 12403""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215 /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  diverso da  /*56,*/ 11215""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (11215))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (11215)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a  True""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (7)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 4""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (4)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co10 è  uguale a  /*53,*/ 13""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 9""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  minore di  /*55,*/ 3""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (3)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 154""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (154)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 7""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (7)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 sia  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                    ]),#0
                    ]),#2
                    ]),#3
                    ]),#0
                    ]),#11
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#12
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#13
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#14
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#15
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#16
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#17
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#18
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#19
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#20
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#21
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#22
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#23
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm2""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm2 del campo mainclass_c1 della lista subclass_c2_lista_l9'""", [
                    ]),#0
                    ]),#24
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[11], ),
                         effect=(self.dbs[23], ),
                         phase = TransPhase.Manuale
                         ),
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[14], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[13], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[9], ),
                         effect=(self.dbs[21], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[10], ),
                         effect=(self.dbs[22], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,
                         guard=(self.dbs[12], ),
                         effect=(self.dbs[24], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,
                         guard=(self.dbs[8], ),
                         effect=(self.dbs[20], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,
                         guard=(self.dbs[7], ),
                         effect=(self.dbs[19], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,
                         guard=(self.dbs[4], ),
                         effect=(self.dbs[16], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6,
                         guard=(self.dbs[5], ),
                         effect=(self.dbs[17], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[6], ),
                         effect=(self.dbs[18], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[15], ),
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

        self.set_subclass_c2_previousco_c10_prev(True)
        self.set_subclass_c2_previousco_c4_prev(GlobalEnumeration.rossogialloxverdex)
        self.set_subclass_c2_previousco_c5_prev(False)
        self.set_subclass_c2_previousco_c8_prev(False)
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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6):
                if(self.guard_NOMINAL_ACTUATION_state6_state3_000()):
                    self.curr_transition = self.Transition._State6__State3__stateSheet_3__nominalActuation__transitionTo_2
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2):
                if(self.guard_PERMANENCE_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6):
                if(self.guard_NOMINAL_ACTUATION_state6_state1_000()):
                    self.curr_transition = self.Transition._State6__State1__stateSheet_3__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state6_state2_000()):
                    self.curr_transition = self.Transition._State6__State2__stateSheet_3__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state6_000()):
                    self.curr_transition = self.Transition._State6__State6__stateSheet_3__nominalActuation__transitionTo_3
                elif(self.guard_PERMANENCE_state6_000()):
                    self.curr_transition = self.Transition._State6__State6__stateSheet_3__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3):
                if(self.guard_NORMALIZATION_state3_state6_000()):
                    self.curr_transition = self.Transition._State3__State6__stateSheet_2__normalization__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state3_state6_000()):
                    self.curr_transition = self.Transition._State3__State6__stateSheet_2__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state3_state6_001()):
                    self.curr_transition = self.Transition._State3__State6__stateSheet_2__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state3_state1_000()):
                    self.curr_transition = self.Transition._State3__State1__stateSheet_2__nominalActuation__transitionTo_2
                elif(self.guard_PERMANENCE_state3_000()):
                    self.curr_transition = self.Transition._State3__State3__stateSheet_2__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        # check what is the current transition
        # to set the current state and to execute the effects of the current transition
        if self.curr_transition == self.Transition.T_Undef:
            # if the current transition variable is not set, an exception will be raised
            return DISCARDED(self._logger, command, self.get_fsmState(), self._command_unexpected)
        elif self.curr_transition == self.Transition._State2__State2__stateSheet_1__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2)
            self.effect_PERMANENCE_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State6__State6__stateSheet_3__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6)
            self.effect_PERMANENCE_state6_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State6__State1__stateSheet_3__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state6_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State6__State2__stateSheet_3__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state6_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State6__State3__stateSheet_3__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_NOMINAL_ACTUATION_state6_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State6__State6__stateSheet_3__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6)
            self.effect_NOMINAL_ACTUATION_state6_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State3__stateSheet_2__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_PERMANENCE_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State6__stateSheet_2__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6)
            self.effect_NOMINAL_ACTUATION_state3_state6_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State6__stateSheet_2__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6)
            self.effect_NOMINAL_ACTUATION_state3_state6_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State1__stateSheet_2__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state3_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State6__stateSheet_2__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state6)
            self.effect_NORMALIZATION_state3_state6_000()
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
    
    def guard_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {68,} commento: {37,}  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 11215 commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 13403 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 11215, Almeno una delle seguenti { 
         commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False , Tutte le seguenti { 
         commento: {67,} commento: {37,}  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  uguale a  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 3 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 non è  diverso da RossoGiallo, Tutte le seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T5 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 11, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  uguale a  True 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 153
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  commento: {56,} 15
        
        
        }
        """
        return db((db(not db((db((db(not db(self.get_subclass_c2_variabile_v9() == True, self.dbs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_controllo_c3() == False, self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 11215, self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13403, self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 11215, self.dbs[2].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[0]) or db((db(not db((db(not db(self.get_subclass_c2_controllo_c3() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v5() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_subclass_c2_variabile_v5() == True, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v9() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p8() == 3, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t5().isScaduto(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(self.get_subclass_c2_timer_t5().isDisattivato(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 11, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_variabile_v5() == True, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isScaduto(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c3() == True, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 153, self.dbs[2].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1]), self.dbs[2].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 15, self.dbs[2].subs[1].subs[0].subs[0]), self.dbs[2].subs[1].subs[0]), self.dbs[2].subs[1])), self.dbs[2])
    
    def guard_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 9 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Almeno una delle seguenti { 
          se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 10 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 9 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 5 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  diverso da  False , Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  commento: {53,} 122
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T7 sia disattivo
        
        
        }
        """
        return db((db(not db((db(not db(self.get_subclass_c2_parametro_p8() < 9, self.dbs[3].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == False, self.dbs[3].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0]) or db(not db((db((db((db((db((db(self.get_consdef() == False, self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() > 10, self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == True, self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p8() > 9, self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() < 5, self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v9() == False, self.dbs[3].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 122, self.dbs[3].subs[0].subs[1].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[1]), self.dbs[3].subs[0].subs[1]), self.dbs[3].subs[0]) and db(self.get_subclass_c2_timer_t7().isDisattivato(), self.dbs[3].subs[1])), self.dbs[3])
    
    def guard_NOMINAL_ACTUATION_state3_state6_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[4])
    
    def guard_NOMINAL_ACTUATION_state3_state6_001(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[5])
    
    def guard_NOMINAL_ACTUATION_state3_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[6])
    
    def guard_NORMALIZATION_state3_state6_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[7])
    
    def guard_PERMANENCE_state6_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {36,}  se il timer SubClass_C2_timer_T3 non è scaduto, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  diverso da  True 
        
        
        }
        """
        return db((db(not db(not db(self.get_subclass_c2_timer_t3().isScaduto(), self.dbs[8].subs[0].subs[0].subs[0]), self.dbs[8].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v5() == True, self.dbs[8].subs[0].subs[1].subs[0]), self.dbs[8].subs[0].subs[1]), self.dbs[8].subs[0])), self.dbs[8])
    
    def guard_NOMINAL_ACTUATION_state6_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[9])
    
    def guard_NOMINAL_ACTUATION_state6_state2_000(self):
        """
        CNL corrispondente:
         {   se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 12215 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 13403, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  minore di  commento: {55,} 1
        
         }
        """
        return db((db(not db((db((db((db((db(self.get_consdef() == False, self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 12215, self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[10].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t3().isAttivato(), self.dbs[10].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13403, self.dbs[10].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[10].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[10].subs[0].subs[0].subs[1].subs[1])), self.dbs[10].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() < 1, self.dbs[10].subs[0].subs[1].subs[0]), self.dbs[10].subs[0].subs[1]), self.dbs[10].subs[0])), self.dbs[10])
    
    def guard_NOMINAL_ACTUATION_state6_state3_000(self):
        """
        CNL corrispondente:
         {  commento: {86,}  Almeno una delle seguenti {
         commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
         commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  diverso da  True , Almeno una delle seguenti { 
         commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 14, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 4
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 15
        
        
        } commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
         commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C9 non è  uguale a RossoGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  uguale a  True , Almeno una delle seguenti { 
         commento: {69,}  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  commento: {36,} o  se il timer SubClass_C2_timer_T3 è scaduto, Almeno una delle seguenti { 
         commento: {69,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  uguale a  True  commento: {36,} o  se il timer SubClass_C2_timer_T8 è scaduto, Solo una delle seguenti { 
         commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T5 non è scaduto, Solo una delle seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T9 è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T9 sia attivo
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  minore di  commento: {55,} 13
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  commento: {53,} 11215
        
        
        } commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
         commento: {68,} commento: {36,}  se il timer SubClass_C2_timer_T5 è scaduto commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 2 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 12 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 124, Almeno una delle seguenti { 
         commento: {69,} commento: {37,}  se la variabile SubClass_C2_variabile_V5 non è  diverso da  True  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 130 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T5 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 11321 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 125, Solo una delle seguenti { 
         commento: {68,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 13403, Almeno una delle seguenti { 
         commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 13 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 15, Solo una delle seguenti { 
         commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 14 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  uguale a  commento: {53,} 7 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 1421 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T7 non è scaduto, Tutte le seguenti { 
         commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 11540 commento: {36,} e  se il timer SubClass_C2_timer_T9 è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 11321 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T5 è attivo, Solo una delle seguenti { 
         commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 8 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T5 è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 13, Almeno una delle seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T5 non è scaduto commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  uguale a  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 135 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 11403, Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T5 non sia disattivo
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T5 sia disattivo
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  uguale a  commento: {53,} 10
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
        
        
        } commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   SubClass_C2_command_comm4   commento: {77,}
         commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 13 commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 13215 commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 14, Solo una delle seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T5 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 14403 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 1 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo commento: {36,} o  se il timer SubClass_C2_timer_T9 non è scaduto, Tutte le seguenti { 
         commento: {67,} commento: {35,}  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 2 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V5 non è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T8 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T5 non è disattivo, Tutte le seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T3 è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Tutte le seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T5 è scaduto, Tutte le seguenti { 
         commento: {69,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 5 commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 15215 commento: {36,} o  se il timer SubClass_C2_timer_T5 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  maggiore di  commento: {54,} 12403, Solo una delle seguenti { 
         commento: {67,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  diverso da  commento: {56,} 11215 commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  uguale a  True , Tutte le seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 7 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 4 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  uguale a  commento: {53,} 13, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  maggiore di  commento: {54,} 9
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  minore di  commento: {55,} 3
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 154
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 7
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  uguale a  commento: {53,} 13
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  diverso da  False 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
        
        
        }
        } }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventSubclass_c2_command_comm4'), self.dbs[11].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c3() == True, self.dbs[11].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 14, self.dbs[11].subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() == 4, self.dbs[11].subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[0].subs[1].subs[1].subs[1]), self.dbs[11].subs[0].subs[0].subs[1].subs[1]), self.dbs[11].subs[0].subs[0].subs[1]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 15, self.dbs[11].subs[0].subs[0].subs[2].subs[0]), self.dbs[11].subs[0].subs[0].subs[2]))
        res_manCmdCondition_1 = (db(self.is_triggered('eventSubclass_c2_command_comm4'), self.dbs[11].subs[0].subs[1].subs[0]) and db(not db((db((db((db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() == True, self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v9() == False, self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v9() == True, self.dbs[11].subs[0].subs[1].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_consdef() == False, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) or db((((db(not db((db(not db(self.get_subclass_c2_controllo_c3() == True, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t3().isScaduto(), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c2_controllo_c3() == True, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t8().isScaduto(), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(self.get_consdef() == False, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t5().isScaduto(), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() == False, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == True, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_timer_t8().isScaduto(), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() < 13, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0])) + (db(not db(not db(self.get_subclass_c2_controllo_c3() == True, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[11].subs[0].subs[1].subs[1].subs[1].subs[1])), self.dbs[11].subs[0].subs[1].subs[1].subs[1]), self.dbs[11].subs[0].subs[1].subs[1]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 11215, self.dbs[11].subs[0].subs[1].subs[2].subs[0]), self.dbs[11].subs[0].subs[1].subs[2]))
        res_manCmdCondition_2 = (db(self.is_triggered('eventSubclass_c2_command_comm4'), self.dbs[11].subs[0].subs[2].subs[0]) and db(not db((db((db((db(self.get_subclass_c2_timer_t5().isScaduto(), self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() == 2, self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 12, self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() == 124, self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[0]) or db((db(not db((db((db((db(not db(not db(self.get_subclass_c2_variabile_v5() == True, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_contatore_co10().get_valore() < 130, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c3() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t5().isAttivato(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() < 11321, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 125, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[0]) or db((((db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13403, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(self.get_consdef() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p8() == 6, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v9() == True, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() > 15, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db(self.get_consdef() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() < 14, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() == 7, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() > 1421, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_timer_t7().isScaduto(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 11540, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 11321, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t5().isAttivato(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db(self.get_subclass_c2_parametro_p8() < 8, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v9() == True, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() < 9, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t5().isScaduto(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(not db(self.get_subclass_c2_timer_t5().isScaduto(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p8() == 6, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v9() == True, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() == 135, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 11403, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t5().isDisattivato(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_consdef() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_variabile_v5() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t5().isDisattivato(), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_subclass_c2_parametro_p8() == 10, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[0])) + (db(not db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[2].subs[1].subs[1].subs[1])), self.dbs[11].subs[0].subs[2].subs[1].subs[1]), self.dbs[11].subs[0].subs[2].subs[1]) and db(not db(self.get_subclass_c2_controllo_c3() == True, self.dbs[11].subs[0].subs[2].subs[2].subs[0]), self.dbs[11].subs[0].subs[2].subs[2]))
        res_manCmdCondition_3 = (db(self.is_triggered('eventSubclass_c2_command_comm4'), self.dbs[11].subs[0].subs[3].subs[0]) and db(not db((db((db((db(self.get_subclass_c2_contatore_co10().get_valore() > 13, self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c3() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_contatore_co10().get_valore() == 13215, self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 14, self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[0]) or db((((db(not db((db((db((db(self.get_subclass_c2_timer_t5().isDisattivato(), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 14403, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p8() == 1, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() > 2, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c3() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_subclass_c2_variabile_v5() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t8().isAttivato(), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t5().isDisattivato(), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c2_timer_t3().isDisattivato(), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t5().isScaduto(), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_subclass_c2_parametro_p8() < 5, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 15215, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_timer_t5().isScaduto(), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() > 12403, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 11215, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c3() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c3() == True, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(self.get_subclass_c2_parametro_p8() > 7, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() < 4, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() == 13, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_parametro_p8() > 9, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_parametro_p8() < 3, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 154, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p8() == 7, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[1])), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_variabile_v5() == False, self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[1].subs[0]), self.dbs[11].subs[0].subs[3].subs[1].subs[1].subs[1]))) == 1), self.dbs[11].subs[0].subs[3].subs[1].subs[1]), self.dbs[11].subs[0].subs[3].subs[1]) and db(not db(self.get_subclass_c2_variabile_v9() == True, self.dbs[11].subs[0].subs[3].subs[2].subs[0]), self.dbs[11].subs[0].subs[3].subs[2]))
        if res_manCmdCondition_0:
            self.set_man_cmd_response('eventSubclass_c2_command_comm4',self.ManCmdResponse.PROCESSED)
        elif res_manCmdCondition_1:
            self.set_man_cmd_response('eventSubclass_c2_command_comm4',self.ManCmdResponse.PROCESSED)
        elif res_manCmdCondition_2:
            self.set_man_cmd_response('eventSubclass_c2_command_comm4',self.ManCmdResponse.PROCESSED)
        elif res_manCmdCondition_3:
            self.set_man_cmd_response('eventSubclass_c2_command_comm4',self.ManCmdResponse.PROCESSED)
        return db((db((db(res_manCmdCondition_0, self.dbs[11].subs[0].subs[0]) or db(res_manCmdCondition_1, self.dbs[11].subs[0].subs[1]) or db(res_manCmdCondition_2, self.dbs[11].subs[0].subs[2]) or db(res_manCmdCondition_3, self.dbs[11].subs[0].subs[3])), self.dbs[11].subs[0])), self.dbs[11])
    
    def guard_NOMINAL_ACTUATION_state6_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[12])
    
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
        
        Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
        Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
        Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NOMINAL_ACTUATION_state3_state6_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NOMINAL_ACTUATION_state3_state6_001(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NOMINAL_ACTUATION_state3_state1_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NORMALIZATION_state3_state6_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_PERMANENCE_state6_000(self):
        """
        CNL corrispondente:
        
        {
        
        Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,}
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NOMINAL_ACTUATION_state6_state1_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NOMINAL_ACTUATION_state6_state2_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NOMINAL_ACTUATION_state6_state3_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    def effect_NOMINAL_ACTUATION_state6_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm2    commento: {79,} }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm2
        for idx, it in enumerate(self.get_subclass_c2_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm2(self)
    
    # effect macros
    def macroSubclass_c2_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co10
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
        
        
         commento: {36,}  se il timer SubClass_C2_timer_T8 è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  True 
        
           
         commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  commento: {56,} 11 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 9 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  True 
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co10
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 1 commento: {35,} o  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo, commento: {66,} Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore SubClass_C2_contatore_Co10

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t8' è attivo )  e  
( negazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (False))) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_controllo_c3)  è uguale a  (False)) )  e  ( negazione di ((subclass_c2_controllo_c3)  è uguale a  (False)) ) )  e  
( il timer 'subclass_c2_timer_t9' è inattivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c3)  è uguale a  (False)) )  e  ( negazione di ((subclass_c2_controllo_c3)  è uguale a  (False)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 9 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  True 

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 9 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (11)))} )  e  ( (subclass_c2_parametro_p8)  è maggiore di  (9) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (11)))} )  e  ( (subclass_c2_parametro_p8)  è maggiore di  (9) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (11)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (9)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo, /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE , /*72,*/Azzera il contatore SubClass_C2_contatore_Co10
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
        if db(self.get_consdef() == False, di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co10().resetta()
        else:
            self.set_subclass_c2_comando_c7(GlobalEnumeration.rossogialloxverdex)
        #  /*36,*/  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C3 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  True
        if db((db((db(self.get_subclass_c2_timer_t8().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c3() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_controllo_c3() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v9(True)
        #  /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/ 11 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 9 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  True , /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  True 
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co10
        if db((db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() == 11, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() > 9, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_comando_c6(True)
        else:
            self.get_subclass_c2_contatore_co10().decrementa()
        #  /*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo, /*66,*/ Assegna al comando SubClass_C2_comando_C7 il valore RossoGialloxVerdex
        if db((db(self.get_subclass_c2_parametro_p8() == 1, di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_comando_c7(GlobalEnumeration.rossogialloxverdex)
    
    def macroSubclass_c2_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 1103 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 15215 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 13 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C2 il valore avvio
        
           
          se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  commento: {36,} o  se il timer SubClass_C2_timer_T5 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 1240 commento: {35,} e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo commento: {36,} o  se il timer SubClass_C2_timer_T5 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore  False 
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1103 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 15215 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore avvio""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1103 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 15215 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((subclass_c2_contatore_co10)  è uguale a  (1103)) )  o  
( (subclass_c2_contatore_co10)  è minore di  (15215) ) )  o  
( ( negazione di ((subclass_c2_contatore_co10)  è uguale a  (13)) )  e  
( negazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo)) ) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_contatore_co10)  è uguale a  (1103)) )  o  
( (subclass_c2_contatore_co10)  è minore di  (15215) ) )  o  
( ( negazione di ((subclass_c2_contatore_co10)  è uguale a  (13)) )  e  
( negazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c2_contatore_co10)  è uguale a  (1103)) )  o  
( (subclass_c2_contatore_co10)  è minore di  (15215) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (1103))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (1103)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (15215)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co10)  è uguale a  (13)) )  e  
( negazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1240 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T5 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1240 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T5 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( negazione di ((subclass_c2_variabile_v5)  è uguale a  (True)) ) )  o  
( ( ( negazione di (il timer 'subclass_c2_timer_t5' è scaduto) )  e  ( negazione di ((subclass_c2_contatore_co10)  è uguale a  (1240)) ) )  e  
( (subclass_c2_controllo_c9)  è uguale a  (rossogiallo) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( negazione di ((subclass_c2_variabile_v5)  è uguale a  (True)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c2_timer_t5' è scaduto) )  e  ( negazione di ((subclass_c2_contatore_co10)  è uguale a  (1240)) ) )  e  
( (subclass_c2_controllo_c9)  è uguale a  (rossogiallo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t5' è scaduto) )  e  ( negazione di ((subclass_c2_contatore_co10)  è uguale a  (1240)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t5' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (1240))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (1240)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t5' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1103 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 15215 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 13 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  diverso da RossoGiallo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C2 il valore avvio
        if db((db((db((db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 1103, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() < 15215, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c2(GlobalEnumeration.avvio)
        #  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T5 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1240 /*35,*/ e  se il controllo SubClass_C2_controllo_C9 è  uguale a RossoGiallo /*36,*/ o  se il timer SubClass_C2_timer_T5 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore  False
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_timer_t5().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 1240, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t5().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v9(False)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m2")
    def macroSubclass_c2_macrove_m2(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se la macro  SubClass_C2_macrova_M6 ( con argomento_a2   uguale a Rosso ,argomento_a6   uguale a Rosso ,argomento_a10   uguale a RossoGiallo  e argomento_a7   uguale a c75Giallo )   è  uguale a  True  commento: {40,} , Solo una delle seguenti { 
         commento: {61,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 144 e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T5 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 13032 commento: {36,} o  se il timer SubClass_C2_timer_T7 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  commento: {56,} 1415, Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  uguale a  commento: {53,} 3
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  commento: {56,} 15
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 4
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 5
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 13
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 11
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T3 non sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T5 non sia disattivo
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se la macro  SubClass_C2_macrova_M6 ( con argomento_a2   uguale a Rosso ,argomento_a6   uguale a Rosso ,argomento_a10   uguale a RossoGiallo  e argomento_a7   uguale a c75Giallo )   è  uguale a  True  /*40,*/ , Solo una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 144 e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415, Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se la macro  SubClass_C2_macrova_M6 ( con argomento_a2   uguale a Rosso ,argomento_a6   uguale a Rosso ,argomento_a10   uguale a RossoGiallo  e argomento_a7   uguale a c75Giallo )   è  uguale a  True  /*40,*/ , Solo una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 144 e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415, Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""EqualImpl\nla macro  SubClass_C2_macrova_M6 ( con argomento_a2   uguale a Rosso ,argomento_a6   uguale a Rosso ,argomento_a10   uguale a RossoGiallo  e argomento_a7   uguale a c75Giallo )   è  uguale a  True""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m6'"""),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 144 e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415, Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 144 e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415, Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 13


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 144 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 144 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 144""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (144)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415, Verifica che   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032 /*36,*/ o  se il timer SubClass_C2_timer_T7 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T5 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V5 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 13032""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (13032)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T7 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T7 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 è  diverso da  /*56,*/ 1415""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (1415)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  uguale a  /*53,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (15))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db(db(self.macroSubclass_c2_macrova_m6(GlobalEnumeration.rossogiallo,GlobalEnumeration.rosso,GlobalEnumeration.rosso,GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 144, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_subclass_c2_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 13032, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 1415, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db((db(self.get_subclass_c2_parametro_p8() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p8() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p8() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t5().isDisattivato(), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m3")
    def macroSubclass_c2_macrove_m3(self, argomento_ave1, argomento_ave3, argomento_ave4, argomento_ave5, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  minore di  commento: {55,} 11154, Solo una delle seguenti { 
         commento: {61,} commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da AC, Tutte le seguenti { 
         commento: {63,} commento: {35,}  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  diverso da  True , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P4 del campo  MainClass_C1     commento: {105,} è  uguale a AC commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 11, Solo una delle seguenti { 
         commento: {43,}  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è attivo, Verifica che   commento: {47,49,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  diverso da  commento: {56,} 9
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 1121
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  commento: {54,} 155
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T9 non sia disattivo
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 sia  maggiore di  commento: {54,} 4
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  uguale a  commento: {53,} 154
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 sia  diverso da  commento: {56,} 13032
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
        
        
         } Verifica che   commento: {47,48,52,}   l'argomento argomento_ave7 non  sia  diverso da  False  commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave7 non  sia  diverso da  False  commento: {39,} 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 7
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 9
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
        
        
         } Verifica che   commento: {48,51,52,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 1
         commento: {104,} o  che   l'argomento argomento_ave7 non  sia  diverso da  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co10 non sia  minore di  commento: {55,} 125
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11154, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da AC, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*47,48,52,*/   l'argomento argomento_ave7 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 9
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo


 } Verifica che   /*48,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 125""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11154, Solo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da AC, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*47,48,52,*/   l'argomento argomento_ave7 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 9
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  minore di  /*55,*/ 11154""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (11154)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da AC, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*47,48,52,*/   l'argomento argomento_ave7 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 9
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da AC, Tutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 }""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo


 } Verifica che   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11, Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 è  uguale a  True ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C3 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  diverso da  True , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (ac)) allora (negazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True)))""", [
                            DIBoolExpr("""EqualImpl\n/*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     /*105,*/ è  uguale a AC""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V5 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V5 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 11""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*43,*/  se MainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T7 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V5 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1121""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (1121)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  maggiore di  /*54,*/ 155""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,48,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 sia  maggiore di  /*54,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 154""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co10 sia  diverso da  /*56,*/ 13032""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (13032)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,52,*/   l'argomento argomento_ave7 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 9
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/   l'argomento argomento_ave7 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  diverso da  False  /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/   l'argomento argomento_ave7 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,52,*/   l'argomento argomento_ave7 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 9
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 125""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave7 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 125""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave7 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C9 sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co10 non sia  minore di  /*55,*/ 125""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co10)  è minore di  (125)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 11154, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9()) if db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_subclass_c2_parametro_p8() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 1121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() > 155, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db((db(self.get_subclass_c2_parametro_p8() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() == 154, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 13032, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(not db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p8() == 7, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p8() == 9, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 1, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(not db(not db(argomento_ave7 == True, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() < 125, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m5")
    def macroSubclass_c2_macrove_m5(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  uguale a c270x commento: {36,} o  se il timer SubClass_C2_timer_T5 non è attivo commento: {36,} o  se il timer SubClass_C2_timer_T7 non è scaduto, Solo una delle seguenti { 
         commento: {62,} commento: {38,}  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 14403,  commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 2 commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  commento: {53,} 14 commento: {38,} e  se il contatore SubClass_C2_contatore_Co10 è  minore di  commento: {55,} 1121 commento: {36,} e  se il timer SubClass_C2_timer_T5 è attivo, Almeno una delle seguenti { 
          se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T7 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
        
        
         } Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  diverso da  commento: {56,} 7
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  uguale a  commento: {53,} 11
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  commento: {56,} 1154
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T5 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T7 non è scaduto, Solo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121 /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T7 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*47,48,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 11
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo


 } Verifica che   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 1154
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T5 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T7 non è scaduto, Solo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121 /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T7 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*47,48,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 11
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T5 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T7 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a c270x /*36,*/ o  se il timer SubClass_C2_timer_T5 non è attivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T5 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T7 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121 /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T7 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 } Verifica che   /*47,48,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 11
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121 /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T7 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121 /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403,  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (14403)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (avviox))) allora (il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l9' è inattivo)""", [
                            DIBoolExpr("""Operatore Logico Not\n/*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     è  diverso da avviox""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l9' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121 /*36,*/ e  se il timer SubClass_C2_timer_T5 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14 /*38,*/ e  se il contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co10 è  minore di  /*55,*/ 1121""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T5 è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T7 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è scaduto, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T7 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T5 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T7 è attivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T7 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T5 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 11
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 11
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  uguale a  /*53,*/ 11""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a RossoGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 1154
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 1154
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  diverso da  /*56,*/ 1154""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co10)  è uguale a  (1154))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co10)  è uguale a  (1154)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  diverso da RossoGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c9)  è uguale a  (rossogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (rossogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 14403, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p8() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() < 1121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t5().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db(not db(not db(self.get_subclass_c2_parametro_p8() == 7, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co10().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(not db(self.get_subclass_c2_contatore_co10().get_valore() == 1154, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m8")
    def macroSubclass_c2_macrove_m8(self, argomento_ave1, argomento_ave10, argomento_ave4, argomento_ave5, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {45,}  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,} 13215 o  se l'argomento argomento_ave10 è  uguale a  False  commento: {39,}  o  se l'argomento argomento_ave10 è  uguale a  False  commento: {39,} , Solo una delle seguenti { 
         commento: {61,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  commento: {56,}  state1  commento: {38,} o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  commento: {54,} 14403, Tutte le seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
         commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è attivo, Verifica che   commento: {48,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
         commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  commento: {54,} 132
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T8 non sia attivo
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co10 sia  minore di  commento: {55,} 1115
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  commento: {54,} 2
        
        
         } Verifica che   commento: {48,52,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
         commento: {104,} o  che   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex commento: {,} 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  commento: {54,} 4
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 13215 o  se l'argomento argomento_ave10 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave10 è  uguale a  False  /*39,*/ , Solo una delle seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132


 } Verifica che   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 2


 } Verifica che   /*48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex /*,*/ 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 13215 o  se l'argomento argomento_ave10 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave10 è  uguale a  False  /*39,*/ , Solo una delle seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132


 } Verifica che   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 2


 } Verifica che   /*48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 13215 o  se l'argomento argomento_ave10 è  uguale a  False  /*39,*/  o  se l'argomento argomento_ave10 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*45,*/  se  MainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 13215 o  se l'argomento argomento_ave10 è  uguale a  False""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_contatore_Co1 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 13215""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (13215)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave10 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave10 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132


 } Verifica che   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 2


 } Verifica che   /*48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132


 } Verifica che   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 2


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403""", [
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co10 non è  maggiore di  /*54,*/ 14403""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (14403)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132


 } Verifica che   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 2


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T7 è attivo, Tutte le seguenti { 
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T7 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V5 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V5 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C3 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T7 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo, Verifica che   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l9' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V9 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C3 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co10 non sia  maggiore di  /*54,*/ 132""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co10)  è maggiore di  (132)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,51,*/  /*,*/  il controllo SubClass_C2_controllo_C9 sia  uguale a RossoGiallo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T8 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore SubClass_C2_contatore_Co10 sia  minore di  /*55,*/ 1115""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave8 non  sia  uguale a RossoGialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (rossogialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() == 13215, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave10 == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave10 == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 14403, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p8() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(argomento_ave10 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co10().get_valore() > 132, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.rossogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co10().get_valore() < 1115, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db(not db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(argomento_ave8 == GlobalEnumeration.rossogialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p8() > 4, di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m1")
    def macroSubclass_c2_macrova_m1(self, argomento_a1, argomento_a4, argomento_a5, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m10")
    def macroSubclass_c2_macrova_m10(self, argomento_a1, argomento_a3, argomento_a4, argomento_a5, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P4 del campo  MainClass_C1     è  uguale a AC  , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     è  uguale a AC  , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     è  uguale a AC""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (False))} )  e  ( negazione di ((subclass_c2_variabile_v5)  è uguale a  (False)) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (False))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v9)  è uguale a  (False)) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (ac)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (ac)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (ac)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (ac)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l9')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m10_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a  False ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P4 del campo  MainClass_C1     è  uguale a AC  , assegna alla macro il valore  False
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db((db(not db(self.get_subclass_c2_variabile_v9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9()) if db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c2_macrova_m4")
    def macroSubclass_c2_macrova_m4(self, argomento_a2, argomento_a3, argomento_a6, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGialloxVerdex commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGialloxVerdex
        return GlobalEnumeration.rossogialloxverdex
    
    @srf_value_macro("macroSubclass_c2_macrova_m6")
    def macroSubclass_c2_macrova_m6(self, argomento_a10, argomento_a2, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c2_macrova_m7")
    def macroSubclass_c2_macrova_m7(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[} commento: {35,}  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True  commento: {44,} o  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True  /*44,*/ o  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True  /*44,*/ o  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c3)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo SubClass_C2_controllo_C3 non è  diverso da  True  /*44,*/ o  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a c270x , assegna alla macro il valore  False
        if db((db(not db(not db(self.get_subclass_c2_controllo_c3() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c2_command_comm4(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm4')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c10_prev(self.get_subclass_c2_previousco_c10())
        self.set_subclass_c2_previousco_c4_prev(self.get_subclass_c2_previousco_c4())
        self.set_subclass_c2_previousco_c5_prev(self.get_subclass_c2_previousco_c5())
        self.set_subclass_c2_previousco_c8_prev(self.get_subclass_c2_previousco_c8())
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
    def init_configuration(self, mainclass_c1, recordfiled5, recordfiled3, recordfiled4):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled5(recordfiled5)
        self.set_recordfiled3(recordfiled3)
        self.set_recordfiled4(recordfiled4)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled5(self, recordfiled5):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"), recordfiled5)

    def set_recordfiled3(self, recordfiled3):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"), recordfiled3)

    def set_recordfiled4(self, recordfiled4):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"), recordfiled4)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled5(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"))

    def get_recordfiled3(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"))

    def get_recordfiled4(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"))



