# Codice del modello 'TestCase12', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_subclass_c2_previousva_pv1(GlobalEnumeration.avanzamento)
        self.set_subclass_c2_previousva_pv2(False)
        self.set_subclass_c2_previousva_pv3(False)
        self.set_subclass_c2_previousva_pv4(0)
        self.set_subclass_c2_previousva_pv5(0)
        self.set_subclass_c2_restoreva_rv1(False)
        self.set_subclass_c2_variabile_v2(False)
        self.set_subclass_c2_variabile_v3(0)
        self.set_subclass_c2_variabile_v6(GlobalEnumeration.c75giallo)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
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
        _State2__State2__stateSheet_1__permanence = 1
        _State1__State1__stateSheet_0__permanence = 2
        _State1__State3__stateSheet_0__nominalActuation__transitionTo_0 = 3
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_1 = 4
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_2 = 5
        _State1__State3__stateSheet_0__nominalActuation__transitionTo_3 = 6
        _State1__State3__stateSheet_0__nominalActuation__transitionTo_4 = 7
        _State1__State3__stateSheet_0__normalization__transitionTo_0 = 8
        _State4__State4__stateSheet_3__permanence = 9
        _State3__State3__stateSheet_2__permanence = 10
        _State3__State2__stateSheet_2__nominalActuation__transitionTo_0 = 11
        _State3__State1__stateSheet_2__nominalActuation__transitionTo_1 = 12
        _State3__State2__stateSheet_2__nominalActuation__transitionTo_2 = 13
        _State3__State2__stateSheet_2__nominalActuation__transitionTo_3 = 14
        _State3__State3__stateSheet_2__nominalActuation__transitionTo_4 = 15
        _State3__State4__stateSheet_2__normalization__transitionTo_0 = 16

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c2_lista_l2, subclass_c2_lista_l4, subclass_c2_lista_l6, subclass_c2_parametro_p5, subclass_c2_parametro_p6, subclass_c2_parametro_p8):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l2(subclass_c2_lista_l2)
        self.set_subclass_c2_lista_l4(subclass_c2_lista_l4)
        self.set_subclass_c2_lista_l6(subclass_c2_lista_l6)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p5(subclass_c2_parametro_p5)
        self.set_subclass_c2_parametro_p6(subclass_c2_parametro_p6)
        self.set_subclass_c2_parametro_p8(subclass_c2_parametro_p8)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(530000)
        self.set_subclass_c2_restoreti_ti1_restore(530000)
        self.set_subclass_c2_restoreti_ti2(34000)
        self.set_subclass_c2_restoreti_ti2_restore(34000)
        self.set_subclass_c2_restoreti_ti3(35000)
        self.set_subclass_c2_restoreti_ti3_restore(35000)
        self.set_subclass_c2_restoreti_ti4(11230000)
        self.set_subclass_c2_restoreti_ti4_restore(11230000)
        self.set_subclass_c2_timer_t1(24000)
        self.set_subclass_c2_timer_t8(5512000)
        self.set_subclass_c2_timer_t9(1000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_restoreti_ti3,self.subclass_c2_restoreti_ti3_restore,self.subclass_c2_restoreti_ti4,self.subclass_c2_restoreti_ti4_restore,self.subclass_c2_timer_t1,self.subclass_c2_timer_t8,self.subclass_c2_timer_t9,]

        # initialize the counters
        self.set_subclass_c2_contatore_co1(0)
        self.set_subclass_c2_contatore_co7(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l2(self, subclass_c2_lista_l2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2",subclass_c2_lista_l2)

    def set_subclass_c2_lista_l4(self, subclass_c2_lista_l4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4",subclass_c2_lista_l4)

    def set_subclass_c2_lista_l6(self, subclass_c2_lista_l6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l6",subclass_c2_lista_l6)


    # getters for record type parameters
    def get_subclass_c2_lista_l2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2")

    def get_subclass_c2_lista_l4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4")

    def get_subclass_c2_lista_l6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l6")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p5(self, subclass_c2_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5",subclass_c2_parametro_p5)

    def set_subclass_c2_parametro_p6(self, subclass_c2_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6",subclass_c2_parametro_p6)

    def set_subclass_c2_parametro_p8(self, subclass_c2_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p8",subclass_c2_parametro_p8)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5")

    def get_subclass_c2_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6")

    def get_subclass_c2_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p8")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c3(self, subclass_c2_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c3",subclass_c2_comando_c3)

    def set_subclass_c2_comando_c6(self, subclass_c2_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c6",subclass_c2_comando_c6)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c1")

    def get_subclass_c2_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c10")

    def get_subclass_c2_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c2")

    def get_subclass_c2_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c5")

    def get_subclass_c2_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c8")

    def get_subclass_c2_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4")


    # setters for state variables
    def set_subclass_c2_previousco_c4_prev(self, subclass_c2_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev",subclass_c2_previousco_c4_prev)
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
    def set_subclass_c2_previousva_pv5(self, subclass_c2_previousva_pv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5",subclass_c2_previousva_pv5)
    def set_subclass_c2_previousva_pv5_prev(self, subclass_c2_previousva_pv5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5_prev",subclass_c2_previousva_pv5_prev)
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_variabile_v2(self, subclass_c2_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2",subclass_c2_variabile_v2)
    def set_subclass_c2_variabile_v3(self, subclass_c2_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v3",subclass_c2_variabile_v3)
    def set_subclass_c2_variabile_v6(self, subclass_c2_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6",subclass_c2_variabile_v6)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev")

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

    def get_subclass_c2_previousva_pv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5")

    def get_subclass_c2_previousva_pv5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv5_prev")

    def get_subclass_c2_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1")

    def get_subclass_c2_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1_restore")

    def get_subclass_c2_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v2")

    def get_subclass_c2_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v3")

    def get_subclass_c2_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_restoreti_ti2(self, timerDuration):
        self.subclass_c2_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2", self.memory)

    def set_subclass_c2_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2_restore", self.memory)

    def set_subclass_c2_restoreti_ti3(self, timerDuration):
        self.subclass_c2_restoreti_ti3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti3", self.memory)

    def set_subclass_c2_restoreti_ti3_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti3_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti3_restore", self.memory)

    def set_subclass_c2_restoreti_ti4(self, timerDuration):
        self.subclass_c2_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti4", self.memory)

    def set_subclass_c2_restoreti_ti4_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti4_restore", self.memory)

    def set_subclass_c2_timer_t1(self, timerDuration):
        self.subclass_c2_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t1", self.memory)

    def set_subclass_c2_timer_t8(self, timerDuration):
        self.subclass_c2_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t8", self.memory)

    def set_subclass_c2_timer_t9(self, timerDuration):
        self.subclass_c2_timer_t9 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t9", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_restoreti_ti2(self):
        return self.subclass_c2_restoreti_ti2

    def get_subclass_c2_restoreti_ti2_restore(self):
        return self.subclass_c2_restoreti_ti2_restore

    def get_subclass_c2_restoreti_ti3(self):
        return self.subclass_c2_restoreti_ti3

    def get_subclass_c2_restoreti_ti3_restore(self):
        return self.subclass_c2_restoreti_ti3_restore

    def get_subclass_c2_restoreti_ti4(self):
        return self.subclass_c2_restoreti_ti4

    def get_subclass_c2_restoreti_ti4_restore(self):
        return self.subclass_c2_restoreti_ti4_restore

    def get_subclass_c2_timer_t1(self):
        return self.subclass_c2_timer_t1

    def get_subclass_c2_timer_t8(self):
        return self.subclass_c2_timer_t8

    def get_subclass_c2_timer_t9(self):
        return self.subclass_c2_timer_t9


    # setters for counters
    def set_subclass_c2_contatore_co1(self, counterInitValue):
        self.subclass_c2_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co1", self.memory)

    def set_subclass_c2_contatore_co7(self, counterInitValue):
        self.subclass_c2_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co7", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co1(self):
        return self.subclass_c2_contatore_co1

    def get_subclass_c2_contatore_co7(self):
        return self.subclass_c2_contatore_co7



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 8 /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1151 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 sia  uguale a  /*53,*/ 6


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 10""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 8 /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto, Solo una delle seguenti { 
 /*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1151 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 sia  uguale a  /*53,*/ 6


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*37,*/  se la variabile SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 8 /*36,*/ o  se il timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 8""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1151 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 sia  uguale a  /*53,*/ 6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1151 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1151""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P6 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 1151""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (1151)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C8 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 sia  uguale a  /*53,*/ 6""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P8 non sia  uguale a  /*53,*/ 10""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (10)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#3
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T9 è attivo /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 non sia scaduto""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T9 è attivo /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Solo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T9 è attivo /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T9 è attivo /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è attivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 1 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 1""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C8 è  uguale a  False""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P8 è  uguale a  /*53,*/ 7""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C8 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V2 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 non sia scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#4
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#5
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#6
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#7
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#8
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 12230 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11451 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 132 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 12230 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11451 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 132 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, Tutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 12230 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11451 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 132 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 12230 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11451 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 132""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 12230""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo""", [
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 13""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 12230""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (12230))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (12230)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11451 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 132""", [
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11451""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 132""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (132))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (132)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Tutte le seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è disattivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 8""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (8)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è attivo""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T9 è scaduto""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*34,*/  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo""", [
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è disattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 6""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (6)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T1 è attivo""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*36,*/  se il timer SubClass_C2_timer_T1 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T1 è disattivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T1 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 11""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4, Tutte le seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 1530""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co7)  è maggiore di  (1530)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 6""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 11""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (11)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 4""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (4)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 6""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v3)  è maggiore di  (6)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è disattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  minore di  /*55,*/ 10""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (10)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 sia  uguale a  False""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 15""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (15)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  /*54,*/ 6""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v3)  è maggiore di  (6)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a  True""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox""", [
                    ]),#1
                    ]),#9
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da avanzamentox""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 è attivo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 3""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T1 è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto, Almeno una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*35,*/  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 14""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230 /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox""", [
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1230""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7 /*36,*/ e  se il timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 7""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (7)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V2 è  uguale a  False""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T8 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  diverso da avanzamentox""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#10
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#11
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#12
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#13
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#14
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T9 è disattivo, Solo una delle seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 1330 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 1, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da avanzamentox


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 non sia attivo""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*36,*/  se il timer SubClass_C2_timer_T9 è disattivo, Solo una delle seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 1330 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 1, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da avanzamentox


 }""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è disattivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 1330 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 1, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da avanzamentox


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 1330 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False , Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 1, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  uguale a  False 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 1330 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 1330 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 1330""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co1)  è maggiore di  (1330)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 1, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  uguale a  False""", [
                    DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 1""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 sia  uguale a  False""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da avanzamentox""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T9 non sia attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#15
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 10 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a avanzamentox""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 10 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 10 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 10 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox""", [
                    DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 10""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V3 non è  maggiore di  /*54,*/ 5""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v3)  è maggiore di  (5)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 sia  uguale a avanzamentox""", [
                    ]),#1
                    ]),#16
                    DIStatement("""ITStatement\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )"""),#1
                    ]),#17
                    DIStatement("""ITStatement\n/*73,*/

   
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 122, /*69,*/Disattiva il timer SubClass_C2_timer_T9""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/

   
 /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 122""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti3_restore' è attivo""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co1)  è minore di  (122)""", [
                    ]),#1
                    ]),#0
                    ]),#18
                    DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     è  uguale a RossoGialloaVerdea /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 13304, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     è  uguale a RossoGialloaVerdea /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 13304""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v6)  è uguale a  (gialloxverdex) )  e  
