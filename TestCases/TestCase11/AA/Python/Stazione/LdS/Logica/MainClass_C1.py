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

class MainClass_C1(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(MainClass_C1, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_mainclass_c1_previousva_pv1(0)
        self.set_mainclass_c1_previousva_pv2(GlobalEnumeration.avviox)
        self.set_mainclass_c1_previousva_pv3(False)
        self.set_mainclass_c1_previousva_pv4(False)
        self.set_mainclass_c1_restoreva_rv1(False)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(0)
        self.set_mainclass_c1_variabile_v6(0)
        self.set_mainclass_c1_variabile_v8(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm10'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm10',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm10',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm3DaSender216acb09'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm3DaSender216acb09',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm3DaSender216acb09',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm5'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm5',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventMainclass_c1_command_comm7'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm7',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p1, mainclass_c1_parametro_p2, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p1(mainclass_c1_parametro_p1)
        self.set_mainclass_c1_parametro_p2(mainclass_c1_parametro_p2)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(545000)
        self.set_mainclass_c1_restoreti_ti1_restore(545000)
        self.set_mainclass_c1_restoreti_ti2(20213000)
        self.set_mainclass_c1_restoreti_ti2_restore(20213000)
        self.set_mainclass_c1_restoreti_ti3(245000)
        self.set_mainclass_c1_restoreti_ti3_restore(245000)
        self.set_mainclass_c1_restoreti_ti4(3000)
        self.set_mainclass_c1_restoreti_ti4_restore(3000)
        self.set_mainclass_c1_timer_t6(2000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_restoreti_ti4,self.mainclass_c1_restoreti_ti4_restore,self.mainclass_c1_timer_t6,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co1(0)
        self.set_mainclass_c1_contatore_co7(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p1(self, mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1",mainclass_c1_parametro_p1)

    def set_mainclass_c1_parametro_p2(self, mainclass_c1_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p2",mainclass_c1_parametro_p2)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1")

    def get_mainclass_c1_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p2")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c10(self, mainclass_c1_comando_c10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c10",mainclass_c1_comando_c10)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c1")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3")

    def get_mainclass_c1_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4")

    def get_mainclass_c1_previousco_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5")

    def get_mainclass_c1_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6")


    # setters for state variables
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c3_prev(self, mainclass_c1_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev",mainclass_c1_previousco_c3_prev)
    def set_mainclass_c1_previousco_c4_prev(self, mainclass_c1_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev",mainclass_c1_previousco_c4_prev)
    def set_mainclass_c1_previousco_c5_prev(self, mainclass_c1_previousco_c5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev",mainclass_c1_previousco_c5_prev)
    def set_mainclass_c1_previousco_c6_prev(self, mainclass_c1_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev",mainclass_c1_previousco_c6_prev)
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
    def set_mainclass_c1_variabile_v6(self, mainclass_c1_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6",mainclass_c1_variabile_v6)
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)

    # getters for state variables
    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev")

    def get_mainclass_c1_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev")

    def get_mainclass_c1_previousco_c5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c5_prev")

    def get_mainclass_c1_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6_prev")

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

    def get_mainclass_c1_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6")

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

    def set_mainclass_c1_restoreti_ti4(self, timerDuration):
        self.mainclass_c1_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4", self.memory)

    def set_mainclass_c1_restoreti_ti4_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti4_restore", self.memory)

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

    def get_mainclass_c1_restoreti_ti4(self):
        return self.mainclass_c1_restoreti_ti4

    def get_mainclass_c1_restoreti_ti4_restore(self):
        return self.mainclass_c1_restoreti_ti4_restore

    def get_mainclass_c1_timer_t6(self):
        return self.mainclass_c1_timer_t6


    # setters for counters
    def set_mainclass_c1_contatore_co1(self, counterInitValue):
        self.mainclass_c1_contatore_co1 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co1", self.memory)

    def set_mainclass_c1_contatore_co7(self, counterInitValue):
        self.mainclass_c1_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co7", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co1(self):
        return self.mainclass_c1_contatore_co1

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
                    DIBoolExpr("""NAryLogicOP (AND)\nNessuna""", [
                    ]),#1
                    DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro MainClass_C1_macroef_M8""", [
                    DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_variabile_v8)  è uguale a  (False)) )  e  
( (consdef)  è uguale a  (False) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (False))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                    ]),#1
                    ]),#1
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8"""),#1
                    ]),#2
                    DIStatement("""ITStatement\n/*73,*/

   
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 14 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  uguale a c270 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, /*69,*/Disattiva il timer MainClass_C1_timer_T6""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 14 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  uguale a c270 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo""", [
                    DIBoolExpr("""NAryLogicOP (OR)\n( ( (mainclass_c1_contatore_co7)  è uguale a  (11) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è attivo) ) )  o  
( (mainclass_c1_contatore_co1)  è maggiore di  (14) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co7)  è uguale a  (11) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è attivo) )""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (11)""", [
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è attivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (14)""", [
                    ]),#1
                    ]),#0
                    DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (True)) )  e  ( negazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270)) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è inattivo) )""", [
                    DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (True)) )  e  ( negazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270)) )""", [
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (True))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                    ]),#0
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270))""", [
                    DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                    ]),#0
                    ]),#1
                    ]),#0
                    DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è inattivo)""", [
                    DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                    ]),#0
                    ]),#1
                    ]),#1
                    ]),#0
                    ]),#3
                    DIStatement("""ITEStatementImpl\nse il controllo ConsDef è uguale a FALSE ,  Applica gli effetti
       della macro MainClass_C1_macroef_M7  /*73,*/

 ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co1""", [
                    DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                    ]),#0
                    DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M7"""),#1
                    ]),#4
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
                         effect=(self.dbs[2], self.dbs[3], self.dbs[4], ),
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

        self.set_mainclass_c1_previousco_c2_prev(GlobalEnumeration.c180x)
        self.set_mainclass_c1_previousco_c3_prev(False)
        self.set_mainclass_c1_previousco_c4_prev(False)
        self.set_mainclass_c1_previousco_c5_prev(GlobalEnumeration.avanzamento)
        self.set_mainclass_c1_previousco_c6_prev(GlobalEnumeration.avanzamento)
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
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro MainClass_C1_macroef_M8   commento: {73,}
        
           
         commento: {38,}  se il contatore MainClass_C1_contatore_Co7 è  uguale a  commento: {53,} 11 commento: {36,} e  se il timer MainClass_C1_timer_T6 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  commento: {54,} 14 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  uguale a c270 commento: {36,} e  se il timer MainClass_C1_timer_T6 non è disattivo, commento: {69,}Disattiva il timer MainClass_C1_timer_T6
        
           
          se il controllo ConsDef è uguale a FALSE ,  Applica gli effetti
               della macro MainClass_C1_macroef_M7  commento: {73,}
        
         ,altrimenti  commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co1
        
        
        
        }
        """
        #  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  False  e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8
        if db((db(self.get_consdef() == False, self.dbs[2].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v8() == False, self.dbs[2].subs[0].subs[1].subs[0].subs[0]), self.dbs[2].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, self.dbs[2].subs[0].subs[1].subs[1])), self.dbs[2].subs[0].subs[1])), self.dbs[2].subs[0]):
            self.macroMainclass_c1_macroef_m8(self.dbs[2].subs[1])
        #  /*73,*/
        #     
        #   /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  uguale a  /*53,*/ 11 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  maggiore di  /*54,*/ 14 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  uguale a c270 /*36,*/ e  se il timer MainClass_C1_timer_T6 non è disattivo, /*69,*/Disattiva il timer MainClass_C1_timer_T6
        if db((db((db((db(self.get_mainclass_c1_contatore_co7().get_valore() == 11, self.dbs[3].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), self.dbs[3].subs[0].subs[0].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co1().get_valore() > 14, self.dbs[3].subs[0].subs[0].subs[1])), self.dbs[3].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p9() == True, self.dbs[3].subs[0].subs[1].subs[0].subs[0].subs[0]), self.dbs[3].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, self.dbs[3].subs[0].subs[1].subs[0].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[0].subs[1])), self.dbs[3].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), self.dbs[3].subs[0].subs[1].subs[1].subs[0]), self.dbs[3].subs[0].subs[1].subs[1])), self.dbs[3].subs[0].subs[1])), self.dbs[3].subs[0]):
            self.get_mainclass_c1_timer_t6().disattiva()
        #  se il controllo ConsDef è uguale a FALSE ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M7  /*73,*/
        #   ,altrimenti  /*70,*/Incrementa il contatore MainClass_C1_contatore_Co1
        if db(self.get_consdef() == False, self.dbs[4].subs[0]):
            self.macroMainclass_c1_macroef_m7(self.dbs[4].subs[1])
        else:
            self.get_mainclass_c1_contatore_co1().incrementa()
    
    # effect macros
    def macroMainclass_c1_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef è uguale a FALSE  commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 14021 commento: {35,} e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore 8
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 14021 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 14021 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( ( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (True)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) ) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_controllo_c1)  è uguale a  (True)) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co1)  è maggiore di  (14021)) )  e  
( (mainclass_c1_controllo_c1)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è maggiore di  (14021))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (14021)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef è uguale a FALSE  /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 14021 /*35,*/ e  se il controllo MainClass_C1_controllo_C1 è  uguale a  False , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore 8
        if db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 14021, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v6(8)
    
    def macroMainclass_c1_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  commento: {56,} 1345 o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C10 il valore avanzamento
        
           
          se la macro  MainClass_C1_macrova_M1 ( con argomento_a1   uguale a True ,argomento_a3   uguale a avviox ,argomento_a2   uguale a c180x ,argomento_a4   uguale a GialloxVerdex ,argomento_a9   uguale a RossoVerde ,argomento_a8   uguale a avviox  e argomento_a7   uguale a avanzamento )  non  è  uguale a avanzamento commento: {40,} ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V8 il valore  True  commento: {67,}
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1345 o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1345 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co7)  è uguale a  (1345)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (1345))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (1345)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\nse la macro  MainClass_C1_macrova_M1 ( con argomento_a1   uguale a True ,argomento_a3   uguale a avviox ,argomento_a2   uguale a c180x ,argomento_a4   uguale a GialloxVerdex ,argomento_a9   uguale a RossoVerde ,argomento_a8   uguale a avviox  e argomento_a7   uguale a avanzamento )  non  è  uguale a avanzamento /*40,*/ ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore  True""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M1 ( con argomento_a1   uguale a True ,argomento_a3   uguale a avviox ,argomento_a2   uguale a c180x ,argomento_a4   uguale a GialloxVerdex ,argomento_a9   uguale a RossoVerde ,argomento_a8   uguale a avviox  e argomento_a7   uguale a avanzamento )  non  è  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1')  è uguale a  (avanzamento)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m1'"""),#0
                            ]),#0
                            ]),#0
                            ]),#1
                ])

        populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1345 o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C10 il valore avanzamento
        if db((db(not db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 1345, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c10(GlobalEnumeration.avanzamento)
        #  se la macro  MainClass_C1_macrova_M1 ( con argomento_a1   uguale a True ,argomento_a3   uguale a avviox ,argomento_a2   uguale a c180x ,argomento_a4   uguale a GialloxVerdex ,argomento_a9   uguale a RossoVerde ,argomento_a8   uguale a avviox  e argomento_a7   uguale a avanzamento )  non  è  uguale a avanzamento /*40,*/ ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V8 il valore  True
        if db(not db(db(self.macroMainclass_c1_macrova_m1(True,GlobalEnumeration.c180x,GlobalEnumeration.avviox,GlobalEnumeration.gialloxverdex,GlobalEnumeration.avanzamento,GlobalEnumeration.avviox,GlobalEnumeration.rossoverde, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) == GlobalEnumeration.avanzamento, di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v8(True)
    
    def macroMainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  True  commento: {36,} e  se il timer MainClass_C1_timer_T6 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  commento: {54,} 5 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x,  Applica gli effetti
               della macro MainClass_C1_macroef_M7  commento: {73,}
        
           
          se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T6 è disattivo commento: {34,} e  se il parametro MainClass_C1_parametro_P1 non è  diverso da c270 commento: {34,} e  se il parametro MainClass_C1_parametro_P2 è  diverso da  commento: {56,} 4 commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  uguale a avanzamento,  Applica gli effetti
               della macro MainClass_C1_macroef_M7  commento: {73,}
        
           
          se la macro  MainClass_C1_macrova_M9 ( con argomento_a7   uguale a avviox ,argomento_a5   uguale a RossoGialloVerde ,argomento_a10   uguale a c270 ,argomento_a6   uguale a c180x ,argomento_a1   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a GialloxVerdex )  non  è  uguale a RossoVerde commento: {40,} , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore 2
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo,  Applica gli effetti
               della macro MainClass_C1_macroef_M7  commento: {73,}
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270,  Applica gli effetti
               della macro MainClass_C1_macroef_M7  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore 9
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x,  Applica gli effetti
       della macro MainClass_C1_macroef_M7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_parametro_p1)  è uguale a  (c270) )  o  
( ( ( (consdef)  è uguale a  (False) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v8)  è uguale a  (True))) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è attivo) ) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v8)  è uguale a  (True))) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di (negazione di ((mainclass_c1_variabile_v8)  è uguale a  (True))) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v8)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_parametro_p2)  è maggiore di  (5)) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (c180x))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p2)  è maggiore di  (5))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p2)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (c180x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c180x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M7"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*73,*/

   
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  diverso da c270 /*34,*/ e  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a avanzamento,  Applica gli effetti
       della macro MainClass_C1_macroef_M7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  diverso da c270 /*34,*/ e  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((stato_restore)  è uguale a  (state1)) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( il timer 'mainclass_c1_timer_t6' è inattivo )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270))) ) )  e  ( negazione di ((mainclass_c1_parametro_p2)  è uguale a  (4)) ) )  e  
