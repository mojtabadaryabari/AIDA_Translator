# Codice del modello 'TestCase13', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.rossogialloverde)
        self.set_mainclass_c1_previousva_pv2(False)
        self.set_mainclass_c1_previousva_pv3(False)
        self.set_mainclass_c1_restoreva_rv1(False)
        self.set_mainclass_c1_variabile_v1(False)
        self.set_mainclass_c1_variabile_v2(GlobalEnumeration.spento)
        self.set_mainclass_c1_variabile_v4(False)
        self.set_mainclass_c1_variabile_v8(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set(['eventMainclass_c1_command_comm3',]),
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
        _State1__State1__stateSheet_0__normalization__transitionTo_0 = 2

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p6, mainclass_c1_parametro_p8):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p6(mainclass_c1_parametro_p6)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(20435000)
        self.set_mainclass_c1_restoreti_ti1_restore(20435000)
        self.set_mainclass_c1_timer_t8(22000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_timer_t8,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co5(0)
        self.set_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p6(self, mainclass_c1_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6",mainclass_c1_parametro_p6)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p6")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c2(self, mainclass_c1_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c2",mainclass_c1_comando_c2)

    def set_mainclass_c1_comando_c4(self, mainclass_c1_comando_c4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c4",mainclass_c1_comando_c4)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c10")

    def get_mainclass_c1_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c3")

    def get_mainclass_c1_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c5")

    def get_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c6")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1")

    def get_mainclass_c1_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8")


    # setters for state variables
    def set_mainclass_c1_previousco_c1_prev(self, mainclass_c1_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev",mainclass_c1_previousco_c1_prev)
    def set_mainclass_c1_previousco_c8_prev(self, mainclass_c1_previousco_c8_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8_prev",mainclass_c1_previousco_c8_prev)
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
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_variabile_v1(self, mainclass_c1_variabile_v1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1",mainclass_c1_variabile_v1)
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v4(self, mainclass_c1_variabile_v4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4",mainclass_c1_variabile_v4)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

    # getters for state variables
    def get_mainclass_c1_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c1_prev")

    def get_mainclass_c1_previousco_c8_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8_prev")

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

    def get_mainclass_c1_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1")

    def get_mainclass_c1_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1_restore")

    def get_mainclass_c1_variabile_v1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v1")

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v4")

    def get_mainclass_c1_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_mainclass_c1_restoreti_ti1(self, timerDuration):
        self.mainclass_c1_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1", self.memory)

    def set_mainclass_c1_restoreti_ti1_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1_restore", self.memory)

    def set_mainclass_c1_timer_t8(self, timerDuration):
        self.mainclass_c1_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t8", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_timer_t8(self):
        return self.mainclass_c1_timer_t8


    # setters for counters
    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)

    def set_mainclass_c1_contatore_co9(self, counterInitValue):
        self.mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co9", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5

    def get_mainclass_c1_contatore_co9(self):
        return self.mainclass_c1_contatore_co9



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*84,*/  Ricezione del comando   MainClass_C1_command_comm3( con argomento_ave2   ,argomento_ave8    e argomento_ave9   )""", [
                    EventDebInfo("""Ricezione Comando Automatico\ncomando   MainClass_C1_command_comm3( con argomento_ave2   ,argomento_ave8    e argomento_ave9   )"""),#0
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 13204 /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T8 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False , Almeno una delle seguenti { 
 /*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 15204


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c270


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a  False""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 13204 /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T8 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False , Almeno una delle seguenti { 
 /*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 15204


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c270


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 13204 /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T8 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 13204 /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 13204 /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 13204""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (13204)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T8 è disattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T8 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T8 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False , Almeno una delle seguenti { 
 /*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 15204


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c270


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False , Almeno una delle seguenti { 
 /*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 15204


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C6 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 non è  diverso da Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  diverso da Verde""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 1435""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (1435)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V1 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 15204


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T8 è scaduto""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13 /*36,*/ o  se il timer MainClass_C1_timer_T8 non è attivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*36,*/  se il timer MainClass_C1_timer_T8 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T8 è attivo""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T8 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (13)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T8 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T8 è scaduto""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T8 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co9)  è minore di  (14)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C6 è  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 141""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (141)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 15204""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è uguale a  (15204))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (15204)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  diverso da c270""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#2
                    DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 122, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 1

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 122""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10'"""),#0
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co9)  è maggiore di  (122)""", [
                    ]),#1
                    ]),#0
                    ]),#3
                    DIStatement("""ITEStatementImpl\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore  True 

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( (mainclass_c1_controllo_c7)  è uguale a  (c270) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde)) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (verde) ) )  e  ( (mainclass_c1_contatore_co5)  è uguale a  (14) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde)) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (verde) ) )  e  ( (mainclass_c1_contatore_co5)  è uguale a  (14) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde)) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (verde) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (14)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#4
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M7   /*73,*/

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v8)  è maggiore di  (5)) )  e  
( negazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (c270))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è maggiore di  (5))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v8)  è maggiore di  (5)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (c270)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( il timer 'mainclass_c1_timer_t8' è inattivo )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M7"""),#1
                    ]),#5
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 13 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 1112, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 13 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 1112""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde)) )  e  ( (mainclass_c1_contatore_co9)  è uguale a  (13) ) )  e  
( negazione di ((mainclass_c1_contatore_co5)  è uguale a  (1112)) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde)) )  e  ( (mainclass_c1_contatore_co9)  è uguale a  (13) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (13)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è uguale a  (1112))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (1112)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#6
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
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[5], self.dbs[6], ),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase automatica
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[3], self.dbs[4], ),
                         phase = TransPhase.Automatica
                         ),
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

        self.set_mainclass_c1_previousco_c1_prev(False)
        self.set_mainclass_c1_previousco_c8_prev(GlobalEnumeration.verde)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())

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
                if(self.guard_NORMALIZATION_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__normalization__transitionTo_0
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
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
            self.effect_PERMANENCE_state1_000(argomento_ave2 = self.get_current_command_arg('argomento_ave2'), argomento_ave8 = self.get_current_command_arg('argomento_ave8'), argomento_ave9 = self.get_current_command_arg('argomento_ave9'))
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__normalization__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_NORMALIZATION_state1_000()
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
        
         commento: {84,}  Ricezione del comando   MainClass_C1_command_comm3( con argomento_ave2   ,argomento_ave8    e argomento_ave9   )   commento: {78,}
        
        }
        """
        return db((db(self.is_triggered('eventMainclass_c1_command_comm3'), self.dbs[1].subs[0])), self.dbs[1])
    
    def guard_NORMALIZATION_state1_000(self):
        """
        CNL corrispondente:
         {  commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  diverso da  commento: {56,} 13204 commento: {36,} e  se il timer MainClass_C1_timer_T8 è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T8 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {68,} commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 1435 commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False , Almeno una delle seguenti { 
         commento: {68,} commento: {36,}  se il timer MainClass_C1_timer_T8 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T8 è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 13 commento: {36,} o  se il timer MainClass_C1_timer_T8 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T8 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T8 non è attivo, Almeno una delle seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 14 commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 141, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  commento: {56,} 15204
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  diverso da c270
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a  False 
        
         }
        """
        return db((db(not db((db((db(self.get_consdef() == False, self.dbs[2].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 13204, self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t8().isDisattivato(), self.dbs[2].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t8().isDisattivato(), self.dbs[2].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[2].subs[0].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_mainclass_c1_controllo_c6() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 1435, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v1() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db((db(self.get_mainclass_c1_timer_t8().isAttivato(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t8().isScaduto(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 13, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t8().isAttivato(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t8().isScaduto(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t8().isAttivato(), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(self.get_mainclass_c1_contatore_co9().get_valore() < 14, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c6() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 141, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 15204, self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1].subs[0].subs[1]), self.dbs[2].subs[0].subs[1].subs[0])) + (db(not db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, self.dbs[2].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[1].subs[0]), self.dbs[2].subs[0].subs[1].subs[1]))) == 1), self.dbs[2].subs[0].subs[1]), self.dbs[2].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c5() == False, self.dbs[2].subs[1].subs[0]), self.dbs[2].subs[1])), self.dbs[2])
    
    # for each effect, the corresponding method is created
    def effect_INITIALIZATION_StatoIniziale_state1_000(self):
        """
        CNL corrispondente:
        
         {
         Nessuna 
         }
        """
        pass
    
    def effect_PERMANENCE_state1_000(self, argomento_ave2, argomento_ave8, argomento_ave9):
        """
        CNL corrispondente:
        
        {
        
          se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  commento: {40,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 122, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 1
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
        
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 14 e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore  True 
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
        
        
        }
        """
        #  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 122, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 1
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8
        if db((db(not db(not db(db(self.macroMainclass_c1_macrova_m10(GlobalEnumeration.spento,True, self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, self.dbs[3].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co9().get_valore() > 122, self.dbs[3].subs[0].subs[1])), self.dbs[3].subs[0]):
            self.set_mainclass_c1_variabile_v8(1)
        else:
            self.get_mainclass_c1_timer_t8().disattiva()
        #  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a c270 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 14 e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore  True 
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8
        if db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[4].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270, self.dbs[4].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, self.dbs[4].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() == 14, self.dbs[4].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1])), self.dbs[4].subs[0]):
            self.set_mainclass_c1_variabile_v1(True)
        else:
            self.get_mainclass_c1_timer_t8().disattiva()
    
    def effect_NORMALIZATION_state1_000(self):
        """
        CNL corrispondente:
         { commento: {37,}  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  commento: {54,} 5 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 è disattivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M7   commento: {73,}
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 13 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 1112, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V1 il valore  True 
        
           
         }
        """
        #  /*37,*/  se la variabile MainClass_C1_variabile_V8 non è  maggiore di  /*54,*/ 5 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M7   /*73,*/
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5
        if db((db((db(not db(self.get_mainclass_c1_variabile_v8() > 5, self.dbs[5].subs[0].subs[0].subs[0].subs[0]), self.dbs[5].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.c270, self.dbs[5].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[5].subs[0].subs[0].subs[1].subs[0]), self.dbs[5].subs[0].subs[0].subs[1])), self.dbs[5].subs[0].subs[0]) or db((db(self.get_consdef() == False, self.dbs[5].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t8().isDisattivato(), self.dbs[5].subs[0].subs[1].subs[1])), self.dbs[5].subs[0].subs[1])), self.dbs[5].subs[0]):
            self.macroMainclass_c1_macroef_m7(self.dbs[5].subs[1])
        else:
            self.get_mainclass_c1_contatore_co5().decrementa()
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 13 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 1112, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V1 il valore  True
        if db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), self.dbs[6].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[6].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, self.dbs[6].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co9().get_valore() == 13, self.dbs[6].subs[0].subs[1].subs[0].subs[1])), self.dbs[6].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 1112, self.dbs[6].subs[0].subs[1].subs[1].subs[0]), self.dbs[6].subs[0].subs[1].subs[1])), self.dbs[6].subs[0].subs[1])), self.dbs[6].subs[0]):
            self.set_mainclass_c1_variabile_v1(True)
    
    # effect macros
    def macroMainclass_c1_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  False  commento: {40,}  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 non è attivo commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  uguale a c180, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
         ,altrimenti   commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore c270 commento: {67,}
        
        
         commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  minore di  commento: {55,} 2 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T8 è attivo,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 3 commento: {67,}
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 141 commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  commento: {35,} e  se il controllo MainClass_C1_controllo_C3 è  uguale a  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
        
           
         commento: {36,}  se il timer MainClass_C1_timer_T8 non è scaduto, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T8
        
        
          se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  commento: {40,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P6 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C5 non è  uguale a  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 7
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T8
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a c180, /*69,*/Disattiva il timer MainClass_C1_timer_T8

 ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a c180""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (False))) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t8' è attivo) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (il timer 'mainclass_c1_timer_t8' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t8' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (False)) )  e  
