# Codice del modello 'TestCase6', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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

        self.set_subclass_c2_previousva_pv1(GlobalEnumeration.avviox)
        self.set_subclass_c2_previousva_pv2(GlobalEnumeration.ac)
        self.set_subclass_c2_previousva_pv3(0)
        self.set_subclass_c2_restoreva_rv1(False)
        self.set_subclass_c2_restoreva_rv2(GlobalEnumeration.c120)
        self.set_subclass_c2_restoreva_rv3(False)
        self.set_subclass_c2_restoreva_rv4(False)
        self.set_subclass_c2_restoreva_rv5(0)
        self.set_subclass_c2_variabile_v7(GlobalEnumeration.ac)

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
    def init_configuration(self, subclass_c2_lista_l1, subclass_c2_lista_l4, subclass_c2_lista_l6, subclass_c2_lista_l8, subclass_c2_parametro_p4, subclass_c2_parametro_p5):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l1(subclass_c2_lista_l1)
        self.set_subclass_c2_lista_l4(subclass_c2_lista_l4)
        self.set_subclass_c2_lista_l6(subclass_c2_lista_l6)
        self.set_subclass_c2_lista_l8(subclass_c2_lista_l8)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p4(subclass_c2_parametro_p4)
        self.set_subclass_c2_parametro_p5(subclass_c2_parametro_p5)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(1000)
        self.set_subclass_c2_restoreti_ti1_restore(1000)
        self.set_subclass_c2_restoreti_ti2(102000)
        self.set_subclass_c2_restoreti_ti2_restore(102000)
        self.set_subclass_c2_timer_t3(5000)
        self.set_subclass_c2_timer_t4(23000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_restoreti_ti2,self.subclass_c2_restoreti_ti2_restore,self.subclass_c2_timer_t3,self.subclass_c2_timer_t4,]

        # initialize the counters
        self.set_subclass_c2_contatore_co10(0)
        self.set_subclass_c2_contatore_co2(0)
        self.set_subclass_c2_contatore_co3(0)
        self.set_subclass_c2_contatore_co5(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l1(self, subclass_c2_lista_l1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l1",subclass_c2_lista_l1)

    def set_subclass_c2_lista_l4(self, subclass_c2_lista_l4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4",subclass_c2_lista_l4)

    def set_subclass_c2_lista_l6(self, subclass_c2_lista_l6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l6",subclass_c2_lista_l6)

    def set_subclass_c2_lista_l8(self, subclass_c2_lista_l8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8",subclass_c2_lista_l8)


    # getters for record type parameters
    def get_subclass_c2_lista_l1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l1")

    def get_subclass_c2_lista_l4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4")

    def get_subclass_c2_lista_l6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l6")

    def get_subclass_c2_lista_l8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p4(self, subclass_c2_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4",subclass_c2_parametro_p4)

    def set_subclass_c2_parametro_p5(self, subclass_c2_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5",subclass_c2_parametro_p5)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4")

    def get_subclass_c2_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c2(self, subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c2",subclass_c2_comando_c2)

    def set_subclass_c2_comando_c3(self, subclass_c2_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c3",subclass_c2_comando_c3)

    def set_subclass_c2_comando_c5(self, subclass_c2_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c5",subclass_c2_comando_c5)

    def set_subclass_c2_comando_c8(self, subclass_c2_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c8",subclass_c2_comando_c8)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c1")

    def get_subclass_c2_controllo_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c10")

    def get_subclass_c2_controllo_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c4")

    def get_subclass_c2_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c5")

    def get_subclass_c2_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c9")

    def get_subclass_c2_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c6")

    def get_subclass_c2_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7")


    # setters for state variables
    def set_subclass_c2_previousco_c6_prev(self, subclass_c2_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c6_prev",subclass_c2_previousco_c6_prev)
    def set_subclass_c2_previousco_c7_prev(self, subclass_c2_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7_prev",subclass_c2_previousco_c7_prev)
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
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_restoreva_rv3(self, subclass_c2_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv3",subclass_c2_restoreva_rv3)
    def set_subclass_c2_restoreva_rv4(self, subclass_c2_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv4",subclass_c2_restoreva_rv4)
    def set_subclass_c2_restoreva_rv5(self, subclass_c2_restoreva_rv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv5",subclass_c2_restoreva_rv5)
    def set_subclass_c2_variabile_v7(self, subclass_c2_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7",subclass_c2_variabile_v7)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c6_prev")

    def get_subclass_c2_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c7_prev")

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

    def get_subclass_c2_restoreva_rv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv5")

    def get_subclass_c2_restoreva_rv5_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv5_restore")

    def get_subclass_c2_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v7")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_restoreti_ti2(self, timerDuration):
        self.subclass_c2_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2", self.memory)

    def set_subclass_c2_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti2_restore", self.memory)

    def set_subclass_c2_timer_t3(self, timerDuration):
        self.subclass_c2_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t3", self.memory)

    def set_subclass_c2_timer_t4(self, timerDuration):
        self.subclass_c2_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t4", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_restoreti_ti2(self):
        return self.subclass_c2_restoreti_ti2

    def get_subclass_c2_restoreti_ti2_restore(self):
        return self.subclass_c2_restoreti_ti2_restore

    def get_subclass_c2_timer_t3(self):
        return self.subclass_c2_timer_t3

    def get_subclass_c2_timer_t4(self):
        return self.subclass_c2_timer_t4


    # setters for counters
    def set_subclass_c2_contatore_co10(self, counterInitValue):
        self.subclass_c2_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co10", self.memory)

    def set_subclass_c2_contatore_co2(self, counterInitValue):
        self.subclass_c2_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co2", self.memory)

    def set_subclass_c2_contatore_co3(self, counterInitValue):
        self.subclass_c2_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co3", self.memory)

    def set_subclass_c2_contatore_co5(self, counterInitValue):
        self.subclass_c2_contatore_co5 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co5", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co10(self):
        return self.subclass_c2_contatore_co10

    def get_subclass_c2_contatore_co2(self):
        return self.subclass_c2_contatore_co2

    def get_subclass_c2_contatore_co3(self):
        return self.subclass_c2_contatore_co3

    def get_subclass_c2_contatore_co5(self):
        return self.subclass_c2_contatore_co5



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
                    DIStatement("""Statement ForAll\nComanda al campo MainClass_C1 di SubClass_C2_lista_L1
 di eseguire  /*113,*/  MainClass_C1_command_comm6( con argomento_ave5   uguale a Rosso ,argomento_ave9   uguale a True ,argomento_ave8   uguale a c270 )""", [
                    DIStatement("""ITStatement\nesegui il comando 'eventMainclass_c1_command_comm6 del campo mainclass_c1 della lista subclass_c2_lista_l1'""", [
                    ]),#0
                    ]),#2
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
                         effect=(self.dbs[2], ),
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

        self.set_subclass_c2_previousco_c6_prev(False)
        self.set_subclass_c2_previousco_c7_prev(True)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())

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
        
        Comanda al campo MainClass_C1 di SubClass_C2_lista_L1
         di eseguire  commento: {113,}  MainClass_C1_command_comm6( con argomento_ave5   uguale a Rosso ,argomento_ave9   uguale a True ,argomento_ave8   uguale a c270 )
        }
        """
        #  Comanda al campo MainClass_C1 di SubClass_C2_lista_L1
        #   di eseguire  /*113,*/  MainClass_C1_command_comm6( con argomento_ave5   uguale a Rosso ,argomento_ave9   uguale a True ,argomento_ave8   uguale a c270 )
        for idx, it in enumerate(self.get_subclass_c2_lista_l1()):
                it.get_mainclass_c1().eventMainclass_c1_command_comm6(self,GlobalEnumeration.rosso,GlobalEnumeration.c270,True)
    
    # effect macros
    def macroSubclass_c2_macroef_m1(self, argomento_af2, argomento_af4, argomento_af6, argomento_af7, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  uguale a  commento: {53,}  state1  commento: {38,} e  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  commento: {56,} 13 commento: {36,} o  se il timer SubClass_C2_timer_T3 è attivo,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x commento: {67,}
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  e  se l'argomento argomento_af6 è  diverso da  True  commento: {39,} ,  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x commento: {67,}
        
           
          se il ripristino dello stato  non è  diverso da  commento: {56,}  state1  commento: {107,}, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
        
           
         commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  diverso da  commento: {56,} 14 commento: {34,} e  se il parametro SubClass_C2_parametro_P5 non è  diverso da c120x, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co5
        
         ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x commento: {67,}
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  uguale a  /*53,*/  state1  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 13 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  uguale a  /*53,*/  state1  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 13 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l1')  è uguale a  (state1))} )  e  
( negazione di (negazione di ((subclass_c2_contatore_co5)  è uguale a  (13))) )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l1')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l1')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_contatore_co5)  è uguale a  (13)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co5)  è uguale a  (13))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co5)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*67,*/

   
 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  e  se l'argomento argomento_af6 è  diverso da  True  /*39,*/ ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*67,*/

   
 /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  e  se l'argomento argomento_af6 è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_restoreva_rv1_restore)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv1_restore)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_af6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_af6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITStatement\n/*67,*/

   
  se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino dello stato  non è  diverso da  /*56,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((stato_restore)  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(stato_restore)  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  diverso da c120x, /*72,*/Azzera il contatore SubClass_C2_contatore_Co5

 ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  diverso da c120x""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_restoreti_ti1_restore' è attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_contatore_co2)  è uguale a  (14)) )  e  
( negazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (c120x))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co2)  è uguale a  (14))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p5)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c2_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  uguale a  /*53,*/  state1  /*38,*/ e  se il contatore SubClass_C2_contatore_Co5 non è  diverso da  /*56,*/ 13 /*36,*/ o  se il timer SubClass_C2_timer_T3 è attivo,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
        if db((db((db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l1())), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co5().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.c120x)
        #  /*67,*/
        #     
        #   /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV1 non è  uguale a  True  e  se l'argomento argomento_af6 è  diverso da  True  /*39,*/ ,  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
        if db((db(not db(self.get_subclass_c2_restoreva_rv1_restore() == True, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) and db(not db(argomento_af6 == True, di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.c120x)
        #  /*67,*/
        #     
        #    se il ripristino dello stato  non è  diverso da  /*56,*/  state1  /*107,*/, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
        if db(not db(not db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[2].subs[0].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[0]), di_ctx.subs[2].subs[0]):
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.c120x)
        #  /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è attivo /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  diverso da  /*56,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 non è  diverso da c120x, /*72,*/Azzera il contatore SubClass_C2_contatore_Co5
        #   ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
        if db((db(self.get_subclass_c2_restoreti_ti1_restore().isAttivato(), di_ctx.subs[3].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 14, di_ctx.subs[3].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.c120x, di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1].subs[1])), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.get_subclass_c2_contatore_co5().resetta()
        else:
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.c120x)
    
    def macroSubclass_c2_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {43,}  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T3 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T3 è attivo commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co2
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C2_comando_C8 il valore  False 
        
        
         commento: {34,}  se il parametro SubClass_C2_parametro_P4 non è  uguale a c120x commento: {34,} o  se il parametro SubClass_C2_parametro_P5 non è  uguale a c120x commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x commento: {36,} o  se il timer SubClass_C2_timer_T4 non è scaduto, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
        
         ,altrimenti   Applica gli effetti
               della macro SubClass_C2_macroef_M1( con argomento_af6   uguale a True ,argomento_af2   uguale a True ,argomento_af7   uguale a AC ,argomento_af4   uguale a c120x ) commento: {73,}
        
        
         commento: {45,}  se  MainClass_C1_contatore_Co9 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  commento: {105,} è  uguale a  commento: {53,} 11 commento: {34,} o  se il parametro SubClass_C2_parametro_P4 non è  diverso da c120x, commento: {72,}Azzera il contatore SubClass_C2_contatore_Co3
        
           
        
        }
        """
        def populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 è attivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x, /*72,*/Azzera il contatore SubClass_C2_contatore_Co2

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 è attivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( ( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)} )  e  ( il timer 'subclass_c2_timer_t3' è inattivo ) )  e  
( il timer 'subclass_c2_timer_t3' è attivo ) )  o  
( negazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x)) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t3' è inattivo) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)} )  e  ( il timer 'subclass_c2_timer_t3' è inattivo ) )  e  
( il timer 'subclass_c2_timer_t3' è attivo ) )  o  
( negazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x)) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)} )  e  ( il timer 'subclass_c2_timer_t3' è inattivo ) )  e  
( il timer 'subclass_c2_timer_t3' è attivo )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti {(il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)} )  e  ( il timer 'subclass_c2_timer_t3' è inattivo )""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t3' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P4 non è  uguale a c120x /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a c120x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T4 non è scaduto, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x

 ,altrimenti   Applica gli effetti
       della macro SubClass_C2_macroef_M1( con argomento_af6   uguale a True ,argomento_af2   uguale a True ,argomento_af7   uguale a AC ,argomento_af4   uguale a c120x )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P4 non è  uguale a c120x /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a c120x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di ((subclass_c2_parametro_p4)  è uguale a  (c120x)) )  o  
