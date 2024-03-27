# Codice del modello 'TestCase18', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_subclass_c2_restoreva_rv1(False)
        self.set_subclass_c2_restoreva_rv2(GlobalEnumeration.rosso)
        self.set_subclass_c2_restoreva_rv3(0)
        self.set_subclass_c2_restoreva_rv4(False)
        self.set_subclass_c2_variabile_v10(GlobalEnumeration.c120)
        self.set_subclass_c2_variabile_v5(False)
        self.set_subclass_c2_variabile_v9(GlobalEnumeration.c270)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
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
        _State1__State1__stateSheet_0__permanence = 1

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, subclass_c2_lista_l3, subclass_c2_lista_l6, subclass_c2_lista_l9, subclass_c2_parametro_p10, subclass_c2_parametro_p2, subclass_c2_parametro_p3, subclass_c2_parametro_p6, subclass_c2_parametro_p7):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l3(subclass_c2_lista_l3)
        self.set_subclass_c2_lista_l6(subclass_c2_lista_l6)
        self.set_subclass_c2_lista_l9(subclass_c2_lista_l9)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p10(subclass_c2_parametro_p10)
        self.set_subclass_c2_parametro_p2(subclass_c2_parametro_p2)
        self.set_subclass_c2_parametro_p3(subclass_c2_parametro_p3)
        self.set_subclass_c2_parametro_p6(subclass_c2_parametro_p6)
        self.set_subclass_c2_parametro_p7(subclass_c2_parametro_p7)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(40413000)
        self.set_subclass_c2_restoreti_ti1_restore(40413000)
        self.set_subclass_c2_restoreti_ti2(325000)
        self.set_subclass_c2_restoreti_ti2_restore(325000)
        self.set_subclass_c2_restoreti_ti3(204000)
        self.set_subclass_c2_restoreti_ti3_restore(204000)
        self.set_subclass_c2_restoreti_ti4(4000)
        self.set_subclass_c2_restoreti_ti4_restore(4000)
        self.set_subclass_c2_timer_t1(55000)
        self.set_subclass_c2_timer_t3(3000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_restoreti_ti3,self.subclass_c2_restoreti_ti3_restore,self.subclass_c2_restoreti_ti4,self.subclass_c2_restoreti_ti4_restore,self.subclass_c2_timer_t1,self.subclass_c2_timer_t3,]

        # initialize the counters
        self.set_subclass_c2_contatore_co2(0)
        self.set_subclass_c2_contatore_co4(0)
        self.set_subclass_c2_contatore_co8(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l3(self, subclass_c2_lista_l3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3",subclass_c2_lista_l3)

    def set_subclass_c2_lista_l6(self, subclass_c2_lista_l6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l6",subclass_c2_lista_l6)

    def set_subclass_c2_lista_l9(self, subclass_c2_lista_l9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9",subclass_c2_lista_l9)


    # getters for record type parameters
    def get_subclass_c2_lista_l3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l3")

    def get_subclass_c2_lista_l6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l6")

    def get_subclass_c2_lista_l9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l9")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p10(self, subclass_c2_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p10",subclass_c2_parametro_p10)

    def set_subclass_c2_parametro_p2(self, subclass_c2_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2",subclass_c2_parametro_p2)

    def set_subclass_c2_parametro_p3(self, subclass_c2_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p3",subclass_c2_parametro_p3)

    def set_subclass_c2_parametro_p6(self, subclass_c2_parametro_p6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6",subclass_c2_parametro_p6)

    def set_subclass_c2_parametro_p7(self, subclass_c2_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7",subclass_c2_parametro_p7)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p10")

    def get_subclass_c2_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2")

    def get_subclass_c2_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p3")

    def get_subclass_c2_parametro_p6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p6")

    def get_subclass_c2_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p7")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c1(self, subclass_c2_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c1",subclass_c2_comando_c1)

    def set_subclass_c2_comando_c5(self, subclass_c2_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c5",subclass_c2_comando_c5)

    def set_subclass_c2_comando_c6(self, subclass_c2_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c6",subclass_c2_comando_c6)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c1")

    def get_subclass_c2_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c4")

    def get_subclass_c2_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c6")

    def get_subclass_c2_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c9")

    def get_subclass_c2_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10")

    def get_subclass_c2_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c2")

    def get_subclass_c2_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c3")

    def get_subclass_c2_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7")

    def get_subclass_c2_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c8")


    # setters for state variables
    def set_subclass_c2_previousco_c10_prev(self, subclass_c2_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev",subclass_c2_previousco_c10_prev)
    def set_subclass_c2_previousco_c2_prev(self, subclass_c2_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c2_prev",subclass_c2_previousco_c2_prev)
    def set_subclass_c2_previousco_c3_prev(self, subclass_c2_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c3_prev",subclass_c2_previousco_c3_prev)
    def set_subclass_c2_previousco_c7_prev(self, subclass_c2_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7_prev",subclass_c2_previousco_c7_prev)
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
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_restoreva_rv3(self, subclass_c2_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3",subclass_c2_restoreva_rv3)
    def set_subclass_c2_restoreva_rv4(self, subclass_c2_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv4",subclass_c2_restoreva_rv4)
    def set_subclass_c2_variabile_v10(self, subclass_c2_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v10",subclass_c2_variabile_v10)
    def set_subclass_c2_variabile_v5(self, subclass_c2_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5",subclass_c2_variabile_v5)
    def set_subclass_c2_variabile_v9(self, subclass_c2_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9",subclass_c2_variabile_v9)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev")

    def get_subclass_c2_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c2_prev")

    def get_subclass_c2_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c3_prev")

    def get_subclass_c2_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7_prev")

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

    def get_subclass_c2_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv4")

    def get_subclass_c2_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv4_restore")

    def get_subclass_c2_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v10")

    def get_subclass_c2_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v5")

    def get_subclass_c2_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v9")


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

    def set_subclass_c2_timer_t3(self, timerDuration):
        self.subclass_c2_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t3", self.memory)


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

    def get_subclass_c2_timer_t3(self):
        return self.subclass_c2_timer_t3


    # setters for counters
    def set_subclass_c2_contatore_co2(self, counterInitValue):
        self.subclass_c2_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co2", self.memory)

    def set_subclass_c2_contatore_co4(self, counterInitValue):
        self.subclass_c2_contatore_co4 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co4", self.memory)

    def set_subclass_c2_contatore_co8(self, counterInitValue):
        self.subclass_c2_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co8", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co2(self):
        return self.subclass_c2_contatore_co2

    def get_subclass_c2_contatore_co4(self):
        return self.subclass_c2_contatore_co4

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

        self.set_subclass_c2_previousco_c10_prev(True)
        self.set_subclass_c2_previousco_c2_prev(GlobalEnumeration.gialloverde)
        self.set_subclass_c2_previousco_c3_prev(False)
        self.set_subclass_c2_previousco_c7_prev(GlobalEnumeration.giallogiallo)
        self.set_subclass_c2_previousco_c8_prev(GlobalEnumeration.spento)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())

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
    def macroSubclass_c2_macroef_m10(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer SubClass_C2_timer_T1 non è disattivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 14, commento: {69,}Disattiva il timer SubClass_C2_timer_T1
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        
        
         commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  commento: {105,} è  maggiore di  commento: {54,} 5 commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  commento: {54,} 115 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  diverso da  commento: {56,} 6, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        
         ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V10 il valore spento commento: {67,}
        
        
         commento: {44,}  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T1 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 11 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  commento: {53,} 12041, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C2_timer_T3
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 1332 commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  commento: {53,} 155 commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 1, commento: {68,}Attiva il timer SubClass_C2_timer_T1
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 14, /*69,*/Disattiva il timer SubClass_C2_timer_T1

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co2)  è minore di  (14)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 115 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  /*56,*/ 6, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo

 ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V10 il valore spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 115 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è maggiore di  (5))}""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co8)  è maggiore di  (115)) )  e  
( negazione di ((subclass_c2_parametro_p6)  è uguale a  (6)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co8)  è maggiore di  (115))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co8)  è maggiore di  (115)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*67,*/


 /*44,*/  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 11 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 12041, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/


 /*44,*/  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 11 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 12041""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(negazione di ((mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (10)))} )  e  
( (subclass_c2_variabile_v5)  è uguale a  (False) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (10)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c2_timer_t1' è scaduto) )  e  ( (subclass_c2_contatore_co4)  è maggiore di  (11) ) )  e  
( (subclass_c2_contatore_co8)  è uguale a  (12041) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c2_timer_t1' è scaduto) )  e  ( (subclass_c2_contatore_co4)  è maggiore di  (11) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t1' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co4)  è maggiore di  (11)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (12041)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 1332 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 155 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 1, /*68,*/Attiva il timer SubClass_C2_timer_T1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 1332 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 155 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( (subclass_c2_contatore_co4)  è maggiore di  (1332) ) )  e  ( (subclass_c2_contatore_co8)  è uguale a  (155) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( (subclass_c2_contatore_co4)  è maggiore di  (1332) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co4)  è maggiore di  (1332)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (155)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p3)  è minore di  (1)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m10_SrfMacroDefInfo(di_ctx)
        #  /*36,*/  se il timer SubClass_C2_timer_T1 non è disattivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 14, /*69,*/Disattiva il timer SubClass_C2_timer_T1
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        if db((db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co2().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_timer_t1().disattiva()
        else:
            self.set_subclass_c2_comando_c5(GlobalEnumeration.giallogiallo)
        #  /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 esiste e  /*105,*/ è  maggiore di  /*54,*/ 5 /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  maggiore di  /*54,*/ 115 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  diverso da  /*56,*/ 6, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        #   ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V10 il valore spento
        if db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() > 5, di_ctx.subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co8().get_valore() > 115, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() == 6, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_comando_c5(GlobalEnumeration.giallogiallo)
        else:
            self.set_subclass_c2_variabile_v10(GlobalEnumeration.spento)
        #  /*67,*/
        #   /*44,*/  se  MainClass_C1_variabile_V2 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T1 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 11 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 12041, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C2_timer_T3
        if db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v2() == 10, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[2].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v5() == False, di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co4().get_valore() > 11, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co8().get_valore() == 12041, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_contatore_co8().decrementa()
        else:
            self.get_subclass_c2_timer_t3().disattiva()
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 1332 /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 è  uguale a  /*53,*/ 155 /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 1, /*68,*/Attiva il timer SubClass_C2_timer_T1
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co4().get_valore() > 1332, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co8().get_valore() == 155, di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p3() < 1, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c2_timer_t1().attiva()
    
    def macroSubclass_c2_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 non è  uguale a  commento: {53,} 4 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x commento: {37,} o  se la variabile SubClass_C2_variabile_V10 non è  diverso da spento commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 11, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        
           
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  e  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da spento /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 11, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da spento /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_parametro_p3)  è uguale a  (4)) ) )  o  
( negazione di ((subclass_c2_parametro_p2)  è uguale a  (giallogiallo)) ) )  o  
( negazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x))) ) )  o  
( negazione di (negazione di ((subclass_c2_variabile_v10)  è uguale a  (spento))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_parametro_p3)  è uguale a  (4)) ) )  o  
( negazione di ((subclass_c2_parametro_p2)  è uguale a  (giallogiallo)) ) )  o  
( negazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_parametro_p3)  è uguale a  (4)) ) )  o  
( negazione di ((subclass_c2_parametro_p2)  è uguale a  (giallogiallo)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((subclass_c2_parametro_p3)  è uguale a  (4)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p3)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (giallogiallo))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v10)  è uguale a  (spento)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v10)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co8)  è uguale a  (11)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co8)  è uguale a  (11))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l3')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 non è  uguale a  /*53,*/ 4 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x /*37,*/ o  se la variabile SubClass_C2_variabile_V10 non è  diverso da spento /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 11, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        if db((db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p3() == 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c5(GlobalEnumeration.giallogiallo)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  e  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8
        if db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c2_contatore_co8().decrementa()
    
    def macroSubclass_c2_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 9 commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  commento: {54,} 11 commento: {37,} e  se la variabile SubClass_C2_variabile_V9 non è  uguale a c120x commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  commento: {53,} 13041, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V9 il valore c120x
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M10  commento: {73,}
        
        
          se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a4   uguale a c120x  e argomento_a3   uguale a GialloVerde )   è  diverso da c120x commento: {40,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        
           
         commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è  diverso da avanzamento, commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co8
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M10  commento: {73,}
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P7 è  minore di  commento: {55,} 5 commento: {38,} e  se il contatore SubClass_C2_contatore_Co4 è  minore di  commento: {55,} 1532, commento: {68,}Attiva il timer SubClass_C2_timer_T1
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 11 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a c120x /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 13041, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore c120x

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 11 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a c120x /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 13041""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l6' è inattivo)} )  e  
( (subclass_c2_parametro_p3)  è minore di  (9) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l6' è inattivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l6' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p3)  è minore di  (9)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (subclass_c2_contatore_co4)  è maggiore di  (11) )  e  ( negazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x)) ) )  e  ( negazione di ((subclass_c2_controllo_c6)  è uguale a  (spento)) ) )  e  
( (subclass_c2_contatore_co4)  è uguale a  (13041) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (subclass_c2_contatore_co4)  è maggiore di  (11) )  e  ( negazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x)) ) )  e  ( negazione di ((subclass_c2_controllo_c6)  è uguale a  (spento)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_contatore_co4)  è maggiore di  (11) )  e  ( negazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co4)  è maggiore di  (11)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (13041)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M10"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*73,*/


  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a4   uguale a c120x  e argomento_a3   uguale a GialloVerde )   è  diverso da c120x /*40,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


  se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a4   uguale a c120x  e argomento_a3   uguale a GialloVerde )   è  diverso da c120x /*40,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m1')  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c2_macrova_m1')  è uguale a  (c120x)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c2_macrova_m1'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da avanzamento, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M10""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da avanzamento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (avanzamento))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M10"""),#1
                            ]),#2
                            DIStatement("""ITStatement\n/*73,*/


 /*34,*/  se il parametro SubClass_C2_parametro_P7 è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 1532, /*68,*/Attiva il timer SubClass_C2_timer_T1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/


 /*34,*/  se il parametro SubClass_C2_parametro_P7 è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 1532""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p7)  è minore di  (5)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co4)  è minore di  (1532)""", [
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 9 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 è  maggiore di  /*54,*/ 11 /*37,*/ e  se la variabile SubClass_C2_variabile_V9 non è  uguale a c120x /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  uguale a  /*53,*/ 13041, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V9 il valore c120x
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M10
        if db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p3() < 9, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_contatore_co4().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co4().get_valore() == 13041, di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v9(GlobalEnumeration.c120x)
        else:
            self.macroSubclass_c2_macroef_m10(di_ctx.subs[0].subs[1])
        #  /*73,*/
        #    se la macro  SubClass_C2_macrova_M1 ( con argomento_a2   uguale a True ,argomento_a4   uguale a c120x  e argomento_a3   uguale a GialloVerde )   è  diverso da c120x /*40,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V9 non è  diverso da c120x, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        if db((db(not db(db(self.macroSubclass_c2_macrova_m1(True,GlobalEnumeration.gialloverde,GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_comando_c5(GlobalEnumeration.giallogiallo)
        #  /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è  diverso da avanzamento, /*71,*/Decrementa il contatore SubClass_C2_contatore_Co8
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M10
        if db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[2].subs[0].subs[0].subs[0][idx]), di_ctx.subs[2].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_contatore_co8().decrementa()
        else:
            self.macroSubclass_c2_macroef_m10(di_ctx.subs[2].subs[1])
        #  /*73,*/
        #   /*34,*/  se il parametro SubClass_C2_parametro_P7 è  minore di  /*55,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co4 è  minore di  /*55,*/ 1532, /*68,*/Attiva il timer SubClass_C2_timer_T1
        if db((db(self.get_subclass_c2_parametro_p7() < 5, di_ctx.subs[3].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co4().get_valore() < 1532, di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c2_timer_t1().attiva()
    
    def macroSubclass_c2_macroef_m5(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {35,}  se il controllo SubClass_C2_controllo_C1 è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , commento: {71,}Decrementa il contatore SubClass_C2_contatore_Co4
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*35,*/  se il controllo SubClass_C2_controllo_C1 è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C2_controllo_C1 è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c2_controllo_c1)  è uguale a  (spento) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (spento)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m5_SrfMacroDefInfo(di_ctx)
        #  /*35,*/  se il controllo SubClass_C2_controllo_C1 è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE , /*71,*/Decrementa il contatore SubClass_C2_contatore_Co4
        if db((db((db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co4().decrementa()
    
    def macroSubclass_c2_macroef_m7(self, argomento_af10, argomento_af6, argomento_af7, argomento_af8, argomento_af9, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a avanzamentox o  se l'argomento argomento_af10 non  è  uguale a GialloVerde commento: {39,}  commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 4, commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C6 il valore  True 
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a avanzamentox o  se l'argomento argomento_af10 non  è  uguale a GialloVerde /*39,*/  /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 4, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a avanzamentox o  se l'argomento argomento_af10 non  è  uguale a GialloVerde /*39,*/  /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( per ognuna delle seguenti {((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (avanzamentox))} )  o  
( negazione di ((argomento_af10)  è uguale a  (gialloverde)) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (avanzamentox))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af10)  è uguale a  (gialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af10)  è uguale a  (gialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p3)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  /*41,*/  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  uguale a avanzamentox o  se l'argomento argomento_af10 non  è  uguale a GialloVerde /*39,*/  /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 4, /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore GialloGiallo
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C6 il valore  True
        if db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_af10 == GlobalEnumeration.gialloverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p3() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c5(GlobalEnumeration.giallogiallo)
        else:
            self.set_subclass_c2_comando_c6(True)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m2")
    def macroSubclass_c2_macrove_m2(self, argomento_ave1, argomento_ave10, argomento_ave6, argomento_ave7, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P10 è  uguale a spento,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è attivo, commento: {88,} quando  commento: {44,}    MainClass_C1_variabile_V8 del campo  MainClass_C1     commento: {105,} è  diverso da  commento: {56,} 2 commento: {35,} o  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento commento: {34,} e  se il parametro SubClass_C2_parametro_P10 non è  diverso da spento, Tutte le seguenti { 
         commento: {44,}  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento, Verifica che   commento: {47,49,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
         commento: {104,} e  che   l'argomento argomento_ave7 sia  uguale a  False  commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T3 non sia scaduto
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo
        
        
         } Verifica che   commento: {47,48,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  maggiore di  commento: {54,} 3
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
         commento: {104,} e  che   l'argomento argomento_ave10 sia  uguale a  False  commento: {,} 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P10 è  uguale a spento,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento /*34,*/ e  se il parametro SubClass_C2_parametro_P10 non è  diverso da spento, Tutte le seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento, Verifica che   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo


 } Verifica che   /*47,48,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che   l'argomento argomento_ave10 sia  uguale a  False""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P10 è  uguale a spento,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento /*34,*/ e  se il parametro SubClass_C2_parametro_P10 non è  diverso da spento, Tutte le seguenti { 
 /*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento, Verifica che   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P10 è  uguale a spento,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 2 /*35,*/ o  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento /*34,*/ e  se il parametro SubClass_C2_parametro_P10 non è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P10 è  uguale a spento,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P10 è  uguale a spento""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è attivo, /*88,*/ quando  /*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (2))) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)""", [
                            DIBoolExpr("""Operatore Logico Not\n/*44,*/    MainClass_C1_variabile_V8 del campo  MainClass_C1     /*105,*/ è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C6 non è  uguale a spento /*34,*/ e  se il parametro SubClass_C2_parametro_P10 non è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 non è  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P10 non è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p10)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento, Verifica che   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave7 sia  uguale a  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave7 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave7 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  uguale a GialloGiallo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che   l'argomento argomento_ave10 sia  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  maggiore di  /*54,*/ 3
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p3)  è maggiore di  (3)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave10 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_subclass_c2_parametro_p10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_subclass_c2_variabile_v10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(argomento_ave7 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(not db(self.get_subclass_c2_parametro_p3() > 3, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(argomento_ave10 == False, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m3")
    def macroSubclass_c2_macrove_m3(self, argomento_ave2, argomento_ave5, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 1532,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  commento: {55,} 6 commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  uguale a  commento: {53,} 13 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è attivo o  se l'argomento argomento_ave5 è  diverso da c120x commento: {39,}  commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo commento: {37,} e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Solo una delle seguenti { 
         commento: {61,} commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {37,} e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  commento: {35,} o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 8, Tutte le seguenti { 
         commento: {45,}  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,} 12504 commento: {35,} o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento commento: {35,} o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  commento: {38,} o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  commento: {56,} 121, Verifica che   commento: {49,51,52,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia attivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T1 sia attivo
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  commento: {56,} 153
         commento: {104,} o  che   l'argomento argomento_ave5 sia  uguale a c120x commento: {,} 
         commento: {104,} o  che   l'argomento argomento_ave5 non  sia  uguale a c120x commento: {39,} 
         commento: {104,} e  che   l'argomento argomento_ave5 sia  uguale a c120x commento: {39,} 
        
        
         } Verifica che   commento: {49,51,52,}  commento: {,}  il timer SubClass_C2_timer_T3 sia disattivo
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  diverso da  commento: {56,} 15
         commento: {104,} o  che   l'argomento argomento_ave5 non  sia  diverso da c120x commento: {,} 
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T1 non sia scaduto
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 1532,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  /*55,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo o  se l'argomento argomento_ave5 è  diverso da c120x /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 8, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento /*35,*/ o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 121, Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c120x /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a c120x /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 sia  uguale a c120x /*39,*/ 


 } Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 15
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  diverso da c120x /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 1532,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  /*55,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo o  se l'argomento argomento_ave5 è  diverso da c120x /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False , Solo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 8, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento /*35,*/ o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 121, Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c120x /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a c120x /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 sia  uguale a c120x /*39,*/ 


 } Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 15
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  diverso da c120x /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 1532,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  /*55,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo o  se l'argomento argomento_ave5 è  diverso da c120x /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 1532,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  /*55,*/ 6 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 1532,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 1532""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (1532)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L6 è attivo, /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è minore di  (6)) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo)""", [
                            DIBoolExpr("""LessThanImpl\n/*41,*/   MainClass_C1_parametro_P9 del campo  MainClass_C1     è  minore di  /*55,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 13 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è attivo""", [
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co2 è  uguale a  /*53,*/ 13""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave5 è  diverso da c120x /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo /*37,*/ e  se la variabile SubClass_C2_variabile_V5 non è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave5 è  diverso da c120x /*39,*/  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave5 è  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 non è  uguale a GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 8, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento /*35,*/ o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 121, Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c120x /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a c120x /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 sia  uguale a c120x /*39,*/ 


 } Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 15
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  diverso da c120x /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 8, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento /*35,*/ o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 121, Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c120x /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a c120x /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 sia  uguale a c120x /*39,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True  /*35,*/ o  se il controllo SubClass_C2_controllo_C6 è  uguale a spento /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V5 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\nlo stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V5 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C6 è  uguale a spento /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C6 è  uguale a spento""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 non è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento /*35,*/ o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 121, Verifica che   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c120x /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a c120x /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento /*35,*/ o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False  /*38,*/ o  se il contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 121""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento /*35,*/ o  se il controllo SubClass_C2_controllo_C9 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504 /*35,*/ o  se il controllo SubClass_C2_controllo_C4 è  uguale a spento""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/ 12504""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (12504)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C4 è  uguale a spento""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C9 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 è  diverso da  /*56,*/ 121""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (121)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c120x /*,*/ 
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  uguale a c120x /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153
 /*104,*/ o  che   l'argomento argomento_ave5 sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C2_timer_T1 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 153""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co2)  è uguale a  (153))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (153)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave5 sia  uguale a c120x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave5 non  sia  uguale a c120x /*39,*/ 
 /*104,*/ e  che   l'argomento argomento_ave5 sia  uguale a c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave5 non  sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave5 sia  uguale a c120x""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 15
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  diverso da c120x /*,*/ 
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 15
 /*104,*/ o  che   l'argomento argomento_ave5 non  sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,51,52,*/  /*,*/  il timer SubClass_C2_timer_T3 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  diverso da  /*56,*/ 15""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave5 non  sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave5)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 1532, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6()) if db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() < 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_contatore_co2().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(argomento_ave5 == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_parametro_p3() < 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co5().get_valore() == 12504, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c4() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 121, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 153, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(argomento_ave5 == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(argomento_ave5 == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(argomento_ave5 == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 15, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(argomento_ave5 == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m7")
    def macroSubclass_c2_macrove_m7(self, argomento_ave2, argomento_ave4, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {38,}  se il contatore SubClass_C2_contatore_Co8 non è  minore di  commento: {55,} 1325, Almeno una delle seguenti { 
         commento: {63,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 2, Solo una delle seguenti { 
         commento: {62,} commento: {42,}  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo commento: {39,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 140 commento: {35,} e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento commento: {39,} , Almeno una delle seguenti { 
         commento: {62,} commento: {34,}  se il parametro SubClass_C2_parametro_P6 è  maggiore di  commento: {54,} 1 commento: {38,} o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  commento: {53,} 144132 commento: {36,} o  se il timer SubClass_C2_timer_T1 non è disattivo commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  minore di  commento: {55,} 10 commento: {34,} o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  commento: {54,} 6, Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se il parametro SubClass_C2_parametro_P3 non è  diverso da  commento: {56,} 6 commento: {36,} e  se il timer SubClass_C2_timer_T3 non è scaduto commento: {36,} o  se il timer SubClass_C2_timer_T3 è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 1250, Tutte le seguenti { 
         commento: {45,}  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  minore di  commento: {55,} 11413 commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  commento: {55,} 152 commento: {34,} e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo commento: {38,} e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  commento: {55,} 135 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  commento: {56,} 10, Verifica che   commento: {47,48,49,52,}   l'argomento argomento_ave2 sia  diverso da spento commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T1 sia attivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T3 non sia disattivo
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P7 sia  maggiore di  commento: {54,} 10
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  diverso da  commento: {56,} 10
        
        
         } Verifica che   commento: {47,50,51,52,}  commento: {,}  il contatore SubClass_C2_contatore_Co8 sia  uguale a  commento: {53,} 1103
         commento: {104,} e  che   l'argomento argomento_ave2 sia  diverso da spento commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P3 non sia  minore di  commento: {55,} 6
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co8 sia  minore di  commento: {55,} 1
        
        
         } Verifica che   commento: {47,52,}  commento: {34,}  il parametro SubClass_C2_parametro_P3 sia  maggiore di  commento: {54,} 2
         commento: {104,} o  che   l'argomento argomento_ave2 sia  uguale a spento commento: {,} 
        
        
         } Verifica che   commento: {47,48,49,50,}  commento: {,}  il timer SubClass_C2_timer_T3 sia attivo
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  commento: {54,} 8
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V10 sia  diverso da spento
        
        
         } Verifica che   commento: {50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x
         commento: {104,} o  che   l'argomento argomento_ave2 non  sia  diverso da spento commento: {,} 
        
        
         } Verifica che   commento: {47,49,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia scaduto
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  commento: {54,} 6
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P7 non sia  minore di  commento: {55,} 3
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T1 sia scaduto
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T3 sia scaduto
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1325, Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2, Solo una delle seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento /*,*/ 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento


 } Verifica che   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave2 non  sia  diverso da spento /*,*/ 


 } Verifica che   /*47,49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia scaduto
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1325, Almeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2, Solo una delle seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento /*,*/ 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento


 } Verifica che   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave2 non  sia  diverso da spento /*,*/ 


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  minore di  /*55,*/ 1325""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co8)  è minore di  (1325)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2, Solo una delle seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento /*,*/ 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento


 } Verifica che   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave2 non  sia  diverso da spento /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2, Solo una delle seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento /*,*/ 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (2))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (2)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento /*,*/ 


 } Verifica che   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento /*39,*/ , Almeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*42,*/  se  MainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento o  se l'argomento argomento_ave4 è  uguale a GialloGiallo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_controllo_C9 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave4 è  uguale a GialloGiallo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento e  se l'argomento argomento_ave2 è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140 /*35,*/ e  se il controllo SubClass_C2_controllo_C1 non è  uguale a spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V10 è  uguale a spento /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V10 è  uguale a spento""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 140""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 non è  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 } Verifica che   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento /*,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132 /*36,*/ o  se il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se il parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1 /*38,*/ o  se il contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132""", [
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P6 è  maggiore di  /*54,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co4 non è  uguale a  /*53,*/ 144132""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co4)  è uguale a  (144132)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T1 non è disattivo /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P3 è  minore di  /*55,*/ 10""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250, Tutte le seguenti { 
 /*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6 /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 non è  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p3)  è uguale a  (6))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (6)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T3 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 1250""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co8)  è uguale a  (1250))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (1250)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10, Verifica che   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*45,*/  se  MainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413 /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co10 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  minore di  /*55,*/ 11413""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co10 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è minore di  (11413)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152 /*34,*/ e  se il parametro SubClass_C2_parametro_P10 è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 152""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co2)  è minore di  (152)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P10 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo /*38,*/ e  se il contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 è  diverso da GialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (giallogiallo)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co2 non è  minore di  /*55,*/ 135""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co2)  è minore di  (135)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P6 non è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,52,*/   l'argomento argomento_ave2 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T1 sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T1 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P7 sia  maggiore di  /*54,*/ 10""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p6)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p6)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103
 /*104,*/ e  che   l'argomento argomento_ave2 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C2_contatore_Co8 sia  uguale a  /*53,*/ 1103""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave2 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V10 sia  uguale a spento""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v9)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P3 non sia  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p3)  è minore di  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore SubClass_C2_contatore_Co8 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2
 /*104,*/ o  che   l'argomento argomento_ave2 sia  uguale a spento""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,52,*/  /*34,*/  il parametro SubClass_C2_parametro_P3 sia  maggiore di  /*54,*/ 2""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave2 sia  uguale a spento""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*47,48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T3 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C9 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v10)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V10 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x
 /*104,*/ o  che   l'argomento argomento_ave2 non  sia  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V10 non sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v10)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v10)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V9 non sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v9)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave2 non  sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia scaduto
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  minore di  /*55,*/ 3
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T1 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P6 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p6)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p7)  è minore di  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C2_timer_T1 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_subclass_c2_contatore_co8().get_valore() < 1325, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(not db(not db(self.get_subclass_c2_parametro_p6() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave4 == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_variabile_v10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co2().get_valore() < 140, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave2 == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_subclass_c2_parametro_p6() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co4().get_valore() == 144132, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p3() < 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p6() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(not db(self.get_subclass_c2_parametro_p3() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 1250, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co10().get_valore() < 11413, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co2().get_valore() < 152, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_parametro_p2() == GlobalEnumeration.giallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co2().get_valore() < 135, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p6() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(argomento_ave2 == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t1().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p7() > 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p6() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(self.get_subclass_c2_contatore_co8().get_valore() == 1103, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(argomento_ave2 == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p3() < 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_subclass_c2_contatore_co8().get_valore() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c2_parametro_p3() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(argomento_ave2 == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p6() > 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(not db(self.get_subclass_c2_variabile_v10() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(argomento_ave2 == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p6() > 6, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p7() < 3, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m8")
    def macroSubclass_c2_macrove_m8(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,}  se il controllo ConsDef  è  uguale a FALSE ,  commento: {43,}  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  commento: {105,} è disattivo, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C9 del campo  MainClass_C1     commento: {105,} è  uguale a avanzamento o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P3 è  diverso da  commento: {56,} 10, Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento commento: {34,} o  se il parametro SubClass_C2_parametro_P3 è  uguale a  commento: {53,} 1 commento: {34,} e  se il parametro SubClass_C2_parametro_P6 è  uguale a  commento: {53,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento, Almeno una delle seguenti { 
         commento: {63,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx commento: {36,} e  se il timer SubClass_C2_timer_T3 è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 1225 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
         commento: {41,}  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  commento: {53,} 4 commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 è scaduto commento: {38,} e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  commento: {56,} 140413, Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C6 sia  diverso da spento
        
        
         } Verifica che   commento: {47,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P7 non sia  uguale a  commento: {53,} 4
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  commento: {53,} 122
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T3 non sia attivo
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T1 non sia scaduto
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 10, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  /*53,*/ 122


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 10, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  /*53,*/ 122


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*43,*/  se MainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_timer_T5 del campo  MainClass_C1 di SubClass_C2_lista_L3 esiste e  /*105,*/ è disattivo, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_controllo_c9 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (avanzamento)) allora (il timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo)""", [
                            DIBoolExpr("""EqualImpl\n/*42,*/    MainClass_C1_controllo_C9 del campo  MainClass_C1     /*105,*/ è  uguale a avanzamento""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5 del campo mainclass_c1 della lista subclass_c2_lista_l3' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P3 è  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p3)  è uguale a  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  /*53,*/ 122


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  /*53,*/ 122


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento /*34,*/ o  se il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C1 è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1 /*34,*/ e  se il parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P3 è  uguale a  /*53,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C2_parametro_P6 è  uguale a  /*53,*/ 9""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C1 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c1)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento


 } Verifica che   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  /*53,*/ 122


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx /*36,*/ e  se il timer SubClass_C2_timer_T3 è scaduto""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L6 è  diverso da c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (c270xx))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è scaduto""", [
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1225""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413, Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4 /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P9 del campo  MainClass_C1 di SubClass_C2_lista_L9 è  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9 del campo mainclass_c1 della lista subclass_c2_lista_l9)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T3 è scaduto /*38,*/ e  se il contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co8 non è  diverso da  /*56,*/ 140413""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co8)  è uguale a  (140413))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (140413)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C6 sia  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  uguale a  /*53,*/ 4
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  /*53,*/ 122""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P7 non sia  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p7)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co8 non sia  uguale a  /*53,*/ 122""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co8)  è uguale a  (122)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T3 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T1 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C2_variabile_V5 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3()) if db(it.get_mainclass_c1().get_mainclass_c1_controllo_c9() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p3() == 10, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_parametro_p3() == 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p6() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c1() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_contatore_co2().get_valore() < 1225, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p9() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l9())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 140413, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p7() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co8().get_valore() == 122, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db(not db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_timer_t1().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v5() == True, di_ctx.subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m1")
    def macroSubclass_c2_macrova_m1(self, argomento_a2, argomento_a3, argomento_a4, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è attivo commento: {41,} o  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a avanzamentox commento: {44,} e  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270xx , assegna alla macro il valore c120x
        
         commento: {46,} assegna alla macro il valore c120x commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è attivo /*41,*/ o  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamentox /*44,*/ e  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270xx , assegna alla macro il valore c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è attivo /*41,*/ o  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamentox /*44,*/ e  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270xx""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_restoreti_ti1_restore' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (avanzamentox))} )  e  
( per ognuna delle seguenti {((mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270xx))} )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (avanzamentox))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p4 del campo mainclass_c1 della lista subclass_c2_lista_l6)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270xx))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l3)  è uguale a  (c270xx)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 non è attivo /*41,*/ o  se MainClass_C1_parametro_P4 del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a avanzamentox /*44,*/ e  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L3 è  uguale a c270xx , assegna alla macro il valore c120x
        if db((db(not db(self.get_subclass_c2_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p4() == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == GlobalEnumeration.c270xx, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l3())), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c120x
        #  /*46,*/ assegna alla macro il valore c120x
        return GlobalEnumeration.c120x
    
    @srf_value_macro("macroSubclass_c2_macrova_m4")
    def macroSubclass_c2_macrova_m4(self, argomento_a1, argomento_a10, argomento_a5, argomento_a6, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore spento commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m4_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore spento
        return GlobalEnumeration.spento
    
    @srf_value_macro("macroSubclass_c2_macrova_m6")
    def macroSubclass_c2_macrova_m6(self, di_ctx: DIValueMacro):
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
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created
    def eventSubclass_c2_command_comm4(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm4')
    
    def eventSubclass_c2_command_comm8(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm8')
    
    def eventSubclass_c2_command_comm9(self, notifying_process, argomento_ave1, argomento_ave2, argomento_ave4, argomento_ave5):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm9', argomento_ave1=argomento_ave1, argomento_ave2=argomento_ave2, argomento_ave4=argomento_ave4, argomento_ave5=argomento_ave5)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c10_prev(self.get_subclass_c2_previousco_c10())
        self.set_subclass_c2_previousco_c2_prev(self.get_subclass_c2_previousco_c2())
        self.set_subclass_c2_previousco_c3_prev(self.get_subclass_c2_previousco_c3())
        self.set_subclass_c2_previousco_c7_prev(self.get_subclass_c2_previousco_c7())
        self.set_subclass_c2_previousco_c8_prev(self.get_subclass_c2_previousco_c8())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())

class SubClass_C2_RecordHeaderR7(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled11, recordfiled3):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled11(recordfiled11)
        self.set_recordfiled3(recordfiled3)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled11(self, recordfiled11):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"), recordfiled11)

    def set_recordfiled3(self, recordfiled3):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"), recordfiled3)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled11(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"))

    def get_recordfiled3(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"))