( (mainclass_c1_parametro_p10)  è uguale a  (c180) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (c180)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*67,*/


 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 3 /*67,*/

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/


 /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (lo stato di 'self')  è uguale a  (state1) )  e  
( (mainclass_c1_variabile_v8)  è minore di  (2) ) )  o  
( negazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde))) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (lo stato di 'self')  è uguale a  (state1) )  e  
( (mainclass_c1_variabile_v8)  è minore di  (2) )""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v8)  è minore di  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( il timer 'mainclass_c1_timer_t8' è attivo )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 141 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 141 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_contatore_co9)  è uguale a  (141)) )  o  
( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))) ) )  o  
( ( ( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True)) )  e  ( (mainclass_c1_controllo_c3)  è uguale a  (True) ) )  e  
( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (False)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_contatore_co9)  è uguale a  (141)) )  o  
( negazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è uguale a  (141))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (141)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True)) )  e  ( (mainclass_c1_controllo_c3)  è uguale a  (True) ) )  e  
( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True)) )  e  ( (mainclass_c1_controllo_c3)  è uguale a  (True) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c3)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer MainClass_C1_timer_T8 non è scaduto, /*69,*/Disattiva il timer MainClass_C1_timer_T8

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T8""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T8 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  uguale a  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 7

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True))) )  e  
( (mainclass_c1_parametro_p6)  è uguale a  (True) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c5)  è uguale a  (False))) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True))) )  e  
( (mainclass_c1_parametro_p6)  è uguale a  (True) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c5)  è uguale a  (False))) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c5)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  False  /*40,*/  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 non è attivo /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  uguale a c180, /*69,*/Disattiva il timer MainClass_C1_timer_T8
        #   ,altrimenti   /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore c270
        if db((db((db(not db(not db(db(self.macroMainclass_c1_macrova_m10(GlobalEnumeration.spento,True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t8().disattiva()
        else:
            self.set_mainclass_c1_variabile_v2(GlobalEnumeration.c270)
        #  /*67,*/
        #   /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  minore di  /*55,*/ 2 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  diverso da Verde o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 3 /*67,*/
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8
        if db((db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v8() < 2, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v8(3)
        else:
            self.get_mainclass_c1_timer_t8().disattiva()
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 141 /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  /*35,*/ e  se il controllo MainClass_C1_controllo_C3 è  uguale a  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5
        if db((db((db((db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 141, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c3() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v1() == False, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co5().decrementa()
        #  /*36,*/  se il timer MainClass_C1_timer_T8 non è scaduto, /*69,*/Disattiva il timer MainClass_C1_timer_T8
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T8
        if db(not db(self.get_mainclass_c1_timer_t8().isScaduto(), di_ctx.subs[3].subs[0].subs[0]), di_ctx.subs[3].subs[0]):
            self.get_mainclass_c1_timer_t8().disattiva()
        else:
            self.get_mainclass_c1_timer_t8().attiva()
        #  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )  non  è  diverso da  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P6 è  uguale a  True  o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  uguale a  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 7
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T8
        if db((db((db((db(not db(not db(db(self.macroMainclass_c1_macrova_m10(GlobalEnumeration.spento,True, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p6() == True, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c5() == False, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c5() == True, di_ctx.subs[4].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v8(7)
        else:
            self.get_mainclass_c1_timer_t8().attiva()
    
    def macroMainclass_c1_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 14204, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
        
           
          se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )   è  uguale a  True  commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T8 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T8 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T8 è attivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M5  commento: {73,}
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 14351 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 11, commento: {69,}Disattiva il timer MainClass_C1_timer_T8
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M5  commento: {73,}
        
        
          se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore GialloGiallo
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V4 il valore  False 
        
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T8 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  commento: {53,} 13, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore 2
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14204, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14204""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (14204)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )   è  uguale a  True  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M5  /*73,*/

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )   è  uguale a  True  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True) )  e  
( il timer 'mainclass_c1_timer_t8' è scaduto ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t8' è scaduto) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True) )  e  
( il timer 'mainclass_c1_timer_t8' è scaduto )""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m10'"""),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t8' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M5"""),#1
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 14351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 11, /*69,*/Disattiva il timer MainClass_C1_timer_T8

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 14351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_variabile_v4)  è uguale a  (True)) )  o  
( ( (mainclass_c1_contatore_co9)  è maggiore di  (14351) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c10)  è uguale a  (c270))) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co9)  è maggiore di  (14351) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c10)  è uguale a  (c270))) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co9)  è maggiore di  (14351)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c10)  è uguale a  (c270)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co9)  è maggiore di  (11)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M5"""),#1
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*73,*/


  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore GialloGiallo

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c5)  è uguale a  (True))) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c5)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_parametro_p8)  è uguale a  (verde) )  e  ( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True)) ) )  e  
( il timer 'mainclass_c1_timer_t8' è attivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_parametro_p8)  è uguale a  (verde) )  e  ( negazione di ((mainclass_c1_variabile_v1)  è uguale a  (True)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 14204, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5
        if db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 14204, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co5().decrementa()
        #  se la macro  MainClass_C1_macrova_M10 ( con argomento_a7   uguale a True  e argomento_a10   uguale a spento )   è  uguale a  True  /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T8 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M5  /*73,*/
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T8
        if db((db((db((db(db(self.macroMainclass_c1_macrova_m10(GlobalEnumeration.spento,True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t8().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t8().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.macroMainclass_c1_macroef_m5(di_ctx.subs[1].subs[1])
        else:
            self.get_mainclass_c1_timer_t8().disattiva()
        #  /*37,*/  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 14351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 11, /*69,*/Disattiva il timer MainClass_C1_timer_T8
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M5
        if db((db((db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co9().get_valore() > 14351, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co9().get_valore() > 11, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t8().disattiva()
        else:
            self.macroMainclass_c1_macroef_m5(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #    se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C5 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore GialloGiallo
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V4 il valore  False
        if db((db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c5() == True, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_comando_c9(GlobalEnumeration.giallogiallo)
        else:
            self.set_mainclass_c1_variabile_v4(False)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T8 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  uguale a  /*53,*/ 13, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore 2
        if db((db((db((db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 13, di_ctx.subs[4].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v8(2)
    
    def macroMainclass_c1_macroef_m8(self, argomento_af1, argomento_af10, argomento_af3, argomento_af4, argomento_af5, argomento_af6, argomento_af7, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {37,}  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  o  se l'argomento argomento_af1 è  uguale a  True  commento: {39,} , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore c270
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  o  se l'argomento argomento_af1 è  uguale a  True  /*39,*/ , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  o  se l'argomento argomento_af1 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(argomento_af1)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V4 non è  uguale a  True  o  se l'argomento argomento_af1 è  uguale a  True  /*39,*/ , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore c270
        if db((db(not db(self.get_mainclass_c1_variabile_v4() == True, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(argomento_af1 == True, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v2(GlobalEnumeration.c270)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m6")
    def macroMainclass_c1_macrove_m6(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde commento: {34,} o  se il parametro MainClass_C1_parametro_P6 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  commento: {54,} 1443 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 1151, Almeno una delle seguenti { 
         commento: {63,}  se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  commento: {54,} 15204, Solo una delle seguenti { 
         commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde commento: {36,} e  se il timer MainClass_C1_timer_T8 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
         commento: {61,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
         commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T8 non è disattivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  commento: {56,} 13351 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
         commento: {61,}  se l'argomento argomento_ave2 è  uguale a  True  commento: {39,}  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 commento: {36,} o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 14, Tutte le seguenti { 
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 12204 commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  commento: {56,} 153, Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co5 sia  uguale a  commento: {53,} 115
        
        
         } Verifica che   commento: {47,48,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co9 sia  diverso da  commento: {56,} 1
        
        
         } Verifica che   commento: {52,}   l'argomento argomento_ave2 non  sia  uguale a  False  commento: {,} 
        
        
         } Verifica che   commento: {48,50,52,}   l'argomento argomento_ave2 sia  uguale a  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 
        
        
         } Verifica che   commento: {47,48,49,50,51,52,}  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co9 sia  diverso da  commento: {56,} 1520
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T8 sia attivo
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
         commento: {104,} o  che   l'argomento argomento_ave8 sia  diverso da Verde commento: {,} 
        
        
         } Verifica che   commento: {47,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  commento: {56,} 1
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V2 sia  diverso da c270
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  maggiore di  commento: {54,} 1
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 1443 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1151, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 15204, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
 /*104,*/ o  che   l'argomento argomento_ave8 sia  diverso da Verde /*,*/ 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da c270
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 1443 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1151, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 15204, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
 /*104,*/ o  che   l'argomento argomento_ave8 sia  diverso da Verde /*,*/ 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 1443 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1151""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P8 è  diverso da Verde /*34,*/ o  se il parametro MainClass_C1_parametro_P6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 1443""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 è  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 1443""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co9 è  maggiore di  /*54,*/ 1443""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1151""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 15204, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
 /*104,*/ o  che   l'argomento argomento_ave8 sia  diverso da Verde /*,*/ 


 } Verifica che   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 15204, Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
 /*104,*/ o  che   l'argomento argomento_ave8 sia  diverso da Verde /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da c180 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 15204""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P10 è  diverso da c180 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 15204""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 è  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 15204""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 


 } Verifica che   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
 /*104,*/ o  che   l'argomento argomento_ave8 sia  diverso da Verde /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270, Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P6 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P8 è  uguale a Verde /*36,*/ e  se il timer MainClass_C1_timer_T8 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a Verde""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T8 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 non è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 } Verifica che   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P8 non è  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P8 non è  uguale a Verde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 } Verifica che   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False  /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Solo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T8 non è disattivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T8 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 è  diverso da  /*56,*/ 13351""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (13351)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 non è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 } Verifica che   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180 /*36,*/ o  se il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se l'argomento argomento_ave2 è  uguale a  True  /*39,*/  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave2 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P10 è  uguale a c180""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T8 è attivo e  se l'argomento argomento_ave9 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T8 è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave9 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave9)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co9)  è minore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153, Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P6 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P6 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 12204""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (12204)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co9 è  diverso da  /*56,*/ 153""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (153)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co5 sia  uguale a  /*53,*/ 115""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C6 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*52,*/   l'argomento argomento_ave2 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,50,52,*/   l'argomento argomento_ave2 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270
 /*104,*/ o  che   l'argomento argomento_ave8 sia  diverso da Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,50,51,52,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  diverso da  /*56,*/ 1520""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (1520)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T8 sia attivo
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T8 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C10 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave8 sia  diverso da Verde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è uguale a  (1))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da c270
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V2 sia  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  maggiore di  /*54,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p6() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co9().get_valore() > 1443, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co9().get_valore() == 1151, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() > 15204, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(not db(self.get_mainclass_c1_parametro_p6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 13351, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(argomento_ave2 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(argomento_ave9 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co9().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 12204, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 153, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co5().get_valore() == 115, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(not db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(argomento_ave2 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(argomento_ave2 == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 1520, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(argomento_ave8 == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.c270, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() > 1, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m9")
    def macroMainclass_c1_macrove_m9(self, argomento_ave10, argomento_ave7, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  diverso da  True  o  se l'argomento argomento_ave7 non  è  uguale a c180 commento: {39,}  commento: {37,} o  se la variabile MainClass_C1_variabile_V1 è  uguale a  True , Tutte le seguenti { 
         commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Solo una delle seguenti { 
         commento: {62,}  se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
         commento: {62,} commento: {37,}  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 commento: {37,} e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 commento: {35,} o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   commento: {49,50,52,}  commento: {,}  il timer MainClass_C1_timer_T8 non sia disattivo
         commento: {104,} o  che   l'argomento argomento_ave7 non  sia  diverso da c180 commento: {,} 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 
        
        
         } Verifica che   commento: {47,48,51,52,}  commento: {,}  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  commento: {56,} 1504
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
         commento: {104,} o  che   l'argomento argomento_ave7 sia  diverso da c180 commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave7 non  sia  uguale a c180 commento: {39,} 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
        
        
         } Verifica che   commento: {47,50,}  commento: {,}  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V8 sia  uguale a  commento: {53,} 4
        
        
         } Verifica che   commento: {52,}   l'argomento argomento_ave7 non  sia  diverso da c180 commento: {,} 
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il timer MainClass_C1_timer_T8 non sia attivo
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da  True 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da  True  o  se l'argomento argomento_ave7 non  è  uguale a c180 /*39,*/  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  uguale a  True , Tutte le seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Solo una delle seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 } Verifica che   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4


 } Verifica che   /*52,*/   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 


 } Verifica che   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da  True  o  se l'argomento argomento_ave7 non  è  uguale a c180 /*39,*/  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  uguale a  True , Tutte le seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Solo una delle seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 } Verifica che   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4


 } Verifica che   /*52,*/   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da  True  o  se l'argomento argomento_ave7 non  è  uguale a c180 /*39,*/  /*37,*/ o  se la variabile MainClass_C1_variabile_V1 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  diverso da  True  o  se l'argomento argomento_ave7 non  è  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V1 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 non  è  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V1 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Solo una delle seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 } Verifica che   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4


 } Verifica che   /*52,*/   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto, Solo una delle seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 } Verifica che   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4


 }""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI1 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 } Verifica che   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 } Verifica che   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 } Verifica che   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile MainClass_C1_variabile_V1 è  uguale a  False , Almeno una delle seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False 


 }""", [
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V1 è  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270, Verifica che   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False  /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180 /*35,*/ o  se il controllo MainClass_C1_controllo_C5 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 non è  diverso da c180""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270 /*37,*/ e  se la variabile MainClass_C1_variabile_V1 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a c270""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI1 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 non è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V1 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 non è  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C5 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c5)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180 /*,*/ 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo
 /*104,*/ o  che   l'argomento argomento_ave7 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,52,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V1 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270
 /*104,*/ o  che   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,52,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 non sia  diverso da  /*56,*/ 1504""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è uguale a  (1504))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (1504)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C10 sia  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180 /*39,*/ 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave7 sia  diverso da c180 /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave7 non  sia  uguale a c180""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 sia  diverso da c180""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave7 non  sia  uguale a c180""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V1 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P6 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p6)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a Verde""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  /*53,*/ 4""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*52,*/   l'argomento argomento_ave7 non  sia  diverso da c180""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (c180))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (c180)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia attivo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T8 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave7 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db((db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(argomento_ave7 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_variabile_v1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 1504, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(argomento_ave7 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave7 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_mainclass_c1_variabile_v1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_mainclass_c1_parametro_p8() == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(argomento_ave7 == GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_timer_t8().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c5() == True, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m10")
    def macroMainclass_c1_macrova_m10(self, argomento_a10, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm3(self, notifying_process, argomento_ave2, argomento_ave8, argomento_ave9):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm3', argomento_ave2=argomento_ave2, argomento_ave8=argomento_ave8, argomento_ave9=argomento_ave9)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c1_prev(self.get_mainclass_c1_previousco_c1())
        self.set_mainclass_c1_previousco_c8_prev(self.get_mainclass_c1_previousco_c8())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())