( ( negazione di ((subclass_c2_parametro_p5)  è uguale a  (c120x)) )  e  
( (subclass_c2_variabile_v7)  è uguale a  (c120x) ) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p5)  è uguale a  (c120x)) )  e  
( (subclass_c2_variabile_v7)  è uguale a  (c120x) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p5)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C2_macroef_M1( con argomento_af6   uguale a True ,argomento_af2   uguale a True ,argomento_af7   uguale a AC ,argomento_af4   uguale a c120x )"""),#1
                            ]),#1
                            DIStatement("""ITStatement\n/*73,*/


 /*45,*/  se  MainClass_C1_contatore_Co9 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  /*105,*/ è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 non è  diverso da c120x, /*72,*/Azzera il contatore SubClass_C2_contatore_Co3""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*73,*/


 /*45,*/  se  MainClass_C1_contatore_Co9 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  /*105,*/ è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 non è  diverso da c120x""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l1)  è uguale a  (11))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co9 del campo mainclass_c1 della lista subclass_c2_lista_l1)  è uguale a  (11)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c2_parametro_p4)  è uguale a  (c120x)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#2
                ])

        populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*43,*/  se MainClass_C1_timer_T9 del campo  MainClass_C1 di SubClass_C2_lista_L8 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T3 è attivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V7 non è  uguale a c120x, /*72,*/Azzera il contatore SubClass_C2_contatore_Co2
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C2_comando_C8 il valore  False
        if db((db((db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t3().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.get_subclass_c2_contatore_co2().resetta()
        else:
            self.set_subclass_c2_comando_c8(False)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P4 non è  uguale a c120x /*34,*/ o  se il parametro SubClass_C2_parametro_P5 non è  uguale a c120x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T4 non è scaduto, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V7 il valore c120x
        #   ,altrimenti   Applica gli effetti
        #         della macro SubClass_C2_macroef_M1( con argomento_af6   uguale a True ,argomento_af2   uguale a True ,argomento_af7   uguale a AC ,argomento_af4   uguale a c120x )
        if db((db((db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v7(GlobalEnumeration.c120x)
        else:
            self.macroSubclass_c2_macroef_m1(True,GlobalEnumeration.c120x,True,GlobalEnumeration.ac, di_ctx.subs[1].subs[1])
        #  /*73,*/
        #   /*45,*/  se  MainClass_C1_contatore_Co9 del campo  MainClass_C1 di SubClass_C2_lista_L1 esiste e  /*105,*/ è  uguale a  /*53,*/ 11 /*34,*/ o  se il parametro SubClass_C2_parametro_P4 non è  diverso da c120x, /*72,*/Azzera il contatore SubClass_C2_contatore_Co3
        if db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co9().get_valore() == 11, di_ctx.subs[2].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l1())), di_ctx.subs[2].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p4() == GlobalEnumeration.c120x, di_ctx.subs[2].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[2].subs[0].subs[1].subs[0]), di_ctx.subs[2].subs[0].subs[1])), di_ctx.subs[2].subs[0]):
            self.get_subclass_c2_contatore_co3().resetta()
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m10")
    def macroSubclass_c2_macrove_m10(self, argomento_ave10, argomento_ave2, argomento_ave4, argomento_ave7, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {36,}  se il timer SubClass_C2_timer_T4 non è scaduto, Verifica che   commento: {47,48,49,50,51,}  commento: {34,}  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C5 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia disattivo
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  commento: {56,} 11024
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto, Verifica che   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 11024
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*36,*/  se il timer SubClass_C2_timer_T4 non è scaduto, Verifica che   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 11024
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T4 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 11024
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 11024""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,49,50,51,*/  /*34,*/  il parametro SubClass_C2_parametro_P5 sia  uguale a c120x""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C5 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo
 /*104,*/ e  che  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 11024""", [
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co2 non sia  diverso da  /*56,*/ 11024""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co2)  è uguale a  (11024))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co2)  è uguale a  (11024)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m10_SrfMacroDefInfo(di_ctx)
        return db((db(not db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co2().get_valore() == 11024, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m4")
    def macroSubclass_c2_macrove_m4(self, argomento_ave1, argomento_ave10, argomento_ave2, argomento_ave4, argomento_ave6, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {37,}  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x commento: {35,} o  se il controllo SubClass_C2_controllo_C9 è  uguale a c120x commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 142 commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x commento: {37,} e  se la variabile SubClass_C2_variabile_V7 è  diverso da c120x, Verifica che   commento: {48,50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co3 sia  minore di  commento: {55,} 15
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
         commento: {104,} o  che  commento: {37,}  la variabile SubClass_C2_variabile_V7 non sia  uguale a c120x
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*37,*/  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 142 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da c120x, Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  minore di  /*55,*/ 15
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a c120x""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 142 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da c120x, Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  minore di  /*55,*/ 15
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a c120x /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 142 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*35,*/ o  se il controllo SubClass_C2_controllo_C9 è  uguale a c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C9 è  uguale a c120x""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 142 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 è  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 142 /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x""", [
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 142""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 è  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  minore di  /*55,*/ 15
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a c120x""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  minore di  /*55,*/ 15
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x
 /*104,*/ o  che  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  minore di  /*55,*/ 15
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da  False 
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  minore di  /*55,*/ 15
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da  False""", [
                            DIBoolExpr("""LessThanImpl\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co3 sia  minore di  /*55,*/ 15""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C5 sia  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c5)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V7 non sia  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V7 sia  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V7 non sia  uguale a c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c9() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_contatore_co2().get_valore() < 142, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db((db((db(self.get_subclass_c2_contatore_co3().get_valore() < 15, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c5() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m5")
    def macroSubclass_c2_macrove_m5(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x commento: {37,} e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da c120x, Solo una delle seguenti { 
         commento: {37,}  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x commento: {36,} o  se il timer SubClass_C2_timer_T3 non è scaduto commento: {38,} o  se il contatore SubClass_C2_contatore_Co2 è  minore di  commento: {55,} 1124, Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 non sia attivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C2_timer_T3 non sia disattivo
        
        
         } Verifica che   commento: {49,}  commento: {,}  il timer SubClass_C2_timer_T3 sia scaduto
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m5_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da c120x, Solo una delle seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1124, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo


 } Verifica che   /*49,*/  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da c120x, Solo una delle seguenti { 
 /*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1124, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da c120x""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x /*37,*/ e  se la variabile SubClass_C2_variabile_V7 non è  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da c270x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv2_restore)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V7 non è  diverso da c120x""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v7)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v7)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P5 è  diverso da c120x""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (c120x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1124, Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto /*38,*/ o  se il contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1124""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*37,*/  se la variabile SubClass_C2_variabile_V7 è  uguale a c120x /*36,*/ o  se il timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C2_variabile_V7 è  uguale a c120x""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T3 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co2 è  minore di  /*55,*/ 1124""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il timer SubClass_C2_timer_T4 non sia attivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T4 non sia attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C2_timer_T3 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche   /*49,*/  /*,*/  il timer SubClass_C2_timer_T3 sia scaduto""", [
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m5_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_subclass_c2_restoreva_rv2_restore() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p5() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db(self.get_subclass_c2_variabile_v7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co2().get_valore() < 1124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db(self.get_subclass_c2_timer_t3().isScaduto(), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m3")
    def macroSubclass_c2_macrova_m3(self, argomento_a5, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore spento commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore spento
        return GlobalEnumeration.spento
    
    @srf_value_macro("macroSubclass_c2_macrova_m6")
    def macroSubclass_c2_macrova_m6(self, argomento_a1, argomento_a10, argomento_a4, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}  se l'argomento argomento_a4 non  è  uguale a  True  commento: {39,} ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1 , commento: {88,} quando  commento: {43,}   MainClass_C1_timer_T9 del campo  MainClass_C1     è attivo commento: {43,} o  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  commento: {105,} è disattivo commento: {34,} e  se lo stato  è  uguale a  commento: {53,}  state1  commento: {106,} commento: {36,} e  se il timer SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore  True 
        
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/  se l'argomento argomento_a4 non  è  uguale a  True  /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T9 del campo  MainClass_C1     è attivo /*43,*/ o  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*34,*/ e  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/  se l'argomento argomento_a4 non  è  uguale a  True  /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T9 del campo  MainClass_C1     è attivo /*43,*/ o  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*34,*/ e  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((argomento_a4)  è uguale a  (True)) )  e  
( per ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_a4)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_a4)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (il timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo) allora ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1))""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t9 del campo mainclass_c1 della lista subclass_c2_lista_l6' è attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l6')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t2 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)} )  e  ( (lo stato di 'self')  è uguale a  (state1) ) )  e  
( negazione di (il timer 'subclass_c2_timer_t4' è attivo) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( per ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t2 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)} )  e  ( (lo stato di 'self')  è uguale a  (state1) )""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {(il timer 'mainclass_c1_timer_t2 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo)}""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t2 del campo mainclass_c1 della lista subclass_c2_lista_l8' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t4' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c2_macrova_m6_SrfMacroDefInfo(di_ctx)
        #  /*[*/  se l'argomento argomento_a4 non  è  uguale a  True  /*39,*/ ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1 , /*88,*/ quando  /*43,*/   MainClass_C1_timer_T9 del campo  MainClass_C1     è attivo /*43,*/ o  se MainClass_C1_timer_T2 del campo  MainClass_C1 di SubClass_C2_lista_L8 esiste e  /*105,*/ è disattivo /*34,*/ e  se lo stato  è  uguale a  /*53,*/  state1  /*106,*/ /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo , assegna alla macro il valore  True
        if db((db((db(not db(argomento_a4 == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l6()) if db(it.get_mainclass_c1().get_mainclass_c1_timer_t9().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_timer_t2().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l8())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return True
        #  /*46,*/ assegna alla macro il valore  False
        return False
    
    @srf_value_macro("macroSubclass_c2_macrova_m9")
    def macroSubclass_c2_macrova_m9(self, argomento_a2, argomento_a6, argomento_a7, argomento_a8, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c6_prev(self.get_subclass_c2_previousco_c6())
        self.set_subclass_c2_previousco_c7_prev(self.get_subclass_c2_previousco_c7())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())

class SubClass_C2_RecordHeaderR2(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled12, recordfiled5, recordfiled11, recordfiled4):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled12(recordfiled12)
        self.set_recordfiled5(recordfiled5)
        self.set_recordfiled11(recordfiled11)
        self.set_recordfiled4(recordfiled4)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled12(self, recordfiled12):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"), recordfiled12)

    def set_recordfiled5(self, recordfiled5):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"), recordfiled5)

    def set_recordfiled11(self, recordfiled11):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"), recordfiled11)

    def set_recordfiled4(self, recordfiled4):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"), recordfiled4)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled12(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"))

    def get_recordfiled5(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"))

    def get_recordfiled11(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"))

    def get_recordfiled4(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"))



class SubClass_C2_RecordHeaderR6(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled8, recordfiled2, recordfiled15, recordfiled3):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled8(recordfiled8)
        self.set_recordfiled2(recordfiled2)
        self.set_recordfiled15(recordfiled15)
        self.set_recordfiled3(recordfiled3)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled8(self, recordfiled8):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"), recordfiled8)

    def set_recordfiled2(self, recordfiled2):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"), recordfiled2)

    def set_recordfiled15(self, recordfiled15):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled15"), recordfiled15)

    def set_recordfiled3(self, recordfiled3):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"), recordfiled3)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled8(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"))

    def get_recordfiled2(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"))

    def get_recordfiled15(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled15"))

    def get_recordfiled3(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled3"))



