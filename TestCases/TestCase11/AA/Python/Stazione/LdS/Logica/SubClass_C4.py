# Codice del modello 'TestCase11', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

class SubClass_C4(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C4, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c4_previousva_pv1(False)
        self.set_subclass_c4_previousva_pv2(0)
        self.set_subclass_c4_previousva_pv3(0)
        self.set_subclass_c4_restoreva_rv1(False)
        self.set_subclass_c4_variabile_v3(GlobalEnumeration.rossoverde)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2 : set([]),
            Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C4
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
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_0 = 3
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_1 = 4
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_2 = 5
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_3 = 6
        _State1__State2__stateSheet_0__normalization__transitionTo_0 = 7

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c4_lista_l9, subclass_c4_parametro_p1, subclass_c4_parametro_p2, subclass_c4_parametro_p9):
        # initialize the record type parameters
        self.set_subclass_c4_lista_l9(subclass_c4_lista_l9)
        # initialize the simple type parameters
        self.set_subclass_c4_parametro_p1(subclass_c4_parametro_p1)
        self.set_subclass_c4_parametro_p2(subclass_c4_parametro_p2)
        self.set_subclass_c4_parametro_p9(subclass_c4_parametro_p9)

        # initialize the timers
        self.set_subclass_c4_restoreti_ti1(2000)
        self.set_subclass_c4_restoreti_ti1_restore(2000)
        self.set_subclass_c4_restoreti_ti2(30213000)
        self.set_subclass_c4_restoreti_ti2_restore(30213000)
        self.set_subclass_c4_restoreti_ti3(1000)
        self.set_subclass_c4_restoreti_ti3_restore(1000)
        self.set_subclass_c4_restoreti_ti4(24000)
        self.set_subclass_c4_restoreti_ti4_restore(24000)
        self.set_subclass_c4_timer_t2(2000)
        self.set_subclass_c4_timer_t3(3000)
        self.set_subclass_c4_timer_t8(545000)

        self.timers = [self.subclass_c4_restoreti_ti1,self.subclass_c4_restoreti_ti1_restore,self.subclass_c4_restoreti_ti2,self.subclass_c4_restoreti_ti2_restore,self.subclass_c4_restoreti_ti3,self.subclass_c4_restoreti_ti3_restore,self.subclass_c4_restoreti_ti4,self.subclass_c4_restoreti_ti4_restore,self.subclass_c4_timer_t2,self.subclass_c4_timer_t3,self.subclass_c4_timer_t8,]

        # initialize the counters
        self.set_subclass_c4_contatore_co5(0)
        self.set_subclass_c4_contatore_co8(0)

    # setters for record type parameters
    def set_subclass_c4_lista_l9(self, subclass_c4_lista_l9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_lista_l9",subclass_c4_lista_l9)


    # getters for record type parameters
    def get_subclass_c4_lista_l9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_lista_l9")


    # setters for simple type parameters
    def set_subclass_c4_parametro_p1(self, subclass_c4_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_parametro_p1",subclass_c4_parametro_p1)

    def set_subclass_c4_parametro_p2(self, subclass_c4_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_parametro_p2",subclass_c4_parametro_p2)

    def set_subclass_c4_parametro_p9(self, subclass_c4_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_parametro_p9",subclass_c4_parametro_p9)


    # getters for simple type parameters
    def get_subclass_c4_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_parametro_p1")

    def get_subclass_c4_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_parametro_p2")

    def get_subclass_c4_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_parametro_p9")


    # setters for comandi al piazzale
    def set_subclass_c4_comando_c10(self, subclass_c4_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_comando_c10",subclass_c4_comando_c10)

    def set_subclass_c4_comando_c2(self, subclass_c4_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_comando_c2",subclass_c4_comando_c2)

    def set_subclass_c4_comando_c9(self, subclass_c4_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_comando_c9",subclass_c4_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c4_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_controllo_c1")

    def get_subclass_c4_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_controllo_c3")

    def get_subclass_c4_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_controllo_c7")

    def get_subclass_c4_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_controllo_c8")

    def get_subclass_c4_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c4")

    def get_subclass_c4_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c5")

    def get_subclass_c4_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c6")


    # setters for state variables
    def set_subclass_c4_previousco_c4_prev(self, subclass_c4_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c4_prev",subclass_c4_previousco_c4_prev)
    def set_subclass_c4_previousco_c5_prev(self, subclass_c4_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c5_prev",subclass_c4_previousco_c5_prev)
    def set_subclass_c4_previousco_c6_prev(self, subclass_c4_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c6_prev",subclass_c4_previousco_c6_prev)
    def set_subclass_c4_previousva_pv1(self, subclass_c4_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv1",subclass_c4_previousva_pv1)
    def set_subclass_c4_previousva_pv1_prev(self, subclass_c4_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv1_prev",subclass_c4_previousva_pv1_prev)
    def set_subclass_c4_previousva_pv2(self, subclass_c4_previousva_pv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv2",subclass_c4_previousva_pv2)
    def set_subclass_c4_previousva_pv2_prev(self, subclass_c4_previousva_pv2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv2_prev",subclass_c4_previousva_pv2_prev)
    def set_subclass_c4_previousva_pv3(self, subclass_c4_previousva_pv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv3",subclass_c4_previousva_pv3)
    def set_subclass_c4_previousva_pv3_prev(self, subclass_c4_previousva_pv3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv3_prev",subclass_c4_previousva_pv3_prev)
    def set_subclass_c4_restoreva_rv1(self, subclass_c4_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_restoreva_rv1",subclass_c4_restoreva_rv1)
    def set_subclass_c4_variabile_v3(self, subclass_c4_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c4_variabile_v3",subclass_c4_variabile_v3)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c4_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c4_prev")

    def get_subclass_c4_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c5_prev")

    def get_subclass_c4_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousco_c6_prev")

    def get_subclass_c4_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv1")

    def get_subclass_c4_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv1_prev")

    def get_subclass_c4_previousva_pv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv2")

    def get_subclass_c4_previousva_pv2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv2_prev")

    def get_subclass_c4_previousva_pv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv3")

    def get_subclass_c4_previousva_pv3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_previousva_pv3_prev")

    def get_subclass_c4_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_restoreva_rv1")

    def get_subclass_c4_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_restoreva_rv1_restore")

    def get_subclass_c4_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c4_variabile_v3")


    # setters for timers
    def set_subclass_c4_restoreti_ti1(self, timerDuration):
        self.subclass_c4_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti1", self.memory)

    def set_subclass_c4_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c4_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti1_restore", self.memory)

    def set_subclass_c4_restoreti_ti2(self, timerDuration):
        self.subclass_c4_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti2", self.memory)

    def set_subclass_c4_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c4_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti2_restore", self.memory)

    def set_subclass_c4_restoreti_ti3(self, timerDuration):
        self.subclass_c4_restoreti_ti3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti3", self.memory)

    def set_subclass_c4_restoreti_ti3_restore(self, timerDuration):
        self.subclass_c4_restoreti_ti3_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti3_restore", self.memory)

    def set_subclass_c4_restoreti_ti4(self, timerDuration):
        self.subclass_c4_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti4", self.memory)

    def set_subclass_c4_restoreti_ti4_restore(self, timerDuration):
        self.subclass_c4_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_restoreti_ti4_restore", self.memory)

    def set_subclass_c4_timer_t2(self, timerDuration):
        self.subclass_c4_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_timer_t2", self.memory)

    def set_subclass_c4_timer_t3(self, timerDuration):
        self.subclass_c4_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_timer_t3", self.memory)

    def set_subclass_c4_timer_t8(self, timerDuration):
        self.subclass_c4_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c4_timer_t8", self.memory)


    # getters for timers
    def get_subclass_c4_restoreti_ti1(self):
        return self.subclass_c4_restoreti_ti1

    def get_subclass_c4_restoreti_ti1_restore(self):
        return self.subclass_c4_restoreti_ti1_restore

    def get_subclass_c4_restoreti_ti2(self):
        return self.subclass_c4_restoreti_ti2

    def get_subclass_c4_restoreti_ti2_restore(self):
        return self.subclass_c4_restoreti_ti2_restore

    def get_subclass_c4_restoreti_ti3(self):
        return self.subclass_c4_restoreti_ti3

    def get_subclass_c4_restoreti_ti3_restore(self):
        return self.subclass_c4_restoreti_ti3_restore

    def get_subclass_c4_restoreti_ti4(self):
        return self.subclass_c4_restoreti_ti4

    def get_subclass_c4_restoreti_ti4_restore(self):
        return self.subclass_c4_restoreti_ti4_restore

    def get_subclass_c4_timer_t2(self):
        return self.subclass_c4_timer_t2

    def get_subclass_c4_timer_t3(self):
        return self.subclass_c4_timer_t3

    def get_subclass_c4_timer_t8(self):
        return self.subclass_c4_timer_t8


    # setters for counters
    def set_subclass_c4_contatore_co5(self, counterInitValue):
        self.subclass_c4_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c4_contatore_co5", self.memory)

    def set_subclass_c4_contatore_co8(self, counterInitValue):
        self.subclass_c4_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c4_contatore_co8", self.memory)


    # getters for counters
    def get_subclass_c4_contatore_co5(self):
        return self.subclass_c4_contatore_co5

    def get_subclass_c4_contatore_co8(self):
        return self.subclass_c4_contatore_co8



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è disattivo, Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 10, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  uguale a  True 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è disattivo, Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 10, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  uguale a  True 


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è disattivo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T3 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 10, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  uguale a  True 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 10, Almeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 10""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 10""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C1 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 10""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c4_parametro_p9)  è minore di  (10)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*35,*/  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534


 }""", [
                    DIBoolExpr("""EqualImpl\nil controllo SubClass_C4_controllo_C1 è  uguale a  False""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10 o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 non è  uguale a c180""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 10""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250 /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C4_contatore_Co5 è  diverso da  /*56,*/ 1250""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co5)  è uguale a  (1250)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nil contatore SubClass_C4_contatore_Co8 è  minore di  /*55,*/ 13213""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C4_timer_T2 non è attivo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T2 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t2' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C4_parametro_P1 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144 /*35,*/ e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C4_timer_T3 è scaduto""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro SubClass_C4_parametro_P1 è  uguale a  True""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C1 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C4_contatore_Co8 non è  minore di  /*55,*/ 144""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c4_contatore_co8)  è minore di  (144)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C1 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""LessThanImpl\nche   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 125021""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  uguale a  /*53,*/ 1534""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 8 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 15 /*36,*/ e  se il timer SubClass_C4_timer_T8 non è attivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 8 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 15 /*36,*/ e  se il timer SubClass_C4_timer_T8 non è attivo, Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 8 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 15 /*36,*/ e  se il timer SubClass_C4_timer_T8 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 8 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 15""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 8""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 8""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 15""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co5)  è uguale a  (15)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T8 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t8' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                    ]),#1
                    ]),#0
                    ]),#3
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#4
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#5
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 è  maggiore di  /*54,*/ 1513 /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 12 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C4_controllo_C3 sia  diverso da GialloxVerdex""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 è  maggiore di  /*54,*/ 1513 /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 12 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C4_controllo_C3 sia  diverso da GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 è  maggiore di  /*54,*/ 1513 /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 12 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 è  maggiore di  /*54,*/ 1513""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 non è  diverso da c180""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_variabile_v3)  è uguale a  (c180))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C4_contatore_Co8 è  maggiore di  /*54,*/ 1513""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 12 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C4_contatore_Co5 non è  uguale a  /*53,*/ 12""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co5)  è uguale a  (12)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C4_controllo_C3 sia  diverso da GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c3)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#6
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*34,*/  se il parametro SubClass_C4_parametro_P2 è  diverso da  True , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 non è scaduto /*35,*/ o  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  minore di  /*55,*/ 1221""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*34,*/  se il parametro SubClass_C4_parametro_P2 è  diverso da  True , Tutte le seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T3 non è scaduto /*35,*/ o  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P2 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C4_timer_T3 non è scaduto /*35,*/ o  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C4_timer_T3 non è scaduto /*35,*/ o  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T3 non è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è scaduto""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C1 è  diverso da  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C1 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  minore di  /*55,*/ 1221""", [
                    DIBoolExpr("""LessThanImpl\n(subclass_c4_contatore_co8)  è minore di  (1221)""", [
                    ]),#0
                    ]),#1
                    ]),#7
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C4_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm4 del campo mainclass_c1 della lista subclass_c4_lista_l9'""", [
                    ]),#0
                    ]),#8
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C4_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm4 del campo mainclass_c1 della lista subclass_c4_lista_l9'""", [
                    ]),#0
                    ]),#9
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C4_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm4 del campo mainclass_c1 della lista subclass_c4_lista_l9'""", [
                    ]),#0
                    ]),#10
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C4_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm4 del campo mainclass_c1 della lista subclass_c4_lista_l9'""", [
                    ]),#0
                    ]),#11
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C4_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a avviox )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm4 del campo mainclass_c1 della lista subclass_c4_lista_l9'""", [
                    ]),#0
                    ]),#12
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C4_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm4 del campo mainclass_c1 della lista subclass_c4_lista_l9'""", [
                    ]),#0
                    ]),#13
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C4_lista_L9
 di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm4 del campo mainclass_c1 della lista subclass_c4_lista_l9'""", [
                    ]),#0
                    ]),#14
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2,
                         guard=(self.dbs[7], ),
                         effect=(self.dbs[14], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2,
                         guard=(self.dbs[6], ),
                         effect=(self.dbs[13], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[9], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[10], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2,
                         guard=(self.dbs[4], ),
                         effect=(self.dbs[11], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,
                         guard=(self.dbs[5], ),
                         effect=(self.dbs[12], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[8], ),
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_subclass_c4_previousco_c4_prev(False)
        self.set_subclass_c4_previousco_c5_prev(GlobalEnumeration.avanzamentox)
        self.set_subclass_c4_previousco_c6_prev(GlobalEnumeration.rossogialloverde)
        self.set_subclass_c4_previousva_pv1_prev(self.get_subclass_c4_previousva_pv1())
        self.set_subclass_c4_previousva_pv2_prev(self.get_subclass_c4_previousva_pv2())
        self.set_subclass_c4_previousva_pv3_prev(self.get_subclass_c4_previousva_pv3())

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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2):
                if(self.guard_PERMANENCE_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1):
                if(self.guard_NORMALIZATION_state1_state2_000()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__normalization__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0
                elif(self.guard_NOMINAL_ACTUATION_state1_state2_000()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state1_state2_001()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_2
                elif(self.guard_NOMINAL_ACTUATION_state1_001()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_3
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2)
            self.effect_PERMANENCE_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_3:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1)
            self.effect_NOMINAL_ACTUATION_state1_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state2)
            self.effect_NORMALIZATION_state1_state2_000()
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
        
         commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C4_timer_T3 non è disattivo, Tutte le seguenti { 
         commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 non è  minore di  commento: {55,} 10, Almeno una delle seguenti { 
         commento: {68,} commento: {35,}  se il controllo SubClass_C4_controllo_C1 è  uguale a  False , Almeno una delle seguenti { 
         commento: {67,} commento: {37,}  se la variabile SubClass_C4_variabile_V3 non è  uguale a c180 commento: {34,} e  se il parametro SubClass_C4_parametro_P9 è  uguale a  commento: {53,} 10 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 è  diverso da  commento: {56,} 1250 commento: {38,} e  se il contatore SubClass_C4_contatore_Co8 è  minore di  commento: {55,} 13213 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C4_timer_T2 non è attivo, Almeno una delle seguenti { 
         commento: {68,} commento: {37,}  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 è  uguale a  False , Almeno una delle seguenti { 
         commento: {36,}  se il timer SubClass_C4_timer_T3 è scaduto commento: {34,} e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  False  commento: {38,} e  se il contatore SubClass_C4_contatore_Co8 non è  minore di  commento: {55,} 144 commento: {35,} e  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  minore di  commento: {55,} 125021
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  uguale a  commento: {53,} 1534
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  uguale a  True 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        return db((db(not db((db(self.get_consdef() == False, self.dbs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_timer_t3().isDisattivato(), self.dbs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0]) or db((db(not db((db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_controllo_c1() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_parametro_p9() < 10, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_controllo_c1() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_parametro_p9() == 10, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_contatore_co5().get_valore() == 1250, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c4_contatore_co8().get_valore() < 13213, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_parametro_p1() == True, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_timer_t2().isAttivato(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_parametro_p1() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db((db(self.get_subclass_c4_timer_t3().isScaduto(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_parametro_p1() == True, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_controllo_c1() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_contatore_co8().get_valore() < 144, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_controllo_c1() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c4_parametro_p1() == True, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c4_contatore_co8().get_valore() < 125021, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_subclass_c4_contatore_co8().get_valore() == 1534, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_parametro_p1() == True, self.dbs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1]), self.dbs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[1])), self.dbs[1])
    
    def guard_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[2])
    
    def guard_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {  commento: {37,}  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 è  maggiore di  commento: {54,} 8 commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  commento: {53,} 15 commento: {36,} e  se il timer SubClass_C4_timer_T8 non è attivo, Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
        
         }
        """
        return db((db(not db((db((db((db((db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_parametro_p9() > 8, self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_contatore_co5().get_valore() == 15, self.dbs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_timer_t8().isAttivato(), self.dbs[3].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0]) or db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[3].subs[0].subs[1]), self.dbs[3].subs[0])), self.dbs[3])
    
    def guard_NOMINAL_ACTUATION_state1_state2_001(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[4])
    
    def guard_NOMINAL_ACTUATION_state1_001(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[5])
    
    def guard_NORMALIZATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {  commento: {37,}  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C4_contatore_Co8 è  maggiore di  commento: {54,} 1513 commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 non è  uguale a  commento: {53,} 12 commento: {35,} e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C4_controllo_C3 sia  diverso da GialloxVerdex
        
         }
        """
        return db((db(not db((db((db((db(not db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[6].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[6].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_contatore_co8().get_valore() > 1513, self.dbs[6].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_contatore_co5().get_valore() == 12, self.dbs[6].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[6].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, self.dbs[6].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[6].subs[0].subs[0].subs[1].subs[1])), self.dbs[6].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[0]) or db(not db(self.get_subclass_c4_controllo_c3() == GlobalEnumeration.gialloxverdex, self.dbs[6].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1]), self.dbs[6].subs[0])), self.dbs[6])
    
    def guard_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {67,} commento: {34,}  se il parametro SubClass_C4_parametro_P2 è  diverso da  True , Tutte le seguenti { 
         commento: {36,}  se il timer SubClass_C4_timer_T3 non è scaduto commento: {35,} o  se il controllo SubClass_C4_controllo_C1 è  diverso da  False  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {35,} e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  minore di  commento: {55,} 1221
        
        
        }
        """
        return db((db(not db(not db(self.get_subclass_c4_parametro_p2() == True, self.dbs[7].subs[0].subs[0].subs[0]), self.dbs[7].subs[0].subs[0]) or db(not db((db(not db(self.get_subclass_c4_timer_t3().isScaduto(), self.dbs[7].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[7].subs[0].subs[1].subs[0].subs[0]) or db((db((db((db((db(not db(self.get_subclass_c4_controllo_c1() == False, self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[7].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[7].subs[0].subs[1].subs[0].subs[1])), self.dbs[7].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[7].subs[0].subs[1].subs[1]), self.dbs[7].subs[0].subs[1]), self.dbs[7].subs[0]) and db(not db(self.get_subclass_c4_contatore_co8().get_valore() < 1221, self.dbs[7].subs[1].subs[0]), self.dbs[7].subs[1])), self.dbs[7])
    
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
        
        Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )
        for idx, it in enumerate(self.get_subclass_c4_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm4(self,GlobalEnumeration.avanzamento,GlobalEnumeration.c270)
    
    def effect_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 ) }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a c270 )
        for idx, it in enumerate(self.get_subclass_c4_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm4(self,GlobalEnumeration.avanzamento,GlobalEnumeration.c270)
    
    def effect_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 ) }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )
        for idx, it in enumerate(self.get_subclass_c4_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm4(self,GlobalEnumeration.gialloxverdex,GlobalEnumeration.c270)
    
    def effect_NOMINAL_ACTUATION_state1_state2_001(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox ) }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox )
        for idx, it in enumerate(self.get_subclass_c4_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm4(self,GlobalEnumeration.gialloxverdex,GlobalEnumeration.avviox)
    
    def effect_NOMINAL_ACTUATION_state1_001(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a avviox ) }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a avanzamento ,argomento_ave9   uguale a avviox )
        for idx, it in enumerate(self.get_subclass_c4_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm4(self,GlobalEnumeration.avanzamento,GlobalEnumeration.avviox)
    
    def effect_NORMALIZATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox ) }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a avviox )
        for idx, it in enumerate(self.get_subclass_c4_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm4(self,GlobalEnumeration.gialloxverdex,GlobalEnumeration.avviox)
    
    def effect_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
        Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
         di eseguire  commento: {113,}  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C4_lista_L9
        #   di eseguire  /*113,*/  MainClass_C1_command_comm4( con argomento_ave4   uguale a GialloxVerdex ,argomento_ave9   uguale a c270 )
        for idx, it in enumerate(self.get_subclass_c4_lista_l9()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm4(self,GlobalEnumeration.gialloxverdex,GlobalEnumeration.c270)
    
    # effect macros
    def macroSubclass_c4_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  commento: {55,} 15, commento: {71,}Decrementa il contatore SubClass_C4_contatore_Co8
        
           
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  commento: {54,} 154 commento: {36,} e  se il timer SubClass_C4_timer_T8 non è disattivo commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , commento: {66,} Assegna al comando SubClass_C4_comando_C9 il valore GialloxVerdex
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a c180 ) commento: {73,}
        
        
         commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C4_timer_T8 non è attivo commento: {35,} o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, commento: {66,} Assegna al comando SubClass_C4_comando_C10 il valore  False 
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è scaduto, commento: {68,}Attiva il timer SubClass_C4_timer_T2
        
           
         commento: {35,}  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , commento: {70,}Incrementa il contatore SubClass_C4_contatore_Co8
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a RossoVerde ) commento: {73,}
        
        
        
        }
        """
        def populate_macroSubclass_c4_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 15, /*71,*/Decrementa il contatore SubClass_C4_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c4_restoreva_rv1_restore)  è uguale a  (False) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_contatore_co5)  è minore di  (15))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c4_contatore_co5)  è minore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 154 /*36,*/ e  se il timer SubClass_C4_timer_T8 non è disattivo /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , /*66,*/ Assegna al comando SubClass_C4_comando_C9 il valore GialloxVerdex

 ,altrimenti   Applica gli effetti
       della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a c180 )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 154 /*36,*/ e  se il timer SubClass_C4_timer_T8 non è disattivo /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( ( negazione di ((subclass_c4_contatore_co5)  è maggiore di  (154)) )  e  
( negazione di (il timer 'subclass_c4_timer_t8' è inattivo) ) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c4_contatore_co5)  è maggiore di  (154)) )  e  
( negazione di (il timer 'subclass_c4_timer_t8' è inattivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_contatore_co5)  è maggiore di  (154))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co5)  è maggiore di  (154)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c4_timer_t8' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c4_parametro_p1)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a c180 )"""),#1
                            ]),#1
                            DIStatement("""ITStatement\n/*73,*/


 /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C4_timer_T8 non è attivo /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, /*66,*/ Assegna al comando SubClass_C4_comando_C10 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C4_timer_T8 non è attivo /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((subclass_c4_restoreva_rv1_restore)  è uguale a  (False)) )  e  ( negazione di ((subclass_c4_parametro_p2)  è uguale a  (True)) ) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di (il timer 'subclass_c4_timer_t8' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c4_restoreva_rv1_restore)  è uguale a  (False)) )  e  ( negazione di ((subclass_c4_parametro_p2)  è uguale a  (True)) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c4_restoreva_rv1_restore)  è uguale a  (False)) )  e  ( negazione di ((subclass_c4_parametro_p2)  è uguale a  (True)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_restoreva_rv1_restore)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c4_timer_t8' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t8' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è scaduto, /*68,*/Attiva il timer SubClass_C4_timer_T2""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C4_restoreTI_TI2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_restoreti_ti2_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore SubClass_C4_contatore_Co8

 ,altrimenti   Applica gli effetti
       della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a RossoVerde )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a RossoVerde )"""),#1
                            ]),#4
                ])

        populate_macroSubclass_c4_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 15, /*71,*/Decrementa il contatore SubClass_C4_contatore_Co8
        if db((db((db(self.get_subclass_c4_restoreva_rv1_restore() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_contatore_co5().get_valore() < 15, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c4_contatore_co8().decrementa()
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 154 /*36,*/ e  se il timer SubClass_C4_timer_T8 non è disattivo /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , /*66,*/ Assegna al comando SubClass_C4_comando_C9 il valore GialloxVerdex
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a c180 )
        if db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_contatore_co5().get_valore() > 154, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_timer_t8().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c4_comando_c9(GlobalEnumeration.gialloxverdex)
        else:
            self.macroSubclass_c4_macroef_m9(GlobalEnumeration.c180,True,GlobalEnumeration.avanzamento,GlobalEnumeration.c180, di_ctx.subs[1].subs[1])
        #  /*73,*/
        #   /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C4_timer_T8 non è attivo /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex, /*66,*/ Assegna al comando SubClass_C4_comando_C10 il valore  False
        if db((db((db((db((db(not db(self.get_subclass_c4_restoreva_rv1_restore() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_parametro_p2() == True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_timer_t8().isAttivato(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_subclass_c4_comando_c10(False)
        #  /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è scaduto, /*68,*/Attiva il timer SubClass_C4_timer_T2
        if db(not db(self.get_subclass_c4_restoreti_ti2_restore().isScaduto(), di_ctx.subs[3].subs[0].subs[0]), di_ctx.subs[3].subs[0]):
            self.get_subclass_c4_timer_t2().attiva()
        #  /*35,*/  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , /*70,*/Incrementa il contatore SubClass_C4_contatore_Co8
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C4_macroef_M9( con argomento_af8   uguale a c180 ,argomento_af7   uguale a avanzamento ,argomento_af5   uguale a True ,argomento_af10   uguale a RossoVerde )
        if db((db(not db(self.get_subclass_c4_controllo_c1() == True, di_ctx.subs[4].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.get_subclass_c4_contatore_co8().incrementa()
        else:
            self.macroSubclass_c4_macroef_m9(GlobalEnumeration.rossoverde,True,GlobalEnumeration.avanzamento,GlobalEnumeration.c180, di_ctx.subs[4].subs[1])
    
    def macroSubclass_c4_macroef_m9(self, argomento_af10, argomento_af5, argomento_af7, argomento_af8, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {45,}  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  commento: {56,} 145021 commento: {35,} e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex commento: {35,} o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  commento: {54,} 143 commento: {34,} e  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True ,  commento: {67,} Assegna alla variabile SubClass_C4_variabile_V3 il valore c180 commento: {67,}
        
           
        
        }
        """
        def populate_macroSubclass_c4_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/ 145021 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 143 /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True ,  /*67,*/ Assegna alla variabile SubClass_C4_variabile_V3 il valore c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/ 145021 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 143 /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( per ognuna delle seguenti {(negazione di ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (145021)))} )  e  
( negazione di (negazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))) ) )  o  
( ( negazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)) )  e  
( (subclass_c4_variabile_v3)  è uguale a  (c180) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(negazione di ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (145021)))} )  e  
( negazione di (negazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (145021)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (145021))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (145021)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)) )  e  
( (subclass_c4_variabile_v3)  è uguale a  (c180) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c4_contatore_co5)  è maggiore di  (143)) )  e  
( negazione di ((subclass_c4_parametro_p1)  è uguale a  (True)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_contatore_co5)  è maggiore di  (143))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co5)  è maggiore di  (143)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c4_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*45,*/  se  MainClass_C1_contatore_Co7 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/ 145021 /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  diverso da GialloxVerdex /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 143 /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True ,  /*67,*/ Assegna alla variabile SubClass_C4_variabile_V3 il valore c180
        if db((db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_contatore_co7().get_valore() == 145021, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_contatore_co5().get_valore() > 143, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c4_variabile_v3(GlobalEnumeration.c180)
    
    # verify macros
    @srf_value_macro("macroSubclass_c4_macrove_m1")
    def macroSubclass_c4_macrove_m1(self, argomento_ave2, argomento_ave4, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  commento: {54,} 154 commento: {35,} o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex commento: {38,} o  se il contatore SubClass_C4_contatore_Co8 non è  uguale a  commento: {53,} 155 commento: {36,} o  se il timer SubClass_C4_timer_T8 è disattivo, Tutte le seguenti { 
         commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo commento: {34,} e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  commento: {36,} e  se il timer SubClass_C4_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  commento: {55,} 11 commento: {36,} o  se il timer SubClass_C4_timer_T3 non è disattivo commento: {36,} o  se il timer SubClass_C4_timer_T3 non è scaduto, Tutte le seguenti { 
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  commento: {56,}  state1  commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  commento: {54,} 140213 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 non è  minore di  commento: {55,} 6 commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  commento: {34,} o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   commento: {47,48,49,50,52,}  commento: {,}  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
         commento: {104,} o  che  commento: {,}  il timer SubClass_C4_timer_T2 non sia attivo
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
         commento: {104,} e  che   l'argomento argomento_ave2 non  sia  uguale a  True  commento: {,} 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  diverso da  False 
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C4_timer_T3 non sia attivo
        
        
         } Verifica che   commento: {47,48,51,52,}   l'argomento argomento_ave2 sia  uguale a  False  commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  commento: {56,} 15
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P9 non sia  uguale a  commento: {53,} 7
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C1 non sia  uguale a  True 
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C4_controllo_C1 non sia  uguale a  False 
        
        
        }
        """
        def populate_macroSubclass_c4_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 154 /*35,*/ o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 non è  uguale a  /*53,*/ 155 /*36,*/ o  se il timer SubClass_C4_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer SubClass_C4_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C4_timer_T3 non è scaduto, Tutte le seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  False 


 } Verifica che   /*48,49,*/  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo


 } Verifica che   /*47,48,51,52,*/   l'argomento argomento_ave2 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  True 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 154 /*35,*/ o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 non è  uguale a  /*53,*/ 155 /*36,*/ o  se il timer SubClass_C4_timer_T8 è disattivo, Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer SubClass_C4_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C4_timer_T3 non è scaduto, Tutte le seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  False 


 } Verifica che   /*48,49,*/  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 154 /*35,*/ o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 non è  uguale a  /*53,*/ 155 /*36,*/ o  se il timer SubClass_C4_timer_T8 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 154 /*35,*/ o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex /*38,*/ o  se il contatore SubClass_C4_contatore_Co8 non è  uguale a  /*53,*/ 155""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 154 /*35,*/ o  se il controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 154""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C4_restoreva_RV1 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_restoreva_rv1_restore)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 154""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C3 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c3)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C4_contatore_Co8 non è  uguale a  /*53,*/ 155""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co8)  è uguale a  (155)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C4_timer_T8 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer SubClass_C4_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C4_timer_T3 non è scaduto, Tutte le seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  False 


 } Verifica che   /*48,49,*/  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer SubClass_C4_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C4_timer_T3 non è scaduto, Tutte le seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer SubClass_C4_timer_T3 non è disattivo /*36,*/ o  se il timer SubClass_C4_timer_T3 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11 /*36,*/ o  se il timer SubClass_C4_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C4_restoreTI_TI2 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_restoreti_ti2_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P2 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C4_contatore_Co5 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c4_contatore_co5)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Verifica che   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213 /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1  /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213""", [
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C4_contatore_Co5 è  maggiore di  /*54,*/ 140213""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C4_parametro_P1 non è  uguale a  False  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P9 non è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c4_parametro_p9)  è minore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,52,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C4_timer_T2 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t2' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ e  che   l'argomento argomento_ave2 non  sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_variabile_v3)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave2 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,52,*/   l'argomento argomento_ave2 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  uguale a  /*53,*/ 7
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  True 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,52,*/   l'argomento argomento_ave2 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  /*56,*/ 15
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,52,*/   l'argomento argomento_ave2 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,51,52,*/   l'argomento argomento_ave2 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_contatore_co8)  è uguale a  (15))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co8)  è uguale a  (15)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p9)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  True 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C4_controllo_C1 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c4_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(not db(not db(self.get_subclass_c4_restoreva_rv1_restore() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_contatore_co5().get_valore() > 154, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_controllo_c3() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_contatore_co8().get_valore() == 155, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db((db((db(not db(self.get_subclass_c4_restoreti_ti2_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_contatore_co5().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_contatore_co5().get_valore() > 140213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_parametro_p9() < 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(argomento_ave2 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db(not db(not db(self.get_subclass_c4_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c4_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(argomento_ave2 == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_contatore_co8().get_valore() == 15, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c4_parametro_p9() == 7, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c4_controllo_c1() == True, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c4_controllo_c1() == False, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c4_macrove_m10")
    def macroSubclass_c4_macrove_m10(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave3, argomento_ave5, argomento_ave6, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex commento: {34,} e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  commento: {36,} o  se il timer SubClass_C4_timer_T3 è attivo commento: {34,} o  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  commento: {54,} 5, Almeno una delle seguenti { 
          se l'argomento argomento_ave5 è  diverso da RossoGialloVerde commento: {39,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C8 del campo  MainClass_C1     commento: {105,} è  uguale a avanzamento, Verifica che   commento: {47,48,51,52,}  commento: {34,}  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 11
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 134
         commento: {104,} o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox commento: {,} 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
         commento: {104,} o  che   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde commento: {39,} 
        
        
         } Verifica che   commento: {50,51,52,}  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 115
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
         commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a RossoGialloVerde commento: {,} 
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
        
        
        }
        """
        def populate_macroSubclass_c4_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*36,*/ o  se il timer SubClass_C4_timer_T3 è attivo /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
  se l'argomento argomento_ave5 è  diverso da RossoGialloVerde /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento, Verifica che   /*47,48,51,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde /*39,*/ 


 } Verifica che   /*50,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 115
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a RossoGialloVerde /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*36,*/ o  se il timer SubClass_C4_timer_T3 è attivo /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
  se l'argomento argomento_ave5 è  diverso da RossoGialloVerde /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento, Verifica che   /*47,48,51,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde /*39,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*36,*/ o  se il timer SubClass_C4_timer_T3 è attivo /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True  /*36,*/ o  se il timer SubClass_C4_timer_T3 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C8 è  diverso da GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C4_timer_T3 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_parametro_p9)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse l'argomento argomento_ave5 è  diverso da RossoGialloVerde /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento, Verifica che   /*47,48,51,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave5 è  diverso da RossoGialloVerde /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave5 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nlo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_controllo_c8 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (avanzamento)) allora ((lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n/*42,*/    MainClass_C1_controllo_C8 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ o  che   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134
 /*104,*/ o  che   l'argomento argomento_ave6 non  sia  uguale a avanzamentox /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co5)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 134""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave6 non  sia  uguale a avanzamentox /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave6 non  sia  uguale a avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c3)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c3)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 115
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a RossoGialloVerde /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 115
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 115
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""LessThanImpl\nche   /*50,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 115""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave10 non  sia  uguale a RossoGialloVerde /*,*/ 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c4_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_parametro_p9() > 5, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db(not db(argomento_ave5 == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9()) if db(it.get_mainclass_c1().get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_subclass_c4_parametro_p2() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_contatore_co5().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c4_contatore_co5().get_valore() < 134, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(argomento_ave6 == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c4_controllo_c3() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(argomento_ave10 == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_subclass_c4_contatore_co5().get_valore() < 115, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(argomento_ave10 == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c4_macrove_m4")
    def macroSubclass_c4_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI1 non è scaduto commento: {34,} o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Almeno una delle seguenti { 
         commento: {63,} commento: {34,}  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  commento: {35,} e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer SubClass_C4_timer_T3 non è scaduto commento: {34,} o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
         commento: {62,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 commento: {35,} o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
         commento: {61,} commento: {36,}  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {61,}  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {61,} commento: {41,}  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  commento: {53,} 5 commento: {38,} e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  commento: {54,} 130213, Tutte le seguenti { 
         commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {61,} commento: {34,}  se il parametro SubClass_C4_parametro_P9 è  minore di  commento: {55,} 2, Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  commento: {54,} 5 commento: {37,} o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo commento: {34,} e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 commento: {34,} o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  commento: {35,} o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex commento: {34,} e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,49,}  commento: {,}  il timer SubClass_C4_timer_T2 sia scaduto
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  commento: {54,} 11
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co8 sia  diverso da  commento: {56,} 130
        
        
         } Verifica che   commento: {47,50,51,}  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  commento: {54,} 11213
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 13
        
        
         } Verifica che   commento: {48,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 13
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C4_timer_T3 non sia attivo
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C4_timer_T3 non sia disattivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C4_timer_T2 sia attivo
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,51,}  commento: {34,}  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co8 sia  minore di  commento: {55,} 1213
        
        
         } Verifica che   commento: {48,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  commento: {53,} 11
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {,}  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
         commento: {104,} e  che  commento: {,}  il timer SubClass_C4_timer_T8 sia scaduto
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C4_timer_T3 non sia disattivo
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
        
        
         } Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro SubClass_C4_parametro_P2 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex
        
        
        }
        """
        def populate_macroSubclass_c4_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 } Verifica che   /*47,48,50,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True , Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  SubClass_C4_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  diverso da  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P1 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C4_parametro_P1 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_parametro_p9)  è maggiore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C4_controllo_C8 è  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C4_timer_T2 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213, Tutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5 /*38,*/ e  se il contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C4_contatore_Co5 non è  maggiore di  /*54,*/ 130213""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co5)  è maggiore di  (130213)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 } Verifica che   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 }""", [
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C4_parametro_P9 è  minore di  /*55,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_parametro_p9)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False , Almeno una delle seguenti { 
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 non è  uguale a  False""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C4_restoreTI_TI2 è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P2 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False  /*35,*/ o  se il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_variabile_v3)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P2 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C4_parametro_P1 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C8 non è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C4_parametro_P1 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,48,49,*/  /*,*/  il timer SubClass_C4_timer_T2 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  maggiore di  /*54,*/ 11""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 130""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co8)  è uguale a  (130)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,51,*/  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  maggiore di  /*54,*/ 11213""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co8)  è maggiore di  (11213)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co5)  è maggiore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 13""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_variabile_v3)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C4_timer_T2 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P1 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1213""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co5)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ o  che  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*,*/  il controllo SubClass_C4_controllo_C3 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c3)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c3)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C4_timer_T8 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C4_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  diverso da GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c8)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c4_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_subclass_c4_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db((db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_parametro_p9() > 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c4_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p2() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_contatore_co5().get_valore() > 130213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_subclass_c4_restoreva_rv1_restore() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(self.get_subclass_c4_parametro_p9() < 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_subclass_c4_parametro_p9() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(self.get_subclass_c4_restoreti_ti2_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c4_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_subclass_c4_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(self.get_subclass_c4_contatore_co8().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c4_contatore_co8().get_valore() == 130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_subclass_c4_contatore_co8().get_valore() > 11213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c4_contatore_co5().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c4_contatore_co5().get_valore() < 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(self.get_subclass_c4_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c4_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c4_timer_t2().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(not db(not db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c4_contatore_co8().get_valore() < 1213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c4_contatore_co5().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(not db(not db(self.get_subclass_c4_controllo_c3() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c4_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_subclass_c4_parametro_p2() == False, di_ctx.subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c4_macrove_m8")
    def macroSubclass_c4_macrove_m8(self, argomento_ave4, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {41,}  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  maggiore di  commento: {54,} 4 commento: {37,} o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 commento: {35,} o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 commento: {34,} o  se il parametro SubClass_C4_parametro_P2 è  uguale a  True  commento: {37,} o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
         commento: {61,} commento: {109,}  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  commento: {35,} e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True , Tutte le seguenti { 
         commento: {61,} commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 commento: {34,} o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  commento: {53,} 6 commento: {36,} e  se il timer SubClass_C4_timer_T3 non è attivo commento: {35,} e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde commento: {39,} , Tutte le seguenti { 
         commento: {63,}  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde commento: {40,}  commento: {38,} o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  commento: {53,} 134 commento: {36,} o  se il timer SubClass_C4_timer_T2 è scaduto commento: {37,} e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
         commento: {61,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo commento: {34,} e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  commento: {36,} o  se il timer SubClass_C4_timer_T2 non è scaduto commento: {34,} o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  commento: {54,} 3, Tutte le seguenti { 
         commento: {63,} commento: {43,}  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è attivo commento: {35,} e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  commento: {37,} e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
         commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
         commento: {62,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {36,} o  se il timer SubClass_C4_timer_T3 è scaduto commento: {34,} e  se il parametro SubClass_C4_parametro_P9 è  uguale a  commento: {53,} 6, Almeno una delle seguenti { 
         commento: {36,}  se il timer SubClass_C4_timer_T2 è scaduto commento: {34,} e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   commento: {47,48,50,}  commento: {,}  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 
        
        
         } Verifica che   commento: {47,48,50,51,52,}   l'argomento argomento_ave9 non  sia  diverso da  False  commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  commento: {53,} 11
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
        
        
         } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  minore di  commento: {55,} 11
         commento: {104,} e  che   l'argomento argomento_ave9 sia  diverso da  True  commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  uguale a  True  commento: {39,} 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C4_parametro_P9 sia  minore di  commento: {55,} 3
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C4_parametro_P9 non sia  diverso da  commento: {56,} 2
        
        
         } Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
         commento: {104,} o  che   l'argomento argomento_ave4 non  sia  diverso da  True  commento: {,} 
        
        
         } Verifica che   commento: {47,49,51,}  commento: {34,}  il parametro SubClass_C4_parametro_P9 non sia  diverso da  commento: {56,} 2
         commento: {104,} e  che  commento: {,}  il timer SubClass_C4_timer_T3 non sia attivo
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 134
        
        
         } Verifica che   commento: {50,51,52,}   l'argomento argomento_ave9 non  sia  diverso da  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  commento: {54,} 12502
         commento: {104,} e  che   l'argomento argomento_ave8 non  sia  uguale a  True  commento: {39,} 
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co8 sia  minore di  commento: {55,} 1513
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C4_contatore_Co8 sia  diverso da  commento: {56,} 114
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
        
        
         } Verifica che   commento: {48,49,51,52,}   l'argomento argomento_ave4 sia  uguale a  False  commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave8 sia  uguale a  True  commento: {39,} 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C4_timer_T3 sia disattivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C4_timer_T2 non sia scaduto
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C4_contatore_Co5 sia  uguale a  commento: {53,} 155
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
        
        
         } Verifica che   commento: {48,51,}  commento: {,}  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C4_contatore_Co8 non sia  minore di  commento: {55,} 1102
        
        
        }
        """
        def populate_macroSubclass_c4_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 è  uguale a  True  /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde /*39,*/ , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134


 } Verifica che   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180


 } Verifica che   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave8 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  uguale a  /*53,*/ 155
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 


 } Verifica che   /*48,51,*/  /*,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  minore di  /*55,*/ 1102""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 è  uguale a  True  /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde /*39,*/ , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134


 } Verifica che   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180


 } Verifica che   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave8 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  uguale a  /*53,*/ 155
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 è  uguale a  True  /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180 /*34,*/ o  se il parametro SubClass_C4_parametro_P2 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180 /*35,*/ o  se il controllo SubClass_C4_controllo_C1 non è  diverso da  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 4 /*37,*/ o  se la variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C4_variabile_V3 è  uguale a c180""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C4_controllo_C1 non è  diverso da  True  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C1 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_controllo_c1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C4_parametro_P2 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde /*39,*/ , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134


 } Verifica che   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180


 } Verifica che   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave8 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  uguale a  /*53,*/ 155
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde /*39,*/ , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134


 } Verifica che   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*109,*/  se il ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False  /*35,*/ e  se il controllo SubClass_C4_controllo_C1 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  SubClass_C4_restoreva_RV1 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C4_controllo_C1 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde /*39,*/ , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134


 } Verifica che   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde /*39,*/ , Tutte le seguenti { 
 /*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270 /*34,*/ o  se il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex e  se l'argomento argomento_ave7 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer SubClass_C4_timer_T3 non è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P9 non è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p9)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T3 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C4_controllo_C3 è  uguale a GialloxVerdex""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180, Solo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134 /*36,*/ o  se il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se la macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde /*40,*/  /*38,*/ o  se il contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  SubClass_C4_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a1   uguale a c270 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a c270 )  non  è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c4_macrova_m6')  è uguale a  (rossogialloverde)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c4_macrova_m6'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C4_contatore_Co5 è  uguale a  /*53,*/ 134""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C4_timer_T2 è scaduto /*37,*/ e  se la variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C4_timer_T2 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3, Tutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto /*34,*/ o  se il parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False  /*36,*/ o  se il timer SubClass_C4_timer_T2 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo /*34,*/ e  se il parametro SubClass_C4_parametro_P2 è  diverso da  False""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c4_lista_l9' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P2 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C4_timer_T2 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C4_parametro_P9 è  maggiore di  /*54,*/ 3""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180, Solo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False  /*37,*/ e  se la variabile SubClass_C4_variabile_V3 non è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo /*35,*/ e  se il controllo SubClass_C4_controllo_C7 è  uguale a  False""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T6 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6 del campo mainclass_c1 della lista subclass_c4_lista_l9' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C4_controllo_C7 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C4_variabile_V3 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_variabile_v3)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo, Almeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 }""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C4_restoreTI_TI1 è attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 } Verifica che   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6, Almeno una delle seguenti { 
 /*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*36,*/ o  se il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C4_timer_T3 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C4_timer_T3 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C4_parametro_P9 è  uguale a  /*53,*/ 6""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False , Verifica che   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C4_timer_T2 è scaduto /*34,*/ e  se il parametro SubClass_C4_parametro_P1 non è  diverso da  False""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C4_timer_T2 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C4_parametro_P1 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,*/  /*,*/  il controllo SubClass_C4_controllo_C8 sia  uguale a GialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile SubClass_C4_variabile_V3 sia  uguale a c180""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C4_parametro_P1 sia  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  uguale a  /*53,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co5)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11
 /*104,*/ e  che   l'argomento argomento_ave9 sia  diverso da  True""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,51,52,*/  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  minore di  /*55,*/ 11""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave9 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro SubClass_C4_parametro_P9 sia  minore di  /*55,*/ 3""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p9)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p9)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True 
 /*104,*/ o  che   l'argomento argomento_ave4 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C4_parametro_P2 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2
 /*104,*/ e  che  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,51,*/  /*34,*/  il parametro SubClass_C4_parametro_P9 non sia  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c4_parametro_p9)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_parametro_p9)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C4_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 134""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co5)  è maggiore di  (134)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114
 /*104,*/ o  che  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502
 /*104,*/ e  che   l'argomento argomento_ave8 non  sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,51,52,*/   l'argomento argomento_ave9 non  sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 non sia  maggiore di  /*54,*/ 12502""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c4_contatore_co5)  è maggiore di  (12502)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave8 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  minore di  /*55,*/ 1513""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C4_contatore_Co8 sia  diverso da  /*56,*/ 114""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_contatore_co8)  è uguale a  (114)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C4_variabile_V3 non sia  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_variabile_v3)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave8 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  uguale a  /*53,*/ 155
 /*104,*/ o  che  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave8 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto
 /*104,*/ o  che  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  uguale a  /*53,*/ 155""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave8 sia  uguale a  True  /*39,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False  /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave8 sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,51,52,*/   l'argomento argomento_ave4 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave8 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C4_timer_T3 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C4_timer_T2 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t2' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C4_contatore_Co5 sia  uguale a  /*53,*/ 155""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C4_controllo_C7 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex
 /*104,*/ e  che  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  minore di  /*55,*/ 1102""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il controllo SubClass_C4_controllo_C8 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c4_controllo_c8)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C4_contatore_Co8 non sia  minore di  /*55,*/ 1102""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c4_contatore_co8)  è minore di  (1102)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c4_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p2() > 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c4_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_parametro_p2() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db(self.get_subclass_c4_restoreva_rv1_restore() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_subclass_c4_parametro_p9() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c4_controllo_c3() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave7 == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(db(self.macroSubclass_c4_macrova_m6(GlobalEnumeration.c270,GlobalEnumeration.c270,GlobalEnumeration.rossogialloverde,True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_contatore_co5().get_valore() == 134, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c4_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c4_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_parametro_p9() > 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c4_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(self.get_subclass_c4_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c4_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c4_parametro_p9() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(self.get_subclass_c4_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c4_parametro_p1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c4_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(not db(argomento_ave9 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_contatore_co5().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c4_parametro_p2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(self.get_subclass_c4_contatore_co5().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(argomento_ave9 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c4_parametro_p9() < 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c4_parametro_p9() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(not db(self.get_subclass_c4_parametro_p2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(argomento_ave4 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(not db(self.get_subclass_c4_parametro_p9() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c4_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c4_contatore_co5().get_valore() > 134, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db((db(not db(not db(argomento_ave9 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c4_contatore_co5().get_valore() > 12502, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave8 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c4_contatore_co8().get_valore() < 1513, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c4_contatore_co8().get_valore() == 114, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c4_variabile_v3() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db((db(argomento_ave4 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(argomento_ave8 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c4_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c4_contatore_co5().get_valore() == 155, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c4_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_subclass_c4_controllo_c8() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c4_contatore_co8().get_valore() < 1102, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c4_macrova_m6")
    def macroSubclass_c4_macrova_m6(self, argomento_a1, argomento_a2, argomento_a3, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {36,}  se il timer SubClass_C4_timer_T3 è attivo commento: {34,} e  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {111,} e  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1  commento: {41,} e  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  commento: {105,} è  uguale a c270 , assegna alla macro il valore RossoGialloVerde
        
         commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
        }
        """
        def populate_macroSubclass_c4_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*36,*/  se il timer SubClass_C4_timer_T3 è attivo /*34,*/ e  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*41,*/ e  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  uguale a c270 , assegna alla macro il valore RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*36,*/  se il timer SubClass_C4_timer_T3 è attivo /*34,*/ e  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*41,*/ e  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'subclass_c4_timer_t3' è attivo )  e  ( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) ) )  e  ( per ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1)))} )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'subclass_c4_timer_t3' è attivo )  e  ( negazione di (negazione di ((lo stato di 'self')  è uguale a  (state1))) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c4_timer_t3' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c4_lista_l9')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (c270))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c4_lista_l9)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c4_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*36,*/  se il timer SubClass_C4_timer_T3 è attivo /*34,*/ e  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  diverso da  /*56,*/  state1  /*41,*/ e  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C4_lista_L9 esiste e  /*105,*/ è  uguale a c270 , assegna alla macro il valore RossoGialloVerde
        if db((db((db((db(self.get_subclass_c4_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C4.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c4_lista_l9())), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogialloverde
        #  /*46,*/ assegna alla macro il valore RossoGialloVerde
        return GlobalEnumeration.rossogialloverde
    
    @srf_value_macro("macroSubclass_c4_macrova_m7")
    def macroSubclass_c4_macrova_m7(self, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
         
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
        }
        """
        def populate_macroSubclass_c4_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c4_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGialloVerde
        return GlobalEnumeration.rossogialloverde
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c4_previousco_c4_prev(self.get_subclass_c4_previousco_c4())
        self.set_subclass_c4_previousco_c5_prev(self.get_subclass_c4_previousco_c5())
        self.set_subclass_c4_previousco_c6_prev(self.get_subclass_c4_previousco_c6())
        self.set_subclass_c4_previousva_pv1_prev(self.get_subclass_c4_previousva_pv1())
        self.set_subclass_c4_previousva_pv2_prev(self.get_subclass_c4_previousva_pv2())
        self.set_subclass_c4_previousva_pv3_prev(self.get_subclass_c4_previousva_pv3())

class SubClass_C4_RecordHeaderR9(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled1, recordfiled18, recordfiled12, recordfiled16):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled1(recordfiled1)
        self.set_recordfiled18(recordfiled18)
        self.set_recordfiled12(recordfiled12)
        self.set_recordfiled16(recordfiled16)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled1(self, recordfiled1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled1"), recordfiled1)

    def set_recordfiled18(self, recordfiled18):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"), recordfiled18)

    def set_recordfiled12(self, recordfiled12):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"), recordfiled12)

    def set_recordfiled16(self, recordfiled16):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled16"), recordfiled16)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled1"))

    def get_recordfiled18(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled18"))

    def get_recordfiled12(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"))

    def get_recordfiled16(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled16"))



