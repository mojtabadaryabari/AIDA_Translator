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

class MainClass_C1(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(MainClass_C1, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.avvio)
        self.set_mainclass_c1_previousva_pv2(0)
        self.set_mainclass_c1_restoreva_rv1(False)
        self.set_mainclass_c1_restoreva_rv2(False)
        self.set_mainclass_c1_restoreva_rv3(GlobalEnumeration.avvio)
        self.set_mainclass_c1_restoreva_rv4(GlobalEnumeration.c180)
        self.set_mainclass_c1_variabile_v10(False)
        self.set_mainclass_c1_variabile_v2(False)
        self.set_mainclass_c1_variabile_v3(GlobalEnumeration.c180)
        self.set_mainclass_c1_variabile_v5(0)
        self.set_mainclass_c1_variabile_v6(False)

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
    def init_configuration(self, mainclass_c1_parametro_p10, mainclass_c1_parametro_p3, mainclass_c1_parametro_p7, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p3(mainclass_c1_parametro_p3)
        self.set_mainclass_c1_parametro_p7(mainclass_c1_parametro_p7)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(34000)
        self.set_mainclass_c1_restoreti_ti1_restore(34000)
        self.set_mainclass_c1_timer_t10(512000)
        self.set_mainclass_c1_timer_t3(45000)
        self.set_mainclass_c1_timer_t4(130000)
        self.set_mainclass_c1_timer_t6(5000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_timer_t10,self.mainclass_c1_timer_t3,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t6,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co3(0)
        self.set_mainclass_c1_contatore_co5(0)
        self.set_mainclass_c1_contatore_co8(0)
        self.set_mainclass_c1_contatore_co9(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p3(self, mainclass_c1_parametro_p3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3",mainclass_c1_parametro_p3)

    def set_mainclass_c1_parametro_p7(self, mainclass_c1_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7",mainclass_c1_parametro_p7)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p3")

    def get_mainclass_c1_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p7")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c1")

    def get_mainclass_c1_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c5")

    def get_mainclass_c1_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c7")

    def get_mainclass_c1_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c8")

    def get_mainclass_c1_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c9")

    def get_mainclass_c1_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10")

    def get_mainclass_c1_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2")

    def get_mainclass_c1_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3")

    def get_mainclass_c1_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4")

    def get_mainclass_c1_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c6")


    # setters for state variables
    def set_mainclass_c1_previousco_c10_prev(self, mainclass_c1_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev",mainclass_c1_previousco_c10_prev)
    def set_mainclass_c1_previousco_c2_prev(self, mainclass_c1_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev",mainclass_c1_previousco_c2_prev)
    def set_mainclass_c1_previousco_c3_prev(self, mainclass_c1_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev",mainclass_c1_previousco_c3_prev)
    def set_mainclass_c1_previousco_c4_prev(self, mainclass_c1_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev",mainclass_c1_previousco_c4_prev)
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
    def set_mainclass_c1_restoreva_rv1(self, mainclass_c1_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv1",mainclass_c1_restoreva_rv1)
    def set_mainclass_c1_restoreva_rv2(self, mainclass_c1_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv2",mainclass_c1_restoreva_rv2)
    def set_mainclass_c1_restoreva_rv3(self, mainclass_c1_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv3",mainclass_c1_restoreva_rv3)
    def set_mainclass_c1_restoreva_rv4(self, mainclass_c1_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_restoreva_rv4",mainclass_c1_restoreva_rv4)
    def set_mainclass_c1_variabile_v10(self, mainclass_c1_variabile_v10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10",mainclass_c1_variabile_v10)
    def set_mainclass_c1_variabile_v2(self, mainclass_c1_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2",mainclass_c1_variabile_v2)
    def set_mainclass_c1_variabile_v3(self, mainclass_c1_variabile_v3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3",mainclass_c1_variabile_v3)
    def set_mainclass_c1_variabile_v5(self, mainclass_c1_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5",mainclass_c1_variabile_v5)
    def set_mainclass_c1_variabile_v6(self, mainclass_c1_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6",mainclass_c1_variabile_v6)

    # getters for state variables
    def get_mainclass_c1_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c10_prev")

    def get_mainclass_c1_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c2_prev")

    def get_mainclass_c1_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c3_prev")

    def get_mainclass_c1_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c4_prev")

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

    def get_mainclass_c1_variabile_v10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v10")

    def get_mainclass_c1_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v2")

    def get_mainclass_c1_variabile_v3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v3")

    def get_mainclass_c1_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v5")

    def get_mainclass_c1_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v6")

    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")


    # setters for timers
    def set_mainclass_c1_restoreti_ti1(self, timerDuration):
        self.mainclass_c1_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1", self.memory)

    def set_mainclass_c1_restoreti_ti1_restore(self, timerDuration):
        self.mainclass_c1_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_restoreti_ti1_restore", self.memory)

    def set_mainclass_c1_timer_t10(self, timerDuration):
        self.mainclass_c1_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t10", self.memory)

    def set_mainclass_c1_timer_t3(self, timerDuration):
        self.mainclass_c1_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t3", self.memory)

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)

    def set_mainclass_c1_timer_t6(self, timerDuration):
        self.mainclass_c1_timer_t6 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t6", self.memory)


    # getters for timers
    def get_mainclass_c1_restoreti_ti1(self):
        return self.mainclass_c1_restoreti_ti1

    def get_mainclass_c1_restoreti_ti1_restore(self):
        return self.mainclass_c1_restoreti_ti1_restore

    def get_mainclass_c1_timer_t10(self):
        return self.mainclass_c1_timer_t10

    def get_mainclass_c1_timer_t3(self):
        return self.mainclass_c1_timer_t3

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t6(self):
        return self.mainclass_c1_timer_t6


    # setters for counters
    def set_mainclass_c1_contatore_co3(self, counterInitValue):
        self.mainclass_c1_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co3", self.memory)

    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)

    def set_mainclass_c1_contatore_co8(self, counterInitValue):
        self.mainclass_c1_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co8", self.memory)

    def set_mainclass_c1_contatore_co9(self, counterInitValue):
        self.mainclass_c1_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co9", self.memory)


    # getters for counters
    def get_mainclass_c1_contatore_co3(self):
        return self.mainclass_c1_contatore_co3

    def get_mainclass_c1_contatore_co5(self):
        return self.mainclass_c1_contatore_co5

    def get_mainclass_c1_contatore_co8(self):
        return self.mainclass_c1_contatore_co8

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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_mainclass_c1_previousco_c10_prev(True)
        self.set_mainclass_c1_previousco_c2_prev(True)
        self.set_mainclass_c1_previousco_c3_prev(GlobalEnumeration.rossogialloverde)
        self.set_mainclass_c1_previousco_c4_prev(True)
        self.set_mainclass_c1_previousco_c6_prev(True)
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
    def macroMainclass_c1_macroef_m3(self, argomento_af5, argomento_af6, argomento_af9, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se il ripristino dello stato  è  diverso da  commento: {56,}  state1  commento: {107,},  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde commento: {67,}
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T4
        
        
          se il controllo ConsDef è uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False ,  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  False commento: {67,}
        
           
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo o  se l'argomento argomento_af9 non  è  diverso da RossoGialloaVerdea commento: {39,} , commento: {69,}Disattiva il timer MainClass_C1_timer_T3
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde /*67,*/

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T4""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\nse il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (True)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*67,*/

   
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo o  se l'argomento argomento_af9 non  è  diverso da RossoGialloaVerdea /*39,*/ , /*69,*/Disattiva il timer MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/

   
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo o  se l'argomento argomento_af9 non  è  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((argomento_af9)  è uguale a  (rossogialloaverdea)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af9)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af9)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  se il ripristino dello stato  è  diverso da  /*56,*/  state1  /*107,*/,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde /*67,*/
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T4
        if db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_variabile_v3(GlobalEnumeration.rossogialloverde)
        else:
            self.get_mainclass_c1_timer_t4().attiva()
        #  se il controllo ConsDef è uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  uguale a  False ,  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  False
        if db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_variabile_v10(False)
        #  /*67,*/
        #     
        #   /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 è attivo o  se l'argomento argomento_af9 non  è  diverso da RossoGialloaVerdea /*39,*/ , /*69,*/Disattiva il timer MainClass_C1_timer_T3
        if db((db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[2].subs[0].subs[0]) or db(not db(not db(argomento_af9 == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t3().disattiva()
    
    def macroMainclass_c1_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {36,} e  se il timer MainClass_C1_timer_T6 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  commento: {54,} 4, commento: {69,}Disattiva il timer MainClass_C1_timer_T4
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox ) commento: {73,}
        
        
         commento: {38,}  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  commento: {54,} 15 commento: {35,} o  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloaVerdea commento: {37,} o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  commento: {36,} o  se il timer MainClass_C1_timer_T3 non è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  True 
        
           
         commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {36,} o  se il timer MainClass_C1_timer_T3 non è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 13123 commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V2 il valore  False 
        
         ,altrimenti  commento: {71,}Decrementa il contatore MainClass_C1_contatore_Co8
        
        
          se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  commento: {55,} 14, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
        
         ,altrimenti  commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  True 
        
        
         commento: {34,}  se il parametro MainClass_C1_parametro_P3 non è  uguale a  commento: {53,} 9 commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  commento: {56,} 1404 commento: {36,} o  se il timer MainClass_C1_timer_T4 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  commento: {54,} 1151, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co8
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 4, /*69,*/Disattiva il timer MainClass_C1_timer_T4

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (True) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (True)) ) )  e  ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) ) )  e  
( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (True) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (True)) ) )  e  ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_restoreva_rv2_restore)  è uguale a  (True) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è uguale a  (True)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv2_restore)  è uguale a  (True)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_parametro_p3)  è maggiore di  (4)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è maggiore di  (4))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*73,*/


 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloaVerdea /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T3 non è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloaVerdea /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T3 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((mainclass_c1_contatore_co5)  è maggiore di  (15)) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))) ) )  o  
( ( (mainclass_c1_variabile_v6)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)) ) ) )  o  
( negazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_contatore_co5)  è maggiore di  (15)) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))) ) )  o  
( ( (mainclass_c1_variabile_v6)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_contatore_co5)  è maggiore di  (15)) )  o  
( negazione di (negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è maggiore di  (15))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co5)  è maggiore di  (15)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_variabile_v6)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*36,*/ o  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 13123 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore  False 

 ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*36,*/ o  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 13123 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)) )  o  
( ( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) )  e  
( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (True)) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) )  e  
( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (True)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (13123)) )  e  
( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (13123))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (13123)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 

 ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co9)  è minore di  (14))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co9)  è minore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 9 /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 1404 /*36,*/ o  se il timer MainClass_C1_timer_T4 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1151, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 9 /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 1404 /*36,*/ o  se il timer MainClass_C1_timer_T4 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1151""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (9)) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (1404))) ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t4' è scaduto) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_parametro_p3)  è uguale a  (9)) )  o  
( negazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (1404))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p3)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_contatore_co3)  è uguale a  (1404)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è uguale a  (1404))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co3)  è uguale a  (1404)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_contatore_co8)  è maggiore di  (1151)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è maggiore di  (1151))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co8)  è maggiore di  (1151)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV2 è  uguale a  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  uguale a  True  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*36,*/ e  se il timer MainClass_C1_timer_T6 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P3 non è  maggiore di  /*54,*/ 4, /*69,*/Disattiva il timer MainClass_C1_timer_T4
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )
        if db((db((db((db((db(self.get_mainclass_c1_restoreva_rv2_restore() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() > 4, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_mainclass_c1_timer_t4().disattiva()
        else:
            self.macroMainclass_c1_macroef_m3(True,GlobalEnumeration.giallox,GlobalEnumeration.rosso, di_ctx.subs[0].subs[1])
        #  /*73,*/
        #   /*38,*/  se il contatore MainClass_C1_contatore_Co5 non è  maggiore di  /*54,*/ 15 /*35,*/ o  se il controllo MainClass_C1_controllo_C9 non è  diverso da RossoGialloaVerdea /*37,*/ o  se la variabile MainClass_C1_variabile_V6 è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T3 non è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  True
        if db((db((db((db((db(not db(self.get_mainclass_c1_contatore_co5().get_valore() > 15, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_variabile_v6() == False, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c9(True)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*36,*/ o  se il timer MainClass_C1_timer_T3 non è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  uguale a  True  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 13123 /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V2 il valore  False 
        #   ,altrimenti  /*71,*/Decrementa il contatore MainClass_C1_contatore_Co8
        if db((db((db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 13123, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.rossogialloverde, di_ctx.subs[2].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_variabile_v2(False)
        else:
            self.get_mainclass_c1_contatore_co8().decrementa()
        #  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co9 non è  minore di  /*55,*/ 14, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
        #   ,altrimenti  /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  True
        if db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co9().get_valore() < 14, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v10(True)
        else:
            self.set_mainclass_c1_comando_c9(True)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P3 non è  uguale a  /*53,*/ 9 /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  diverso da  /*56,*/ 1404 /*36,*/ o  se il timer MainClass_C1_timer_T4 non è scaduto o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 non è  maggiore di  /*54,*/ 1151, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co8
        if db((db((db((db(not db(self.get_mainclass_c1_parametro_p3() == 9, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_contatore_co3().get_valore() == 1404, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t4().isScaduto(), di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co8().get_valore() > 1151, di_ctx.subs[4].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[1].subs[1])), di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v10(True)
        else:
            self.get_mainclass_c1_contatore_co8().resetta()
    
    def macroMainclass_c1_macroef_m7(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        {  se il ripristino dello stato  non è  uguale a  commento: {53,}  state1  commento: {107,},  Applica gli effetti
               della macro MainClass_C1_macroef_M6  commento: {73,}
        
         ,altrimenti  commento: {72,}Azzera il contatore MainClass_C1_contatore_Co9
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P3 è  uguale a  commento: {53,} 8 commento: {37,} o  se la variabile MainClass_C1_variabile_V10 non è  diverso da  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  False 
        
         ,altrimenti  commento: {69,}Disattiva il timer MainClass_C1_timer_T4
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True , commento: {70,}Incrementa il contatore MainClass_C1_contatore_Co5
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V5 il valore 9
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 142 commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 non è  maggiore di  commento: {54,} 1430, commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox ) commento: {73,}
        
        
          se il controllo ConsDef  è  uguale a FALSE  commento: {37,} e  se la variabile MainClass_C1_variabile_V2 non è  uguale a  False  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True , commento: {67,} Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde
        
         ,altrimenti   Applica gli effetti
               della macro MainClass_C1_macroef_M9  commento: {73,}
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/,  Applica gli effetti
       della macro MainClass_C1_macroef_M6  /*73,*/

 ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co9""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M6"""),#1
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  False 

 ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (mainclass_c1_restoreva_rv1_restore)  è uguale a  (False) )  o  
( (mainclass_c1_parametro_p3)  è uguale a  (8) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3)  è uguale a  (8)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_variabile_v10)  è uguale a  (False))) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_variabile_v10)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c8)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore 9""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 142 /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  maggiore di  /*54,*/ 1430, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 142 /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  maggiore di  /*54,*/ 1430""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( il timer 'mainclass_c1_timer_t4' è attivo ) )  o  
( negazione di ((mainclass_c1_contatore_co8)  è minore di  (142)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( il timer 'mainclass_c1_timer_t4' è attivo )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è minore di  (142))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (142)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co3)  è maggiore di  (1430))""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_contatore_co3)  è maggiore di  (1430)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )"""),#1
                            ]),#3
                            DIStatement("""ITEStatementImpl\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde

 ,altrimenti   Applica gli effetti
       della macro MainClass_C1_macroef_M9""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*73,*/


  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_variabile_v2)  è uguale a  (False)) ) )  e  ( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (True)) ) )  e  ( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_variabile_v2)  è uguale a  (False)) ) )  e  ( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_variabile_v2)  è uguale a  (False)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M9"""),#1
                            ]),#4
                ])

        populate_macroMainclass_c1_macroef_m7_SrfMacroDefInfo(di_ctx)
        #  se il ripristino dello stato  non è  uguale a  /*53,*/  state1  /*107,*/,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M6  /*73,*/
        #   ,altrimenti  /*72,*/Azzera il contatore MainClass_C1_contatore_Co9
        if db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.macroMainclass_c1_macroef_m6(di_ctx.subs[0].subs[1])
        else:
            self.get_mainclass_c1_contatore_co9().resetta()
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 è  uguale a  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P3 è  uguale a  /*53,*/ 8 /*37,*/ o  se la variabile MainClass_C1_variabile_V10 non è  diverso da  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C8 non è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  False 
        #   ,altrimenti  /*69,*/Disattiva il timer MainClass_C1_timer_T4
        if db((db((db(self.get_mainclass_c1_restoreva_rv1_restore() == False, di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p3() == 8, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c8() == False, di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c9(False)
        else:
            self.get_mainclass_c1_timer_t4().disattiva()
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  uguale a  True , /*70,*/Incrementa il contatore MainClass_C1_contatore_Co5
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V5 il valore 9
        if db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == True, di_ctx.subs[2].subs[0].subs[0]), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_contatore_co5().incrementa()
        else:
            self.set_mainclass_c1_variabile_v5(9)
        #  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 142 /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 non è  maggiore di  /*54,*/ 1430, /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  True 
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M3( con argomento_af5   uguale a True ,argomento_af9   uguale a Rosso ,argomento_af6   uguale a Giallox )
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[3].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[3].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() < 142, di_ctx.subs[3].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[0].subs[1])), di_ctx.subs[3].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co3().get_valore() > 1430, di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_mainclass_c1_variabile_v10(True)
        else:
            self.macroMainclass_c1_macroef_m3(True,GlobalEnumeration.giallox,GlobalEnumeration.rosso, di_ctx.subs[3].subs[1])
        #  /*73,*/
        #    se il controllo ConsDef  è  uguale a FALSE  /*37,*/ e  se la variabile MainClass_C1_variabile_V2 non è  uguale a  False  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  uguale a  True  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P9 è  uguale a  True , /*67,*/ Assegna alla variabile MainClass_C1_variabile_V3 il valore RossoGialloVerde
        #   ,altrimenti   Applica gli effetti
        #         della macro MainClass_C1_macroef_M9
        if db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v2() == False, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[4].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[4].subs[0].subs[0].subs[1])), di_ctx.subs[4].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[4].subs[0].subs[1])), di_ctx.subs[4].subs[0]):
            self.set_mainclass_c1_variabile_v3(GlobalEnumeration.rossogialloverde)
        else:
            self.macroMainclass_c1_macroef_m9(di_ctx.subs[4].subs[1])
    
    def macroMainclass_c1_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {36,} e  se il timer MainClass_C1_timer_T3 non è attivo commento: {36,} o  se il timer MainClass_C1_timer_T6 non è scaduto commento: {38,} e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  commento: {53,} 14 commento: {34,} o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  commento: {34,} o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False ,  Applica gli effetti
               della macro MainClass_C1_macroef_M6  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V6 il valore  True 
        
        
         commento: {35,}  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {38,} o  se il contatore MainClass_C1_contatore_Co3 è  minore di  commento: {55,} 13451 o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 non è  uguale a RossoGialloaVerdea commento: {34,} e  se il parametro MainClass_C1_parametro_P3 è  minore di  commento: {55,} 7, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  False 
        
           
          se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a RossoGialloVerde ,argomento_a2   uguale a c180x ,argomento_a7   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a4   uguale a c180 )   è  diverso da Verde commento: {40,}  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  commento: {56,} 152 o  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 133, commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  True 
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T3
        
        
         commento: {109,}  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False ,  Applica gli effetti
               della macro MainClass_C1_macroef_M7   commento: {73,}
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 14 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False ,  Applica gli effetti
       della macro MainClass_C1_macroef_M6  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 14 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  
( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) ) )  o  
( ( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) )  e  
( (mainclass_c1_contatore_co8)  è uguale a  (14) ) ) )  o  
( negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False)) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  
( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) ) )  o  
( ( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) )  e  
( (mainclass_c1_contatore_co8)  è uguale a  (14) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto) )  e  
( negazione di (il timer 'mainclass_c1_timer_t3' è attivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t3' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_timer_t6' è scaduto) )  e  
( (mainclass_c1_contatore_co8)  è uguale a  (14) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t6' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (14)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M6"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13451 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  uguale a RossoGialloaVerdea /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 7, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13451 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  uguale a RossoGialloaVerdea /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)) )  o  
( (mainclass_c1_contatore_co3)  è minore di  (13451) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co3)  è minore di  (13451)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_parametro_p10)  è uguale a  (rossogialloaverdea)) ) )  e  
( (mainclass_c1_parametro_p3)  è minore di  (7) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di ((mainclass_c1_parametro_p10)  è uguale a  (rossogialloaverdea)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p10)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (7)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\nse la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a RossoGialloVerde ,argomento_a2   uguale a c180x ,argomento_a7   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a4   uguale a c180 )   è  diverso da Verde /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 152 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 133, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  True 

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a RossoGialloVerde ,argomento_a2   uguale a c180x ,argomento_a7   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a4   uguale a c180 )   è  diverso da Verde /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 152 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 133""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9')  è uguale a  (verde)) )  o  
( negazione di ((mainclass_c1_contatore_co8)  è uguale a  (152)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9')  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9')  è uguale a  (verde)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co8)  è uguale a  (152))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co8)  è uguale a  (152)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_contatore_co5)  è uguale a  (133) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (133)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#2
                            DIStatement("""ITStatement\n/*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False ,  Applica gli effetti
       della macro MainClass_C1_macroef_M7""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv1_restore)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv1_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M7"""),#1
                            ]),#3
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ e  se il timer MainClass_C1_timer_T3 non è attivo /*36,*/ o  se il timer MainClass_C1_timer_T6 non è scaduto /*38,*/ e  se il contatore MainClass_C1_contatore_Co8 è  uguale a  /*53,*/ 14 /*34,*/ o  se il parametro MainClass_C1_parametro_P9 è  diverso da  False  /*34,*/ o  se il parametro MainClass_C1_parametro_P9 non è  diverso da  False ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M6  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V6 il valore  True
        if db((db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co8().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(not db(self.get_mainclass_c1_parametro_p9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroMainclass_c1_macroef_m6(di_ctx.subs[0].subs[1])
        else:
            self.set_mainclass_c1_variabile_v6(True)
        #  /*35,*/  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*38,*/ o  se il contatore MainClass_C1_contatore_Co3 è  minore di  /*55,*/ 13451 o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 non è  uguale a RossoGialloaVerdea /*34,*/ e  se il parametro MainClass_C1_parametro_P3 è  minore di  /*55,*/ 7, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  False
        if db((db((db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co3().get_valore() < 13451, di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p3() < 7, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c9(False)
        #  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a RossoGialloVerde ,argomento_a2   uguale a c180x ,argomento_a7   uguale a c180 ,argomento_a3   uguale a RossoGialloVerde  e argomento_a4   uguale a c180 )   è  diverso da Verde /*40,*/  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 è  diverso da  /*56,*/ 152 o  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ e  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 133, /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  True 
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T3
        if db((db((db(not db(db(self.macroMainclass_c1_macrova_m9(GlobalEnumeration.c180x,GlobalEnumeration.rossogialloverde,GlobalEnumeration.c180,GlobalEnumeration.rossogialloverde,GlobalEnumeration.c180,True, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.verde, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co8().get_valore() == 152, di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co5().get_valore() == 133, di_ctx.subs[2].subs[0].subs[1].subs[1])), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.set_mainclass_c1_comando_c9(True)
        else:
            self.get_mainclass_c1_timer_t3().attiva()
        #  /*109,*/  se il ripristino della variabile  MainClass_C1_restoreva_RV1 non è  diverso da  False ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M7
        if db(not db(not db(self.get_mainclass_c1_restoreva_rv1_restore() == False, di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]), di_ctx.subs[3].subs[0]):
            self.macroMainclass_c1_macroef_m7(di_ctx.subs[3].subs[1])
    
    def macroMainclass_c1_macroef_m9(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se lo stato  non è  diverso da  commento: {56,}  state1  commento: {106,} o  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False , commento: {66,} Assegna al comando MainClass_C1_comando_C9 il valore  False 
        
         ,altrimenti  commento: {67,} Assegna alla variabile MainClass_C1_variabile_V10 il valore  False 
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  False 

 ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((lo stato di 'self')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( negazione di ((mainclass_c1_controllo_c7)  è uguale a  (False)) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m9_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  non è  diverso da  /*56,*/  state1  /*106,*/ o  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  False , /*66,*/ Assegna al comando MainClass_C1_comando_C9 il valore  False 
        #   ,altrimenti  /*67,*/ Assegna alla variabile MainClass_C1_variabile_V10 il valore  False
        if db((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c9(False)
        else:
            self.set_mainclass_c1_variabile_v10(False)
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m1")
    def macroMainclass_c1_macrove_m1(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {37,}  se la variabile MainClass_C1_variabile_V2 non è  uguale a  True  commento: {36,} o  se il timer MainClass_C1_timer_T10 è attivo, Verifica che   commento: {47,48,50,51,}  commento: {,}  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True 
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V5 sia  uguale a  commento: {53,} 5
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  commento: {54,} 151
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile MainClass_C1_variabile_V2 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T10 è attivo, Verifica che   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile MainClass_C1_variabile_V2 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T10 è attivo, Verifica che   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile MainClass_C1_variabile_V2 non è  uguale a  True  /*36,*/ o  se il timer MainClass_C1_timer_T10 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V2 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T10 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a  /*53,*/ 5
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True 
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,50,51,*/  /*,*/  il controllo MainClass_C1_controllo_C7 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P9 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V5 sia  uguale a  /*53,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  /*54,*/ 151""", [
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C7 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*,*/  il contatore MainClass_C1_contatore_Co3 sia  maggiore di  /*54,*/ 151""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m1_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_mainclass_c1_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t10().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(not db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_mainclass_c1_variabile_v5() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_contatore_co3().get_valore() > 151, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m10")
    def macroMainclass_c1_macrove_m10(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {36,}  se il timer MainClass_C1_timer_T6 non è scaduto, Verifica che   commento: {48,49,}  commento: {,}  il timer MainClass_C1_timer_T3 non sia disattivo
         commento: {104,} e  che  commento: {,}  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde
         commento: {104,} o  che  commento: {36,}  il timer MainClass_C1_timer_T10 non sia scaduto
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer MainClass_C1_timer_T6 non è scaduto, Verifica che   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia scaduto""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer MainClass_C1_timer_T6 non è scaduto, Verifica che   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T6 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde
 /*104,*/ o  che  /*36,*/  il timer MainClass_C1_timer_T10 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia disattivo
 /*104,*/ e  che  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,*/  /*,*/  il timer MainClass_C1_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer MainClass_C1_timer_T10 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_mainclass_c1_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c5() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m8")
    def macroMainclass_c1_macrove_m8(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {61,}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox commento: {40,}  commento: {36,} o  se il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
         commento: {62,}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox commento: {40,}  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo commento: {36,} o  se il timer MainClass_C1_timer_T3 è attivo commento: {34,} e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  commento: {54,} 2, Almeno una delle seguenti { 
         commento: {62,}  se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  commento: {55,} 122 commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  commento: {36,} o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
         commento: {63,} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo commento: {34,} o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  commento: {54,} 4 commento: {38,} e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  commento: {53,} 1430 e  se il controllo ConsDef  è  uguale a FALSE  commento: {37,} o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde commento: {34,} e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
          se il controllo ConsDef è uguale a FALSE  commento: {36,} e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T3 sia disattivo
        
        
         } Verifica che   commento: {47,48,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  commento: {54,} 6
         commento: {104,} e  che  commento: {34,}  il parametro MainClass_C1_parametro_P3 non sia  minore di  commento: {55,} 3
        
        
         } Verifica che   commento: {49,50,51,}  commento: {,}  il contatore MainClass_C1_contatore_Co9 sia  minore di  commento: {55,} 14
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T3 non sia scaduto
        
        
         } Verifica che   commento: {49,51,}  commento: {,}  il timer MainClass_C1_timer_T4 sia disattivo
         commento: {104,} o  che  commento: {,}  il contatore MainClass_C1_contatore_Co3 non sia  minore di  commento: {55,} 14
         commento: {104,} o  che  commento: {38,}  il contatore MainClass_C1_contatore_Co3 sia  minore di  commento: {55,} 14
        
        
         } Verifica che   commento: {47,48,50,}  commento: {34,}  il parametro MainClass_C1_parametro_P3 sia  minore di  commento: {55,} 7
         commento: {104,} o  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ o  se il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3


 } Verifica che   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co3 non sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 14


 } Verifica che   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ o  se il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE , Tutte le seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3


 } Verifica che   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co3 non sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 14


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ o  se il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a RossoGialloaVerdea  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (giallox)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P10 è  diverso da RossoGialloaVerdea""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3


 } Verifica che   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 } Verifica che   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co3 non sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 14


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3


 } Verifica che   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo /*36,*/ o  se il timer MainClass_C1_timer_T3 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a RossoGialloVerde ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (giallox)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer MainClass_C1_timer_T3 è attivo /*34,*/ e  se il parametro MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T3 è attivo""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro MainClass_C1_parametro_P7 è  maggiore di  /*54,*/ 2""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3


 } Verifica che   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False  /*36,*/ o  se il timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122 /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore MainClass_C1_contatore_Co8 non è  minore di  /*55,*/ 122""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co8)  è minore di  (122)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo MainClass_C1_controllo_C7 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V10 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T10 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 } Verifica che   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True , Solo una delle seguenti { 
  se il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE  /*37,*/ o  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo /*34,*/ o  se il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4 /*38,*/ e  se il contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P7 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p7)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore MainClass_C1_contatore_Co9 è  uguale a  /*53,*/ 1430""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde /*34,*/ e  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P9 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\nse il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef è uguale a FALSE  /*36,*/ e  se il timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T3 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T3 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p3)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro MainClass_C1_parametro_P3 non sia  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p3)  è minore di  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True""", [
                            DIBoolExpr("""LessThanImpl\nche   /*49,50,51,*/  /*,*/  il contatore MainClass_C1_contatore_Co9 sia  minore di  /*55,*/ 14""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V2 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v2)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T3 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co3 non sia  minore di  /*55,*/ 14
 /*104,*/ o  che  /*38,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo
 /*104,*/ o  che  /*,*/  il contatore MainClass_C1_contatore_Co3 non sia  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,51,*/  /*,*/  il timer MainClass_C1_timer_T4 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore MainClass_C1_contatore_Co3 non sia  minore di  /*55,*/ 14""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co3)  è minore di  (14)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore MainClass_C1_contatore_Co3 sia  minore di  /*55,*/ 14""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  minore di  /*55,*/ 7
 /*104,*/ o  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,48,50,*/  /*34,*/  il parametro MainClass_C1_parametro_P3 sia  minore di  /*55,*/ 7""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m8_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(db(self.macroMainclass_c1_macrova_m4(GlobalEnumeration.c180,GlobalEnumeration.rossogialloverde,GlobalEnumeration.rossogialloaverdea,GlobalEnumeration.avvio,GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.giallox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db((db((db(not db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p10() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(not db(db(self.macroMainclass_c1_macrova_m4(GlobalEnumeration.rossogialloverde,GlobalEnumeration.rossogialloverde,GlobalEnumeration.rosso,GlobalEnumeration.avvio,GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.giallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_mainclass_c1_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p7() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_contatore_co8().get_valore() < 122, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_parametro_p7() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_contatore_co9().get_valore() == 1430, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_mainclass_c1_parametro_p3() < 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_mainclass_c1_contatore_co9().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v2() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db(self.get_mainclass_c1_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co3().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_mainclass_c1_contatore_co3().get_valore() < 14, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(self.get_mainclass_c1_parametro_p3() < 7, di_ctx.subs[0].subs[1].subs[0]) or db((db(self.get_mainclass_c1_variabile_v10() == True, di_ctx.subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m4")
    def macroMainclass_c1_macrova_m4(self, argomento_a1, argomento_a10, argomento_a5, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {34,}  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True  commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 non è  diverso da Giallox commento: {37,} e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde e  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a c180 ,argomento_a2   uguale a Verde ,argomento_a7   uguale a RossoGialloVerde ,argomento_a3   uguale a c180  e argomento_a4   uguale a c180 )   è  diverso da Verde commento: {40,}  , assegna alla macro il valore Giallox
        
         commento: {46,} assegna alla macro il valore Giallox commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 non è  diverso da Giallox /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde e  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a c180 ,argomento_a2   uguale a Verde ,argomento_a7   uguale a RossoGialloVerde ,argomento_a3   uguale a c180  e argomento_a4   uguale a c180 )   è  diverso da Verde /*40,*/  , assegna alla macro il valore Giallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 non è  diverso da Giallox /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde e  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a c180 ,argomento_a2   uguale a Verde ,argomento_a7   uguale a RossoGialloVerde ,argomento_a3   uguale a c180  e argomento_a4   uguale a c180 )   è  diverso da Verde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_parametro_p9)  è uguale a  (True)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox))) )  e  ( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde)) ) )  e  
( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9')  è uguale a  (verde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox))) )  e  ( negazione di ((mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9')  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9')  è uguale a  (verde)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m9'"""),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*34,*/  se il parametro MainClass_C1_parametro_P9 non è  diverso da  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 non è  diverso da Giallox /*37,*/ e  se la variabile MainClass_C1_variabile_V3 è  diverso da RossoGialloVerde e  se la macro  MainClass_C1_macrova_M9 ( con argomento_a9   uguale a True ,argomento_a6   uguale a c180 ,argomento_a2   uguale a Verde ,argomento_a7   uguale a RossoGialloVerde ,argomento_a3   uguale a c180  e argomento_a4   uguale a c180 )   è  diverso da Verde /*40,*/  , assegna alla macro il valore Giallox
        if db((db(not db(not db(self.get_mainclass_c1_parametro_p9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(not db(self.get_mainclass_c1_restoreva_rv3_restore() == GlobalEnumeration.giallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v3() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(db(self.macroMainclass_c1_macrova_m9(GlobalEnumeration.verde,GlobalEnumeration.c180,GlobalEnumeration.c180,GlobalEnumeration.c180,GlobalEnumeration.rossogialloverde,True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.giallox
        #  /*46,*/ assegna alla macro il valore Giallox
        return GlobalEnumeration.giallox
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox commento: {40,}  commento: {35,} o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea commento: {34,} o  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} commento: {35,} e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  , assegna alla macro il valore Giallox
        
         commento: {46,} assegna alla macro il valore Giallox commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*34,*/ o  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  , assegna alla macro il valore Giallox""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*34,*/ o  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (giallox)) )  o  
( negazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (giallox))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4')  è uguale a  (giallox)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroMainclass_c1_macrova_m4'"""),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c9)  è uguale a  (rossogialloaverdea)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((lo stato di 'self')  è uguale a  (state1)) )  e  
( negazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (False))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((mainclass_c1_controllo_c7)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se la macro  MainClass_C1_macrova_M4 ( con argomento_a1   uguale a c180 ,argomento_a8   uguale a avvio ,argomento_a10   uguale a RossoGialloVerde ,argomento_a5   uguale a Rosso  e argomento_a9   uguale a RossoGialloaVerdea )   è  diverso da Giallox /*40,*/  /*35,*/ o  se il controllo MainClass_C1_controllo_C9 è  diverso da RossoGialloaVerdea /*34,*/ o  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ /*35,*/ e  se il controllo MainClass_C1_controllo_C7 non è  diverso da  False  , assegna alla macro il valore Giallox
        if db((db((db(not db(db(self.macroMainclass_c1_macrova_m4(GlobalEnumeration.c180,GlobalEnumeration.rossogialloverde,GlobalEnumeration.rosso,GlobalEnumeration.avvio,GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == GlobalEnumeration.giallox, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c9() == GlobalEnumeration.rossogialloaverdea, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_mainclass_c1_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.giallox
        #  /*46,*/ assegna alla macro il valore Giallox
        return GlobalEnumeration.giallox
    
    @srf_value_macro("macroMainclass_c1_macrova_m9")
    def macroMainclass_c1_macrova_m9(self, argomento_a2, argomento_a3, argomento_a4, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se il controllo ConsDef è uguale a FALSE  commento: {35,} e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  commento: {109,} o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  diverso da Giallox e  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 non  è  uguale a Verde commento: {39,}  o  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} , assegna alla macro il valore Verde
        
         commento: {46,} assegna alla macro il valore Verde commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  diverso da Giallox e  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 non  è  uguale a Verde /*39,*/  o  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ , assegna alla macro il valore Verde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  diverso da Giallox e  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 non  è  uguale a Verde /*39,*/  o  se il ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_controllo_c7)  è uguale a  (True) ) )  o  
( ( ( negazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((argomento_a2)  è uguale a  (verde)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (mainclass_c1_controllo_c7)  è uguale a  (True) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox)) )  e  ( (consdef)  è uguale a  (False) ) )  e  
( negazione di ((argomento_a2)  è uguale a  (verde)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox)) )  e  ( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_restoreva_rv3_restore)  è uguale a  (giallox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a2)  è uguale a  (verde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a2)  è uguale a  (verde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m9_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se il controllo ConsDef è uguale a FALSE  /*35,*/ e  se il controllo MainClass_C1_controllo_C7 è  uguale a  True  /*109,*/ o  se il ripristino della variabile  MainClass_C1_restoreva_RV3 è  diverso da Giallox e  se il controllo ConsDef è uguale a FALSE  e  se l'argomento argomento_a2 non  è  uguale a Verde /*39,*/  o  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ , assegna alla macro il valore Verde
        if db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_restoreva_rv3_restore() == GlobalEnumeration.giallox, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_a2 == GlobalEnumeration.verde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.verde
        #  /*46,*/ assegna alla macro il valore Verde
        return GlobalEnumeration.verde
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c10_prev(self.get_mainclass_c1_previousco_c10())
        self.set_mainclass_c1_previousco_c2_prev(self.get_mainclass_c1_previousco_c2())
        self.set_mainclass_c1_previousco_c3_prev(self.get_mainclass_c1_previousco_c3())
        self.set_mainclass_c1_previousco_c4_prev(self.get_mainclass_c1_previousco_c4())
        self.set_mainclass_c1_previousco_c6_prev(self.get_mainclass_c1_previousco_c6())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())

