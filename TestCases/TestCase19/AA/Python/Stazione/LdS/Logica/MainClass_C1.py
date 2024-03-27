# Codice del modello 'TestCase19', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.verde)
        self.set_mainclass_c1_previousva_pv2(0)
        self.set_mainclass_c1_previousva_pv3(False)
        self.set_mainclass_c1_previousva_pv4(0)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(GlobalEnumeration.rossoverde)
        self.set_mainclass_c1_variabile_v1(False)
        self.set_mainclass_c1_variabile_v10(0)
        self.set_mainclass_c1_variabile_v3(0)
        self.set_mainclass_c1_variabile_v4(False)
        self.set_mainclass_c1_variabile_v7(GlobalEnumeration.rossoverde)

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
    def init_configuration(self, mainclass_c1_parametro_p1, mainclass_c1_parametro_p10, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p1(mainclass_c1_parametro_p1)
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(3000)
        self.set_mainclass_c1_restoreti_ti1_restore(3000)
        self.set_mainclass_c1_restoreti_ti2(34000)
        self.set_mainclass_c1_restoreti_ti2_restore(34000)
        self.set_mainclass_c1_timer_t2(3000)
        self.set_mainclass_c1_timer_t3(310000)
        self.set_mainclass_c1_timer_t4(432000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_timer_t2,self.mainclass_c1_timer_t3,self.mainclass_c1_timer_t4,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)
        self.set_mainclass_c1_contatore_co6(0)
        self.set_mainclass_c1_contatore_co7(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p1(self, mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1",mainclass_c1_parametro_p1)

    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1")

    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1")


    # setters for state variables
    def set_mainclass_c1_previousco_c1_prev(self, mainclass_c1_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev",mainclass_c1_previousco_c1_prev)
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
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v3(self, mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3",mainclass_c1_variabile_v3)
    def set_mainclass_c1_variabile_v4(self, mainclass_c1_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4",mainclass_c1_variabile_v4)
    def set_mainclass_c1_variabile_v7(self, mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7",mainclass_c1_variabile_v7)

    # getters for state variables
    def get_mainclass_c1_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev")

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

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3")

    def get_mainclass_c1_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4")

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

    def set_mainclass_c1_timer_t2(self, timerDuration):
        self.mainclass_c1_timer_t2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t2", self.memory)

    def set_mainclass_c1_timer_t3(self, timerDuration):
        self.mainclass_c1_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t3", self.memory)

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_restoreti_ti2(self):
        return self.mainclass_c1_restoreti_ti2

    def get_mainclass_c1_restoreti_ti2_restore(self):
        return self.mainclass_c1_restoreti_ti2_restore

    def get_mainclass_c1_timer_t2(self):
        return self.mainclass_c1_timer_t2

    def get_mainclass_c1_timer_t3(self):
        return self.mainclass_c1_timer_t3

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)

    def set_mainclass_c1_contatore_co6(self, counterInitValue):
        self.mainclass_c1_contatore_co6 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co6", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1

    def get_mainclass_c1_contatore_co6(self):
        return self.mainclass_c1_contatore_co6

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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 144 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 2


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 1332""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 144 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 2


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde /*37,*/ o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (gialloverde)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V4 non è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (15)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è disattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 144 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 2


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 144 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x, Almeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 2


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 144 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x""", [
                    DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 144""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7 /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde""", [
                    DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 8""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a  /*53,*/ 7""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 non è  diverso da c180x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v7)  è uguale a  (c180x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (c180x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 2


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145, Solo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (gialloverde)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6 /*38,*/ e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T3 è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 è  diverso da  /*56,*/ 6""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (6)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 145""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co6)  è uguale a  (145)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5, Almeno una delle seguenti { 
  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\nla variabile MainClass_C1_variabile_V3 è  maggiore di  /*54,*/ 2""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 è  diverso da  /*56,*/ 5""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (5)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  /*56,*/ 2""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (2)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T2 non sia scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 sia  uguale a  /*53,*/ 1332""", [
                    ]),#1
                    ]),#1
                    DIStatement("""ITStatement\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  è  diverso da  /*56,*/  state1""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#2
                    DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a AC ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a c180 ,argomento_a2   uguale a RossoGialloxVerdex  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore 2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a AC ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a c180 ,argomento_a2   uguale a RossoGialloxVerdex  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (False)) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (6)) ) )  e  
( il timer 'mainclass_c1_timer_t4' è scaduto )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (False)) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (6)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (False)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6'"""),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (6))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (6)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                    ]),#1
                    ]),#0
                    ]),#3
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
                         effect=(self.dbs[2], self.dbs[3], ),
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
        
         commento: {67,} commento: {34,}  se il parametro MainClass_C1_parametro_P10 non è  uguale a GialloVerde commento: {37,} o  se la variabile MainClass_C1_variabile_V4 non è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 15 e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
         commento: {68,} commento: {38,}  se il contatore MainClass_C1_contatore_Co6 è  uguale a  commento: {53,} 144 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  commento: {53,} 7 commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  diverso da c180x, Almeno una delle seguenti { 
         commento: {69,} commento: {35,}  se il controllo MainClass_C1_controllo_C8 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da GialloVerde commento: {36,} o  se il timer MainClass_C1_timer_T3 è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da  commento: {56,} 6 commento: {38,} e  se il contatore MainClass_C1_contatore_Co6 è  diverso da  commento: {56,} 145, Solo una delle seguenti { 
         commento: {68,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  maggiore di  commento: {54,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  commento: {56,} 5, Almeno una delle seguenti { 
          se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a  False 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da  commento: {56,} 2
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T2 non sia scaduto
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co6 sia  uguale a  commento: {53,} 1332
        
        
        }
        """
        return db((db(not db((db((db((db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v4() == False, self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 15, self.dbs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[0]) or db((db(not db((db(self.get_mainclass_c1_contatore_co6().get_valore() == 144, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(self.get_mainclass_c1_parametro_p9() == 8, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p9() == 7, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v7() == GlobalEnumeration.c180x, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_mainclass_c1_controllo_c8() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t3().isAttivato(), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() == 6, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co6().get_valore() == 145, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v3() > 2, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == 5, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_mainclass_c1_controllo_c8() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == 2, self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t2().isScaduto(), self.dbs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[1])), self.dbs[1].subs[0].subs[1]), self.dbs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co6().get_valore() == 1332, self.dbs[1].subs[1])), self.dbs[1])
    
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
        
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  False 
        
           
          se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a AC ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a c180 ,argomento_a2   uguale a RossoGialloxVerdex  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  commento: {53,} 6 commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  uguale a  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore 2
        
        
        
        }
        """
        #  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  False
        if db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[2].subs[0].subs[0]), self.dbs[2].subs[0]):
            self.set_mainclass_c1_variabile_v4(False)
        #  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a AC ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a c180 ,argomento_a2   uguale a RossoGialloxVerdex  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  /*53,*/ 6 /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  uguale a  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  True 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore 2
        if db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m6(GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.gialloverde,GlobalEnumeration.ac,True,GlobalEnumeration.c180,GlobalEnumeration.verde, self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == 6, self.dbs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isScaduto(), self.dbs[3].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c8() == True, self.dbs[3].subs[0].subs[1])), self.dbs[3].subs[0]):
            self.set_mainclass_c1_variabile_v4(True)
        else:
            self.set_mainclass_c1_variabile_v3(2)
    
    # effect macros
    def macroMainclass_c1_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE , commento: {69,}Disattiva il timer MainClass_C1_timer_T4
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T4""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE , /*69,*/Disattiva il timer MainClass_C1_timer_T4
        if db(self.get_consdef() == False, di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t4().disattiva()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m5")
    def macroMainclass_c1_macrove_m5(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave4, argomento_ave6, argomento_ave7, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V3 non è  maggiore di  commento: {54,} 10 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  uguale a  commento: {53,} 8, Almeno una delle seguenti { 
         commento: {63,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} e  se il timer MainClass_C1_timer_T4 è scaduto, Solo una delle seguenti { 
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   commento: {48,52,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
         commento: {104,} e  che   l'argomento argomento_ave9 non  sia  diverso da c180 commento: {,} 
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
        
        
         } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  commento: {56,} 11
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
         commento: {104,} e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde commento: {,} 
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 sia  minore di  commento: {55,} 113
        
        
         } Verifica che   commento: {47,49,51,52,}  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
         commento: {104,} e  che   l'argomento argomento_ave3 non  sia  diverso da c180x commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  commento: {54,} 11
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T2 sia attivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da  commento: {56,} 5
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T4 sia attivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 non è  maggiore di  /*54,*/ 10 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 113


 } Verifica che   /*47,49,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  diverso da c180x /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 non è  maggiore di  /*54,*/ 10 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8, Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 113


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V3 non è  maggiore di  /*54,*/ 10 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 non è  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v3)  è maggiore di  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V3 è  uguale a  /*53,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 113


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto, Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer MainClass_C1_timer_T4 è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo, Verifica che   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da c180 /*,*/ 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che   l'argomento argomento_ave9 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,52,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave9 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave9)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde /*,*/ 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 113""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
 /*104,*/ e  che   l'argomento argomento_ave6 sia  uguale a GialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co6 non sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co6)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co6)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave6 sia  uguale a GialloVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 113""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  diverso da c180x /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  /*54,*/ 11
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  diverso da c180x /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che   l'argomento argomento_ave3 non  sia  diverso da c180x""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,51,52,*/  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 non  sia  diverso da c180x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave3)  è uguale a  (c180x))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 sia  maggiore di  /*54,*/ 11""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  /*56,*/ 5
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T2 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T2 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (5))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_mainclass_c1_variabile_v3() > 10, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v3() == 8, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_restoreti_ti2_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(argomento_ave9 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co6().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(argomento_ave6 == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co7().get_valore() < 113, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave3 == GlobalEnumeration.c180x, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() > 11, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t2().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == 5, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m8")
    def macroMainclass_c1_macrove_m8(self, argomento_ave10, argomento_ave3, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 è  minore di  commento: {55,} 121 commento: {36,} e  se il timer MainClass_C1_timer_T2 è scaduto o  se l'argomento argomento_ave6 non  è  uguale a c180x commento: {39,} , Solo una delle seguenti { 
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
        
        
         } Verifica che   commento: {47,49,}  commento: {,}  il timer MainClass_C1_timer_T4 non sia disattivo
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 non sia  diverso da GialloVerde
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto o  se l'argomento argomento_ave6 non  è  uguale a c180x /*39,*/ , Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 


 } Verifica che   /*47,49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  diverso da GialloVerde""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto o  se l'argomento argomento_ave6 non  è  uguale a c180x /*39,*/ , Solo una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto o  se l'argomento argomento_ave6 non  è  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P10 è  uguale a GialloVerde""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co6 è  minore di  /*55,*/ 121 /*36,*/ e  se il timer MainClass_C1_timer_T2 è scaduto""", [
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co6 è  minore di  /*55,*/ 121""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T2 è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave6 non  è  uguale a c180x""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  diverso da GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 non sia  diverso da GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co6().get_valore() < 121, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t2().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave6 == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m9")
    def macroMainclass_c1_macrove_m9(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,}  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {62,}  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  commento: {40,}  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  commento: {53,} 110 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  commento: {54,} 1245 commento: {36,} o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
         commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  commento: {56,} 123210 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 non è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   commento: {47,48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  commento: {53,} 134
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
        
        
         } Verifica che   commento: {47,48,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c180
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T4 non sia attivo
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia attivo
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  minore di  commento: {55,} 13
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T4 non sia disattivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde


 }""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 } Verifica che   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M6 ( con argomento_a6   uguale a True ,argomento_a9   uguale a Verde ,argomento_a4   uguale a c270x ,argomento_a3   uguale a GialloVerde ,argomento_a7   uguale a RossoGialloxVerdex ,argomento_a2   uguale a c180  e argomento_a1   uguale a RossoGialloxVerdex )   è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m6'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo, Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245 /*36,*/ o  se il timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co6 è  uguale a  /*53,*/ 110""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co6 non è  maggiore di  /*54,*/ 1245""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co6)  è maggiore di  (1245)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True  o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 non è  diverso da GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x, Verifica che   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V7 è  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co6 è  diverso da  /*56,*/ 123210""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co6)  è uguale a  (123210)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 non è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v3)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V7 è  uguale a c180x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 134""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (134)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da GialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c180""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V7 non sia  diverso da c180x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v7)  è uguale a  (c180x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True 
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C8 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 13
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  uguale a GialloVerde""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(not db(db(self.macroMainclass_c1_macrova_m6(GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.c180,GlobalEnumeration.gialloverde,GlobalEnumeration.c270x,True,GlobalEnumeration.rossogialloxverdex,GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co6().get_valore() == 110, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co6().get_valore() > 1245, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_contatore_co6().get_valore() == 123210, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 134, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_variabile_v7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo o  se il controllo ConsDef è uguale a FALSE  commento: {109,} e  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  o  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  commento: {54,} 6 , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo o  se il controllo ConsDef è uguale a FALSE  /*109,*/ e  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  o  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  /*54,*/ 6 , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo o  se il controllo ConsDef è uguale a FALSE  /*109,*/ e  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  o  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti2_restore' è attivo) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (True) ) ) )  o  
( negazione di ((stato_restore)  è uguale a  (state1)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'mainclass_c1_restoreti_ti2_restore' è attivo) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (True) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti2_restore' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (True) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (True)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è maggiore di  (6))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_restoreva_rv1_restore)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 non è attivo o  se il controllo ConsDef è uguale a FALSE  /*109,*/ e  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  o  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  maggiore di  /*54,*/ 6 , assegna alla macro il valore  True
        if db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti2_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_restoreva_rv2_restore() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_restoreva_rv1_restore() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm7(self, notifying_process, argomento_ave1, argomento_ave10):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm7', argomento_ave1=argomento_ave1, argomento_ave10=argomento_ave10)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c1_prev(self.get_mainclass_c1_previousco_c1())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