( negazione di ((mainclass_c1_controllo_c8)  è uguale a  (avanzamento)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'mainclass_c1_timer_t6' è inattivo )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270))) ) )  e  ( negazione di ((mainclass_c1_parametro_p2)  è uguale a  (4)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_timer_t6' è inattivo )  e  ( negazione di (negazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270))) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p2)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p2)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M7"""),#1
                            ]),#1
                            DIStatement("""ITStatement\n/*73,*/

   
  se la macro  MainClass_C1_macrova_M9 ( con argomento_a7   uguale a avviox ,argomento_a5   uguale a RossoGialloVerde ,argomento_a10   uguale a c270 ,argomento_a6   uguale a c180x ,argomento_a1   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a GialloxVerdex )  non  è  uguale a RossoVerde /*40,*/ , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore 2""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M9 ( con argomento_a7   uguale a avviox ,argomento_a5   uguale a RossoGialloVerde ,argomento_a10   uguale a c270 ,argomento_a6   uguale a c180x ,argomento_a1   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a GialloxVerdex )  non  è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9')  è uguale a  (rossoverde)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9'"""),#0
                            ]),#0
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo,  Applica gli effetti
       della macro MainClass_C1_macroef_M7""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M7"""),#1
                            ]),#3
                            DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270,  Applica gli effetti
       della macro MainClass_C1_macroef_M7  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/

   
 /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_controllo_c8)  è uguale a  (avanzamento)) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (c180x))) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_controllo_c8)  è uguale a  (avanzamento)) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (c180x))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (c180x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (c180x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M7"""),#1
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  True  /*36,*/ e  se il timer MainClass_C1_timer_T6 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 5 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M7
        if db((db((db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p2() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroMainclass_c1_macroef_m7(di_ctx.subs[0].subs[1])
        #  /*73,*/
        #     
        #    se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T6 è disattivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 non è  diverso da c270 /*34,*/ e  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 4 /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  uguale a avanzamento,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M7
        if db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db((db((db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p2() == 4, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.macroMainclass_c1_macroef_m7(di_ctx.subs[1].subs[1])
        #  /*73,*/
        #     
        #    se la macro  MainClass_C1_macrova_M9 ( con argomento_a7   uguale a avviox ,argomento_a5   uguale a RossoGialloVerde ,argomento_a10   uguale a c270 ,argomento_a6   uguale a c180x ,argomento_a1   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a2   uguale a GialloxVerdex )  non  è  uguale a RossoVerde /*40,*/ , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore 2
        if db(not db(db(self.macroMainclass_c1_macrova_m9(GlobalEnumeration.c180,GlobalEnumeration.c270,GlobalEnumeration.gialloxverdex,GlobalEnumeration.rossogialloverde,GlobalEnumeration.rossogialloverde,GlobalEnumeration.c180x,GlobalEnumeration.avviox, di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) == GlobalEnumeration.rossoverde, di_ctx.subs[2].subs[0].subs[0]), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v6(2)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M7
        if db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[3].subs[0].subs[0]), di_ctx.subs[3].subs[0]):
            self.macroMainclass_c1_macroef_m7(di_ctx.subs[3].subs[1])
        #  /*73,*/
        #     
        #   /*35,*/  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  diverso da c180x o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M7  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore 9
        if db((db((db((db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c180x, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[4].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.macroMainclass_c1_macroef_m7(di_ctx.subs[4].subs[1])
        else:
            self.set_mainclass_c1_variabile_v6(9)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m2")
    def macroMainclass_c1_macrove_m2(self, argomento_ave4, argomento_ave5, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {34,}  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,}, Tutte le seguenti { 
         commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T6 è attivo commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  minore di  commento: {55,} 4 o  se l'argomento argomento_ave4 non  è  uguale a c270 commento: {39,} , Solo una delle seguenti { 
         commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 14 commento: {36,} o  se il timer MainClass_C1_timer_T6 è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   commento: {47,49,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  commento: {54,} 102
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T6 sia scaduto
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia scaduto
        
        
         } Verifica che   commento: {47,48,50,}  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  uguale a avanzamento
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a c270 /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto


 } Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a avanzamento""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/, Tutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a c270 /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto


 } Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a c270 /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto


 } Verifica che   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a c270 /*39,*/ , Solo una delle seguenti { 
 /*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 4 o  se l'argomento argomento_ave4 non  è  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è attivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 4""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 non  è  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo, Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14 /*36,*/ o  se il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P1 è  uguale a c270 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P1 è  uguale a c270""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T6 è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 102""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (102)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T6 sia scaduto""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T6 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 sia  uguale a avanzamento""", [
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v6() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(argomento_ave4 == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co7().get_valore() > 102, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m3")
    def macroMainclass_c1_macrove_m3(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,}, Solo una delle seguenti { 
         commento: {62,}  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P2 è  minore di  commento: {55,} 1 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  commento: {56,} 1150213 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 124, Almeno una delle seguenti { 
         commento: {63,}  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,} commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
         commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  commento: {56,} 135 commento: {36,} e  se il timer MainClass_C1_timer_T6 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 commento: {35,} o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x commento: {34,} o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  commento: {56,} 10 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
         commento: {63,} commento: {34,}  se il parametro MainClass_C1_parametro_P2 è  uguale a  commento: {53,} 8 commento: {34,} e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 120213 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 14, Solo una delle seguenti { 
         commento: {63,} commento: {36,}  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
         commento: {61,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto commento: {37,} e  se la variabile MainClass_C1_variabile_V6 è  diverso da  commento: {56,} 9 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
         commento: {63,} commento: {38,}  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  commento: {53,} 14 commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  commento: {54,} 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  commento: {54,} 11 o  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  minore di  commento: {55,} 10 commento: {38,} o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  commento: {55,} 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
         commento: {62,}  se il controllo ConsDef è uguale a FALSE  commento: {34,} o  se il parametro MainClass_C1_parametro_P2 è  diverso da  commento: {56,} 9 commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  minore di  commento: {55,} 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
          se il controllo ConsDef è uguale a FALSE , Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,48,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  commento: {56,} 12
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  commento: {54,} 13
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
        
        
         } Verifica che   commento: {48,49,50,51,}  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  maggiore di  commento: {54,} 5
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 1150213
         commento: {104,} e  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 non sia  diverso da  commento: {56,} 8
        
        
         } Verifica che   commento: {47,48,50,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 sia  maggiore di  commento: {54,} 7
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  minore di  commento: {55,} 14
        
        
         } Verifica che   commento: {47,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  minore di  commento: {55,} 14
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270
        
        
         } Verifica che   commento: {47,49,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P2 sia  maggiore di  commento: {54,} 6
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  commento: {53,} 1
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 102
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
        
        
         } Verifica che   commento: {48,51,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  diverso da  commento: {56,} 11
         commento: {104,} e  che  commento: {38,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 1113
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x
        
        
         } Verifica che   commento: {47,49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  uguale a  commento: {53,} 13
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P2 sia  minore di  commento: {55,} 6
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V6 sia  minore di  commento: {55,} 10
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V6 sia  maggiore di  commento: {54,} 3
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 non sia attivo
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {,}  il timer MainClass_C1_timer_T6 non sia scaduto
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia attivo
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia disattivo
         commento: {104,} o  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 sia  uguale a  False 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/, Solo una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124, Almeno una delle seguenti { 
 /*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x


 } Verifica che   /*47,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo


 } Verifica che   /*47,48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/, Solo una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124, Almeno una delle seguenti { 
 /*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x


 } Verifica che   /*47,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124, Almeno una delle seguenti { 
 /*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x


 } Verifica che   /*47,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124, Almeno una delle seguenti { 
 /*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213""", [
                            DIBoolExpr("""LessThanImpl\nil parametro MainClass_C1_parametro_P2 è  minore di  /*55,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 è  diverso da  /*56,*/ 1150213""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (1150213)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (124)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/ /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 } Verifica che   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Solo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 /*35,*/ o  se il controllo MainClass_C1_controllo_C7 non è  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135 /*36,*/ e  se il timer MainClass_C1_timer_T6 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  diverso da  /*56,*/ 135""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (135))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (135)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  uguale a c180x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P2 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p2)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p2)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 } Verifica che   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14, Solo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8 /*34,*/ e  se il parametro MainClass_C1_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\nil parametro MainClass_C1_parametro_P2 è  uguale a  /*53,*/ 8""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 120213""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (120213)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 14""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto, Solo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 }""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T6 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x, Tutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto /*37,*/ e  se la variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti4_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo MainClass_C1_controllo_C1 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a c180x""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C1 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C7 è  uguale a c180x""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 } Verifica che   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True  /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14 /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo MainClass_C1_controllo_C1 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P2 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p2)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 } Verifica che   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11 o  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 è  diverso da  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v6)  è minore di  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  minore di  /*55,*/ 124""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co7)  è minore di  (124)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 } Verifica che   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270, Tutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ o  se il parametro MainClass_C1_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P1 è  diverso da c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE , Almeno una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9 o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9 /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef è uguale a FALSE  /*34,*/ o  se il parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P2 è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p2)  è uguale a  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile MainClass_C1_variabile_V6 è  minore di  /*55,*/ 9""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef è uguale a FALSE , Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co1)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (12)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co7 non sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V8 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  uguale a c270""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*48,49,50,51,*/  /*,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 5""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C8 sia  diverso da avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213
 /*104,*/ e  che  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1150213""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (1150213)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V6 non sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6)  è uguale a  (8))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 7""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C1 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  minore di  /*55,*/ 14""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P1 non sia  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  maggiore di  /*54,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  uguale a  /*53,*/ 1""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co1)  è uguale a  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 102""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,51,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11
 /*104,*/ e  che  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C8 non sia  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 1113""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (1113)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*48,*/  /*,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a c180x""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  uguale a  /*53,*/ 13""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\nche  /*34,*/  il parametro MainClass_C1_parametro_P2 sia  minore di  /*55,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V6 sia  minore di  /*55,*/ 10""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""GreaterThanImpl\nche  /*37,*/  la variabile MainClass_C1_variabile_V6 sia  maggiore di  /*54,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T6 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia scaduto
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,*/  /*,*/  il timer MainClass_C1_timer_T6 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V8 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_parametro_p2() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 1150213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 135, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p2() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_mainclass_c1_parametro_p2() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() > 120213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() > 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_mainclass_c1_restoreti_ti4_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v6() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p2() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co7().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v6() < 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() < 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p2() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v6() < 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co7().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db((db(self.get_mainclass_c1_variabile_v6() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 1150213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_variabile_v6() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v6() > 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co7().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_mainclass_c1_contatore_co7().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(self.get_mainclass_c1_parametro_p2() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_mainclass_c1_contatore_co7().get_valore() > 102, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 1113, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(self.get_mainclass_c1_contatore_co7().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_parametro_p2() < 6, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v6() < 10, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(self.get_mainclass_c1_variabile_v6() > 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db((db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m5")
    def macroMainclass_c1_macrove_m5(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {62,} commento: {38,}  se il contatore MainClass_C1_contatore_Co7 è  minore di  commento: {55,} 1113 commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  minore di  commento: {55,} 10 commento: {37,} o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  commento: {54,} 2 commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  commento: {56,} 1145, Almeno una delle seguenti { 
         commento: {36,}  se il timer MainClass_C1_timer_T6 non è disattivo commento: {35,} e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento commento: {35,} e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  commento: {38,} e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  commento: {54,} 15021 commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Verifica che   commento: {47,48,49,51,}  commento: {34,}  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  commento: {54,} 14
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T6 non sia attivo
         commento: {104,} e  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 sia attivo
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x
        
        
         } Verifica che   commento: {48,49,51,}  commento: {,}  il timer MainClass_C1_timer_T6 sia attivo
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co1 non sia  minore di  commento: {55,} 15
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T6 non sia attivo
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 1113 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1145, Almeno una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T6 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15021 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Verifica che   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x


 } Verifica che   /*48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 1113 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1145, Almeno una delle seguenti { 
 /*36,*/  se il timer MainClass_C1_timer_T6 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15021 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Verifica che   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 1113 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10 /*37,*/ o  se la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1145""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 1113 /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\nil contatore MainClass_C1_contatore_Co7 è  minore di  /*55,*/ 1113""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 non è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v6)  è minore di  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1145""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V6 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V8 non è  diverso da  False  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V8 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V6 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_variabile_v6)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co7 non è  diverso da  /*56,*/ 1145""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co7)  è uguale a  (1145))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co7)  è uguale a  (1145)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer MainClass_C1_timer_T6 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15021 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  True , Verifica che   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T6 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15021 /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T6 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True  /*38,*/ e  se il contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15021""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T6 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento /*35,*/ e  se il controllo MainClass_C1_controllo_C1 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T6 non è disattivo /*35,*/ e  se il controllo MainClass_C1_controllo_C8 è  diverso da avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T6 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C8 è  diverso da avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C1 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c1)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co1 non è  maggiore di  /*54,*/ 15021""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co1)  è maggiore di  (15021)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,51,*/  /*34,*/  il parametro MainClass_C1_parametro_P1 sia  uguale a c270""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co7 sia  maggiore di  /*54,*/ 14""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T6 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer MainClass_C1_timer_T6 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  uguale a c180x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (c180x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 15
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 sia attivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,51,*/  /*,*/  il timer MainClass_C1_timer_T6 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co1 non sia  minore di  /*55,*/ 15""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T6 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_mainclass_c1_contatore_co7().get_valore() < 1113, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v6() < 10, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db((db(not db(not db(self.get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v6() > 2, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_contatore_co7().get_valore() == 1145, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db((db((db(not db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c8() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co1().get_valore() > 15021, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db((db(self.get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co7().get_valore() > 14, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == GlobalEnumeration.c180x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co1().get_valore() < 15, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t6().isAttivato(), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m1")
    def macroMainclass_c1_macrova_m1(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è attivo   commento: {38,} o  se il contatore MainClass_C1_contatore_Co1 è  minore di  commento: {55,} 1245  , assegna alla macro il valore avanzamento
        
         commento: {46,} assegna alla macro il valore avanzamento commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è attivo   /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1245  , assegna alla macro il valore avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è attivo   /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1245""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti4_restore' è attivo""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co1)  è minore di  (1245)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI4 è attivo   /*38,*/ o  se il contatore MainClass_C1_contatore_Co1 è  minore di  /*55,*/ 1245  , assegna alla macro il valore avanzamento
        if db((db(self.get_mainclass_c1_restoreti_ti4_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co1().get_valore() < 1245, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.avanzamento
        #  /*46,*/ assegna alla macro il valore avanzamento
        return GlobalEnumeration.avanzamento
    
    @srf_value_macro("macroMainclass_c1_macrova_m10")
    def macroMainclass_c1_macrova_m10(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {36,}  se il timer MainClass_C1_timer_T6 è scaduto commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a  True  commento: {35,} o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef è uguale a FALSE  commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto e  se il controllo ConsDef è uguale a FALSE  , assegna alla macro il valore RossoVerde
        
         commento: {46,} assegna alla macro il valore RossoVerde commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef è uguale a FALSE  /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto e  se il controllo ConsDef è uguale a FALSE  , assegna alla macro il valore RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef è uguale a FALSE  /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto e  se il controllo ConsDef è uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( il timer 'mainclass_c1_timer_t6' è scaduto )  o  
( negazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (True)) ) )  o  
( ( (mainclass_c1_controllo_c1)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( il timer 'mainclass_c1_timer_t6' è scaduto )  o  
( negazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (True)) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv2_restore)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_controllo_c1)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_restoreti_ti2_restore' è scaduto )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m10_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*36,*/  se il timer MainClass_C1_timer_T6 è scaduto /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV2 non è  uguale a  True  /*35,*/ o  se il controllo MainClass_C1_controllo_C1 è  uguale a  False  e  se il controllo ConsDef è uguale a FALSE  /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto e  se il controllo ConsDef è uguale a FALSE  , assegna alla macro il valore RossoVerde
        if db((db((db((db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_restoreva_rv2_restore() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_controllo_c1() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_restoreti_ti2_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossoverde
        #  /*46,*/ assegna alla macro il valore RossoVerde
        return GlobalEnumeration.rossoverde
    
    @srf_value_macro("macroMainclass_c1_macrova_m4")
    def macroMainclass_c1_macrova_m4(self, argomento_a1, argomento_a10, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} e  se il contatore MainClass_C1_contatore_Co7 è  maggiore di  commento: {54,} 12213 , assegna alla macro il valore c270
        
         commento: {46,} assegna alla macro il valore c270 commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  maggiore di  /*54,*/ 12213 , assegna alla macro il valore c270""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  maggiore di  /*54,*/ 12213""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co7)  è maggiore di  (12213)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ e  se il contatore MainClass_C1_contatore_Co7 è  maggiore di  /*54,*/ 12213 , assegna alla macro il valore c270
        if db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co7().get_valore() > 12213, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c270
        #  /*46,*/ assegna alla macro il valore c270
        return GlobalEnumeration.c270
    
    @srf_value_macro("macroMainclass_c1_macrova_m9")
    def macroMainclass_c1_macrova_m9(self, argomento_a1, argomento_a10, argomento_a2, argomento_a3, argomento_a5, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  , assegna alla macro il valore RossoVerde
        
         commento: {46,} assegna alla macro il valore RossoVerde commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  , assegna alla macro il valore RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C1 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo MainClass_C1_controllo_C1 non è  uguale a  True  , assegna alla macro il valore RossoVerde
        if db(not db(self.get_mainclass_c1_controllo_c1() == True, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossoverde
        #  /*46,*/ assegna alla macro il valore RossoVerde
        return GlobalEnumeration.rossoverde
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm10(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm10')
    
    def eventMainclass_c1_command_comm3DaSender216acb09(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm3DaSender216acb09')
    
    def eventMainclass_c1_command_comm5(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm5')
    
    def eventMainclass_c1_command_comm7(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm7')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm4(self, notifying_process, argomento_ave4, argomento_ave9):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm4', argomento_ave4=argomento_ave4, argomento_ave9=argomento_ave9)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c3_prev(self.get_mainclass_c1_previousco_c3())
        self.set_mainclass_c1_previousco_c4_prev(self.get_mainclass_c1_previousco_c4())
        self.set_mainclass_c1_previousco_c5_prev(self.get_mainclass_c1_previousco_c5())
        self.set_mainclass_c1_previousco_c6_prev(self.get_mainclass_c1_previousco_c6())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())
        self.set_mainclass_c1_previousva_pv3_prev(self.get_mainclass_c1_previousva_pv3())
        self.set_mainclass_c1_previousva_pv4_prev(self.get_mainclass_c1_previousva_pv4())

