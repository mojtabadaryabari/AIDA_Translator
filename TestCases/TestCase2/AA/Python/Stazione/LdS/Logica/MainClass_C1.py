# Codice del modello 'TestCase2', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.rossogiallox)
        self.set_mainclass_c1_previousva_pv2(False)
        self.set_mainclass_c1_previousva_pv3(False)
        self.set_mainclass_c1_previousva_pv4(False)
        self.set_mainclass_c1_previousva_pv5(0)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_variabile_v2(GlobalEnumeration.rossogiallox)
        self.set_mainclass_c1_variabile_v5(GlobalEnumeration.rosso)
        self.set_mainclass_c1_variabile_v6(False)
        self.set_mainclass_c1_variabile_v7(GlobalEnumeration.rosso)
        self.set_mainclass_c1_variabile_v8(GlobalEnumeration.c180x)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2 : set([]),
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set(['eventMainclass_c1_command_comm7',]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm7'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.NOOP)


        if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
        # for each manual command that can be received in Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1
            if self.is_triggered('eventMainclass_c1_command_comm7'):
                self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.BLOCKED)

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
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_0 = 3
        _State1__State2__stateSheet_0__nominalActuation__transitionTo_1 = 4
        _State1__State1__stateSheet_0__nominalActuation__transitionTo_2 = 5

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1_parametro_p3):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(2000)
        self.set_mainclass_c1_restoreti_ti1_restore(2000)
        self.set_mainclass_c1_restoreti_ti2(5000)
        self.set_mainclass_c1_restoreti_ti2_restore(5000)
        self.set_mainclass_c1_restoreti_ti3(40000)
        self.set_mainclass_c1_restoreti_ti3_restore(40000)
        self.set_mainclass_c1_timer_t4(5432000)
        self.set_mainclass_c1_timer_t6(415000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t6,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)
        self.set_mainclass_c1_contatore_co2(0)
        self.set_mainclass_c1_contatore_co5(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c2(self, mainclass_c1_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c2",mainclass_c1_comando_c2)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c5")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

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
    def set_mainclass_c1_previousva_pv5(self, mainclass_c1_previousva_pv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5",mainclass_c1_previousva_pv5)
    def set_mainclass_c1_previousva_pv5_prev(self, mainclass_c1_previousva_pv5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5_prev",mainclass_c1_previousva_pv5_prev)
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v6(self, mainclass_c1_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6",mainclass_c1_variabile_v6)
    def set_mainclass_c1_variabile_v7(self, mainclass_c1_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7",mainclass_c1_variabile_v7)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

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

    def get_mainclass_c1_previousva_pv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5")

    def get_mainclass_c1_previousva_pv5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv5_prev")

    def get_mainclass_c1_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1")

    def get_mainclass_c1_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1_restore")

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

    def get_mainclass_c1_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6")

    def get_mainclass_c1_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v7")

    def get_mainclass_c1_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8")

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

    def set_mainclass_c1_restoreti_ti3(self, timerDuration):
        self.mainclass_c1_restoreti_ti3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti3", self.memory)

    def set_mainclass_c1_restoreti_ti3_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti3_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti3_restore", self.memory)

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)

    def set_mainclass_c1_timer_t6(self, timerDuration):
        self.mainclass_c1_timer_t6 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t6", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_restoreti_ti2(self):
        return self.mainclass_c1_restoreti_ti2

    def get_mainclass_c1_restoreti_ti2_restore(self):
        return self.mainclass_c1_restoreti_ti2_restore

    def get_mainclass_c1_restoreti_ti3(self):
        return self.mainclass_c1_restoreti_ti3

    def get_mainclass_c1_restoreti_ti3_restore(self):
        return self.mainclass_c1_restoreti_ti3_restore

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t6(self):
        return self.mainclass_c1_timer_t6


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)

    def set_mainclass_c1_contatore_co2(self, counterInitValue):
        self.mainclass_c1_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co2", self.memory)

    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1

    def get_mainclass_c1_contatore_co2(self):
        return self.mainclass_c1_contatore_co2

    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5



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
                    DIBoolExpr("""NAryLogicOP (AND)\n/*93,*/  Tutte le seguenti {
 Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*36,*/  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo


}""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*93,*/  Tutte le seguenti {
 Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*36,*/  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm7"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*36,*/  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*36,*/  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*36,*/  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*36,*/  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*36,*/  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è attivo""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V6 è  uguale a  False""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#1
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#2
                    DIBoolExpr("""NAryLogicOP (AND)\n/*86,*/  Almeno una delle seguenti {
 /*82,*/  Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


} /*82,*/  Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True 


}
}""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*86,*/  Almeno una delle seguenti {
 /*82,*/  Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


} /*82,*/  Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True 


}
}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm7"""),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm7"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 13 /*37,*/ o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 13""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (13)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 non è  uguale a AC""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (ac)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  uguale a c270x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#1
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm7"""),#2
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*83,*/  Tutte le seguenti {
 Ricezione del  comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True 


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm7"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*77,*/
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*77,*/
 /*69,*/ /*37,*/  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox /*37,*/ e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox""", [
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 non è  uguale a avviox""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (avviox)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V7 non è  uguale a avviox""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v7)  è uguale a  (avviox)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V6 è  uguale a  True""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  uguale a c270x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 è  diverso da  True""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*35,*/  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 }""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
 /*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  diverso da c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415, Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False""", [
                    DIBoolExpr("""GreaterThanImpl\nil contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 1415""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex""", [
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (True)""", [
                    ]),#0
                    ]),#2
                    ]),#3
                    ]),#0
                    ]),#3
                    DIBoolExpr("""NAryLogicOP (AND)\n/*93,*/  Tutte le seguenti {
 Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 120


}""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*93,*/  Tutte le seguenti {
 Ricezione del comando manuale   MainClass_C1_command_comm7   /*77,*/
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 } Verifica che   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 120


}""", [
                    EventDebInfo("""Ricezione Comando Manuale\ncomando manuale   MainClass_C1_command_comm7"""),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*77,*/
 /*69,*/ /*35,*/  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 }""", [
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/ /*36,*/  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*36,*/  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/ /*36,*/  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T6 non è attivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  diverso da c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 } Verifica che   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/ /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 }""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  uguale a c270x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 } Verifica che   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154 /*38,*/ o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 12150""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (12150)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 154""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (154)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo""", [
                    DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 11""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T6 non è disattivo""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*69,*/  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P3 è  uguale a c270x""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 non è  uguale a  True""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (True)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*68,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123 e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 123""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (123)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  diverso da c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*68,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V6 è  uguale a  True""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11 /*35,*/ e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 11""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (11)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C5 è  uguale a c270x""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x


 }""", [
                    DIBoolExpr("""ImpliesLogicOpImpl\n/*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/ /*37,*/  se la variabile MainClass_C1_variabile_V2 è  uguale a AC /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x""", [
                    DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V2 è  uguale a AC""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da c270x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è disattivo""", [
                    DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 è  diverso da c270x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è disattivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215, Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                    ]),#0
                    DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P3 è  uguale a c270x""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co2 non è  diverso da  /*56,*/ 13215""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (13215))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (13215)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (c270x)""", [
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
                    DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\nche   /*47,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x""", [
                    ]),#1
                    ]),#1
                    ]),#1
                    DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  /*56,*/ 120""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è uguale a  (120))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (120)""", [
                    ]),#0
                    ]),#0
                    ]),#2
                    ]),#0
                    ]),#4
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#5
                    DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )  o  
( il timer 'mainclass_c1_timer_t6' è attivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#6
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore AC

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( ( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )  e  
( (consdef)  è uguale a  (False) ) ) )  o  
( ( negazione di (negazione di ((mainclass_c1_variabile_v6)  è uguale a  (False))) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( ( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_variabile_v6)  è uguale a  (False))) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v6)  è uguale a  (False)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#7
                    DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE , /*72,*/Azzera il contatore MainClass_C1_contatore_Co1""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                    ]),#0
                    ]),#8
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  /*53,*/ 3 /*36,*/ o  se il timer MainClass_C1_timer_T6 non è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  /*53,*/ 3 /*36,*/ o  se il timer MainClass_C1_timer_T6 non è disattivo""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (3))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (3)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#9
                    DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M4""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4"""),#1
                    ]),#10
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 13043,  Applica gli effetti
       della macro MainClass_C1_macroef_M3""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 13043""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_restoreti_ti3_restore' è inattivo )  e  ( il timer 'mainclass_c1_timer_t6' è inattivo )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti3_restore' è inattivo""", [
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è minore di  (13043))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (13043)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3"""),#1
                    ]),#11
                    DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 152 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 152 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'mainclass_c1_timer_t6' è scaduto )  o  
( ( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))) )  e  
( (mainclass_c1_contatore_co5)  è uguale a  (152) ) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))) )  e  
( (mainclass_c1_contatore_co5)  è uguale a  (152) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (152)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#12
                    DIStatement("""ITStatement\n/*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t6' è attivo )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x))) )""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v6)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#13
                    DIStatement("""ITStatement\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a avviox ,argomento_a4   uguale a Rosso  e argomento_a3   uguale a c270x )  non  è  uguale a  False  /*40,*/ , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co1""", [
                    DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a avviox ,argomento_a4   uguale a Rosso  e argomento_a3   uguale a c270x )  non  è  uguale a  False""", [
                    DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (False)""", [
                    DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                    ]),#0
                    ]),#0
                    ]),#14
                    DIStatement("""ITEStatementImpl\n/*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11043 /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 14, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M3""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11043 /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 14""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co1)  è maggiore di  (11043)) )  e  ( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è maggiore di  (11043))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (11043)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2)  è uguale a  (14)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3"""),#1
                    ]),#15
                    DIStatement("""ITStatement\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 132 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da AC, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  False""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 132 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da AC""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co1)  è minore di  (132)) )  e  
( negazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (ac))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è minore di  (132))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (132)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v2)  è uguale a  (ac)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (ac))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (ac)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#16
                    DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloxVerdex,  Applica gli effetti
       della macro MainClass_C1_macroef_M3  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti3_restore' è inattivo) )  o  
( ( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )  e  
( (consdef)  è uguale a  (False) ) ) )  o  
( ( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )  e  
( il timer 'mainclass_c1_timer_t4' è attivo ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'mainclass_c1_restoreti_ti3_restore' è inattivo) )  o  
( ( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti3_restore' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti3_restore' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t4' è inattivo) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )  e  
( il timer 'mainclass_c1_timer_t4' è attivo )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3"""),#1
                    ]),#17
                    DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 144, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M4""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 144""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co1)  è uguale a  (144)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (144))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (144)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M4"""),#1
                    ]),#18
                    DIStatement("""ITEStatementImpl\n/*73,*/


 /*37,*/  se la variabile MainClass_C1_variabile_V6 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*37,*/  se la variabile MainClass_C1_variabile_V6 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v6)  è uguale a  (False)) )  e  
( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (c270x)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#19
                    DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 1532 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 151, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co2""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 1532 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 151""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( ( (mainclass_c1_contatore_co5)  è uguale a  (1532) )  e  
( (mainclass_c1_contatore_co1)  è maggiore di  (15) ) ) )  o  
( ( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)) )  e  
( negazione di ((mainclass_c1_variabile_v2)  è uguale a  (ac)) ) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( ( (mainclass_c1_contatore_co5)  è uguale a  (1532) )  e  
( (mainclass_c1_contatore_co1)  è maggiore di  (15) ) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co5)  è uguale a  (1532) )  e  
( (mainclass_c1_contatore_co1)  è maggiore di  (15) )""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (1532)""", [
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (15)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)) )  e  
( negazione di ((mainclass_c1_variabile_v2)  è uguale a  (ac)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (ac))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (ac)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è maggiore di  (151))""", [
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (151)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#20
                    DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 115 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore AC""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 115 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( (mainclass_c1_contatore_co5)  è minore di  (115) ) )  e  
( (mainclass_c1_variabile_v6)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( (mainclass_c1_contatore_co5)  è minore di  (115) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (115)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x)) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (c270x))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#21
                    DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , /*68,*/Attiva il timer MainClass_C1_timer_T6

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#22
                    DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex""", [
                    DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto""", [
                    ]),#0
                    ]),#23
                     )
        add_instance_deb_info(self.station_name, self.name, self.instance_name, CdLDebInfo([
            # transizioni iniziali
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[3], ),
                         effect=(self.dbs[14], self.dbs[15], self.dbs[16], self.dbs[17], ),
                         phase = TransPhase.Manuale
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[4], ),
                         effect=(self.dbs[18], self.dbs[19], self.dbs[20], self.dbs[21], ),
                         phase = TransPhase.Manuale
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[6], self.dbs[7], self.dbs[8], self.dbs[9], self.dbs[10], ),
                         phase = TransPhase.Manuale
                         ),
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[5], ),
                         effect=(self.dbs[22], self.dbs[23], ),
                         phase = TransPhase.Stato
                         ),
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2,
                         guard=(self.dbs[2], ),
                         effect=(self.dbs[11], self.dbs[12], self.dbs[13], ),
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

        self.set_mainclass_c1_previousco_c1_prev(False)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())
        self.set_mainclass_c1_previousva_pv5_prev(self.get_mainclass_c1_previousva_pv5())

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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                if(self.guard_NOMINAL_ACTUATION_state1_state2_001()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1
                elif(self.guard_NOMINAL_ACTUATION_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_2
                elif(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                if(self.guard_PERMANENCE_state2_000()):
                    self.curr_transition = self.Transition._State2__State2__stateSheet_1__permanence
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
                if(self.guard_NOMINAL_ACTUATION_state1_state2_000()):
                    self.curr_transition = self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_0
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            elif self.is_current_state(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_PERMANENCE_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__permanence:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_PERMANENCE_state1_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_0:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_000()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State2__stateSheet_0__nominalActuation__transitionTo_1:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state2)
            self.effect_NOMINAL_ACTUATION_state1_state2_001()
            self.response_wait()
        elif self.curr_transition == self.Transition._State1__State1__stateSheet_0__nominalActuation__transitionTo_2:
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
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
        
         commento: {93,}  Tutte le seguenti {
         Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
         commento: {36,}  se il timer MainClass_C1_timer_T4 è attivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
        
        
        }
        }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[1].subs[0].subs[0]) and db(not db((db((db((db((db(self.get_mainclass_c1_timer_t4().isAttivato(), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[1].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[1].subs[0].subs[1].subs[1]), self.dbs[1].subs[0].subs[1]))
        if res_manCmdCondition_0:
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.PROCESSED)
        return db((db(res_manCmdCondition_0, self.dbs[1].subs[0])), self.dbs[1])
    
    def guard_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         {  Nessuna  }
        """
        return db((True), self.dbs[2])
    
    def guard_NOMINAL_ACTUATION_state1_state2_001(self):
        """
        CNL corrispondente:
         {  commento: {86,}  Almeno una delle seguenti {
         commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
         commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   MainClass_C1_command_comm7   commento: {77,}
         commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 13 commento: {37,} o  se la variabile MainClass_C1_variabile_V2 non è  uguale a AC commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
        } commento: {82,}  Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
         commento: {83,}  Tutte le seguenti {
         Ricezione del  comando manuale   MainClass_C1_command_comm7   commento: {77,}
         commento: {69,} commento: {37,}  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox commento: {37,} e  se la variabile MainClass_C1_variabile_V7 non è  uguale a avviox commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T6 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  diverso da  True , Solo una delle seguenti { 
         commento: {68,} commento: {35,}  se il controllo MainClass_C1_controllo_C9 non è  uguale a GialloxVerdex, Almeno una delle seguenti { 
         commento: {67,}  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Tutte le seguenti { 
         commento: {38,}  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 1415, Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a  False 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a  True 
        
        
        }
        } }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[3].subs[0].subs[1].subs[0]) and db(not db((db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 13, self.dbs[3].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.ac, self.dbs[3].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[3].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[3].subs[0].subs[1].subs[1].subs[1]), self.dbs[3].subs[0].subs[1].subs[1]))
        res_manCmdCondition_1 = (db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[3].subs[0].subs[3].subs[0]) and db(not db((db((db((db(not db(self.get_mainclass_c1_variabile_v7() == GlobalEnumeration.avviox, self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v7() == GlobalEnumeration.avviox, self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v6() == True, self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t6().isAttivato(), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v6() == True, self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[1].subs[1])), self.dbs[3].subs[0].subs[3].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[3].subs[1].subs[0]) or db((((db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.gialloxverdex, self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_consdef() == False, self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 1415, self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1].subs[1])), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0].subs[1]), self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[0])) + (db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[3].subs[0].subs[3].subs[1].subs[1].subs[1]))) == 1), self.dbs[3].subs[0].subs[3].subs[1].subs[1]), self.dbs[3].subs[0].subs[3].subs[1]) and db(not db(self.get_mainclass_c1_variabile_v6() == True, self.dbs[3].subs[0].subs[3].subs[2].subs[0]), self.dbs[3].subs[0].subs[3].subs[2]))
        if (db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[3].subs[0].subs[0]) or db(res_manCmdCondition_0, self.dbs[3].subs[0].subs[1]) or db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[3].subs[0].subs[2]) or db(res_manCmdCondition_1, self.dbs[3].subs[0].subs[3])):
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.PROCESSED)
        return db((db((db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[3].subs[0].subs[0]) or db(res_manCmdCondition_0, self.dbs[3].subs[0].subs[1]) or db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[3].subs[0].subs[2]) or db(res_manCmdCondition_1, self.dbs[3].subs[0].subs[3])), self.dbs[3].subs[0])), self.dbs[3])
    
    def guard_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         {  commento: {93,}  Tutte le seguenti {
         Ricezione del comando manuale   MainClass_C1_command_comm7   commento: {77,}
         commento: {69,} commento: {35,}  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex, Solo una delle seguenti { 
         commento: {69,} commento: {36,}  se il timer MainClass_C1_timer_T6 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Solo una delle seguenti { 
         commento: {69,} commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x, Solo una delle seguenti { 
         commento: {67,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 12150 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 154 commento: {38,} o  se il contatore MainClass_C1_contatore_Co2 è  uguale a  commento: {53,} 11 commento: {36,} e  se il timer MainClass_C1_timer_T6 non è disattivo, Tutte le seguenti { 
         commento: {69,}  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  uguale a  True , Solo una delle seguenti { 
         commento: {68,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 123 e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x, Almeno una delle seguenti { 
         commento: {68,} commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 11 commento: {35,} e  se il controllo MainClass_C1_controllo_C5 è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, Almeno una delle seguenti { 
         commento: {67,} commento: {37,}  se la variabile MainClass_C1_variabile_V2 è  uguale a AC commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {36,} e  se il timer MainClass_C1_timer_T4 è disattivo, Tutte le seguenti { 
          se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  diverso da  commento: {56,} 13215, Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  diverso da c270x
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a GialloxVerdex
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  uguale a c270x
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  diverso da  commento: {56,} 120
        
        
        } }
        """
        res_manCmdCondition_0 = (db(self.is_triggered('eventMainclass_c1_command_comm7'), self.dbs[4].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[4].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[0]) or db((((db(not db((db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((((db(not db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 12150, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 154, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co2().get_valore() == 11, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v6() == True, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 123, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_mainclass_c1_variabile_v6() == True, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 11, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.ac, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 13215, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_consdef() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1]))) == 1), self.dbs[4].subs[0].subs[1].subs[1].subs[0].subs[1]), self.dbs[4].subs[0].subs[1].subs[1].subs[0])) + (db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[4].subs[0].subs[1].subs[1].subs[1]))) == 1), self.dbs[4].subs[0].subs[1].subs[1]), self.dbs[4].subs[0].subs[1]) and db(not db(not db(self.get_mainclass_c1_contatore_co2().get_valore() == 120, self.dbs[4].subs[0].subs[2].subs[0].subs[0]), self.dbs[4].subs[0].subs[2].subs[0]), self.dbs[4].subs[0].subs[2]))
        if res_manCmdCondition_0:
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.PROCESSED)
        return db((db(res_manCmdCondition_0, self.dbs[4].subs[0])), self.dbs[4])
    
    def guard_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         Nessuna 
        }
        """
        return db((True), self.dbs[5])
    
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
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x commento: {36,} o  se il timer MainClass_C1_timer_T6 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co2
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {35,} o  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co1
        
        
          se il controllo ConsDef è uguale a FALSE , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co1
        
           
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  commento: {53,} 3 commento: {36,} o  se il timer MainClass_C1_timer_T6 non è disattivo, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T6
        
        
         commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M4  commento: {73,}
        
        
        
        }
        """
        #  /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x /*36,*/ o  se il timer MainClass_C1_timer_T6 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co2
        if db((db((db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[6].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t6().isAttivato(), self.dbs[6].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[6].subs[0].subs[1].subs[0]), self.dbs[6].subs[0].subs[1])), self.dbs[6].subs[0]):
            self.get_mainclass_c1_contatore_co5().incrementa()
        else:
            self.get_mainclass_c1_contatore_co2().decrementa()
        #  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co1
        if db((db((db((db(self.get_consdef() == False, self.dbs[7].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[7].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[7].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[7].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[7].subs[0].subs[0].subs[0].subs[1])), self.dbs[7].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[7].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[7].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[7].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[7].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[7].subs[0].subs[0].subs[1].subs[1])), self.dbs[7].subs[0].subs[0].subs[1])), self.dbs[7].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.c270x, self.dbs[7].subs[0].subs[1].subs[0].subs[0]), self.dbs[7].subs[0].subs[1].subs[0]), self.dbs[7].subs[0].subs[1])), self.dbs[7].subs[0]):
            self.set_mainclass_c1_variabile_v2(GlobalEnumeration.ac)
        else:
            self.get_mainclass_c1_contatore_co1().decrementa()
        #  se il controllo ConsDef è uguale a FALSE , /*72,*/Azzera il contatore MainClass_C1_contatore_Co1
        if db(self.get_consdef() == False, self.dbs[8].subs[0]):
            self.get_mainclass_c1_contatore_co1().resetta()
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  /*53,*/ 3 /*36,*/ o  se il timer MainClass_C1_timer_T6 non è disattivo, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T6
        if db((db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == 3, self.dbs[9].subs[0].subs[0].subs[0]), self.dbs[9].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[9].subs[0].subs[1].subs[0]), self.dbs[9].subs[0].subs[1])), self.dbs[9].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
        else:
            self.get_mainclass_c1_timer_t6().attiva()
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M4
        if db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[10].subs[0].subs[0].subs[0]), self.dbs[10].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[10].subs[0].subs[1])), self.dbs[10].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
        else:
            self.macroMainclass_c1_macroef_m4(self.dbs[10].subs[1])
    
    def effect_NOMINAL_ACTUATION_state1_state2_000(self):
        """
        CNL corrispondente:
         { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è disattivo commento: {36,} e  se il timer MainClass_C1_timer_T6 è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 13043,  Applica gli effetti
               della macro MainClass_C1_macroef_M3  commento: {73,}
        
           
         commento: {36,}  se il timer MainClass_C1_timer_T6 è scaduto commento: {34,} o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 152 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co2
        
        
         commento: {36,}  se il timer MainClass_C1_timer_T6 è attivo commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
        
           
         }
        """
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 è disattivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 13043,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M3
        if db((db((db(self.get_mainclass_c1_restoreti_ti3_restore().isDisattivato(), self.dbs[11].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[11].subs[0].subs[0].subs[1])), self.dbs[11].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 13043, self.dbs[11].subs[0].subs[1].subs[0]), self.dbs[11].subs[0].subs[1])), self.dbs[11].subs[0]):
            self.macroMainclass_c1_macroef_m3(self.dbs[11].subs[1])
        #  /*73,*/
        #     
        #   /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto /*34,*/ o  se il parametro MainClass_C1_parametro_P3 non è  diverso da c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 152 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a GialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co2
        if db((db((db(self.get_mainclass_c1_timer_t6().isScaduto(), self.dbs[12].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[12].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[12].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[12].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() == 152, self.dbs[12].subs[0].subs[0].subs[1].subs[1])), self.dbs[12].subs[0].subs[0].subs[1])), self.dbs[12].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[12].subs[0].subs[1].subs[0].subs[0]), self.dbs[12].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[12].subs[0].subs[1].subs[1].subs[0]), self.dbs[12].subs[0].subs[1].subs[1])), self.dbs[12].subs[0].subs[1])), self.dbs[12].subs[0]):
            self.set_mainclass_c1_variabile_v8(GlobalEnumeration.c270x)
        else:
            self.get_mainclass_c1_contatore_co2().resetta()
        #  /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da c270x /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  diverso da  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  False
        if db((db((db(self.get_mainclass_c1_timer_t6().isAttivato(), self.dbs[13].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.c270x, self.dbs[13].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[13].subs[0].subs[0].subs[1].subs[0]), self.dbs[13].subs[0].subs[0].subs[1])), self.dbs[13].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v6() == True, self.dbs[13].subs[0].subs[1].subs[0].subs[0]), self.dbs[13].subs[0].subs[1].subs[0]), self.dbs[13].subs[0].subs[1])), self.dbs[13].subs[0]):
            self.set_mainclass_c1_variabile_v6(False)
    
    def effect_NOMINAL_ACTUATION_state1_state2_001(self):
        """
        CNL corrispondente:
         {  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a avviox ,argomento_a4   uguale a Rosso  e argomento_a3   uguale a c270x )  non  è  uguale a  False  commento: {40,} , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co1
        
           
         commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 11043 commento: {36,} e  se il timer MainClass_C1_timer_T4 non è disattivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  commento: {53,} 14, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M3  commento: {73,}
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 132 commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  diverso da AC, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T4 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {36,} e  se il timer MainClass_C1_timer_T4 è attivo commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloxVerdex,  Applica gli effetti
               della macro MainClass_C1_macroef_M3  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
        
        
         }
        """
        #  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a avviox ,argomento_a4   uguale a Rosso  e argomento_a3   uguale a c270x )  non  è  uguale a  False  /*40,*/ , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co1
        if db(not db(db(self.macroMainclass_c1_macrova_m1(GlobalEnumeration.avviox,GlobalEnumeration.c270x,GlobalEnumeration.rosso,GlobalEnumeration.avviox, self.dbs[14].subs[0].subs[0].subs[0]), self.dbs[14].subs[0].subs[0].subs[0]) == False, self.dbs[14].subs[0].subs[0]), self.dbs[14].subs[0]):
            self.get_mainclass_c1_contatore_co1().incrementa()
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 11043 /*36,*/ e  se il timer MainClass_C1_timer_T4 non è disattivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 è  uguale a  /*53,*/ 14, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M3
        if db((db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 11043, self.dbs[15].subs[0].subs[0].subs[0].subs[0]), self.dbs[15].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[15].subs[0].subs[0].subs[1].subs[0]), self.dbs[15].subs[0].subs[0].subs[1])), self.dbs[15].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co2().get_valore() == 14, self.dbs[15].subs[0].subs[1])), self.dbs[15].subs[0]):
            self.set_mainclass_c1_variabile_v6(True)
        else:
            self.macroMainclass_c1_macroef_m3(self.dbs[15].subs[1])
        #  /*73,*/
        #    se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 132 /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  diverso da AC, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  False
        if db((db((db((db((db(self.get_consdef() == False, self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[16].subs[0].subs[0].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[16].subs[0].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[16].subs[0].subs[0].subs[1])), self.dbs[16].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 132, self.dbs[16].subs[0].subs[1].subs[0].subs[0]), self.dbs[16].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.ac, self.dbs[16].subs[0].subs[1].subs[1].subs[0].subs[0]), self.dbs[16].subs[0].subs[1].subs[1].subs[0]), self.dbs[16].subs[0].subs[1].subs[1])), self.dbs[16].subs[0].subs[1])), self.dbs[16].subs[0]):
            self.set_mainclass_c1_variabile_v6(False)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T4 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*36,*/ e  se il timer MainClass_C1_timer_T4 è attivo /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  uguale a GialloxVerdex,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M3  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True
        if db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti3_restore().isDisattivato(), self.dbs[17].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[17].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), self.dbs[17].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[17].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[17].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[17].subs[0].subs[0].subs[0].subs[1])), self.dbs[17].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[17].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[17].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isAttivato(), self.dbs[17].subs[0].subs[0].subs[1].subs[1])), self.dbs[17].subs[0].subs[0].subs[1])), self.dbs[17].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[17].subs[0].subs[1])), self.dbs[17].subs[0]):
            self.macroMainclass_c1_macroef_m3(self.dbs[17].subs[1])
        else:
            self.set_mainclass_c1_variabile_v6(True)
    
    def effect_NOMINAL_ACTUATION_state1_000(self):
        """
        CNL corrispondente:
         { commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 144, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M4  commento: {73,}
        
        
         commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  diverso da  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
        
        
          se il controllo ConsDef è uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 1532 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex commento: {37,} e  se la variabile MainClass_C1_variabile_V2 è  diverso da AC commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 151, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co2
        
           
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 115 commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
        
           
         }
        """
        #  /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 144, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M4
        if db((db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[18].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 144, self.dbs[18].subs[0].subs[1].subs[0].subs[0]), self.dbs[18].subs[0].subs[1].subs[0]), self.dbs[18].subs[0].subs[1])), self.dbs[18].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
        else:
            self.macroMainclass_c1_macroef_m4(self.dbs[18].subs[1])
        #  /*73,*/
        #   /*37,*/  se la variabile MainClass_C1_variabile_V6 è  diverso da  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  False 
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5
        if db((db((db(not db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[19].subs[0].subs[0].subs[0].subs[0]), self.dbs[19].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.c270x, self.dbs[19].subs[0].subs[0].subs[1].subs[0]), self.dbs[19].subs[0].subs[0].subs[1])), self.dbs[19].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.c270x, self.dbs[19].subs[0].subs[1].subs[0]), self.dbs[19].subs[0].subs[1])), self.dbs[19].subs[0]):
            self.set_mainclass_c1_variabile_v6(False)
        else:
            self.get_mainclass_c1_contatore_co5().decrementa()
        #  se il controllo ConsDef è uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 1532 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*37,*/ e  se la variabile MainClass_C1_variabile_V2 è  diverso da AC /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 151, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co2
        if db((db((db((db(self.get_consdef() == False, self.dbs[20].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_contatore_co5().get_valore() == 1532, self.dbs[20].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co1().get_valore() > 15, self.dbs[20].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[20].subs[0].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[20].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[20].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == GlobalEnumeration.ac, self.dbs[20].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[20].subs[0].subs[0].subs[1].subs[1])), self.dbs[20].subs[0].subs[0].subs[1])), self.dbs[20].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 151, self.dbs[20].subs[0].subs[1].subs[0]), self.dbs[20].subs[0].subs[1])), self.dbs[20].subs[0]):
            self.get_mainclass_c1_contatore_co2().incrementa()
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 115 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  diverso da c270x /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore AC
        if db((db((db((db(self.get_consdef() == False, self.dbs[21].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() < 115, self.dbs[21].subs[0].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[21].subs[0].subs[0].subs[1])), self.dbs[21].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, self.dbs[21].subs[0].subs[1].subs[0].subs[0]), self.dbs[21].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, self.dbs[21].subs[0].subs[1].subs[1].subs[0]), self.dbs[21].subs[0].subs[1].subs[1])), self.dbs[21].subs[0].subs[1])), self.dbs[21].subs[0]):
            self.set_mainclass_c1_variabile_v2(GlobalEnumeration.ac)
    
    def effect_PERMANENCE_state2_000(self):
        """
        CNL corrispondente:
        
        {
        
         commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , commento: {68,}Attiva il timer MainClass_C1_timer_T6
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
        
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
           
        
        }
        """
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False , /*68,*/Attiva il timer MainClass_C1_timer_T6
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        if db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[22].subs[0].subs[0].subs[0].subs[0]), self.dbs[22].subs[0].subs[0].subs[0]), self.dbs[22].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v6() == False, self.dbs[22].subs[0].subs[1])), self.dbs[22].subs[0]):
            self.get_mainclass_c1_timer_t6().attiva()
        else:
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        if db(self.get_mainclass_c1_restoreti_ti2_restore().isScaduto(), self.dbs[23].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
    
    # effect macros
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a Rosso ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )   è  diverso da  False  commento: {40,}  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a avviox commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T6
        
        
          se il controllo ConsDef è uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 12 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  commento: {55,} 115 o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex commento: {35,} o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 1304, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
        
           
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  commento: {54,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  commento: {56,} 1132 commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 13, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a Rosso ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )   è  diverso da  False  /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a avviox /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a Rosso ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )   è  diverso da  False  /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a avviox /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (False)) )  e  
( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (c270x)) ) )  o  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (avviox)) ) )  o  
( ( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))) )  e  
( (mainclass_c1_parametro_p3)  è uguale a  (c270x) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (False)) )  e  
( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (c270x)) ) )  o  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (avviox)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (False)) )  e  
( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (c270x)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (avviox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))) )  e  
( (mainclass_c1_parametro_p3)  è uguale a  (c270x) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef è uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 12 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 115 o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 12 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 115 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( (mainclass_c1_contatore_co1)  è maggiore di  (12) ) )  o  
( ( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)) )  e  
( negazione di ((mainclass_c1_contatore_co1)  è minore di  (115)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( (mainclass_c1_contatore_co1)  è maggiore di  (12) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (12)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)) )  e  
( negazione di ((mainclass_c1_contatore_co1)  è minore di  (115)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è minore di  (115))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (115)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 1304, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 1304""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x)) )  e  
( negazione di (negazione di ((mainclass_c1_contatore_co1)  è uguale a  (1304))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co1)  è uguale a  (1304)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (1304))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (1304)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 1132 /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 13, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 1132 /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_restoreva_rv1_restore)  è maggiore di  (4) )  e  
( negazione di (negazione di ((mainclass_c1_contatore_co5)  è uguale a  (1132))) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_restoreva_rv1_restore)  è maggiore di  (4)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co5)  è uguale a  (1132)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è uguale a  (1132))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (1132)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è maggiore di  (13))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (13)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a avviox ,argomento_a10   uguale a Rosso ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )   è  diverso da  False  /*40,*/  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  diverso da c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a avviox /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da GialloxVerdex /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T6
        if db((db((db((db((db(not db(db(self.macroMainclass_c1_macrova_m1(GlobalEnumeration.rosso,GlobalEnumeration.c270x,GlobalEnumeration.avviox,GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v5() == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
        else:
            self.get_mainclass_c1_timer_t6().attiva()
        #  se il controllo ConsDef è uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True
        if db(self.get_consdef() == False, di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v8(GlobalEnumeration.c270x)
        else:
            self.set_mainclass_c1_variabile_v6(True)
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 12 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  minore di  /*55,*/ 115 o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore GialloxVerdex
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co1().get_valore() > 12, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 115, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
        else:
            self.set_mainclass_c1_comando_c2(GlobalEnumeration.gialloxverdex)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C7 è  diverso da GialloxVerdex /*35,*/ o  se il controllo MainClass_C1_controllo_C8 è  diverso da c270x /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 1304, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore c270x
        if db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.c270x, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 1304, di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v8(GlobalEnumeration.c270x)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 non è  diverso da  /*56,*/ 1132 /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 13, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5
        if db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() > 4, di_ctx.subs[4].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co5().get_valore() == 1132, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 13, di_ctx.subs[4].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.get_mainclass_c1_contatore_co5().incrementa()
    
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  commento: {54,} 120 commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 14432 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 è  uguale a c270x, commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co5
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 120 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 14432 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a c270x, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 120 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 14432 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a c270x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( (mainclass_c1_contatore_co5)  è maggiore di  (120) ) )  e  
( negazione di ((mainclass_c1_contatore_co1)  è uguale a  (14432)) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( (mainclass_c1_contatore_co5)  è maggiore di  (120) ) )  e  
( negazione di ((mainclass_c1_contatore_co1)  è uguale a  (14432)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  ( (mainclass_c1_contatore_co5)  è maggiore di  (120) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (120)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (14432))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (14432)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_variabile_v8)  è uguale a  (c270x) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (c270x)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  maggiore di  /*54,*/ 120 /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 14432 o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 è  uguale a c270x, /*71,*/Decrementa il contatore MainClass_C1_contatore_Co5
        if db((db((db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() > 120, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 14432, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_contatore_co5().decrementa()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m10")
    def macroMainclass_c1_macrove_m10(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  commento: {53,} 14, Tutte le seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 1521 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
          se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  commento: {40,}  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   commento: {48,51,}  commento: {,}  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co2 non sia  minore di  commento: {55,} 135
        
        
         } Verifica che   commento: {48,49,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia disattivo
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T4 sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T4 sia attivo
        
        
         } Verifica che   commento: {49,50,}  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T4 non sia disattivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 14, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1521 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  minore di  /*55,*/ 135


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo


 } Verifica che   /*49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 14, Tutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1521 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  minore di  /*55,*/ 135


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V6 è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\nla variabile MainClass_C1_variabile_V6 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1521 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  minore di  /*55,*/ 135


 } Verifica che   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1521 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  minore di  /*55,*/ 135


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1521 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1521""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1521""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE , Verifica che   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  minore di  /*55,*/ 135""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True  /*40,*/  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  uguale a c270x""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M1 ( con argomento_a5   uguale a Rosso ,argomento_a10   uguale a avviox ,argomento_a4   uguale a avviox  e argomento_a3   uguale a c270x )  non  è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (True)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P3 è  uguale a c270x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  uguale a c270x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V6 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P3 non è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  minore di  /*55,*/ 135""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,51,*/  /*,*/  il controllo MainClass_C1_controllo_C5 non sia  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co2 non sia  minore di  /*55,*/ 135""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co2)  è minore di  (135)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T4 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_mainclass_c1_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co1().get_valore() == 1521, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(not db(db(self.macroMainclass_c1_macrova_m1(GlobalEnumeration.avviox,GlobalEnumeration.c270x,GlobalEnumeration.avviox,GlobalEnumeration.rosso, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() < 135, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(self.get_mainclass_c1_variabile_v6() == False, di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m1")
    def macroMainclass_c1_macrova_m1(self, argomento_a10, argomento_a3, argomento_a4, argomento_a5, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} e  se l'argomento argomento_a10 è  diverso da avviox commento: {39,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  commento: {53,} 1515 , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se l'argomento argomento_a10 è  diverso da avviox /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1515 , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se l'argomento argomento_a10 è  diverso da avviox /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1515""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (stato_restore)  è uguale a  (state1) )  e  
( negazione di ((argomento_a10)  è uguale a  (avviox)) )""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a10)  è uguale a  (avviox))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a10)  è uguale a  (avviox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (1515)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ e  se l'argomento argomento_a10 è  diverso da avviox /*39,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  uguale a  /*53,*/ 1515 , assegna alla macro il valore  True
        if db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_a10 == GlobalEnumeration.avviox, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co1().get_valore() == 1515, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm7(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm7')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm8(self, notifying_process, argomento_ave2, argomento_ave6, argomento_ave7, argomento_ave8, argomento_ave9):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm8', argomento_ave2=argomento_ave2, argomento_ave6=argomento_ave6, argomento_ave7=argomento_ave7, argomento_ave8=argomento_ave8, argomento_ave9=argomento_ave9)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c1_prev(self.get_mainclass_c1_previousco_c1())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())
        self.set_mainclass_c1_previousva_pv5_prev(self.get_mainclass_c1_previousva_pv5())