( per ognuna delle seguenti {se ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)) allora (il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)} )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)) allora (il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)) allora (il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è uguale a  (13304))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (13304)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#19
                    DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 3 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C2_timer_T1

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 3 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)))} )  o  
( ( negazione di ((subclass_c2_variabile_v3)  è uguale a  (3)) )  e  
( negazione di (negazione di ((subclass_c2_parametro_p8)  è uguale a  (1))) ) )""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)))}""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v3)  è uguale a  (3)) )  e  
( negazione di (negazione di ((subclass_c2_parametro_p8)  è uguale a  (1))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è uguale a  (3))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (3)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p8)  è uguale a  (1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (1))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (1)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_controllo_c8)  è uguale a  (False) )  e  ( (subclass_c2_variabile_v3)  è maggiore di  (3) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_controllo_c8)  è uguale a  (False) )  e  ( (subclass_c2_variabile_v3)  è maggiore di  (3) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v3)  è maggiore di  (3)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#20
                    DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True , /*68,*/Attiva il timer SubClass_C2_timer_T9

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( il timer 'subclass_c2_restoreti_ti2_restore' è attivo )  e  
( il timer 'subclass_c2_timer_t9' è inattivo ) )  o  
( negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t1' è inattivo) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'subclass_c2_restoreti_ti2_restore' è attivo )  e  
( il timer 'subclass_c2_timer_t9' è inattivo ) )  o  
( negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_restoreti_ti2_restore' è attivo )  e  
( il timer 'subclass_c2_timer_t9' è inattivo )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti2_restore' è attivo""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                    ]),#21
                    DIStatement("""ITStatement\n/*73,*/


 /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 8 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False ,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 8 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( negazione di ((subclass_c2_parametro_p8)  è uguale a  (8)) ) )  o  
( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  o  
( negazione di ((subclass_c2_parametro_p8)  è uguale a  (8)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (8))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (8)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (False)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )"""),#1
                    ]),#22
                    DIStatement("""ITStatement\n/*73,*/

   
 /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'subclass_c2_timer_t1' è inattivo) )  o  
( ( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#23
                    DIStatement("""ITEStatementImpl\n/*36,*/  se il timer SubClass_C2_timer_T9 è attivo,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T10 del campo  MainClass_C1     /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , /*68,*/Attiva il timer SubClass_C2_timer_T9

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T9 è attivo,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T10 del campo  MainClass_C1     /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t9' è attivo )  e  ( per ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1))} )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1))""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                    ]),#24
                    DIStatement("""ITEStatementImpl\n/*73,*/


 /*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 12123, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 1

 ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T8""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/


 /*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 12123""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co1)  è maggiore di  (12123)""", [
                    ]),#1
                    ]),#0
                    ]),#25
                    DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 150, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 8

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 150""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (False)))}""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è uguale a  (150))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (150)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#26
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto,  Applica gli effetti
       della macro SubClass_C2_macroef_M6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti3_restore' è attivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((subclass_c2_controllo_c8)  è uguale a  (False)) ) )  e  
( negazione di (il timer 'subclass_c2_timer_t1' è scaduto) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((subclass_c2_controllo_c8)  è uguale a  (False)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M6"""),#1
                    ]),#27
                    DIStatement("""ITStatement\n/*73,*/

   
 /*34,*/  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 3""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*34,*/  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_variabile_v3)  è minore di  (7) )  e  ( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) ) )  e  
( (subclass_c2_variabile_v6)  è uguale a  (gialloxverdex) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v3)  è minore di  (7) )  e  ( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (7)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#28
                    DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T1 è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo, /*69,*/Disattiva il timer SubClass_C2_timer_T9""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T1 è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'subclass_c2_timer_t9' è scaduto) )  o  
( ( negazione di ((subclass_c2_variabile_v3)  è uguale a  (6)) )  e  
( il timer 'subclass_c2_timer_t1' è scaduto ) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v3)  è uguale a  (6)) )  e  
( il timer 'subclass_c2_timer_t1' è scaduto )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è uguale a  (6))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (6)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t1' è scaduto) )  e  
( negazione di (il timer 'subclass_c2_timer_t9' è inattivo) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#29
                    DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox

 ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co7""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True))} )  e  
( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) ) )  o  
( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True))} )  e  
( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True))}""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#30
                    DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 12451 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 12451 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (11)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (12451)) ) )  o  
( il timer 'subclass_c2_timer_t9' è inattivo ) )  o  
( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (11)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (12451)) ) )  o  
( il timer 'subclass_c2_timer_t9' è inattivo )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (11)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (12451)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co7)  è maggiore di  (11)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è maggiore di  (11))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co7)  è maggiore di  (11)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è uguale a  (12451))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (12451)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t8' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#31
                    DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 4,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 15230, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1 , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 1""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 4,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 15230, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p8)  è uguale a  (4)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (4))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (4)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (15230))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (15230))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (15230)""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#32
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo, /*72,*/Azzera il contatore SubClass_C2_contatore_Co1""", [
                    DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo""", [
                    ]),#0
                    ]),#33
                    DIStatement("""ITStatement\n/*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex, /*68,*/Attiva il timer SubClass_C2_timer_T9""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    ]),#34
                    DIStatement("""ITEStatementImpl\n/*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 12, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 12""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (False)))}""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è uguale a  (12))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (12)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#35
                    DIStatement("""ITStatement\n/*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 13 /*36,*/ o  se il timer SubClass_C2_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  uguale a  /*53,*/ 1251 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 13 /*36,*/ o  se il timer SubClass_C2_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  uguale a  /*53,*/ 1251 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( negazione di ((subclass_c2_contatore_co1)  è maggiore di  (13)) )  o  
( il timer 'subclass_c2_timer_t1' è inattivo ) )  o  
( negazione di ((subclass_c2_parametro_p8)  è minore di  (5)) ) )  o  
( (subclass_c2_contatore_co1)  è uguale a  (1251) ) )  o  
( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((subclass_c2_contatore_co1)  è maggiore di  (13)) )  o  
( il timer 'subclass_c2_timer_t1' è inattivo ) )  o  
( negazione di ((subclass_c2_parametro_p8)  è minore di  (5)) ) )  o  
( (subclass_c2_contatore_co1)  è uguale a  (1251) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_contatore_co1)  è maggiore di  (13)) )  o  
( il timer 'subclass_c2_timer_t1' è inattivo ) )  o  
( negazione di ((subclass_c2_parametro_p8)  è minore di  (5)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c2_contatore_co1)  è maggiore di  (13)) )  o  
( il timer 'subclass_c2_timer_t1' è inattivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è maggiore di  (13))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co1)  è maggiore di  (13)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è minore di  (5))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (5)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (1251)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#1
                    ]),#0
                    ]),#36
                    DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T1""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (avanzamentox)""", [
                    ]),#1
                    ]),#0
                    ]),#37
                    DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co3 del campo  MainClass_C1     è  uguale a  /*53,*/ 12, /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co3 del campo  MainClass_C1     è  uguale a  /*53,*/ 12""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (12)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (12)) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (12)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#38
                    DIStatement("""ITStatement\nse la macro  SubClass_C2_macrova_M9 ( con argomento_a2   uguale a True ,argomento_a7   uguale a GialloGiallo ,argomento_a3   uguale a avanzamento  e argomento_a4   uguale a c75Giallo )  non  è  diverso da avanzamentox /*40,*/ ,  Applica gli effetti
       della macro SubClass_C2_macroef_M9""", [
                    DIBoolExpr("""Operatore Logico Not\nla macro  SubClass_C2_macrova_M9 ( con argomento_a2   uguale a True ,argomento_a7   uguale a GialloGiallo ,argomento_a3   uguale a avanzamento  e argomento_a4   uguale a c75Giallo )  non  è  diverso da avanzamentox""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9')  è uguale a  (avanzamentox)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m9'"""),#0
                    ]),#0
                    ]),#0
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M9"""),#1
                    ]),#39
                    DIStatement("""ITStatement\n/*73,*/

   
 /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#40
                    DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co1

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( (subclass_c2_variabile_v3)  è uguale a  (2) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (subclass_c2_controllo_c8)  è uguale a  (False) ) )  e  
( negazione di (negazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( (subclass_c2_variabile_v3)  è uguale a  (2) ) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( (subclass_c2_controllo_c8)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( (subclass_c2_variabile_v3)  è uguale a  (2) ) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( (subclass_c2_variabile_v3)  è uguale a  (2) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (2)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#1
                    ]),#0
                    ]),#41
                    DIStatement("""ITEStatementImpl\nse la macro  SubClass_C2_macrova_M1 ( con argomento_a1   uguale a c75Giallo ,argomento_a8   uguale a GialloxVerdex  e argomento_a10   uguale a GialloxVerdex )   è  diverso da GialloxVerdex /*40,*/ , /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1

 ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co1""", [
                    DIBoolExpr("""Operatore Logico Not\nla macro  SubClass_C2_macrova_M1 ( con argomento_a1   uguale a c75Giallo ,argomento_a8   uguale a GialloxVerdex  e argomento_a10   uguale a GialloxVerdex )   è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m1')  è uguale a  (gialloxverdex)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m1'"""),#0
                    ]),#0
                    ]),#0
                    ]),#42
                    DIStatement("""ITStatement\nse la macro  SubClass_C2_macrova_M5 ( con argomento_a8   uguale a avanzamento ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a GialloaVerdea  e argomento_a6   uguale a GialloaVerdea )   è  uguale a  False  /*40,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1512 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  uguale a avanzamentox, /*68,*/Attiva il timer SubClass_C2_timer_T8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse la macro  SubClass_C2_macrova_M5 ( con argomento_a8   uguale a avanzamento ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a GialloaVerdea  e argomento_a6   uguale a GialloaVerdea )   è  uguale a  False  /*40,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1512 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  uguale a avanzamentox""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m5')  è uguale a  (False)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m5'"""),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_contatore_co1)  è minore di  (1512)) )  e  ( (subclass_c2_controllo_c8)  è uguale a  (False) ) )  e  
( negazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co1)  è minore di  (1512)) )  e  ( (subclass_c2_controllo_c8)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è minore di  (1512))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co1)  è minore di  (1512)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#43
                    DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 4

 ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo)} )  e  
( il timer 'subclass_c2_timer_t9' è attivo )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo)}""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#1
                    ]),#0
                    ]),#44
                    DIStatement("""ITStatement\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)} )  e  ( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) ) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (False))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)} )  e  ( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) )""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)}""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (False)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#45
                    DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 9

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M9""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti2_restore' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M9"""),#1
                    ]),#46
                    DIStatement("""ITStatement\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer SubClass_C2_timer_T1""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    ]),#47
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False ,  Applica gli effetti
       della macro SubClass_C2_macroef_M9  /*73,*/

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M9"""),#1
                    ]),#48
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 11123 /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 8 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  False ,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) /*73,*/

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 11123 /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 8 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( (subclass_c2_variabile_v2)  è uguale a  (False) )  e  
( negazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (14))) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((subclass_c2_contatore_co1)  è minore di  (11123)) ) )  o  
( negazione di ((subclass_c2_variabile_v3)  è minore di  (8)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (subclass_c2_variabile_v2)  è uguale a  (False) )  e  
( negazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (14))) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((subclass_c2_contatore_co1)  è minore di  (11123)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_variabile_v2)  è uguale a  (False) )  e  
( negazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (14))) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v2)  è uguale a  (False) )  e  
( negazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (14))) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (14)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (14))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (14)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è minore di  (11123))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co1)  è minore di  (11123)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è minore di  (8))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (8)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                    ]),#49
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True ,  /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a RossoGialloaVerdea, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co9 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 1104 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  diverso da  /*56,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True ,  /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a RossoGialloaVerdea, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co9 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 1104 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  diverso da  /*56,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True))) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (1104)) allora ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea))} ) )  e  ( (subclass_c2_parametro_p8)  è maggiore di  (10) ) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v3)  è uguale a  (4))) ) )  o  
( (subclass_c2_controllo_c8)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True))) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (1104)) allora ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea))} ) )  e  ( (subclass_c2_parametro_p8)  è maggiore di  (10) ) )  e  
( negazione di (negazione di ((subclass_c2_variabile_v3)  è uguale a  (4))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True))) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (1104)) allora ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea))} ) )  e  ( (subclass_c2_parametro_p8)  è maggiore di  (10) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True))) )  e  ( per ognuna delle seguenti {se ((mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (1104)) allora ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea))} )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (1104)) allora ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (1104)) allora ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (1104)""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea)""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (10)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v3)  è uguale a  (4)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è uguale a  (4))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (4)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t9' è inattivo) )  e  
( negazione di (il timer 'subclass_c2_timer_t1' è attivo) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#50
                    DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 145 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 151230, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 145 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 151230""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (subclass_c2_parametro_p6)  è uguale a  (False) )  o  
( ( il timer 'subclass_c2_timer_t9' è attivo )  e  
( (subclass_c2_contatore_co7)  è uguale a  (145) ) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_parametro_p6)  è uguale a  (False) )  o  
( ( il timer 'subclass_c2_timer_t9' è attivo )  e  
( (subclass_c2_contatore_co7)  è uguale a  (145) ) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c2_parametro_p6)  è uguale a  (False) )  o  
( ( il timer 'subclass_c2_timer_t9' è attivo )  e  
( (subclass_c2_contatore_co7)  è uguale a  (145) ) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t9' è attivo )  e  
( (subclass_c2_contatore_co7)  è uguale a  (145) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (145)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è uguale a  (151230))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (151230)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#51
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 4 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1345 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  uguale a  /*53,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 4 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1345 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  uguale a  /*53,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'subclass_c2_restoreti_ti4_restore' è inattivo )  o  
( ( ( (subclass_c2_variabile_v3)  è minore di  (4) )  e  ( negazione di ((subclass_c2_contatore_co1)  è minore di  (1345)) ) )  e  
( negazione di ((subclass_c2_variabile_v3)  è uguale a  (4)) ) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti4_restore' è inattivo""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_variabile_v3)  è minore di  (4) )  e  ( negazione di ((subclass_c2_contatore_co1)  è minore di  (1345)) ) )  e  
( negazione di ((subclass_c2_variabile_v3)  è uguale a  (4)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v3)  è minore di  (4) )  e  ( negazione di ((subclass_c2_contatore_co1)  è minore di  (1345)) )""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (4)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è minore di  (1345))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co1)  è minore di  (1345)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è uguale a  (4))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (4)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)) )  e  
( negazione di ((subclass_c2_controllo_c8)  è uguale a  (False)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#52
                    DIStatement("""ITEStatementImpl\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  diverso da RossoGialloaVerdea /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 154 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo,  Applica gli effetti
       della macro SubClass_C2_macroef_M9  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  diverso da RossoGialloaVerdea /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 154 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea)))} )  e  ( (subclass_c2_controllo_c8)  è uguale a  (True) ) )  e  ( negazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True))) ) )  e  
( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea)))} )  e  ( (subclass_c2_controllo_c8)  è uguale a  (True) ) )  e  ( negazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True))) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea)))} )  e  ( (subclass_c2_controllo_c8)  è uguale a  (True) )""", [
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea)))}""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co7)  è minore di  (154)) )  e  
( il timer 'subclass_c2_timer_t1' è attivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è minore di  (154))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (154)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M9"""),#1
                    ]),#53
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True ,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) /*73,*/

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True))) )  e  ( negazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                    ]),#54
                    DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C2_timer_T9 non è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 11512, /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 11512""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'subclass_c2_timer_t9' è attivo) )  o  
( ( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )  e  
( negazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)) ) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox)) )  e  
( negazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v2)  è uguale a  (True) )  e  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (11512)) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è uguale a  (11512))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (11512)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#55
                    DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T8 è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  uguale a  False , /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T8 è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)) )  e  ( il timer 'subclass_c2_timer_t8' è scaduto ) )  e  ( (subclass_c2_controllo_c1)  è uguale a  (avanzamentox) ) )  e  ( negazione di ((subclass_c2_variabile_v2)  è uguale a  (True)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)) )  e  ( il timer 'subclass_c2_timer_t8' è scaduto ) )  e  ( (subclass_c2_controllo_c1)  è uguale a  (avanzamentox) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)) )  e  ( il timer 'subclass_c2_timer_t8' è scaduto )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#56
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro SubClass_C2_macroef_M7   /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M7"""),#1
                    ]),#57
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  maggiore di  /*54,*/ 7, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     /*105,*/ è  uguale a  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 

 ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T9""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  maggiore di  /*54,*/ 7, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     /*105,*/ è  uguale a  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  e  
( per ognuna delle seguenti {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True)) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (7))} ) )  o  
( ( negazione di (negazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex))) )  e  
( negazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True))) ) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( per ognuna delle seguenti {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True)) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (7))} )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True)) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (7))}""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True)) allora ((mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (7))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (True)""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (7)""", [
                    ]),#1
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex))) )  e  
( negazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#58
                    DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True ,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )""", [
                    DIBoolExpr("""EqualImpl\nil ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True""", [
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                    ]),#59
                    DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9, /*69,*/Disattiva il timer SubClass_C2_timer_T9""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è maggiore di  (9))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (9)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#60
                    DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1))} )  e  ( negazione di (il timer 'subclass_c2_timer_t9' è attivo) ) )  e  
( (subclass_c2_controllo_c8)  è uguale a  (True) ) )  o  
( negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1))} )  e  ( negazione di (il timer 'subclass_c2_timer_t9' è attivo) ) )  e  
( (subclass_c2_controllo_c8)  è uguale a  (True) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1))} )  e  ( negazione di (il timer 'subclass_c2_timer_t9' è attivo) )""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1))}""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t1' è attivo )  e  
( negazione di (il timer 'subclass_c2_timer_t9' è inattivo) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t9' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#61
                    DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 2,  Applica gli effetti
       della macro SubClass_C2_macroef_M6""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) )  e  ( (consdef)  è uguale a  (False) ) )  e  ( negazione di ((subclass_c2_controllo_c8)  è uguale a  (False)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p6)  è uguale a  (False)) )  e  ( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è maggiore di  (2))""", [
                    DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p8)  è maggiore di  (2)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M6"""),#1
                    ]),#62
                    DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è disattivo, /*72,*/Azzera il contatore SubClass_C2_contatore_Co1

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo)} )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (subclass_c2_parametro_p8)  è minore di  (6) ) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((subclass_c2_variabile_v3)  è uguale a  (4)) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo)} )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (subclass_c2_parametro_p8)  è minore di  (6) ) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo)} )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (subclass_c2_parametro_p8)  è minore di  (6) ) )""", [
                    DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo)}""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4 del campo mainclass_c1 della lista subclass_c2_lista_l4' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (subclass_c2_parametro_p8)  è minore di  (6) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p8)  è minore di  (6)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è uguale a  (4))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (4)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t8' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#63
                    DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 15 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 144, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 15 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 144""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (15)) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t1' è inattivo) ) )  o  
( negazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))) ) )  o  
( (subclass_c2_variabile_v3)  è minore di  (10) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (15)) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t1' è inattivo) ) )  o  
( negazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (15)) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t1' è inattivo) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_controllo_c8)  è uguale a  (True) )  e  
( negazione di ((subclass_c2_contatore_co1)  è uguale a  (15)) )""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è uguale a  (15))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (15)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (avanzamentox))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (avanzamentox)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (10)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co1)  è minore di  (144))""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co1)  è minore di  (144)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#64
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
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[8], ),
                         effect=(self.dbs[38], self.dbs[39], self.dbs[40], self.dbs[41], self.dbs[42], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[7], ),
                         effect=(self.dbs[33], self.dbs[34], self.dbs[35], self.dbs[36], self.dbs[37], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[20], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[21], self.dbs[22], self.dbs[23], self.dbs[24], self.dbs[25], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[4], ),
                         effect=(self.dbs[26], self.dbs[27], self.dbs[28], self.dbs[29], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[5], ),
                         effect=(self.dbs[30], self.dbs[31], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[6], ),
                         effect=(self.dbs[32], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[17], self.dbs[18], self.dbs[19], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4,
                         guard=(self.dbs[16], ),
                         effect=(self.dbs[61], self.dbs[62], self.dbs[63], self.dbs[64], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4,
                         guard=(self.dbs[15], ),
                         effect=(self.dbs[60], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[10], ),
                         effect=(self.dbs[45], self.dbs[46], self.dbs[47], self.dbs[48], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1,
                         guard=(self.dbs[11], ),
                         effect=(self.dbs[49], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[12], ),
                         effect=(self.dbs[50], self.dbs[51], self.dbs[52], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2,
                         guard=(self.dbs[13], ),
                         effect=(self.dbs[53], self.dbs[54], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[14], ),
                         effect=(self.dbs[55], self.dbs[56], self.dbs[57], self.dbs[58], self.dbs[59], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3,
                         guard=(self.dbs[9], ),
                         effect=(self.dbs[43], self.dbs[44], ),
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

        self.set_subclass_c2_previousco_c4_prev(False)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())
        self.set_subclass_c2_previousva_pv5_prev(self.get_subclass_c2_previousva_pv5())

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
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
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
                if(self.guard_NORMALIZATION_state1_state3_000()):
                    self.curr_transition = self.Transition._State1__State3__stateSheet_0__normalization__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_state3_000()):
                    self.curr_transition = self.Transition._State1__State3__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_state2_000()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state1_state2_001()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_2
                elif(self.guard_NOMINAL_ACTUATION_state1_state3_001()):
                    self.curr_transition = self.Transition._State1__State3__stateSheet_0__nominalActuation__transitionTo_3
                elif(self.guard_NOMINAL_ACTUATION_state1_state3_002()):
                    self.curr_transition = self.Transition._State1__State3__stateSheet_0__nominalActuation__transitionTo_4
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4):
                if(self.guard_PERMANENCE_state4_000()):
                    self.curr_transition = self.Transition._State4__State4__stateSheet_3__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3):
                if(self.guard_NORMALIZATION_state3_state4_000()):
                    self.curr_transition = self.Transition._State3__State4__stateSheet_2__normalization__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state3_state2_000()):
                    self.curr_transition = self.Transition._State3__State2__stateSheet_2__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state3_state1_000()):
                    self.curr_transition = self.Transition._State3__State1__stateSheet_2__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state3_state2_001()):
                    self.curr_transition = self.Transition._State3__State2__stateSheet_2__nominalActuation__transitionTo_2
                elif(self.guard_NOMINAL_ACTUATION_state3_state2_002()):
                    self.curr_transition = self.Transition._State3__State2__stateSheet_2__nominalActuation__transitionTo_3
                elif(self.guard_NOMINAL_ACTUATION_state3_000()):
                    self.curr_transition = self.Transition._State3__State3__stateSheet_2__nominalActuation__transitionTo_4
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
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4):
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
        elif self.curr_transition == self.Transition._State1__State3__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_NOMINAL_ACTUATION_state1_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State3__stateSheet_0__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_NOMINAL_ACTUATION_state1_state3_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State3__stateSheet_0__nominalActuation__transitionTo_4:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_NOMINAL_ACTUATION_state1_state3_002()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State3__stateSheet_0__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_NORMALIZATION_state1_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State4__State4__stateSheet_3__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4)
            self.effect_PERMANENCE_state4_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State3__stateSheet_2__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_PERMANENCE_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State2__stateSheet_2__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state3_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State1__stateSheet_2__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state3_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State2__stateSheet_2__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state3_state2_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State2__stateSheet_2__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state3_state2_002()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State3__stateSheet_2__nominalActuation__transitionTo_4:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state3)
            self.effect_NOMINAL_ACTUATION_state3_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State3__State4__stateSheet_2__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state4)
            self.effect_NORMALIZATION_state3_state4_000()
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
        
         commento: {69,} commento: {37,}  se la variabile SubClass_C2_variabile_V3 è  maggiore di  commento: {54,} 8 commento: {36,} o  se il timer SubClass_C2_timer_T9 non è scaduto, Solo una delle seguenti { 
         commento: {36,}  se il timer SubClass_C2_timer_T9 non è scaduto commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 1151 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V3 sia  uguale a  commento: {53,} 6
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P8 non sia  uguale a  commento: {53,} 10
        
        
        }
        """
        return db((db(not db((db(self.get_subclass_c2_variabile_v3() > 8, self.dbs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0]) or db(not db((db((db((db((db(not db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p6() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p6() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 1151, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c8() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_variabile_v3() == 6, self.dbs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[0].subs[1]), self.dbs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p8() == 10, self.dbs[1].subs[1].subs[0]), self.dbs[1].subs[1])), self.dbs[1])
    
    def guard_NOMINAL_ACTUATION_state1_state3_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[2])
    
    def guard_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[3])
    
    def guard_NOMINAL_ACTUATION_state1_state2_001(self):
        """
        CNL corrispondente:
         {  commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T9 è attivo commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 1 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False , Solo una delle seguenti { 
         commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  uguale a  commento: {53,} 7 commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
         commento: {37,}  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T1 non sia attivo
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T9 non sia scaduto
        
         }
        """
        return db((db(not db((db((db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[4].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), self.dbs[4].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_parametro_p8() > 1, self.dbs[4].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c8() == False, self.dbs[4].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[0]) or db((((db(not db((db((db(self.get_subclass_c2_parametro_p8() == 7, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c8() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v2() == True, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[4].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[4].subs[0].subs[1].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1]))) == 1), self.dbs[4].subs[0].subs[1]), self.dbs[4].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[4].subs[1].subs[0]), self.dbs[4].subs[1])), self.dbs[4])
    
    def guard_NOMINAL_ACTUATION_state1_state3_001(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[5])
    
    def guard_NOMINAL_ACTUATION_state1_state3_002(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[6])
    
    def guard_NORMALIZATION_state1_state3_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[7])
    
    def guard_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[8])
    
    def guard_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {67,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 13 commento: {36,} e  se il timer SubClass_C2_timer_T9 non è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 12230 commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 11451 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 132 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, Tutte le seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 8 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Tutte le seguenti { 
         commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T1 non è disattivo commento: {36,} o  se il timer SubClass_C2_timer_T8 è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox, Solo una delle seguenti { 
         commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T9 è scaduto, Solo una delle seguenti { 
         commento: {69,} commento: {34,}  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T8 è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
         commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T1 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 è attivo, Solo una delle seguenti { 
         commento: {67,} commento: {36,}  se il timer SubClass_C2_timer_T1 è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo, Tutte le seguenti { 
         commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 11 commento: {36,} o  se il timer SubClass_C2_timer_T8 non è attivo commento: {36,} o  se il timer SubClass_C2_timer_T9 non è attivo, Solo una delle seguenti { 
         commento: {67,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 1530 commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  uguale a  commento: {53,} 6 commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  commento: {53,} 11 commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 4, Tutte le seguenti { 
         commento: {37,}  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  commento: {54,} 6 commento: {36,} o  se il timer SubClass_C2_timer_T9 è disattivo, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V3 non sia  minore di  commento: {55,} 10
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 sia  uguale a  False 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 15
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V3 non sia  maggiore di  commento: {54,} 6
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  uguale a  True 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a avanzamentox
        
        
        }
        """
        return db((db(not db((db((db((db((db(self.get_subclass_c2_contatore_co7().get_valore() < 13, self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 12230, self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_contatore_co7().get_valore() == 11451, self.dbs[9].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 132, self.dbs[9].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[9].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[9].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c2_timer_t8().isDisattivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p8() < 8, self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t8().isAttivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(self.get_consdef() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t8().isDisattivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v3() < 6, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(self.get_subclass_c2_timer_t1().isDisattivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c2_contatore_co7().get_valore() == 11, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t8().isAttivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(not db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() > 1530, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v3() == 6, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 11, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() > 4, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(self.get_subclass_c2_variabile_v3() > 6, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_variabile_v3() < 10, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_consdef() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_subclass_c2_parametro_p6() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 15, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_variabile_v3() > 6, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_consdef() == False, self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isScaduto(), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[9].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1].subs[0].subs[1]), self.dbs[9].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c8() == True, self.dbs[9].subs[0].subs[1].subs[1])), self.dbs[9].subs[0].subs[1]), self.dbs[9].subs[0]) and db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[9].subs[1])), self.dbs[9])
    
    def guard_NOMINAL_ACTUATION_state3_state2_000(self):
        """
        CNL corrispondente:
         {  commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T8 è attivo commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo commento: {34,} o  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {68,} commento: {35,}  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  minore di  commento: {55,} 14 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto, Almeno una delle seguenti { 
         commento: {67,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 1230 commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
          se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 7 commento: {36,} e  se il timer SubClass_C2_timer_T9 non è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  commento: {36,} e  se il timer SubClass_C2_timer_T8 non è attivo, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da  True 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  diverso da avanzamentox
        
         }
        """
        return db((db(not db((db((db((db((db((db(self.get_consdef() == False, self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t8().isAttivato(), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() > 3, self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[10].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[10].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[10].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[0]) or db((((db(not db((db((db((db((db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co1().get_valore() < 14, self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() == True, self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isScaduto(), self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c2_contatore_co7().get_valore() < 1230, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(self.get_consdef() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p8() > 7, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v2() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isAttivato(), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[10].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[10].subs[0].subs[1].subs[0].subs[1]), self.dbs[10].subs[0].subs[1].subs[0])) + (db(not db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[10].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[10].subs[0].subs[1].subs[1].subs[0]), self.dbs[10].subs[0].subs[1].subs[1]))) == 1), self.dbs[10].subs[0].subs[1]), self.dbs[10].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[10].subs[1].subs[0]), self.dbs[10].subs[1])), self.dbs[10])
    
    def guard_NOMINAL_ACTUATION_state3_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[11])
    
    def guard_NOMINAL_ACTUATION_state3_state2_001(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[12])
    
    def guard_NOMINAL_ACTUATION_state3_state2_002(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[13])
    
    def guard_NOMINAL_ACTUATION_state3_000(self):
        """
        CNL corrispondente:
         {  Nessuna  commento: {80,} }
        """
        return db((True), self.dbs[14])
    
    def guard_NORMALIZATION_state3_state4_000(self):
        """
        CNL corrispondente:
         {  commento: {69,} commento: {36,}  se il timer SubClass_C2_timer_T9 è disattivo, Solo una delle seguenti { 
         commento: {69,} commento: {38,}  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  commento: {54,} 1330 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  diverso da  False , Solo una delle seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 1, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V2 sia  uguale a  False 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C5 sia  diverso da avanzamentox
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T9 non sia attivo
        
         }
        """
        return db((db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[15].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_subclass_c2_contatore_co1().get_valore() > 1330, self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p6() == False, self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[15].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[15].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() < 1, self.dbs[15].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_variabile_v2() == False, self.dbs[15].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[15].subs[0].subs[1].subs[0].subs[1]), self.dbs[15].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, self.dbs[15].subs[0].subs[1].subs[1].subs[0]), self.dbs[15].subs[0].subs[1].subs[1]))) == 1), self.dbs[15].subs[0].subs[1]), self.dbs[15].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[15].subs[1].subs[0]), self.dbs[15].subs[1])), self.dbs[15])
    
    def guard_PERMANENCE_state4_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {68,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 10 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  maggiore di  commento: {54,} 5, Almeno una delle seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 sia  uguale a avanzamentox
        
        
        }
        """
        return db((db(not db((db((db(self.get_subclass_c2_parametro_p8() < 10, self.dbs[16].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[16].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[16].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[16].subs[0].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v3() > 5, self.dbs[16].subs[0].subs[0].subs[1].subs[0]), self.dbs[16].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0]) or db(not db((db(not db(self.get_subclass_c2_parametro_p6() == True, self.dbs[16].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[16].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[16].subs[0].subs[1].subs[0].subs[1])), self.dbs[16].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[16].subs[0].subs[1].subs[1]), self.dbs[16].subs[0].subs[1]), self.dbs[16].subs[0]) and db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[16].subs[1])), self.dbs[16])
    
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
        
         commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento ) commento: {73,}
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  minore di  commento: {55,} 122, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
        
           
         commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex,  commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C9 del campo  MainClass_C1     è  uguale a RossoGialloaVerdea commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  commento: {53,} 13304, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        
           
        
        }
        """
        #  /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )
        if db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, self.dbs[17].subs[0].subs[0].subs[0]), self.dbs[17].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[17].subs[0].subs[1])), self.dbs[17].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.c270,True,GlobalEnumeration.avanzamento,GlobalEnumeration.avanzamento, self.dbs[17].subs[1])
        #  /*73,*/
        #     
        #   /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 122, /*69,*/Disattiva il timer SubClass_C2_timer_T9
        if db((db(self.get_subclass_c2_restoreti_ti3_restore().isAttivato(), self.dbs[18].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co1().get_valore() < 122, self.dbs[18].subs[0].subs[1])), self.dbs[18].subs[0]):
            self.get_subclass_c2_timer_t9().disattiva()
        #  /*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     è  uguale a RossoGialloaVerdea /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 13304, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        if db((db((db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[19].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t10().isAttivato(), self.dbs[19].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6()) if db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, self.dbs[19].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[19].subs[0].subs[0].subs[1])), self.dbs[19].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 13304, self.dbs[19].subs[0].subs[1].subs[0]), self.dbs[19].subs[0].subs[1])), self.dbs[19].subs[0]):
            self.set_subclass_c2_variabile_v6(GlobalEnumeration.gialloxverdex)
    
    def effect_NOMINAL_ACTUATION_state1_state3_000(self):
        """
        CNL corrispondente:
         { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 3 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 1 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  maggiore di  commento: {54,} 3 e  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer SubClass_C2_timer_T1
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
        
         }
        """
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 3 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 1 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  maggiore di  /*54,*/ 3 e  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer SubClass_C2_timer_T1
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[20].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), self.dbs[20].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), self.dbs[20].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v3() == 3, self.dbs[20].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[20].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p8() == 1, self.dbs[20].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[20].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[1].subs[1])), self.dbs[20].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_controllo_c8() == False, self.dbs[20].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v3() > 3, self.dbs[20].subs[0].subs[1].subs[0].subs[1])), self.dbs[20].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[20].subs[0].subs[1].subs[1])), self.dbs[20].subs[0].subs[1])), self.dbs[20].subs[0]):
            self.get_subclass_c2_timer_t1().attiva()
        else:
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
    
    def effect_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True , commento: {68,}Attiva il timer SubClass_C2_timer_T9
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
        
         commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {34,} o  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 8 commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False ,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento ) commento: {73,}
        
           
         commento: {36,}  se il timer SubClass_C2_timer_T1 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
           
         commento: {36,}  se il timer SubClass_C2_timer_T9 è attivo,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T10 del campo  MainClass_C1     commento: {105,} è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , commento: {68,}Attiva il timer SubClass_C2_timer_T9
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
        
         commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  commento: {54,} 12123, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T8
        
        
         }
        """
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True , /*68,*/Attiva il timer SubClass_C2_timer_T9
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
        if db((db((db((db((db(self.get_subclass_c2_restoreti_ti2_restore().isAttivato(), self.dbs[21].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[21].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v2() == True, self.dbs[21].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[21].subs[0].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), self.dbs[21].subs[0].subs[0].subs[1].subs[0]), self.dbs[21].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[21].subs[0].subs[1].subs[0].subs[0]), self.dbs[21].subs[0].subs[1].subs[0]), self.dbs[21].subs[0].subs[1])), self.dbs[21].subs[0]):
            self.get_subclass_c2_timer_t9().attiva()
        else:
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.avanzamentox,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.avanzamento, self.dbs[21].subs[1])
        #  /*73,*/
        #   /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*34,*/ o  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 8 /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  diverso da  False ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a avanzamento )
        if db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, self.dbs[22].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[22].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() == 8, self.dbs[22].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[22].subs[0].subs[0].subs[0].subs[1])), self.dbs[22].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[22].subs[0].subs[0].subs[1].subs[0]), self.dbs[22].subs[0].subs[0].subs[1])), self.dbs[22].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[22].subs[0].subs[1].subs[0].subs[0]), self.dbs[22].subs[0].subs[1].subs[0]), self.dbs[22].subs[0].subs[1])), self.dbs[22].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.c270,True,GlobalEnumeration.avanzamento,GlobalEnumeration.gialloaverdea, self.dbs[22].subs[1])
        #  /*73,*/
        #     
        #   /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db((db((db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), self.dbs[23].subs[0].subs[0].subs[0].subs[0]), self.dbs[23].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p6() == False, self.dbs[23].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[23].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[23].subs[0].subs[0].subs[1].subs[1])), self.dbs[23].subs[0].subs[0].subs[1])), self.dbs[23].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[23].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[23].subs[0].subs[1].subs[0].subs[0]), self.dbs[23].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[23].subs[0].subs[1].subs[1])), self.dbs[23].subs[0].subs[1])), self.dbs[23].subs[0]):
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
        #  /*36,*/  se il timer SubClass_C2_timer_T9 è attivo,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T10 del campo  MainClass_C1     /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , /*68,*/Attiva il timer SubClass_C2_timer_T9
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
        if db((db((db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[24].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[24].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t10().isAttivato(), self.dbs[24].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[24].subs[0].subs[0].subs[1])), self.dbs[24].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[24].subs[0].subs[1].subs[0]), self.dbs[24].subs[0].subs[1])), self.dbs[24].subs[0]):
            self.get_subclass_c2_timer_t9().attiva()
        else:
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.avanzamentox,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.gialloaverdea, self.dbs[24].subs[1])
        #  /*73,*/
        #   /*37,*/  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 12123, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T8
        if db((db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[25].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co1().get_valore() > 12123, self.dbs[25].subs[0].subs[1])), self.dbs[25].subs[0]):
            self.set_subclass_c2_variabile_v3(1)
        else:
            self.get_subclass_c2_timer_t8().attiva()
    
    def effect_NOMINAL_ACTUATION_state1_state2_001(self):
        """
        CNL corrispondente:
         { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 150, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 8
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        
        
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto,  Applica gli effetti
               della macro SubClass_C2_macroef_M6  commento: {73,}
        
           
         commento: {34,}  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 7 commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 3
        
           
         commento: {36,}  se il timer SubClass_C2_timer_T9 non è scaduto commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer SubClass_C2_timer_T1 è scaduto commento: {36,} o  se il timer SubClass_C2_timer_T1 non è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T9 non è disattivo, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
        
           
         }
        """
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 150, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 8
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        if db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == False, self.dbs[26].subs[0].subs[0].subs[0].subs[0][idx]), self.dbs[26].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), self.dbs[26].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 150, self.dbs[26].subs[0].subs[1].subs[0]), self.dbs[26].subs[0].subs[1])), self.dbs[26].subs[0]):
            self.set_subclass_c2_variabile_v3(8)
        else:
            self.set_subclass_c2_variabile_v6(GlobalEnumeration.gialloxverdex)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI3 è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False  /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M6
        if db((db(self.get_subclass_c2_restoreti_ti3_restore().isAttivato(), self.dbs[27].subs[0].subs[0]) or db((db((db((db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[27].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[27].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[27].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[27].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[27].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[27].subs[0].subs[1].subs[0].subs[1])), self.dbs[27].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isScaduto(), self.dbs[27].subs[0].subs[1].subs[1].subs[0]), self.dbs[27].subs[0].subs[1].subs[1])), self.dbs[27].subs[0].subs[1])), self.dbs[27].subs[0]):
            self.macroSubclass_c2_macroef_m6(self.dbs[27].subs[1])
        #  /*73,*/
        #     
        #   /*34,*/  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 7 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 3
        if db((db((db((db(not db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[28].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[28].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[28].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[28].subs[0].subs[0].subs[0].subs[1])), self.dbs[28].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[28].subs[0].subs[0].subs[1].subs[0]), self.dbs[28].subs[0].subs[0].subs[1])), self.dbs[28].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v3() < 7, self.dbs[28].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[28].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[28].subs[0].subs[1].subs[0].subs[1])), self.dbs[28].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[28].subs[0].subs[1].subs[1])), self.dbs[28].subs[0].subs[1])), self.dbs[28].subs[0]):
            self.set_subclass_c2_variabile_v3(3)
        #  /*36,*/  se il timer SubClass_C2_timer_T9 non è scaduto /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T1 è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo, /*69,*/Disattiva il timer SubClass_C2_timer_T9
        if db((db((db(not db(self.get_subclass_c2_timer_t9().isScaduto(), self.dbs[29].subs[0].subs[0].subs[0].subs[0]), self.dbs[29].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v3() == 6, self.dbs[29].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[29].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t1().isScaduto(), self.dbs[29].subs[0].subs[0].subs[1].subs[1])), self.dbs[29].subs[0].subs[0].subs[1])), self.dbs[29].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t1().isScaduto(), self.dbs[29].subs[0].subs[1].subs[0].subs[0]), self.dbs[29].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[29].subs[0].subs[1].subs[1].subs[0]), self.dbs[29].subs[0].subs[1].subs[1])), self.dbs[29].subs[0].subs[1])), self.dbs[29].subs[0]):
            self.get_subclass_c2_timer_t9().disattiva()
    
    def effect_NOMINAL_ACTUATION_state1_state3_001(self):
        """
        CNL corrispondente:
         { commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T9 non è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        
         ,altrimenti  commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
        
        
         commento: {38,}  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 11 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 12451 commento: {36,} o  se il timer SubClass_C2_timer_T9 è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T8 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        
        
         }
        """
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 non è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        #   ,altrimenti  /*72,*/Azzera il contatore SubClass_C2_contatore_Co7
        if db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == True, self.dbs[30].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), self.dbs[30].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[30].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[30].subs[0].subs[0].subs[0].subs[1])), self.dbs[30].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[30].subs[0].subs[0].subs[1].subs[0]), self.dbs[30].subs[0].subs[0].subs[1])), self.dbs[30].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[30].subs[0].subs[1].subs[0]), self.dbs[30].subs[0].subs[1])), self.dbs[30].subs[0]):
            self.set_subclass_c2_comando_c6(GlobalEnumeration.avanzamentox)
        else:
            self.get_subclass_c2_contatore_co7().resetta()
        #  /*38,*/  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 12451 /*36,*/ o  se il timer SubClass_C2_timer_T9 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        if db((db((db((db((db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() > 11, self.dbs[31].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[31].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[31].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[31].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 12451, self.dbs[31].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[31].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[31].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[31].subs[0].subs[0].subs[0].subs[1])), self.dbs[31].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() == False, self.dbs[31].subs[0].subs[0].subs[1].subs[0]), self.dbs[31].subs[0].subs[0].subs[1])), self.dbs[31].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t8().isDisattivato(), self.dbs[31].subs[0].subs[1].subs[0]), self.dbs[31].subs[0].subs[1])), self.dbs[31].subs[0]):
            self.set_subclass_c2_variabile_v3(6)
        else:
            self.set_subclass_c2_comando_c6(GlobalEnumeration.avanzamentox)
    
    def effect_NOMINAL_ACTUATION_state1_state3_002(self):
        """
        CNL corrispondente:
         { commento: {34,}  se il parametro SubClass_C2_parametro_P8 non è  diverso da  commento: {56,} 4,  commento: {45,}  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  commento: {105,} è  uguale a  commento: {53,} 15230, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
        
           
         }
        """
        #  /*34,*/  se il parametro SubClass_C2_parametro_P8 non è  diverso da  /*56,*/ 4,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 15230, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1 , /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
        if db((db(not db(not db(self.get_subclass_c2_parametro_p8() == 4, self.dbs[32].subs[0].subs[0].subs[0].subs[0]), self.dbs[32].subs[0].subs[0].subs[0]), self.dbs[32].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co3().get_valore() == 15230, self.dbs[32].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[32].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[32].subs[0].subs[1])), self.dbs[32].subs[0]):
            self.set_subclass_c2_variabile_v3(1)
    
    def effect_NORMALIZATION_state1_state3_000(self):
        """
        CNL corrispondente:
         { commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co1
        
           
         commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex, commento: {68,}Attiva il timer SubClass_C2_timer_T9
        
           
         commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 12, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
        
        
         commento: {38,}  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  commento: {54,} 13 commento: {36,} o  se il timer SubClass_C2_timer_T1 è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  minore di  commento: {55,} 5 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  uguale a  commento: {53,} 1251 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
           
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T1
        
        
         }
        """
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è disattivo, /*72,*/Azzera il contatore SubClass_C2_contatore_Co1
        if db(self.get_subclass_c2_restoreti_ti1_restore().isDisattivato(), self.dbs[33].subs[0]):
            self.get_subclass_c2_contatore_co1().resetta()
        #  /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex, /*68,*/Attiva il timer SubClass_C2_timer_T9
        if db(not db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[34].subs[0].subs[0].subs[0]), self.dbs[34].subs[0].subs[0]), self.dbs[34].subs[0]):
            self.get_subclass_c2_timer_t9().attiva()
        #  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 12, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1
        if db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == False, self.dbs[35].subs[0].subs[0].subs[0].subs[0][idx]), self.dbs[35].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), self.dbs[35].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 12, self.dbs[35].subs[0].subs[1].subs[0]), self.dbs[35].subs[0].subs[1])), self.dbs[35].subs[0]):
            self.set_subclass_c2_variabile_v6(GlobalEnumeration.gialloxverdex)
        else:
            self.get_subclass_c2_contatore_co1().decrementa()
        #  /*38,*/  se il contatore SubClass_C2_contatore_Co1 non è  maggiore di  /*54,*/ 13 /*36,*/ o  se il timer SubClass_C2_timer_T1 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  minore di  /*55,*/ 5 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  uguale a  /*53,*/ 1251 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False  /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox, /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db((db((db((db((db((db(not db(self.get_subclass_c2_contatore_co1().get_valore() > 13, self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t1().isDisattivato(), self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() < 5, self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[36].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[36].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co1().get_valore() == 1251, self.dbs[36].subs[0].subs[0].subs[0].subs[1])), self.dbs[36].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() == False, self.dbs[36].subs[0].subs[0].subs[1].subs[0]), self.dbs[36].subs[0].subs[0].subs[1])), self.dbs[36].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[36].subs[0].subs[1])), self.dbs[36].subs[0]):
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  uguale a avanzamentox, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T1
        if db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, self.dbs[37].subs[0].subs[0].subs[0].subs[0]), self.dbs[37].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v2() == True, self.dbs[37].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[37].subs[0].subs[0].subs[1].subs[0]), self.dbs[37].subs[0].subs[0].subs[1])), self.dbs[37].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[37].subs[0].subs[1])), self.dbs[37].subs[0]):
            self.get_subclass_c2_contatore_co1().decrementa()
        else:
            self.get_subclass_c2_timer_t1().disattiva()
    
    def effect_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
          se il controllo ConsDef  è  uguale a FALSE ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co3 del campo  MainClass_C1     è  uguale a  commento: {53,} 12, commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
           
          se la macro  SubClass_C2_macrova_M9 ( con argomento_a2   uguale a True ,argomento_a7   uguale a GialloGiallo ,argomento_a3   uguale a avanzamento  e argomento_a4   uguale a c75Giallo )  non  è  diverso da avanzamentox commento: {40,} ,  Applica gli effetti
               della macro SubClass_C2_macroef_M9  commento: {73,}
        
           
         commento: {35,}  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
        
           
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  uguale a  commento: {53,} 2 e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo, commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co1
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        
        
          se la macro  SubClass_C2_macrova_M1 ( con argomento_a1   uguale a c75Giallo ,argomento_a8   uguale a GialloxVerdex  e argomento_a10   uguale a GialloxVerdex )   è  diverso da GialloxVerdex commento: {40,} , commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
        
         ,altrimenti  commento: {70,}Incrementa il contatore SubClass_C2_contatore_Co1
        
        
        
        }
        """
        #  se il controllo ConsDef  è  uguale a FALSE ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L2 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co3 del campo  MainClass_C1     è  uguale a  /*53,*/ 12, /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db((db(self.get_consdef() == False, self.dbs[38].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[38].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co3().get_valore() == 12, self.dbs[38].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[38].subs[0].subs[1])), self.dbs[38].subs[0]):
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
        #  se la macro  SubClass_C2_macrova_M9 ( con argomento_a2   uguale a True ,argomento_a7   uguale a GialloGiallo ,argomento_a3   uguale a avanzamento  e argomento_a4   uguale a c75Giallo )  non  è  diverso da avanzamentox /*40,*/ ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M9
        if db(not db(not db(db(self.macroSubclass_c2_macrova_m9(True,GlobalEnumeration.avanzamento,GlobalEnumeration.c75giallo,GlobalEnumeration.giallogiallo, self.dbs[39].subs[0].subs[0].subs[0].subs[0]), self.dbs[39].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.avanzamentox, self.dbs[39].subs[0].subs[0].subs[0]), self.dbs[39].subs[0].subs[0]), self.dbs[39].subs[0]):
            self.macroSubclass_c2_macroef_m9(self.dbs[39].subs[1])
        #  /*73,*/
        #     
        #   /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  uguale a  True , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7
        if db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[40].subs[0].subs[0]), self.dbs[40].subs[0]):
            self.get_subclass_c2_contatore_co7().resetta()
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  uguale a  /*53,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo, /*70,*/Incrementa il contatore SubClass_C2_contatore_Co1
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        if db((db((db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v3() == 2, self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[41].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c8() == False, self.dbs[41].subs[0].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, self.dbs[41].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[41].subs[0].subs[0].subs[1].subs[0]), self.dbs[41].subs[0].subs[0].subs[1])), self.dbs[41].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[41].subs[0].subs[1])), self.dbs[41].subs[0]):
            self.get_subclass_c2_contatore_co1().incrementa()
        else:
            self.set_subclass_c2_comando_c6(GlobalEnumeration.avanzamentox)
        #  se la macro  SubClass_C2_macrova_M1 ( con argomento_a1   uguale a c75Giallo ,argomento_a8   uguale a GialloxVerdex  e argomento_a10   uguale a GialloxVerdex )   è  diverso da GialloxVerdex /*40,*/ , /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1
        #   ,altrimenti  /*70,*/Incrementa il contatore SubClass_C2_contatore_Co1
        if db(not db(db(self.macroSubclass_c2_macrova_m1(GlobalEnumeration.c75giallo,GlobalEnumeration.gialloxverdex,GlobalEnumeration.gialloxverdex, self.dbs[42].subs[0].subs[0].subs[0]), self.dbs[42].subs[0].subs[0].subs[0]) == GlobalEnumeration.gialloxverdex, self.dbs[42].subs[0].subs[0]), self.dbs[42].subs[0]):
            self.get_subclass_c2_contatore_co1().decrementa()
        else:
            self.get_subclass_c2_contatore_co1().incrementa()
    
    def effect_PERMANENCE_state3_000(self):
        """
        CNL corrispondente:
        
        {
        
          se la macro  SubClass_C2_macrova_M5 ( con argomento_a8   uguale a avanzamento ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a GialloaVerdea  e argomento_a6   uguale a GialloaVerdea )   è  uguale a  False  commento: {40,}  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 1512 commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  uguale a avanzamentox, commento: {68,}Attiva il timer SubClass_C2_timer_T8
        
           
         commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 è attivo commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 4
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T1
        
        
        
        }
        """
        #  se la macro  SubClass_C2_macrova_M5 ( con argomento_a8   uguale a avanzamento ,argomento_a10   uguale a RossoGialloGiallo ,argomento_a5   uguale a c75Giallo ,argomento_a9   uguale a GialloaVerdea  e argomento_a6   uguale a GialloaVerdea )   è  uguale a  False  /*40,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1512 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  uguale a avanzamentox, /*68,*/Attiva il timer SubClass_C2_timer_T8
        if db((db(db(self.macroSubclass_c2_macrova_m5(GlobalEnumeration.rossogiallogiallo,GlobalEnumeration.c75giallo,GlobalEnumeration.gialloaverdea,GlobalEnumeration.avanzamento,GlobalEnumeration.gialloaverdea, self.dbs[43].subs[0].subs[0].subs[0]), self.dbs[43].subs[0].subs[0].subs[0]) == False, self.dbs[43].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_contatore_co1().get_valore() < 1512, self.dbs[43].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[43].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c8() == False, self.dbs[43].subs[0].subs[1].subs[0].subs[1])), self.dbs[43].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, self.dbs[43].subs[0].subs[1].subs[1].subs[0]), self.dbs[43].subs[0].subs[1].subs[1])), self.dbs[43].subs[0].subs[1])), self.dbs[43].subs[0]):
            self.get_subclass_c2_timer_t8().attiva()
        #  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 è attivo /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 4
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T1
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isAttivato(), self.dbs[44].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), self.dbs[44].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[44].subs[0].subs[0].subs[1])), self.dbs[44].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[44].subs[0].subs[1])), self.dbs[44].subs[0]):
            self.set_subclass_c2_variabile_v3(4)
        else:
            self.get_subclass_c2_timer_t1().attiva()
    
    def effect_NOMINAL_ACTUATION_state3_state2_000(self):
        """
        CNL corrispondente:
         { commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è attivo commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è attivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 9
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M9  commento: {73,}
        
        
          se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer SubClass_C2_timer_T1
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False ,  Applica gli effetti
               della macro SubClass_C2_macroef_M9  commento: {73,}
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
        
        
         }
        """
        #  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è attivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
        if db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isAttivato(), self.dbs[45].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), self.dbs[45].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() == False, self.dbs[45].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v2() == False, self.dbs[45].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[45].subs[0].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[0].subs[1])), self.dbs[45].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[45].subs[0].subs[1].subs[0]), self.dbs[45].subs[0].subs[1])), self.dbs[45].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI2 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 9
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M9
        if db(not db(self.get_subclass_c2_restoreti_ti2_restore().isDisattivato(), self.dbs[46].subs[0].subs[0]), self.dbs[46].subs[0]):
            self.set_subclass_c2_variabile_v3(9)
        else:
            self.macroSubclass_c2_macroef_m9(self.dbs[46].subs[1])
        #  /*73,*/
        #    se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer SubClass_C2_timer_T1
        if db(self.get_consdef() == False, self.dbs[47].subs[0]):
            self.get_subclass_c2_timer_t1().disattiva()
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M9  /*73,*/
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1
        if db(not db(self.get_subclass_c2_restoreva_rv1_restore() == False, self.dbs[48].subs[0].subs[0]), self.dbs[48].subs[0]):
            self.macroSubclass_c2_macroef_m9(self.dbs[48].subs[1])
        else:
            self.get_subclass_c2_contatore_co1().decrementa()
    
    def effect_NOMINAL_ACTUATION_state3_state1_000(self):
        """
        CNL corrispondente:
         { commento: {37,}  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 14 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 11123 commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 8 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  False ,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
        
         }
        """
        #  /*37,*/  se la variabile SubClass_C2_variabile_V2 è  uguale a  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 14 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 11123 /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 8 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  False ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) /*73,*/
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db((db((db((db((db((db(self.get_subclass_c2_variabile_v2() == False, self.dbs[49].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 14, self.dbs[49].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[49].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[49].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[49].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[49].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[49].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() < 11123, self.dbs[49].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[49].subs[0].subs[0].subs[0].subs[1])), self.dbs[49].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v3() < 8, self.dbs[49].subs[0].subs[0].subs[1].subs[0]), self.dbs[49].subs[0].subs[0].subs[1])), self.dbs[49].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[49].subs[0].subs[1].subs[0]), self.dbs[49].subs[0].subs[1])), self.dbs[49].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.c270,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.gialloaverdea, self.dbs[49].subs[1])
        else:
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
    
    def effect_NOMINAL_ACTUATION_state3_state2_001(self):
        """
        CNL corrispondente:
         { commento: {37,}  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True ,  commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a RossoGialloaVerdea, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co9 del campo  MainClass_C1     commento: {105,} è  maggiore di  commento: {54,} 1104 commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 10 commento: {37,} e  se la variabile SubClass_C2_variabile_V3 non è  diverso da  commento: {56,} 4 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T9 non è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T1 non è attivo, commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  False 
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 145 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  commento: {53,} 151230, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 4 commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 1345 commento: {37,} e  se la variabile SubClass_C2_variabile_V3 non è  uguale a  commento: {53,} 4 commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
        
           
         }
        """
        #  /*37,*/  se la variabile SubClass_C2_variabile_V2 non è  diverso da  True ,  /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a RossoGialloaVerdea, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co9 del campo  MainClass_C1     /*105,*/ è  maggiore di  /*54,*/ 1104 /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 10 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  diverso da  /*56,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T9 non è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo, /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  False
        if db((db((db((db((db((db(not db(not db(self.get_subclass_c2_variabile_v2() == True, self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co9().get_valore() > 1104, self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p8() > 10, self.dbs[50].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[50].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v3() == 4, self.dbs[50].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[50].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[50].subs[0].subs[0].subs[0].subs[1])), self.dbs[50].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c8() == False, self.dbs[50].subs[0].subs[0].subs[1])), self.dbs[50].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[50].subs[0].subs[1].subs[0].subs[0]), self.dbs[50].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[50].subs[0].subs[1].subs[1].subs[0]), self.dbs[50].subs[0].subs[1].subs[1])), self.dbs[50].subs[0].subs[1])), self.dbs[50].subs[0]):
            self.set_subclass_c2_comando_c6(GlobalEnumeration.avanzamentox)
        else:
            self.set_subclass_c2_variabile_v2(False)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 145 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  uguale a  /*53,*/ 151230, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
        if db((db((db((db((db(self.get_subclass_c2_parametro_p6() == False, self.dbs[51].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[51].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co7().get_valore() == 145, self.dbs[51].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[51].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[51].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[51].subs[0].subs[0].subs[0].subs[1])), self.dbs[51].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[51].subs[0].subs[0].subs[1])), self.dbs[51].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 151230, self.dbs[51].subs[0].subs[1].subs[0]), self.dbs[51].subs[0].subs[1])), self.dbs[51].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 4 /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1345 /*37,*/ e  se la variabile SubClass_C2_variabile_V3 non è  uguale a  /*53,*/ 4 /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7
        if db((db((db(self.get_subclass_c2_restoreti_ti4_restore().isDisattivato(), self.dbs[52].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v3() < 4, self.dbs[52].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co1().get_valore() < 1345, self.dbs[52].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[52].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[52].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v3() == 4, self.dbs[52].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[52].subs[0].subs[0].subs[1].subs[1])), self.dbs[52].subs[0].subs[0].subs[1])), self.dbs[52].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v2() == True, self.dbs[52].subs[0].subs[1].subs[0].subs[0]), self.dbs[52].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[52].subs[0].subs[1].subs[1].subs[0]), self.dbs[52].subs[0].subs[1].subs[1])), self.dbs[52].subs[0].subs[1])), self.dbs[52].subs[0]):
            self.get_subclass_c2_contatore_co7().resetta()
    
    def effect_NOMINAL_ACTUATION_state3_state2_002(self):
        """
        CNL corrispondente:
         { commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  diverso da RossoGialloaVerdea commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  minore di  commento: {55,} 154 commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo,  Applica gli effetti
               della macro SubClass_C2_macroef_M9  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 2
        
        
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True ,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
        
         }
        """
        #  /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  diverso da RossoGialloaVerdea /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 154 /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M9  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 2
        if db((db((db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, self.dbs[53].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), self.dbs[53].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), self.dbs[53].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c8() == True, self.dbs[53].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[53].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[53].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[53].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[53].subs[0].subs[0].subs[0].subs[1])), self.dbs[53].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[53].subs[0].subs[0].subs[1].subs[0]), self.dbs[53].subs[0].subs[0].subs[1])), self.dbs[53].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 154, self.dbs[53].subs[0].subs[1].subs[0].subs[0]), self.dbs[53].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[53].subs[0].subs[1].subs[1])), self.dbs[53].subs[0].subs[1])), self.dbs[53].subs[0]):
            self.macroSubclass_c2_macroef_m9(self.dbs[53].subs[1])
        else:
            self.set_subclass_c2_variabile_v3(2)
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) /*73,*/
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db((db((db(not db(not db(self.get_subclass_c2_restoreva_rv1_restore() == True, self.dbs[54].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[54].subs[0].subs[0].subs[0].subs[0]), self.dbs[54].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[54].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[54].subs[0].subs[0].subs[1].subs[0]), self.dbs[54].subs[0].subs[0].subs[1])), self.dbs[54].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() == True, self.dbs[54].subs[0].subs[1].subs[0]), self.dbs[54].subs[0].subs[1])), self.dbs[54].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.avanzamentox,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.avanzamento, self.dbs[54].subs[1])
        else:
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
    
    def effect_NOMINAL_ACTUATION_state3_000(self):
        """
        CNL corrispondente:
         { commento: {36,}  se il timer SubClass_C2_timer_T9 non è attivo commento: {35,} o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex commento: {37,} o  se la variabile SubClass_C2_variabile_V2 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 11512, commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  commento: {36,} e  se il timer SubClass_C2_timer_T8 è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  commento: {37,} e  se la variabile SubClass_C2_variabile_V2 è  uguale a  False , commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
           
          se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro SubClass_C2_macroef_M7   commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        
        
          se il controllo ConsDef  è  uguale a FALSE ,  commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  maggiore di  commento: {54,} 7, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V10 del campo  MainClass_C1     commento: {105,} è  uguale a  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        
         ,altrimenti  commento: {68,}Attiva il timer SubClass_C2_timer_T9
        
        
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True ,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
           
         }
        """
        #  /*36,*/  se il timer SubClass_C2_timer_T9 non è attivo /*35,*/ o  se il controllo SubClass_C2_controllo_C1 è  diverso da avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da GialloxVerdex /*37,*/ o  se la variabile SubClass_C2_variabile_V2 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 11512, /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore avanzamentox
        if db((db((db(not db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[55].subs[0].subs[0].subs[0].subs[0]), self.dbs[55].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[55].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[55].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[55].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[55].subs[0].subs[0].subs[1].subs[1])), self.dbs[55].subs[0].subs[0].subs[1])), self.dbs[55].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v2() == True, self.dbs[55].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 11512, self.dbs[55].subs[0].subs[1].subs[1].subs[0]), self.dbs[55].subs[0].subs[1].subs[1])), self.dbs[55].subs[0].subs[1])), self.dbs[55].subs[0]):
            self.set_subclass_c2_comando_c6(GlobalEnumeration.avanzamentox)
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  /*36,*/ e  se il timer SubClass_C2_timer_T8 è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  uguale a avanzamentox /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  diverso da  True  /*37,*/ e  se la variabile SubClass_C2_variabile_V2 è  uguale a  False , /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db((db((db((db((db(not db(self.get_subclass_c2_restoreva_rv1_restore() == True, self.dbs[56].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[56].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t8().isScaduto(), self.dbs[56].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[56].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, self.dbs[56].subs[0].subs[0].subs[0].subs[1])), self.dbs[56].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v2() == True, self.dbs[56].subs[0].subs[0].subs[1].subs[0]), self.dbs[56].subs[0].subs[0].subs[1])), self.dbs[56].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v2() == False, self.dbs[56].subs[0].subs[1])), self.dbs[56].subs[0]):
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
        #  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M7   /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        if db(self.get_consdef() == False, self.dbs[57].subs[0]):
            self.macroSubclass_c2_macroef_m7(self.dbs[57].subs[1])
        else:
            self.set_subclass_c2_variabile_v3(6)
        #  se il controllo ConsDef  è  uguale a FALSE ,  /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  maggiore di  /*54,*/ 7, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V10 del campo  MainClass_C1     /*105,*/ è  uguale a  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  diverso da GialloxVerdex /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a GialloxVerdex, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True 
        #   ,altrimenti  /*68,*/Attiva il timer SubClass_C2_timer_T9
        if db((db((db((db(self.get_consdef() == False, self.dbs[58].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() > 7, self.dbs[58].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4()) if db(it.get_mainclass_c1().get_mainclass_c1_variabile_v10() == True, self.dbs[58].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), self.dbs[58].subs[0].subs[0].subs[0].subs[1])), self.dbs[58].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[58].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[58].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[58].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c8() == True, self.dbs[58].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[58].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[58].subs[0].subs[0].subs[1].subs[1])), self.dbs[58].subs[0].subs[0].subs[1])), self.dbs[58].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v6() == GlobalEnumeration.gialloxverdex, self.dbs[58].subs[0].subs[1].subs[0]), self.dbs[58].subs[0].subs[1])), self.dbs[58].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
        else:
            self.get_subclass_c2_timer_t9().attiva()
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  True ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
        if db(self.get_subclass_c2_restoreva_rv1_restore() == True, self.dbs[59].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.avanzamentox,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.gialloaverdea, self.dbs[59].subs[1])
    
    def effect_NORMALIZATION_state3_state4_000(self):
        """
        CNL corrispondente:
         { commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 9, commento: {69,}Disattiva il timer SubClass_C2_timer_T9
        
           
         }
        """
        #  /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 9, /*69,*/Disattiva il timer SubClass_C2_timer_T9
        if db((db((db(not db(self.get_subclass_c2_restoreva_rv1_restore() == True, self.dbs[60].subs[0].subs[0].subs[0].subs[0]), self.dbs[60].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[60].subs[0].subs[0].subs[1])), self.dbs[60].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p8() > 9, self.dbs[60].subs[0].subs[1].subs[0]), self.dbs[60].subs[0].subs[1])), self.dbs[60].subs[0]):
            self.get_subclass_c2_timer_t9().disattiva()
    
    def effect_PERMANENCE_state4_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C2_timer_T9 non è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T1 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T9 non è disattivo, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  commento: {54,} 2,  Applica gli effetti
               della macro SubClass_C2_macroef_M6  commento: {73,}
        
           
         commento: {43,}  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è attivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P8 è  minore di  commento: {55,} 6 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer SubClass_C2_timer_T8 non è disattivo, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co1
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        
        
         commento: {35,}  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  commento: {56,} 15 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 10 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 144, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co1
        
           
        
        }
        """
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T9 non è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T9 non è disattivo, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 1
        if db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[61].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), self.dbs[61].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isAttivato(), self.dbs[61].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[61].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[61].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c8() == True, self.dbs[61].subs[0].subs[0].subs[0].subs[1])), self.dbs[61].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[61].subs[0].subs[0].subs[1].subs[0]), self.dbs[61].subs[0].subs[0].subs[1])), self.dbs[61].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t1().isAttivato(), self.dbs[61].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), self.dbs[61].subs[0].subs[1].subs[1].subs[0]), self.dbs[61].subs[0].subs[1].subs[1])), self.dbs[61].subs[0].subs[1])), self.dbs[61].subs[0]):
            self.set_subclass_c2_variabile_v3(6)
        else:
            self.set_subclass_c2_variabile_v3(1)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo SubClass_C2_controllo_C8 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 non è  maggiore di  /*54,*/ 2,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M6
        if db((db((db((db(not db(self.get_subclass_c2_parametro_p6() == False, self.dbs[62].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[62].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[62].subs[0].subs[0].subs[0].subs[1])), self.dbs[62].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == False, self.dbs[62].subs[0].subs[0].subs[1].subs[0]), self.dbs[62].subs[0].subs[0].subs[1])), self.dbs[62].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p8() > 2, self.dbs[62].subs[0].subs[1].subs[0]), self.dbs[62].subs[0].subs[1])), self.dbs[62].subs[0]):
            self.macroSubclass_c2_macroef_m6(self.dbs[62].subs[1])
        #  /*73,*/
        #     
        #   /*43,*/  se MainClass_C1_timer_T4 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è attivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P8 è  minore di  /*55,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T8 non è disattivo, /*72,*/Azzera il contatore SubClass_C2_contatore_Co1
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V3 il valore 6
        if db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t4().isAttivato(), self.dbs[63].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), self.dbs[63].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[63].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p8() < 6, self.dbs[63].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[63].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[63].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[63].subs[0].subs[0].subs[0].subs[1])), self.dbs[63].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v3() == 4, self.dbs[63].subs[0].subs[0].subs[1].subs[0]), self.dbs[63].subs[0].subs[0].subs[1])), self.dbs[63].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t8().isDisattivato(), self.dbs[63].subs[0].subs[1].subs[0]), self.dbs[63].subs[0].subs[1])), self.dbs[63].subs[0]):
            self.get_subclass_c2_contatore_co1().resetta()
        else:
            self.set_subclass_c2_variabile_v3(6)
        #  /*35,*/  se il controllo SubClass_C2_controllo_C8 è  uguale a  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co1 è  diverso da  /*56,*/ 15 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  diverso da avanzamentox /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 144, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co1
        if db((db((db((db((db((db(self.get_subclass_c2_controllo_c8() == True, self.dbs[64].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 15, self.dbs[64].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[64].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[64].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), self.dbs[64].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[64].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[64].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, self.dbs[64].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[64].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[64].subs[0].subs[0].subs[0].subs[1])), self.dbs[64].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v3() < 10, self.dbs[64].subs[0].subs[0].subs[1])), self.dbs[64].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() < 144, self.dbs[64].subs[0].subs[1].subs[0]), self.dbs[64].subs[0].subs[1])), self.dbs[64].subs[0]):
            self.get_subclass_c2_contatore_co1().decrementa()
    
    # effect macros
    def macroSubclass_c2_macroef_m3(self, argomento_af1, argomento_af10, argomento_af5, argomento_af8, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a RossoGialloaVerdea, commento: {66,} Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        
           
         commento: {43,}  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  uguale a  commento: {53,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T8 è disattivo, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co7
        
         ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex commento: {67,}
        
        
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False  o  se l'argomento argomento_af5 non  è  diverso da GialloaVerdea commento: {39,}  commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C10 non è  diverso da  True  commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False , commento: {72,}Azzera il contatore SubClass_C2_contatore_Co7
        
         ,altrimenti  commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co7
        
        
         commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L4 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T1 è attivo commento: {36,} o  se il timer SubClass_C2_timer_T8 è attivo commento: {35,} e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox commento: {36,} o  se il timer SubClass_C2_timer_T9 è attivo commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V2 il valore  True  commento: {67,}
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a RossoGialloaVerdea, /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a RossoGialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T8 è disattivo, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co7

 ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T8 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo)} )  e  
( (subclass_c2_variabile_v3)  è minore di  (1) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_variabile_v3)  è uguale a  (9)) )  e  
( il timer 'subclass_c2_timer_t8' è inattivo )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è inattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*67,*/


 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False  o  se l'argomento argomento_af5 non  è  diverso da GialloaVerdea /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C10 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7

 ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/


 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False  o  se l'argomento argomento_af5 non  è  diverso da GialloaVerdea /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C10 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (False)) )  o  
( ( ( ( negazione di (negazione di ((argomento_af5)  è uguale a  (gialloaverdea))) )  e  ( (subclass_c2_variabile_v3)  è minore di  (2) ) )  e  ( negazione di (negazione di ((subclass_c2_controllo_c10)  è uguale a  (True))) ) )  e  
( negazione di ((subclass_c2_parametro_p6)  è uguale a  (True)) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (negazione di ((argomento_af5)  è uguale a  (gialloaverdea))) )  e  ( (subclass_c2_variabile_v3)  è minore di  (2) ) )  e  ( negazione di (negazione di ((subclass_c2_controllo_c10)  è uguale a  (True))) ) )  e  
( negazione di ((subclass_c2_parametro_p6)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((argomento_af5)  è uguale a  (gialloaverdea))) )  e  ( (subclass_c2_variabile_v3)  è minore di  (2) ) )  e  ( negazione di (negazione di ((subclass_c2_controllo_c10)  è uguale a  (True))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((argomento_af5)  è uguale a  (gialloaverdea))) )  e  ( (subclass_c2_variabile_v3)  è minore di  (2) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((argomento_af5)  è uguale a  (gialloaverdea)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af5)  è uguale a  (gialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af5)  è uguale a  (gialloaverdea)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c10)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L4 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L4 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l4' è inattivo)} )  e  
( il timer 'subclass_c2_timer_t1' è attivo ) )  o  
( ( il timer 'subclass_c2_timer_t8' è attivo )  e  
( negazione di (negazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox))) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l4' è inattivo)} )  e  
( il timer 'subclass_c2_timer_t1' è attivo )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l4' è inattivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c2_lista_l4' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t8' è attivo )  e  
( negazione di (negazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox))) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c5)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c2_timer_t9' è attivo )  e  
( negazione di (il timer 'subclass_c2_timer_t1' è scaduto) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a RossoGialloaVerdea, /*66,*/ Assegna al comando SubClass_C2_comando_C3 il valore avanzamentox
        if db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c3(GlobalEnumeration.avanzamentox)
        #  /*43,*/  se MainClass_C1_timer_T3 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T8 è disattivo, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co7
        #   ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2())), di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v3() < 1, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v3() == 9, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t8().isDisattivato(), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co7().decrementa()
        else:
            self.set_subclass_c2_variabile_v6(GlobalEnumeration.gialloxverdex)
        #  /*67,*/
        #   /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  False  o  se l'argomento argomento_af5 non  è  diverso da GialloaVerdea /*39,*/  /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C10 non è  diverso da  True  /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V2 non è  uguale a  False , /*72,*/Azzera il contatore SubClass_C2_contatore_Co7
        #   ,altrimenti  /*71,*/Decrementa il contatore SubClass_C2_contatore_Co7
        if db((db((db(not db(self.get_subclass_c2_restoreva_rv1_restore() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db((db((db(not db(not db(argomento_af5 == GlobalEnumeration.gialloaverdea, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v3() < 2, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c10() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_contatore_co7().resetta()
        else:
            self.get_subclass_c2_contatore_co7().decrementa()
        #  /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C2_lista_L4 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T1 è attivo /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo /*35,*/ e  se il controllo SubClass_C2_controllo_C5 non è  diverso da avanzamentox /*36,*/ o  se il timer SubClass_C2_timer_T9 è attivo /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V2 il valore  True
        if db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t8().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t9().isAttivato(), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c2_variabile_v2(True)
    
    def macroSubclass_c2_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  diverso da  commento: {56,} 4 commento: {35,} o  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 14,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
           
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  minore di  commento: {55,} 13304, commento: {69,}Disattiva il timer SubClass_C2_timer_T1
        
           
         commento: {35,}  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 1, commento: {68,}Attiva il timer SubClass_C2_timer_T1
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c2_parametro_p8)  è uguale a  (4)) )  o  
( (subclass_c2_controllo_c5)  è uguale a  (avanzamentox) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p8)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p8)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (avanzamentox)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (14))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*73,*/

   
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 13304, /*69,*/Disattiva il timer SubClass_C2_timer_T1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 13304""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co1)  è minore di  (13304)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 1, /*68,*/Attiva il timer SubClass_C2_timer_T1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True))) )  o  
( negazione di ((subclass_c2_controllo_c8)  è uguale a  (True)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_controllo_c8)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è minore di  (1))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroSubclass_c2_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P8 è  diverso da  /*56,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a c270 ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
        if db((db((db(not db(self.get_subclass_c2_parametro_p8() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.c270,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[1])
        #  /*73,*/
        #     
        #   /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  minore di  /*55,*/ 13304, /*69,*/Disattiva il timer SubClass_C2_timer_T1
        if db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co1().get_valore() < 13304, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_timer_t1().disattiva()
        #  /*35,*/  se il controllo SubClass_C2_controllo_C8 non è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C8 è  diverso da  True  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 1, /*68,*/Attiva il timer SubClass_C2_timer_T1
        if db((db((db(not db(not db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v3() < 1, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_timer_t1().attiva()
    
    def macroSubclass_c2_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {42,}  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  True ,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  True ,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*42,*/  se  MainClass_C1_controllo_C8 del campo  MainClass_C1 di SubClass_C2_lista_L2 è  diverso da  True ,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a GialloaVerdea ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
        if db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2())), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.avanzamentox,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.gialloaverdea, di_ctx.subs[0].subs[1])
    
    def macroSubclass_c2_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore SubClass_C2_contatore_Co1 è  uguale a  commento: {53,} 14512 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 123,  Applica gli effetti
               della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea ) commento: {73,}
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  False  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 non è  minore di  commento: {55,} 4 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  commento: {54,} 1504 o  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer SubClass_C2_timer_T9
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore SubClass_C2_contatore_Co1 è  uguale a  /*53,*/ 14512 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123,  Applica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C2_contatore_Co1 è  uguale a  /*53,*/ 14512 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_contatore_co1)  è uguale a  (14512) )  e  ( negazione di (il timer 'subclass_c2_timer_t1' è attivo) ) )  e  ( negazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (False))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_contatore_co1)  è uguale a  (14512) )  e  ( negazione di (il timer 'subclass_c2_timer_t1' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (14512)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v2)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co7)  è uguale a  (123)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (123))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (123)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )"""),#1
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 1504 o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer SubClass_C2_timer_T9

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 1504 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_restoreva_rv1_restore)  è uguale a  (False) )  o  
( negazione di ((subclass_c2_variabile_v3)  è minore di  (4)) ) )  o  
( (subclass_c2_contatore_co1)  è maggiore di  (1504) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (subclass_c2_restoreva_rv1_restore)  è uguale a  (False) )  o  
( negazione di ((subclass_c2_variabile_v3)  è minore di  (4)) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v3)  è minore di  (4))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co1)  è maggiore di  (1504)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore SubClass_C2_contatore_Co1 è  uguale a  /*53,*/ 14512 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V2 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 123,  Applica gli effetti
        #         della macro SubClass_C2_macroef_M3( con argomento_af1   uguale a avanzamentox ,argomento_af8   uguale a avanzamento ,argomento_af10   uguale a True ,argomento_af5   uguale a GialloaVerdea )
        if db((db((db((db(self.get_subclass_c2_contatore_co1().get_valore() == 14512, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 123, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c2_macroef_m3(GlobalEnumeration.avanzamentox,True,GlobalEnumeration.gialloaverdea,GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[1])
        #  /*73,*/
        #     
        #   /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 non è  minore di  /*55,*/ 4 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 1504 o  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer SubClass_C2_timer_T9
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore GialloxVerdex
        if db((db((db((db(self.get_subclass_c2_restoreva_rv1_restore() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v3() < 4, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co1().get_valore() > 1504, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_timer_t9().disattiva()
        else:
            self.set_subclass_c2_variabile_v6(GlobalEnumeration.gialloxverdex)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m10")
    def macroSubclass_c2_macrove_m10(self, argomento_ave2, argomento_ave3, argomento_ave5, argomento_ave6, argomento_ave7, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P8 è  maggiore di  commento: {54,} 6 commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  commento: {55,} 1430 o  se l'argomento argomento_ave5 è  uguale a  True  commento: {39,}  o  se l'argomento argomento_ave5 è  uguale a  True  commento: {39,}  e  se l'argomento argomento_ave5 non  è  uguale a  True  commento: {39,}  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 1145, Solo una delle seguenti { 
         commento: {62,} commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  diverso da RossoGialloaVerdea commento: {37,} e  se la variabile SubClass_C2_variabile_V3 è  diverso da  commento: {56,} 10 commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox commento: {38,} o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  commento: {54,} 141 commento: {35,} e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox commento: {35,} o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox, Almeno una delle seguenti { 
          se la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox commento: {40,} ,  commento: {45,}  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  commento: {105,} è  uguale a  commento: {53,} 1223, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1 , Verifica che   commento: {49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T8 non sia disattivo
        
        
         } Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True 
         commento: {104,} e  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo commento: {,} 
        
        
         } Verifica che   commento: {48,49,50,51,52,}  commento: {,}  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
         commento: {104,} o  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T9 sia scaduto
         commento: {104,} e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox commento: {39,} 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C10 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co1 non sia  uguale a  commento: {53,} 14
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1430 o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave5 non  è  uguale a  True  /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 1145, Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141 /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox, Almeno una delle seguenti { 
  se la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 1223, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1 , Verifica che   /*49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo /*,*/ 


 } Verifica che   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co1 non sia  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1430 o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave5 non  è  uguale a  True  /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 1145, Solo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141 /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox, Almeno una delle seguenti { 
  se la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 1223, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1 , Verifica che   /*49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1430 o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave5 non  è  uguale a  True  /*39,*/  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 1145""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1430 o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  o  se l'argomento argomento_ave5 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave5 non  è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1430 o  se l'argomento argomento_ave5 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1430""", [
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P8 è  maggiore di  /*54,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co1 non è  minore di  /*55,*/ 1430""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co1)  è minore di  (1430)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave5 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave5 è  uguale a  True  /*39,*/  e  se l'argomento argomento_ave5 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave5 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave5 non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 1145""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (1145))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (1145)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141 /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox, Almeno una delle seguenti { 
  se la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 1223, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1 , Verifica che   /*49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141 /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox, Almeno una delle seguenti { 
  se la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 1223, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1 , Verifica che   /*49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141 /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox /*35,*/ o  se il controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox /*38,*/ o  se il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141 /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea /*37,*/ e  se la variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V3 è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v3)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P5 è  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141 /*35,*/ e  se il controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox""", [
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co1 è  maggiore di  /*54,*/ 141""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C5 è  uguale a avanzamentox""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 non è  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 1223, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1 , Verifica che   /*49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox /*40,*/ ,  /*45,*/  se  MainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 1223, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  SubClass_C2_macrova_M7 ( con argomento_a9   uguale a c270 ,argomento_a6   uguale a GialloxVerdex ,argomento_a2   uguale a avanzamentox ,argomento_a7   uguale a c270 ,argomento_a3   uguale a GialloxVerdex  e argomento_a4   uguale a GialloxVerdex )   è  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m7')  è uguale a  (avanzamentox)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m7'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co3 del campo  MainClass_C1 di SubClass_C2_lista_L2 esiste e  /*105,*/ è  uguale a  /*53,*/ 1223, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (1223))""", [
                            DIBoolExpr("""EqualImpl\n/*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3 del campo mainclass_c1 della lista subclass_c2_lista_l2)  è uguale a  (1223)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co1 non sia  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,51,52,*/  /*,*/  la variabile SubClass_C2_variabile_V2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave9 non  sia  diverso da RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (rossogiallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox /*39,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C10 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T9 sia scaduto
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a avanzamentox""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T9 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave2 non  sia  uguale a avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C10 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co1 non sia  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co1)  è uguale a  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(self.get_subclass_c2_parametro_p8() > 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() < 1430, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave5 == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(argomento_ave5 == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave5 == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 1145, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p10() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v3() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_contatore_co1().get_valore() > 141, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c5() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(not db(db(self.macroSubclass_c2_macrova_m7(GlobalEnumeration.avanzamentox,GlobalEnumeration.gialloxverdex,GlobalEnumeration.gialloxverdex,GlobalEnumeration.gialloxverdex,GlobalEnumeration.c270,GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co3().get_valore() == 1223, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db(not db(not db(self.get_subclass_c2_parametro_p6() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(argomento_ave9 == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(not db(self.get_subclass_c2_variabile_v2() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave9 == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_timer_t9().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(argomento_ave2 == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_controllo_c10() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co1().get_valore() == 14, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m8")
    def macroSubclass_c2_macrove_m8(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {36,}  se il timer SubClass_C2_timer_T9 non è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False , Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C1 non sia  diverso da avanzamentox
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False , Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False , Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T9 non è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P6 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T9 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  diverso da avanzamentox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C1 non sia  diverso da avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c1)  è uguale a  (avanzamentox))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m1")
    def macroSubclass_c2_macrova_m1(self, argomento_a1, argomento_a10, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore GialloxVerdex commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore GialloxVerdex
        return GlobalEnumeration.gialloxverdex
    
    @srf_value_macro("macroSubclass_c2_macrova_m4")
    def macroSubclass_c2_macrova_m4(self, argomento_a1, argomento_a10, argomento_a2, argomento_a5, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  uguale a  False ,  commento: {41,}  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  diverso da RossoGialloaVerdea, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1  commento: {37,} o  se la variabile SubClass_C2_variabile_V3 è  minore di  commento: {55,} 8,  commento: {45,}  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a  commento: {53,} 152, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  commento: {42,} e  se  MainClass_C1_controllo_C5 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  diverso da RossoGialloVerde commento: {44,} o  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  True  commento: {110,} e  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è attivo e  se l'argomento argomento_a1 è  uguale a  True  commento: {39,} ,  commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a  True , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T3 del campo  MainClass_C1     è attivo , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  False ,  /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a  /*53,*/ 152, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*42,*/ e  se  MainClass_C1_controllo_C5 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da RossoGialloVerde /*44,*/ o  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True  /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è attivo e  se l'argomento argomento_a1 è  uguale a  True  /*39,*/ ,  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a  True , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T3 del campo  MainClass_C1     è attivo , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  False ,  /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a  /*53,*/ 152, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*42,*/ e  se  MainClass_C1_controllo_C5 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da RossoGialloVerde /*44,*/ o  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True  /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è attivo e  se l'argomento argomento_a1 è  uguale a  True  /*39,*/ ,  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a  True , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T3 del campo  MainClass_C1     è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (subclass_c2_parametro_p6)  è uguale a  (False) )  e  
( per ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1)) allora (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)))} ) )  o  
( ( ( (subclass_c2_variabile_v3)  è minore di  (8) )  e  ( per ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (152))} ) )  e  
( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c5 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloverde)))} ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_parametro_p6)  è uguale a  (False) )  e  
( per ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1)) allora (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)))} )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1)) allora (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1)) allora (negazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_variabile_v3)  è minore di  (8) )  e  ( per ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (152))} ) )  e  
( per ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c5 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloverde)))} )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_variabile_v3)  è minore di  (8) )  e  ( per ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (152))} )""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v3)  è minore di  (8)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (152))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)) allora ((mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (152))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (152)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((mainclass_c1_controllo_c5 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloverde)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True))} )  e  ( il timer 'subclass_c2_restoreti_ti4_restore' è attivo ) )  e  
( ( (argomento_a1)  è uguale a  (True) )  e  ( per ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo) allora ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True))} ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True))} )  e  ( il timer 'subclass_c2_restoreti_ti4_restore' è attivo )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti4_restore' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (argomento_a1)  è uguale a  (True) )  e  ( per ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo) allora ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True))} )""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a1)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se (il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo) allora ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo) allora ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True))""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  uguale a  False ,  /*41,*/  se MainClass_C1_parametro_P10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  diverso da RossoGialloaVerdea, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  /*37,*/ o  se la variabile SubClass_C2_variabile_V3 è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co8 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a  /*53,*/ 152, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*42,*/ e  se  MainClass_C1_controllo_C5 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  diverso da RossoGialloVerde /*44,*/ o  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True  /*110,*/ e  se il ripristino del timer  SubClass_C2_restoreTI_TI4 è attivo e  se l'argomento argomento_a1 è  uguale a  True  /*39,*/ ,  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a  True , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T3 del campo  MainClass_C1     è attivo , assegna alla macro il valore  True
        if db((db((db((db(self.get_subclass_c2_parametro_p6() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p10() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v3() < 8, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co8().get_valore() == 152, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_restoreti_ti4_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db(argomento_a1 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c2_macrova_m5")
    def macroSubclass_c2_macrova_m5(self, argomento_a10, argomento_a5, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m5_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c2_macrova_m7")
    def macroSubclass_c2_macrova_m7(self, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore avanzamentox
        return GlobalEnumeration.avanzamentox
    
    @srf_value_macro("macroSubclass_c2_macrova_m9")
    def macroSubclass_c2_macrova_m9(self, argomento_a2, argomento_a3, argomento_a4, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {36,}  se il timer SubClass_C2_timer_T1 non è scaduto , assegna alla macro il valore avanzamentox
        
         commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è scaduto , assegna alla macro il valore avanzamentox""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*36,*/  se il timer SubClass_C2_timer_T1 non è scaduto , assegna alla macro il valore avanzamentox
        if db(not db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.avanzamentox
        #  /*46,*/ assegna alla macro il valore avanzamentox
        return GlobalEnumeration.avanzamentox
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c4_prev(self.get_subclass_c2_previousco_c4())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())
        self.set_subclass_c2_previousva_pv5_prev(self.get_subclass_c2_previousva_pv5())

class SubClass_C2_RecordHeaderR1(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled12, recordfiled13, recordfiled14):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled12(recordfiled12)
        self.set_recordfiled13(recordfiled13)
        self.set_recordfiled14(recordfiled14)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled12(self, recordfiled12):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"), recordfiled12)

    def set_recordfiled13(self, recordfiled13):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"), recordfiled13)

    def set_recordfiled14(self, recordfiled14):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled14"), recordfiled14)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled12(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"))

    def get_recordfiled13(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled13"))

    def get_recordfiled14(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled14"))



