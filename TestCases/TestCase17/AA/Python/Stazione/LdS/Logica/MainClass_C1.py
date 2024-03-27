# Codice del modello 'TestCase17', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_mainclass_c1_previousva_pv1(GlobalEnumeration.rossoverde)
        self.set_mainclass_c1_previousva_pv2(0)
        self.set_mainclass_c1_restoreva_rv1(0)
        self.set_mainclass_c1_restoreva_rv2(GlobalEnumeration.rossogialloverde)
        self.set_mainclass_c1_restoreva_rv3(0)
        self.set_mainclass_c1_restoreva_rv4(False)
        self.set_mainclass_c1_variabile_v10(0)
        self.set_mainclass_c1_variabile_v2(GlobalEnumeration.rossogialloverde)
        self.set_mainclass_c1_variabile_v3(GlobalEnumeration.avviox)
        self.set_mainclass_c1_variabile_v8(0)
        self.set_mainclass_c1_variabile_v9(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of MainClass_C1
        if self.is_triggered('eventMainclass_c1_command_comm10'):
            self.set_man_cmd_response('eventMainclass_c1_command_comm10',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventMainclass_c1_command_comm10',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, mainclass_c1_parametro_p1, mainclass_c1_parametro_p10, mainclass_c1_parametro_p4, mainclass_c1_parametro_p8, mainclass_c1_parametro_p9):
        # initialize the record type parameters
        # initialize the simple type parameters
        self.set_mainclass_c1_parametro_p1(mainclass_c1_parametro_p1)
        self.set_mainclass_c1_parametro_p10(mainclass_c1_parametro_p10)
        self.set_mainclass_c1_parametro_p4(mainclass_c1_parametro_p4)
        self.set_mainclass_c1_parametro_p8(mainclass_c1_parametro_p8)
        self.set_mainclass_c1_parametro_p9(mainclass_c1_parametro_p9)

        # initialize the timers
        self.set_mainclass_c1_restoreti_ti1(5421000)
        self.set_mainclass_c1_restoreti_ti1_restore(5421000)
        self.set_mainclass_c1_restoreti_ti2(33000)
        self.set_mainclass_c1_restoreti_ti2_restore(33000)
        self.set_mainclass_c1_restoreti_ti3(40000)
        self.set_mainclass_c1_restoreti_ti3_restore(40000)
        self.set_mainclass_c1_timer_t1(2000)
        self.set_mainclass_c1_timer_t4(354000)
        self.set_mainclass_c1_timer_t5(1000)
        self.set_mainclass_c1_timer_t8(32130000)
        self.set_mainclass_c1_timer_t9(55000)

        self.timers = [self.mainclass_c1_restoreti_ti1,self.mainclass_c1_restoreti_ti1_restore,self.mainclass_c1_restoreti_ti2,self.mainclass_c1_restoreti_ti2_restore,self.mainclass_c1_restoreti_ti3,self.mainclass_c1_restoreti_ti3_restore,self.mainclass_c1_timer_t1,self.mainclass_c1_timer_t4,self.mainclass_c1_timer_t5,self.mainclass_c1_timer_t8,self.mainclass_c1_timer_t9,]

        # initialize the counters
        self.set_mainclass_c1_contatore_co2(0)
        self.set_mainclass_c1_contatore_co5(0)

    # setters for record type parameters

    # getters for record type parameters

    # setters for simple type parameters
    def set_mainclass_c1_parametro_p1(self, mainclass_c1_parametro_p1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1",mainclass_c1_parametro_p1)

    def set_mainclass_c1_parametro_p10(self, mainclass_c1_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10",mainclass_c1_parametro_p10)

    def set_mainclass_c1_parametro_p4(self, mainclass_c1_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4",mainclass_c1_parametro_p4)

    def set_mainclass_c1_parametro_p8(self, mainclass_c1_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8",mainclass_c1_parametro_p8)

    def set_mainclass_c1_parametro_p9(self, mainclass_c1_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9",mainclass_c1_parametro_p9)


    # getters for simple type parameters
    def get_mainclass_c1_parametro_p1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p1")

    def get_mainclass_c1_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p10")

    def get_mainclass_c1_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p4")

    def get_mainclass_c1_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p8")

    def get_mainclass_c1_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_parametro_p9")


    # setters for comandi al piazzale
    def set_mainclass_c1_comando_c2(self, mainclass_c1_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c2",mainclass_c1_comando_c2)

    def set_mainclass_c1_comando_c3(self, mainclass_c1_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c3",mainclass_c1_comando_c3)

    def set_mainclass_c1_comando_c6(self, mainclass_c1_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c6",mainclass_c1_comando_c6)

    def set_mainclass_c1_comando_c7(self, mainclass_c1_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c7",mainclass_c1_comando_c7)

    def set_mainclass_c1_comando_c9(self, mainclass_c1_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_comando_c9",mainclass_c1_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_mainclass_c1_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c10")

    def get_mainclass_c1_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c4")

    def get_mainclass_c1_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_controllo_c5")

    def get_mainclass_c1_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_previousco_c8")


    # setters for state variables
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
    def set_mainclass_c1_variabile_v8(self, mainclass_c1_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8",mainclass_c1_variabile_v8)
    def set_mainclass_c1_variabile_v9(self, mainclass_c1_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v9",mainclass_c1_variabile_v9)

    # getters for state variables
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

    def get_mainclass_c1_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"mainclass_c1_variabile_v8")

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

    def set_mainclass_c1_timer_t1(self, timerDuration):
        self.mainclass_c1_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t1", self.memory)

    def set_mainclass_c1_timer_t4(self, timerDuration):
        self.mainclass_c1_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t4", self.memory)

    def set_mainclass_c1_timer_t5(self, timerDuration):
        self.mainclass_c1_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t5", self.memory)

    def set_mainclass_c1_timer_t8(self, timerDuration):
        self.mainclass_c1_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t8", self.memory)

    def set_mainclass_c1_timer_t9(self, timerDuration):
        self.mainclass_c1_timer_t9 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "mainclass_c1_timer_t9", self.memory)


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

    def get_mainclass_c1_timer_t1(self):
        return self.mainclass_c1_timer_t1

    def get_mainclass_c1_timer_t4(self):
        return self.mainclass_c1_timer_t4

    def get_mainclass_c1_timer_t5(self):
        return self.mainclass_c1_timer_t5

    def get_mainclass_c1_timer_t8(self):
        return self.mainclass_c1_timer_t8

    def get_mainclass_c1_timer_t9(self):
        return self.mainclass_c1_timer_t9


    # setters for counters
    def set_mainclass_c1_contatore_co2(self, counterInitValue):
        self.mainclass_c1_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co2", self.memory)

    def set_mainclass_c1_contatore_co5(self, counterInitValue):
        self.mainclass_c1_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "mainclass_c1_contatore_co5", self.memory)


    # getters for counters
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

        self.set_mainclass_c1_previousco_c8_prev(True)
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
    def macroMainclass_c1_macroef_m3(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
         
        { commento: {34,}  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  commento: {53,} 123 commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 2 commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  minore di  commento: {55,} 10 commento: {34,} o  se il parametro MainClass_C1_parametro_P10 è  uguale a  commento: {53,} 5,  Applica gli effetti
               della macro MainClass_C1_macroef_M8( con argomento_af3   uguale a c75Giallo ,argomento_af8   uguale a c75Giallo ) commento: {73,}
        
           
          se il controllo ConsDef è uguale a FALSE , commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  True 
        
           
          se il controllo ConsDef  è  uguale a FALSE  commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 è  minore di  commento: {55,} 154 o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer MainClass_C1_timer_T4 non è attivo commento: {38,} o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  commento: {55,} 1221, commento: {68,}Attiva il timer MainClass_C1_timer_T8
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 123 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a  /*53,*/ 5,  Applica gli effetti
       della macro MainClass_C1_macroef_M8( con argomento_af3   uguale a c75Giallo ,argomento_af8   uguale a c75Giallo )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 123 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (lo stato di 'self')  è uguale a  (state1) )  o  
( ( ( (mainclass_c1_contatore_co5)  è uguale a  (123) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è minore di  (2)) ) )  e  
( (mainclass_c1_parametro_p10)  è minore di  (10) ) )""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (mainclass_c1_contatore_co5)  è uguale a  (123) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è minore di  (2)) ) )  e  
( (mainclass_c1_parametro_p10)  è minore di  (10) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (mainclass_c1_contatore_co5)  è uguale a  (123) )  e  ( negazione di ((mainclass_c1_variabile_v10)  è minore di  (2)) )""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co5)  è uguale a  (123)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è minore di  (2))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v10)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p10)  è minore di  (10)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p10)  è uguale a  (5)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M8( con argomento_af3   uguale a c75Giallo ,argomento_af8   uguale a c75Giallo )"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*73,*/

   
  se il controllo ConsDef è uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  True""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef è uguale a FALSE""", [
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 154 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 1221, /*68,*/Attiva il timer MainClass_C1_timer_T8""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 154 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 1221""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( (consdef)  è uguale a  (False) )  o  
( (mainclass_c1_contatore_co5)  è minore di  (154) ) )  o  
( (consdef)  è uguale a  (False) ) )  o  
( negazione di (il timer 'mainclass_c1_timer_t4' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( (consdef)  è uguale a  (False) )  o  
( (mainclass_c1_contatore_co5)  è minore di  (154) ) )  o  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( (consdef)  è uguale a  (False) )  o  
( (mainclass_c1_contatore_co5)  è minore di  (154) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (154)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_timer_t4' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co5)  è minore di  (1221))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5)  è minore di  (1221)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroMainclass_c1_macroef_m3_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  uguale a  /*53,*/ 123 /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  minore di  /*55,*/ 10 /*34,*/ o  se il parametro MainClass_C1_parametro_P10 è  uguale a  /*53,*/ 5,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M8( con argomento_af3   uguale a c75Giallo ,argomento_af8   uguale a c75Giallo )
        if db((db((db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_mainclass_c1_contatore_co5().get_valore() == 123, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() < 2, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_parametro_p10() < 10, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_parametro_p10() == 5, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroMainclass_c1_macroef_m8(GlobalEnumeration.c75giallo,GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[1])
        #  /*73,*/
        #     
        #    se il controllo ConsDef è uguale a FALSE , /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  True
        if db(self.get_consdef() == False, di_ctx.subs[1].subs[0]):
            self.set_mainclass_c1_comando_c2(True)
        #  se il controllo ConsDef  è  uguale a FALSE  /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 è  minore di  /*55,*/ 154 o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer MainClass_C1_timer_T4 non è attivo /*38,*/ o  se il contatore MainClass_C1_contatore_Co5 non è  minore di  /*55,*/ 1221, /*68,*/Attiva il timer MainClass_C1_timer_T8
        if db((db((db((db((db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_contatore_co5().get_valore() < 154, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[2].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[2].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[0].subs[1])), di_ctx.subs[2].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_contatore_co5().get_valore() < 1221, di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_mainclass_c1_timer_t8().attiva()
    
    def macroMainclass_c1_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro MainClass_C1_parametro_P10 è  maggiore di  commento: {54,} 4 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
               della macro MainClass_C1_macroef_M3   commento: {73,}
        
           
        
        }
        """
        def populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se il parametro MainClass_C1_parametro_P10 è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
       della macro MainClass_C1_macroef_M3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P10 è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p10)  è maggiore di  (4)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro MainClass_C1_macroef_M3"""),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro MainClass_C1_parametro_P10 è  maggiore di  /*54,*/ 4 e  se il controllo ConsDef  è  uguale a FALSE ,  Applica gli effetti
        #         della macro MainClass_C1_macroef_M3
        if db((db(self.get_mainclass_c1_parametro_p10() > 4, di_ctx.subs[0].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroMainclass_c1_macroef_m3(di_ctx.subs[0].subs[1])
    
    def macroMainclass_c1_macroef_m8(self, argomento_af3, argomento_af8, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        {  se l'argomento argomento_af3 non  è  diverso da c75Giallo commento: {39,}  commento: {38,} e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  commento: {55,} 111 commento: {34,} o  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  commento: {36,} o  se il timer MainClass_C1_timer_T5 è attivo, commento: {66,} Assegna al comando MainClass_C1_comando_C2 il valore  True 
        
         ,altrimenti  commento: {68,}Attiva il timer MainClass_C1_timer_T4
        
        
        
        }
        """
        def populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\nse l'argomento argomento_af3 non  è  diverso da c75Giallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 111 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  True 

 ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T4""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nse l'argomento argomento_af3 non  è  diverso da c75Giallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 111 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (negazione di ((argomento_af3)  è uguale a  (c75giallo))) )  e  
( negazione di ((mainclass_c1_contatore_co2)  è minore di  (111)) ) )  o  
( negazione di ((mainclass_c1_parametro_p8)  è uguale a  (True)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((argomento_af3)  è uguale a  (c75giallo))) )  e  
( negazione di ((mainclass_c1_contatore_co2)  è minore di  (111)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((argomento_af3)  è uguale a  (c75giallo)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af3)  è uguale a  (c75giallo))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af3)  è uguale a  (c75giallo)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2)  è minore di  (111))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co2)  è minore di  (111)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p8)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  se l'argomento argomento_af3 non  è  diverso da c75Giallo /*39,*/  /*38,*/ e  se il contatore MainClass_C1_contatore_Co2 non è  minore di  /*55,*/ 111 /*34,*/ o  se il parametro MainClass_C1_parametro_P8 è  diverso da  True  /*36,*/ o  se il timer MainClass_C1_timer_T5 è attivo, /*66,*/ Assegna al comando MainClass_C1_comando_C2 il valore  True 
        #   ,altrimenti  /*68,*/Attiva il timer MainClass_C1_timer_T4
        if db((db((db((db(not db(not db(argomento_af3 == GlobalEnumeration.c75giallo, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_contatore_co2().get_valore() < 111, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_parametro_p8() == True, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_mainclass_c1_comando_c2(True)
        else:
            self.get_mainclass_c1_timer_t4().attiva()
    
    # verify macros
    @srf_value_macro("macroMainclass_c1_macrove_m10")
    def macroMainclass_c1_macrove_m10(self, argomento_ave6, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {37,}  se la variabile MainClass_C1_variabile_V9 è  diverso da  False , Tutte le seguenti { 
         commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto commento: {36,} o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento commento: {39,}  commento: {36,} o  se il timer MainClass_C1_timer_T8 non è disattivo, Verifica che   commento: {49,50,52,}   l'argomento argomento_ave6 non  sia  uguale a  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V8 non sia  minore di  commento: {55,} 4
         commento: {104,} e  che  commento: {,}  il timer MainClass_C1_timer_T1 sia disattivo
        
        
         } Verifica che   commento: {48,52,}   l'argomento argomento_ave6 sia  uguale a  True  commento: {,} 
         commento: {104,} o  che  commento: {,}  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
         commento: {104,} e  che  commento: {35,}  il controllo MainClass_C1_controllo_C5 sia  uguale a  False 
         commento: {104,} o  che  commento: {35,}  il controllo MainClass_C1_controllo_C5 sia  diverso da  False 
         commento: {104,} o  che   l'argomento argomento_ave6 sia  diverso da  True  commento: {39,} 
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  diverso da  False , Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T8 non è disattivo, Verifica che   /*49,50,52,*/   l'argomento argomento_ave6 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo


 } Verifica che   /*48,52,*/   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  diverso da  True""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile MainClass_C1_variabile_V9 è  diverso da  False , Tutte le seguenti { 
 /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T8 non è disattivo, Verifica che   /*49,50,52,*/   l'argomento argomento_ave6 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile MainClass_C1_variabile_V9 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T8 non è disattivo, Verifica che   /*49,50,52,*/   l'argomento argomento_ave6 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento /*39,*/  /*36,*/ o  se il timer MainClass_C1_timer_T8 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo o  se l'argomento argomento_ave9 è  uguale a avanzamento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto /*36,*/ o  se il timer MainClass_C1_timer_T4 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino del timer  MainClass_C1_restoreTI_TI1 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer MainClass_C1_timer_T4 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave9 è  uguale a avanzamento""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer MainClass_C1_timer_T8 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,52,*/   l'argomento argomento_ave6 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,52,*/   l'argomento argomento_ave6 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,52,*/   l'argomento argomento_ave6 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile MainClass_C1_variabile_V8 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v8)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer MainClass_C1_timer_T1 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,52,*/   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  False 
 /*104,*/ o  che   l'argomento argomento_ave6 sia  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,52,*/   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  uguale a  False 
 /*104,*/ o  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,52,*/   l'argomento argomento_ave6 sia  uguale a  True  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,52,*/   l'argomento argomento_ave6 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento
 /*104,*/ e  che  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo MainClass_C1_controllo_C4 sia  diverso da avanzamento""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c4)  è uguale a  (avanzamento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  uguale a  False""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo MainClass_C1_controllo_C5 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave6 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_mainclass_c1_variabile_v9() == False, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_mainclass_c1_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(argomento_ave9 == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(argomento_ave6 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v8() < 4, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(self.get_mainclass_c1_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(argomento_ave6 == True, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_controllo_c4() == GlobalEnumeration.avanzamento, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_mainclass_c1_controllo_c5() == False, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_mainclass_c1_controllo_c5() == False, di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(argomento_ave6 == True, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroMainclass_c1_macrove_m9")
    def macroMainclass_c1_macrove_m9(self, argomento_ave10, argomento_ave5, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro MainClass_C1_parametro_P1 è  diverso da  True , Verifica che   commento: {49,50,52,}   l'argomento argomento_ave10 non  sia  diverso da AC commento: {,} 
         commento: {104,} o  che  commento: {,}  il timer MainClass_C1_timer_T5 non sia disattivo
         commento: {104,} e  che  commento: {,}  la variabile MainClass_C1_variabile_V10 sia  uguale a  commento: {53,} 2
         commento: {104,} e  che   l'argomento argomento_ave10 sia  uguale a AC commento: {39,} 
         commento: {104,} o  che  commento: {37,}  la variabile MainClass_C1_variabile_V10 non sia  minore di  commento: {55,} 2
        
        
        }
        """
        def populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro MainClass_C1_parametro_P1 è  diverso da  True , Verifica che   /*49,50,52,*/   l'argomento argomento_ave10 non  sia  diverso da AC /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  /*53,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave10 sia  uguale a AC /*39,*/ 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro MainClass_C1_parametro_P1 è  diverso da  True , Verifica che   /*49,50,52,*/   l'argomento argomento_ave10 non  sia  diverso da AC /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  /*53,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave10 sia  uguale a AC /*39,*/ 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro MainClass_C1_parametro_P1 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,52,*/   l'argomento argomento_ave10 non  sia  diverso da AC /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  /*53,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave10 sia  uguale a AC /*39,*/ 
 /*104,*/ o  che  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*49,50,52,*/   l'argomento argomento_ave10 non  sia  diverso da AC /*,*/ 
 /*104,*/ o  che  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  /*53,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave10 sia  uguale a AC""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,52,*/   l'argomento argomento_ave10 non  sia  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave10)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  /*53,*/ 2
 /*104,*/ e  che   l'argomento argomento_ave10 sia  uguale a AC""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo
 /*104,*/ e  che  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  /*53,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer MainClass_C1_timer_T5 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile MainClass_C1_variabile_V10 sia  uguale a  /*53,*/ 2""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave10 sia  uguale a AC""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile MainClass_C1_variabile_V10 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v10)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_mainclass_c1_parametro_p1() == True, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(not db(not db(argomento_ave10 == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_mainclass_c1_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_mainclass_c1_variabile_v10() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(argomento_ave10 == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_mainclass_c1_variabile_v10() < 2, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroMainclass_c1_macrova_m1")
    def macroMainclass_c1_macrova_m1(self, argomento_a10, argomento_a6, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m1_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c75Giallo
        return GlobalEnumeration.c75giallo
    
    @srf_value_macro("macroMainclass_c1_macrova_m4")
    def macroMainclass_c1_macrova_m4(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a5, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m4_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore c75Giallo
        return GlobalEnumeration.c75giallo
    
    @srf_value_macro("macroMainclass_c1_macrova_m5")
    def macroMainclass_c1_macrova_m5(self, argomento_a10, argomento_a6, argomento_a7, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se l'argomento argomento_a7 è  uguale a  False  commento: {39,}  , assegna alla macro il valore c75Giallo
        
         commento: {46,} assegna alla macro il valore c75Giallo commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se l'argomento argomento_a7 è  uguale a  False  /*39,*/  , assegna alla macro il valore c75Giallo""", [
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_a7 è  uguale a  False""", [
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m5_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se l'argomento argomento_a7 è  uguale a  False  /*39,*/  , assegna alla macro il valore c75Giallo
        if db(argomento_a7 == False, di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.c75giallo
        #  /*46,*/ assegna alla macro il valore c75Giallo
        return GlobalEnumeration.c75giallo
    
    @srf_value_macro("macroMainclass_c1_macrova_m6")
    def macroMainclass_c1_macrova_m6(self, argomento_a1, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {110,}  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto commento: {34,} e  se il parametro MainClass_C1_parametro_P10 è  maggiore di  commento: {54,} 2 commento: {34,} e  se il parametro MainClass_C1_parametro_P8 è  uguale a  False  commento: {37,} e  se la variabile MainClass_C1_variabile_V10 non è  minore di  commento: {55,} 7 commento: {110,} o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo commento: {34,} e  se lo stato  è  diverso da  commento: {56,}  state1  commento: {106,} , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  maggiore di  /*54,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 7 /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  maggiore di  /*54,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 7 /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( ( il timer 'mainclass_c1_restoreti_ti2_restore' è scaduto )  e  ( (mainclass_c1_parametro_p10)  è maggiore di  (2) ) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (False) ) )  e  
( negazione di ((mainclass_c1_variabile_v10)  è minore di  (7)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( il timer 'mainclass_c1_restoreti_ti2_restore' è scaduto )  e  ( (mainclass_c1_parametro_p10)  è maggiore di  (2) ) )  e  ( (mainclass_c1_parametro_p8)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( il timer 'mainclass_c1_restoreti_ti2_restore' è scaduto )  e  ( (mainclass_c1_parametro_p10)  è maggiore di  (2) )""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti2_restore' è scaduto""", [
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p10)  è maggiore di  (2)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p8)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v10)  è minore di  (7))""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_variabile_v10)  è minore di  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo) )  e  
( negazione di ((lo stato di 'self')  è uguale a  (state1)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'mainclass_c1_restoreti_ti1_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_restoreti_ti1_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'self')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroMainclass_c1_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*110,*/  se il ripristino del timer  MainClass_C1_restoreTI_TI2 è scaduto /*34,*/ e  se il parametro MainClass_C1_parametro_P10 è  maggiore di  /*54,*/ 2 /*34,*/ e  se il parametro MainClass_C1_parametro_P8 è  uguale a  False  /*37,*/ e  se la variabile MainClass_C1_variabile_V10 non è  minore di  /*55,*/ 7 /*110,*/ o  se il ripristino del timer  MainClass_C1_restoreTI_TI1 non è disattivo /*34,*/ e  se lo stato  è  diverso da  /*56,*/  state1  /*106,*/ , assegna alla macro il valore  True
        if db((db((db((db((db(self.get_mainclass_c1_restoreti_ti2_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p10() > 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_mainclass_c1_parametro_p8() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_mainclass_c1_variabile_v10() < 7, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_mainclass_c1_restoreti_ti1_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroMainclass_c1_macrova_m7")
    def macroMainclass_c1_macrova_m7(self, argomento_a2, argomento_a3, argomento_a4, argomento_a5, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore AC commento: {],}
        }
        """
        def populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroMainclass_c1_macrova_m7_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore AC
        return GlobalEnumeration.ac
    
    # for each manual command, the corresponding method is created
    def eventMainclass_c1_command_comm10(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventMainclass_c1_command_comm10')
    
    # for each automatic command, the corresponding method is created
    def eventMainclass_c1_command_comm3(self, notifying_process):
        notifying_process.response_notify_auto_cmd(self, 'eventMainclass_c1_command_comm3')
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_mainclass_c1_previousco_c8_prev(self.get_mainclass_c1_previousco_c8())
        self.set_mainclass_c1_previousva_pv1_prev(self.get_mainclass_c1_previousva_pv1())
        self.set_mainclass_c1_previousva_pv2_prev(self.get_mainclass_c1_previousva_pv2())

