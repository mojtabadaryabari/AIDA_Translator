# Codice del modello 'TestCase16', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_restoreva_rv3(False)
        self.set_mainclass_c1_restoreva_rv4(False)
        self.set_mainclass_c1_restoreva_rv5(GlobalEnumeration.rossogialloxverdex)
        self.set_mainclass_c1_variabile_v5(False)
        self.set_mainclass_c1_variabile_v6(GlobalEnumeration.rosso)
        self.set_mainclass_c1_variabile_v9(GlobalEnumeration.c180)

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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p8, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(3000)
        self.set_mainclass_c1_restoreti_ti1_restore(3000)
        self.set_mainclass_c1_restoreti_ti2(2000)
        self.set_mainclass_c1_restoreti_ti2_restore(2000)
        self.set_mainclass_c1_restoreti_ti3(21320000)
        self.set_mainclass_c1_restoreti_ti3_restore(21320000)
        self.set_mainclass_c1_restoreti_ti4(154000)
        self.set_mainclass_c1_restoreti_ti4_restore(154000)
        self.set_mainclass_c1_timer_t7(554000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_timer_t7,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co10(0)
        self.set_mainclass_c1_contatore_co4(0)
        self.set_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c1(self, mainclass_c1_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c1",mainclass_c1_comando_c1)

    def set_mainclass_c1_comando_c5(self, mainclass_c1_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c5",mainclass_c1_comando_c5)

    def set_mainclass_c1_comando_c7(self, mainclass_c1_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c7",mainclass_c1_comando_c7)

    def set_mainclass_c1_comando_c8(self, mainclass_c1_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c8",mainclass_c1_comando_c8)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c10")

    def get_mainclass_c1_controllo_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c2")

    def get_mainclass_c1_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c6")

    def get_mainclass_c1_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3")


    # setters for state variables
    def set_mainclass_c1_previousco_c3_prev(self, mainclass_c1_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev",mainclass_c1_previousco_c3_prev)
    def set_mainclass_c1_previousva_pv1(self, mainclass_c1_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1",mainclass_c1_previousva_pv1)
    def set_mainclass_c1_previousva_pv1_prev(self, mainclass_c1_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev",mainclass_c1_previousva_pv1_prev)
    def set_mainclass_c1_previousva_pv2(self, mainclass_c1_previousva_pv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2",mainclass_c1_previousva_pv2)
    def set_mainclass_c1_previousva_pv2_prev(self, mainclass_c1_previousva_pv2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2_prev",mainclass_c1_previousva_pv2_prev)
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_restoreva_rv4(self, mainclass_c1_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4",mainclass_c1_restoreva_rv4)
    def set_mainclass_c1_restoreva_rv5(self, mainclass_c1_restoreva_rv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5",mainclass_c1_restoreva_rv5)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v6(self, mainclass_c1_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6",mainclass_c1_variabile_v6)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
    def get_mainclass_c1_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev")

    def get_mainclass_c1_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1")

    def get_mainclass_c1_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv1_prev")

    def get_mainclass_c1_previousva_pv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2")

    def get_mainclass_c1_previousva_pv2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousva_pv2_prev")

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

    def get_mainclass_c1_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4")

    def get_mainclass_c1_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4_restore")

    def get_mainclass_c1_restoreva_rv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5")

    def get_mainclass_c1_restoreva_rv5_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv5_restore")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

    def get_mainclass_c1_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6")

    def get_mainclass_c1_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9")

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

    def set_mainclass_c1_restoreti_ti4(self, timerDuration):
        self.mainclass_c1_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4", self.memory)

    def set_mainclass_c1_restoreti_ti4_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4_restore", self.memory)

    def set_mainclass_c1_timer_t7(self, timerDuration):
        self.mainclass_c1_timer_t7 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t7", self.memory)


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

    def get_mainclass_c1_restoreti_ti4(self):
        return self.mainclass_c1_restoreti_ti4

    def get_mainclass_c1_restoreti_ti4_restore(self):
        return self.mainclass_c1_restoreti_ti4_restore

    def get_mainclass_c1_timer_t7(self):
        return self.mainclass_c1_timer_t7


    # setters for counters
    def set_mainclass_c1_contatore_co10(self, counterInitValue):
        self.mainclass_c1_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co10", self.memory)

    def set_mainclass_c1_contatore_co4(self, counterInitValue):
        self.mainclass_c1_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co4", self.memory)

    def set_mainclass_c1_contatore_co9(self, counterInitValue):
        self.mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co9", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co10(self):
        return self.mainclass_c1_contatore_co10

    def get_mainclass_c1_contatore_co4(self):
        return self.mainclass_c1_contatore_co4

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
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#1
                    DIStatement("""ITStatement\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo,  Applica gli effetti
       della macro MainClass_C1_macroef_M1""", [
                    DIBoolExpr("""NAryLogicOP (AND)\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  ( negazione di (negazione di ((mainclass_c1_controllo_c10)  è uguale a  (True))) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c10)  è uguale a  (True)))""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M1"""),#1
                    ]),#2
                    DIStatement("""ITStatement\n/*73,*/

   
  se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T7 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  minore di  /*55,*/ 123 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co9""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
  se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T7 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  minore di  /*55,*/ 123 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( ( ( ( negazione di (il timer 'mainclass_c1_timer_t7' è attivo) )  e  ( (mainclass_c1_contatore_co10)  è minore di  (123) ) )  e  ( (mainclass_c1_variabile_v9)  è uguale a  (c120x) ) )  e  
( (mainclass_c1_controllo_c6)  è uguale a  (False) ) )""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( ( negazione di (il timer 'mainclass_c1_timer_t7' è attivo) )  e  ( (mainclass_c1_contatore_co10)  è minore di  (123) ) )  e  ( (mainclass_c1_variabile_v9)  è uguale a  (c120x) ) )  e  
( (mainclass_c1_controllo_c6)  è uguale a  (False) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'mainclass_c1_timer_t7' è attivo) )  e  ( (mainclass_c1_contatore_co10)  è minore di  (123) ) )  e  ( (mainclass_c1_variabile_v9)  è uguale a  (c120x) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t7' è attivo) )  e  ( (mainclass_c1_contatore_co10)  è minore di  (123) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t7' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10)  è minore di  (123)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c120x)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#0
                    ]),#3
                    DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co9

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_restoreva_rv1_restore)  è minore di  (9)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    ]),#4
                    DIStatement("""ITStatement\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True""", [
                    DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                    DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                    ]),#0
                    ]),#0
                    ]),#5
                    DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1341, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  False 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1341""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_parametro_p8)  è minore di  (8)) )  o  
( ( negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t7' è scaduto) ) ) )  o  
( (mainclass_c1_variabile_v9)  è uguale a  (c120x) )""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_parametro_p8)  è minore di  (8)) )  o  
( ( negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t7' è scaduto) ) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è minore di  (8))""", [
                    DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p8)  è minore di  (8)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t7' è scaduto) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t7' è scaduto)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è scaduto""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c120x)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (1341)""", [
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
                         guard=(self.dbs[1], ),
                         effect=(self.dbs[2], self.dbs[3], self.dbs[4], self.dbs[5], self.dbs[6], ),
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

        self.set_mainclass_c1_previousco_c3_prev(True)
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())

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
        
         Nessuna  commento: {80,}
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
        
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo,  Applica gli effetti
               della macro MainClass_C1_macroef_M1  commento: {73,}
        
           
          se il controllo ConsDef è uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T7 non è attivo commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 è  minore di  commento: {55,} 123 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x commento: {35,} e  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co9
        
           
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  commento: {55,} 9 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo, commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co9
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
        
        
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  True 
        
           
         commento: {34,}  se il parametro MainClass_C1_parametro_P8 non è  minore di  commento: {55,} 8 commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo commento: {36,} e  se il timer MainClass_C1_timer_T7 non è scaduto commento: {37,} o  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  commento: {53,} 1341, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  False 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
        
        
        
        }
        """
        #  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  diverso da  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M1
        if db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[2].subs[0].subs[0].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c10() == True, self.dbs[2].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[0].subs[1].subs[0]), self.dbs[2].subs[0].subs[0].subs[1])), self.dbs[2].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, self.dbs[2].subs[0].subs[1])), self.dbs[2].subs[0]):
            self.macroMainclass_c1_macroef_m1(self.dbs[2].subs[1])
        #  /*73,*/
        #     
        #    se il controllo ConsDef è uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T7 non è attivo /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 è  minore di  /*55,*/ 123 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x /*35,*/ e  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  o  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore MainClass_C1_contatore_Co9
        if db((db((db(self.get_consdef() == False, self.dbs[3].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_timer_t7().isAttivato(), self.dbs[3].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() < 123, self.dbs[3].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c120x, self.dbs[3].subs[0].subs[0].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c6() == False, self.dbs[3].subs[0].subs[0].subs[1].subs[1])), self.dbs[3].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0]) or db(self.get_consdef() == False, self.dbs[3].subs[0].subs[1])), self.dbs[3].subs[0]):
            self.get_mainclass_c1_contatore_co9().decrementa()
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  minore di  /*55,*/ 9 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo, /*70,*/Incrementa il contatore MainClass_C1_contatore_Co9
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True
        if db((db(self.get_mainclass_c1_restoreva_rv1_restore() < 9, self.dbs[4].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, self.dbs[4].subs[0].subs[1].subs[0]), self.dbs[4].subs[0].subs[1])), self.dbs[4].subs[0]):
            self.get_mainclass_c1_contatore_co9().incrementa()
        else:
            self.set_mainclass_c1_comando_c1(True)
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/, /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  True
        if db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, self.dbs[5].subs[0].subs[0]), self.dbs[5].subs[0]):
            self.set_mainclass_c1_comando_c1(True)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P8 non è  minore di  /*55,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto /*37,*/ o  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 è  uguale a  /*53,*/ 1341, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  False 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
        if db((db((db((db(not db(self.get_mainclass_c1_parametro_p8() < 8, self.dbs[6].subs[0].subs[0].subs[0].subs[0].subs[0]), self.dbs[6].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, self.dbs[6].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), self.dbs[6].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isScaduto(), self.dbs[6].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), self.dbs[6].subs[0].subs[0].subs[0].subs[1].subs[1])), self.dbs[6].subs[0].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c120x, self.dbs[6].subs[0].subs[0].subs[1])), self.dbs[6].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co10().get_valore() == 1341, self.dbs[6].subs[0].subs[1])), self.dbs[6].subs[0]):
            self.set_mainclass_c1_variabile_v5(False)
        else:
            self.set_mainclass_c1_variabile_v6(GlobalEnumeration.c75giallo)
    
    # effect macros
    def macroMainclass_c1_macroef_m1(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  commento: {53,} 12 commento: {37,} o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo o  se il controllo ConsDef  è  uguale a FALSE , commento: {68,}Attiva il timer MainClass_C1_timer_T7
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 12 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo o  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer MainClass_C1_timer_T7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 12 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True)) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (12)) ) )  o  
( negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True)) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è uguale a  (12)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (12)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  uguale a  /*53,*/ 12 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo o  se il controllo ConsDef  è  uguale a FALSE , /*68,*/Attiva il timer MainClass_C1_timer_T7
        if db((db((db((db(not db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 12, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t7().attiva()
    
    def macroMainclass_c1_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer MainClass_C1_timer_T7 è attivo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 non è  minore di  commento: {55,} 143 commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 è  minore di  commento: {55,} 12205 o  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T7 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da  False  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  commento: {56,} 124 commento: {35,} o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , commento: {72,}Azzera il contatore MainClass_C1_contatore_Co9
        
           
         commento: {37,}  se la variabile MainClass_C1_variabile_V6 non è  diverso da c75Giallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  diverso da  commento: {56,} 131 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  diverso da  commento: {56,} 10 commento: {36,} e  se il timer MainClass_C1_timer_T7 è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T7 è disattivo, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  False 
        
           
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,}, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V9 il valore c120x
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T7
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*36,*/  se il timer MainClass_C1_timer_T7 è attivo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 143 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 12205 o  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T7 è attivo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 143 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 12205 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( il timer 'mainclass_c1_timer_t7' è attivo )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è minore di  (143)) ) ) )  o  
( (mainclass_c1_contatore_co9)  è minore di  (12205) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'mainclass_c1_timer_t7' è attivo )  o  
( (consdef)  è uguale a  (False) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è minore di  (143)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'mainclass_c1_timer_t7' è attivo )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_contatore_co4)  è minore di  (143)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è minore di  (143))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co4)  è minore di  (143)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co9)  è minore di  (12205)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T7 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T7 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (True)) ) )  o  
( ( negazione di (il timer 'mainclass_c1_timer_t7' è inattivo) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True)) )  e  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di ((mainclass_c1_variabile_v5)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c6)  è uguale a  (True)) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t7' è inattivo) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t7' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , /*72,*/Azzera il contatore MainClass_C1_contatore_Co9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo)) )  o  
( ( (mainclass_c1_controllo_c6)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_parametro_p10)  è uguale a  (False)) ) ) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (124))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo)) )  o  
( ( (mainclass_c1_controllo_c6)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_parametro_p10)  è uguale a  (False)) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c6)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_parametro_p10)  è uguale a  (False)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co4)  è uguale a  (124)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co4)  è uguale a  (124))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co4)  è uguale a  (124)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*37,*/  se la variabile MainClass_C1_variabile_V6 non è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 131 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da  /*56,*/ 10 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T7 è disattivo, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V6 non è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 131 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da  /*56,*/ 10 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T7 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo))) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co9)  è uguale a  (131))) ) )  o  
( ( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (10)) ) )  e  
( il timer 'mainclass_c1_timer_t7' è scaduto ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo))) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co9)  è uguale a  (131))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co9)  è uguale a  (131)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è uguale a  (131))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9)  è uguale a  (131)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (10)) ) )  e  
( il timer 'mainclass_c1_timer_t7' è scaduto )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (10)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore c120x

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T7""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer MainClass_C1_timer_T7 è attivo o  se il controllo ConsDef  è  uguale a FALSE  o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 non è  minore di  /*55,*/ 143 /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 è  minore di  /*55,*/ 12205 o  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore c75Giallo
        if db((db((db((db((db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co4().get_valore() < 143, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co9().get_valore() < 12205, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v6(GlobalEnumeration.c75giallo)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  True  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V5 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T7 non è disattivo e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False
        if db((db((db((db((db(not db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v5() == True, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c10() == False, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c1(False)
        #  /*37,*/  se la variabile MainClass_C1_variabile_V6 non è  uguale a c75Giallo /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da  False  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 non è  diverso da  /*56,*/ 124 /*35,*/ o  se il controllo MainClass_C1_controllo_C6 è  uguale a  False , /*72,*/Azzera il contatore MainClass_C1_contatore_Co9
        if db((db((db((db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p10() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co4().get_valore() == 124, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co9().resetta()
        #  /*37,*/  se la variabile MainClass_C1_variabile_V6 non è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  diverso da  /*56,*/ 131 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  diverso da  /*56,*/ 10 /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T7 è disattivo, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  False
        if db((db((db((db(not db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co9().get_valore() == 131, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == 10, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[3].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v5(False)
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V9 il valore c120x
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T7
        if db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[4].subs[0].subs[0]), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v9(GlobalEnumeration.c120x)
        else:
            self.get_mainclass_c1_timer_t7().disattiva()
    
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 14 commento: {38,} o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  commento: {54,} 14054 commento: {37,} e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  False commento: {67,}
        
           
          se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,} commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  uguale a  commento: {53,} 12,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore  True  commento: {67,}
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 14 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 14054 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 14 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 14054 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co4)  è minore di  (14)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co10)  è maggiore di  (14054)) )  e  
( (mainclass_c1_variabile_v9)  è uguale a  (c120x) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co10)  è maggiore di  (14054))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co10)  è maggiore di  (14054)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*67,*/

   
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  uguale a  /*53,*/ 12,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/

   
  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  uguale a  /*53,*/ 12""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((stato_restore)  è uguale a  (state1)) )  e  
( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo)) ) )  o  
( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  e  
( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c10)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_contatore_co10)  è uguale a  (12)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co10)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (12)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 14 /*38,*/ o  se il contatore MainClass_C1_contatore_Co10 non è  maggiore di  /*54,*/ 14054 /*37,*/ e  se la variabile MainClass_C1_variabile_V9 è  uguale a c120x,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  False
        if db((db(self.get_mainclass_c1_contatore_co4().get_valore() < 14, di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co10().get_valore() > 14054, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v5(False)
        #  /*67,*/
        #     
        #    se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/ /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  uguale a  /*53,*/ 12,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore  True
        if db((db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c10() == False, di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() == 12, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v5(True)
    
    def macroMainclass_c1_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T7 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C1 il valore  False 
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T7 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T7 è disattivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_controllo_c10)  è uguale a  (False)) ) )  e  ( il timer 'mainclass_c1_timer_t7' è inattivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_controllo_c10)  è uguale a  (False)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C10 è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T7 è disattivo e  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C1 il valore  False
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c1(False)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        {  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False , Verifica che   commento: {47,48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False , Verifica che   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False , Verifica che   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C10 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C10 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da  False 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P10 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c10() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db((db(not db(self.get_mainclass_c1_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m4")
    def macroMainclass_c1_macrove_m4(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {37,}  se la variabile MainClass_C1_variabile_V6 è  diverso da c75Giallo, Verifica che   commento: {48,49,50,}  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T7 non sia attivo
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V6 è  diverso da c75Giallo, Verifica che   /*48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V6 è  diverso da c75Giallo, Verifica che   /*48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 è  diverso da c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m5")
    def macroMainclass_c1_macrove_m5(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo commento: {35,} e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  commento: {55,} 132 commento: {35,} e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a  commento: {53,} 2 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {61,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  commento: {54,} 14054 commento: {35,} e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  commento: {36,} e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
          se il controllo ConsDef è uguale a FALSE , Verifica che   commento: {48,49,50,51,}  commento: {,}  il timer MainClass_C1_timer_T7 sia disattivo
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 122054
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T7 non sia attivo
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
        
        
         } Verifica che   commento: {47,50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo
        
        
         } Verifica che   commento: {47,50,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 13
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False 
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo


 } Verifica che   /*47,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo


 } Verifica che   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 2 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132 /*35,*/ e  se il controllo MainClass_C1_controllo_C10 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo /*35,*/ e  se il controllo MainClass_C1_controllo_C6 non è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P9 è  uguale a c75Giallo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C6 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co10 non è  minore di  /*55,*/ 132""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10)  è minore di  (132)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C10 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P8 è  uguale a  /*53,*/ 2""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 è  diverso da c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T7 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054 /*35,*/ e  se il controllo MainClass_C1_controllo_C2 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co9 non è  maggiore di  /*54,*/ 14054""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co9)  è maggiore di  (14054)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c2)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T7 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef è uguale a FALSE , Verifica che   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,51,*/  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054""", [
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 122054""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (122054)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  diverso da c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 13
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 13""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 13""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V5 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V9 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db((db((db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() < 132, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_mainclass_c1_contatore_co9().get_valore() > 14054, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co10().get_valore() == 122054, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(not db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() < 13, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v5() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m6")
    def macroMainclass_c1_macrove_m6(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T7 è scaduto commento: {36,} e  se il timer MainClass_C1_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C2 non è  uguale a  False , Almeno una delle seguenti { 
         commento: {63,} commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  commento: {56,} 3 commento: {38,} e  se il contatore MainClass_C1_contatore_Co4 è  minore di  commento: {55,} 11 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 1213, Solo una delle seguenti { 
         commento: {36,}  se il timer MainClass_C1_timer_T7 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  commento: {53,} 13205 commento: {35,} o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   commento: {48,50,}  commento: {,}  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P8 sia  uguale a  commento: {53,} 6
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  commento: {53,} 15
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
        
        
         } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 113
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P8 non sia  uguale a  commento: {53,} 6
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a  False , Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 1213, Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 6
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 15
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a  False , Almeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 1213, Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 6
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 15
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C2 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T7 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T7 è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T7 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T7 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C2 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 1213, Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 6
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 15
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 1213, Solo una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 1213""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3 /*38,*/ e  se il contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV1 è  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (3)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co4 è  minore di  /*55,*/ 11""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 1213""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False , Verifica che   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205 /*35,*/ o  se il controllo MainClass_C1_controllo_C2 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer MainClass_C1_timer_T7 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T7 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co4 è  uguale a  /*53,*/ 13205""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C2 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,50,*/  /*,*/  la variabile MainClass_C1_variabile_V9 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v9)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 6
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 15
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 6
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 6
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P8 sia  uguale a  /*53,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C2 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 non sia  uguale a  /*53,*/ 15""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co10)  è uguale a  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 113
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 113""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P8 non sia  uguale a  /*53,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m6_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co4().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() == 1213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(not db(self.get_mainclass_c1_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co4().get_valore() == 13205, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_mainclass_c1_parametro_p8() == 6, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c2() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co10().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_mainclass_c1_contatore_co10().get_valore() < 113, di_ctx.subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p8() == 6, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m9")
    def macroMainclass_c1_macrove_m9(self, argomento_ave10, argomento_ave2, argomento_ave7, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,}  se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,} commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo, Solo una delle seguenti { 
         commento: {35,}  se il controllo MainClass_C1_controllo_C10 è  uguale a  True , Verifica che   commento: {47,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T7 sia disattivo
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co10 sia  minore di  commento: {55,} 1532
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer MainClass_C1_timer_T7 non sia attivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo, Solo una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C10 è  uguale a  True , Verifica che   /*47,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1532


 } Verifica che   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo, Solo una delle seguenti { 
 /*35,*/  se il controllo MainClass_C1_controllo_C10 è  uguale a  True , Verifica che   /*47,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1532


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 non è  uguale a c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C10 è  uguale a  True , Verifica che   /*47,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1532""", [
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C10 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1532""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 non sia  uguale a c75Giallo""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T7 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1532""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da c75Giallo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co10 sia  minore di  /*55,*/ 1532""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer MainClass_C1_timer_T7 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v6() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_parametro_p9() == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co10().get_valore() < 1532, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t7().isAttivato(), di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m10")
    def macroMainclass_c1_macrova_m10(self, argomento_a10, argomento_a2, argomento_a5, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  commento: {34,} o  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore RossoGialloGiallo
        
         commento: {46,} assegna alla macro il valore RossoGialloGiallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se lo stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c6)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C6 è  diverso da  False  /*34,*/ o  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore RossoGialloGiallo
        if db((db(not db(self.get_mainclass_c1_controllo_c6() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogiallogiallo
        #  /*46,*/ assegna alla macro il valore RossoGialloGiallo
        return GlobalEnumeration.rossogiallogiallo
    
    @srf_value_macro("macroMainclass_c1_macrova_m2")
    def macroMainclass_c1_macrova_m2(self, argomento_a1, argomento_a3, argomento_a4, argomento_a5, argomento_a6, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m2_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m2_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroMainclass_c1_macrova_m3")
    def macroMainclass_c1_macrova_m3(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a7, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a1, argomento_a3, argomento_a4, argomento_a6, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c75Giallo
        return GlobalEnumeration.c75giallo
    
    @srf_value_macro("macroMainclass_c1_macrova_m8")
    def macroMainclass_c1_macrova_m8(self, argomento_a10, argomento_a2, argomento_a5, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m8_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c3_prev(self.get_mainclass_c1_previousco_c3())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())

