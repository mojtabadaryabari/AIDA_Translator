# Codice del modello 'TestCase24', automaticamente generato in data 29/01/2024 da AIDA (plugin eu.fbk.tools.chess.rfi.codeGenerator versione 1.0.0.202312151600).
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
        self.set_subclass_c2_previousva_pv2(GlobalEnumeration.spento)
        self.set_subclass_c2_previousva_pv3(False)
        self.set_subclass_c2_previousva_pv4(False)
        self.set_subclass_c2_restoreva_rv1(0)
        self.set_subclass_c2_restoreva_rv2(GlobalEnumeration.giallox)
        self.set_subclass_c2_variabile_v6(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C2
        if self.is_triggered('eventSubclass_c2_command_comm6DaSender17ae81e7'):
            self.set_man_cmd_response('eventSubclass_c2_command_comm6DaSender17ae81e7',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c2_command_comm6DaSender17ae81e7',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, subclass_c2_lista_l1, subclass_c2_lista_l10, subclass_c2_lista_l2, subclass_c2_lista_l4, subclass_c2_lista_l8, subclass_c2_parametro_p2, subclass_c2_parametro_p4, subclass_c2_parametro_p5, subclass_c2_parametro_p9):
        # initialize the record type parameters
        self.set_subclass_c2_lista_l1(subclass_c2_lista_l1)
        self.set_subclass_c2_lista_l10(subclass_c2_lista_l10)
        self.set_subclass_c2_lista_l2(subclass_c2_lista_l2)
        self.set_subclass_c2_lista_l4(subclass_c2_lista_l4)
        self.set_subclass_c2_lista_l8(subclass_c2_lista_l8)
        # initialize the simple type parameters
        self.set_subclass_c2_parametro_p2(subclass_c2_parametro_p2)
        self.set_subclass_c2_parametro_p4(subclass_c2_parametro_p4)
        self.set_subclass_c2_parametro_p5(subclass_c2_parametro_p5)
        self.set_subclass_c2_parametro_p9(subclass_c2_parametro_p9)

        # initialize the timers
        self.set_subclass_c2_restoreti_ti1(121000)
        self.set_subclass_c2_restoreti_ti1_restore(121000)
        self.set_subclass_c2_timer_t1(31000)
        self.set_subclass_c2_timer_t3(43000)
        self.set_subclass_c2_timer_t4(2542000)
        self.set_subclass_c2_timer_t8(5000)
        self.set_subclass_c2_timer_t9(4054000)

        self.timers = [self.subclass_c2_restoreti_ti1,self.subclass_c2_restoreti_ti1_restore,self.subclass_c2_timer_t1,self.subclass_c2_timer_t3,self.subclass_c2_timer_t4,self.subclass_c2_timer_t8,self.subclass_c2_timer_t9,]

        # initialize the counters
        self.set_subclass_c2_contatore_co7(0)

    # setters for record type parameters
    def set_subclass_c2_lista_l1(self, subclass_c2_lista_l1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l1",subclass_c2_lista_l1)

    def set_subclass_c2_lista_l10(self, subclass_c2_lista_l10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10",subclass_c2_lista_l10)

    def set_subclass_c2_lista_l2(self, subclass_c2_lista_l2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2",subclass_c2_lista_l2)

    def set_subclass_c2_lista_l4(self, subclass_c2_lista_l4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4",subclass_c2_lista_l4)

    def set_subclass_c2_lista_l8(self, subclass_c2_lista_l8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8",subclass_c2_lista_l8)


    # getters for record type parameters
    def get_subclass_c2_lista_l1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l1")

    def get_subclass_c2_lista_l10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l10")

    def get_subclass_c2_lista_l2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l2")

    def get_subclass_c2_lista_l4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l4")

    def get_subclass_c2_lista_l8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_lista_l8")


    # setters for simple type parameters
    def set_subclass_c2_parametro_p2(self, subclass_c2_parametro_p2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2",subclass_c2_parametro_p2)

    def set_subclass_c2_parametro_p4(self, subclass_c2_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4",subclass_c2_parametro_p4)

    def set_subclass_c2_parametro_p5(self, subclass_c2_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5",subclass_c2_parametro_p5)

    def set_subclass_c2_parametro_p9(self, subclass_c2_parametro_p9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p9",subclass_c2_parametro_p9)


    # getters for simple type parameters
    def get_subclass_c2_parametro_p2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p2")

    def get_subclass_c2_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p4")

    def get_subclass_c2_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p5")

    def get_subclass_c2_parametro_p9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_parametro_p9")


    # setters for comandi al piazzale
    def set_subclass_c2_comando_c1(self, subclass_c2_comando_c1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c1",subclass_c2_comando_c1)

    def set_subclass_c2_comando_c2(self, subclass_c2_comando_c2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c2",subclass_c2_comando_c2)

    def set_subclass_c2_comando_c5(self, subclass_c2_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c5",subclass_c2_comando_c5)

    def set_subclass_c2_comando_c8(self, subclass_c2_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_comando_c8",subclass_c2_comando_c8)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c2_controllo_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c3")

    def get_subclass_c2_controllo_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c6")

    def get_subclass_c2_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c7")

    def get_subclass_c2_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c8")

    def get_subclass_c2_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_controllo_c9")

    def get_subclass_c2_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10")

    def get_subclass_c2_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4")


    # setters for state variables
    def set_subclass_c2_previousco_c10_prev(self, subclass_c2_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev",subclass_c2_previousco_c10_prev)
    def set_subclass_c2_previousco_c4_prev(self, subclass_c2_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev",subclass_c2_previousco_c4_prev)
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
    def set_subclass_c2_previousva_pv4(self, subclass_c2_previousva_pv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4",subclass_c2_previousva_pv4)
    def set_subclass_c2_previousva_pv4_prev(self, subclass_c2_previousva_pv4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4_prev",subclass_c2_previousva_pv4_prev)
    def set_subclass_c2_restoreva_rv1(self, subclass_c2_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1",subclass_c2_restoreva_rv1)
    def set_subclass_c2_restoreva_rv2(self, subclass_c2_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2",subclass_c2_restoreva_rv2)
    def set_subclass_c2_variabile_v6(self, subclass_c2_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6",subclass_c2_variabile_v6)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c2_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c10_prev")

    def get_subclass_c2_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousco_c4_prev")

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

    def get_subclass_c2_previousva_pv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4")

    def get_subclass_c2_previousva_pv4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_previousva_pv4_prev")

    def get_subclass_c2_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1")

    def get_subclass_c2_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv1_restore")

    def get_subclass_c2_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2")

    def get_subclass_c2_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_restoreva_rv2_restore")

    def get_subclass_c2_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c2_variabile_v6")


    # setters for timers
    def set_subclass_c2_restoreti_ti1(self, timerDuration):
        self.subclass_c2_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1", self.memory)

    def set_subclass_c2_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c2_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_restoreti_ti1_restore", self.memory)

    def set_subclass_c2_timer_t1(self, timerDuration):
        self.subclass_c2_timer_t1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t1", self.memory)

    def set_subclass_c2_timer_t3(self, timerDuration):
        self.subclass_c2_timer_t3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t3", self.memory)

    def set_subclass_c2_timer_t4(self, timerDuration):
        self.subclass_c2_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t4", self.memory)

    def set_subclass_c2_timer_t8(self, timerDuration):
        self.subclass_c2_timer_t8 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t8", self.memory)

    def set_subclass_c2_timer_t9(self, timerDuration):
        self.subclass_c2_timer_t9 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c2_timer_t9", self.memory)


    # getters for timers
    def get_subclass_c2_restoreti_ti1(self):
        return self.subclass_c2_restoreti_ti1

    def get_subclass_c2_restoreti_ti1_restore(self):
        return self.subclass_c2_restoreti_ti1_restore

    def get_subclass_c2_timer_t1(self):
        return self.subclass_c2_timer_t1

    def get_subclass_c2_timer_t3(self):
        return self.subclass_c2_timer_t3

    def get_subclass_c2_timer_t4(self):
        return self.subclass_c2_timer_t4

    def get_subclass_c2_timer_t8(self):
        return self.subclass_c2_timer_t8

    def get_subclass_c2_timer_t9(self):
        return self.subclass_c2_timer_t9


    # setters for counters
    def set_subclass_c2_contatore_co7(self, counterInitValue):
        self.subclass_c2_contatore_co7 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c2_contatore_co7", self.memory)


    # getters for counters
    def get_subclass_c2_contatore_co7(self):
        return self.subclass_c2_contatore_co7



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

        self.set_subclass_c2_previousco_c10_prev(False)
        self.set_subclass_c2_previousco_c4_prev(GlobalEnumeration.rossogiallox)
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())

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
    def macroSubclass_c2_macroef_m8(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro SubClass_C2_parametro_P4 non è  minore di  commento: {55,} 6 commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  minore di  commento: {55,} 6 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} o  se il timer SubClass_C2_timer_T3 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , commento: {66,} Assegna al comando SubClass_C2_comando_C5 il valore  False 
        
           
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  diverso da  commento: {56,}  state1  commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  commento: {54,} 13, commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore 9
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C2_variabile_V6 il valore 1
        
        
        
        }
        """
        def populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*34,*/  se il parametro SubClass_C2_parametro_P4 non è  minore di  /*55,*/ 6 /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P4 non è  minore di  /*55,*/ 6 /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di ((subclass_c2_parametro_p4)  è minore di  (6)) )  e  
( negazione di ((subclass_c2_variabile_v6)  è minore di  (6)) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) ) ) )  o  
( negazione di (il timer 'subclass_c2_timer_t3' è inattivo) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di ((subclass_c2_parametro_p4)  è minore di  (6)) )  e  
( negazione di ((subclass_c2_variabile_v6)  è minore di  (6)) ) )  o  
( ( (consdef)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c2_parametro_p4)  è minore di  (6)) )  e  
( negazione di ((subclass_c2_variabile_v6)  è minore di  (6)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è minore di  (6))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p4)  è minore di  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è minore di  (6))""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v6)  è minore di  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c2_timer_t3' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t3' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 13, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore 9

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {(negazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l1')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l1')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c2_lista_l1')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co7)  è maggiore di  (13)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c2_macroef_m8_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro SubClass_C2_parametro_P4 non è  minore di  /*55,*/ 6 /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 6 o  se il controllo ConsDef  è  uguale a FALSE  e  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ o  se il timer SubClass_C2_timer_T3 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE , /*66,*/ Assegna al comando SubClass_C2_comando_C5 il valore  False
        if db((db((db((db((db(not db(self.get_subclass_c2_parametro_p4() < 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() < 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c2_comando_c5(False)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C2_lista_L1 è  diverso da  /*56,*/  state1  /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 13, /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore 9
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C2_variabile_V6 il valore 1
        if db((db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l1())), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_contatore_co7().get_valore() > 13, di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c2_variabile_v6(9)
        else:
            self.set_subclass_c2_variabile_v6(1)
    
    # verify macros
    @srf_value_macro("macroSubclass_c2_macrove_m2")
    def macroSubclass_c2_macrove_m2(self, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
         
        { commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da spento commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  commento: {53,} 14 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  minore di  commento: {55,} 4 commento: {35,} e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {62,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  commento: {54,} 7 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  diverso da  commento: {56,} 5 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  diverso da  commento: {56,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  commento: {53,} 5 commento: {36,} e  se il timer SubClass_C2_timer_T9 è scaduto, Almeno una delle seguenti { 
         commento: {63,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  commento: {54,} 1413, Solo una delle seguenti { 
         commento: {63,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  uguale a  commento: {53,} 4 commento: {35,} o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  commento: {55,} 13054, Solo una delle seguenti { 
         commento: {62,} commento: {44,}  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  commento: {36,} o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
         commento: {63,}  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C2_timer_T8 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
         commento: {63,} commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo commento: {35,} e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
         commento: {62,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 è  minore di  commento: {55,} 8 commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  diverso da  commento: {56,} 2 commento: {35,} e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  commento: {56,} 142, Almeno una delle seguenti { 
         commento: {62,}  se il controllo ConsDef  è  uguale a FALSE ,  commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  uguale a c120x, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     commento: {105,} è  uguale a  commento: {53,}  state1  o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P5 è  minore di  commento: {55,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  commento: {53,} 5 commento: {34,} e  se il parametro SubClass_C2_parametro_P4 è  minore di  commento: {55,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
         commento: {61,} commento: {36,}  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
         commento: {61,}  se il ripristino dello stato  è  uguale a  commento: {53,}  state1  commento: {107,} commento: {37,} e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  commento: {54,} 1 commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox commento: {36,} o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
         commento: {61,} commento: {38,}  se il contatore SubClass_C2_contatore_Co7 è  minore di  commento: {55,} 1113 commento: {36,} o  se il timer SubClass_C2_timer_T3 è disattivo commento: {34,} o  se il parametro SubClass_C2_parametro_P9 è  minore di  commento: {55,} 3 commento: {36,} e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  commento: {35,} o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
         commento: {61,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  uguale a  commento: {53,} 9, Tutte le seguenti { 
         commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,} commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  commento: {54,} 6 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  commento: {54,} 5, Almeno una delle seguenti { 
         commento: {63,} commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  minore di  commento: {55,} 9 commento: {34,} o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da  commento: {56,} 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
         commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo commento: {36,} e  se il timer SubClass_C2_timer_T4 è disattivo commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  minore di  commento: {55,} 10 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 è  diverso da  commento: {56,} 5 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  commento: {53,} 122, Verifica che   commento: {48,50,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  minore di  commento: {55,} 5
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V6 non sia  diverso da  commento: {56,} 9
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  uguale a  commento: {53,} 151
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 3
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,49,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia disattivo
        
        
         } Verifica che   commento: {48,49,50,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 6
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T8 sia scaduto
        
        
         } Verifica che   commento: {47,49,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  maggiore di  commento: {54,} 4
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T9 non sia disattivo
         commento: {104,} o  che  commento: {36,}  il timer SubClass_C2_timer_T4 sia disattivo
        
        
         } Verifica che   commento: {47,}  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  minore di  commento: {55,} 1
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C2_timer_T1 non sia disattivo
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 8
        
        
         } Verifica che   commento: {47,48,49,50,51,}  commento: {,}  il timer SubClass_C2_timer_T8 non sia scaduto
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  uguale a  commento: {53,} 8
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  minore di  commento: {55,} 2
         commento: {104,} o  che  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 13305
        
        
         } Verifica che   commento: {47,48,50,}   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  commento: {54,} 7
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  minore di  commento: {55,} 4
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P4 non sia  diverso da  commento: {56,} 10
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {48,}  commento: {,}  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
         commento: {104,} e  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
        
        
         } Verifica che   commento: {47,50,}  commento: {,}  la variabile SubClass_C2_variabile_V6 non sia  diverso da  commento: {56,} 7
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  uguale a  commento: {53,} 8
        
        
         } Verifica che   commento: {47,48,49,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 12
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T9 non sia disattivo
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
         commento: {104,} e  che   il controllo ConsDef  sia  uguale a FALSE 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  commento: {54,} 9
        
        
         } Verifica che   commento: {50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  commento: {54,} 114
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  minore di  commento: {55,} 1
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C2_contatore_Co7 non sia  minore di  commento: {55,} 132
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da spento /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 1413, Solo una delle seguenti { 
 /*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  /*54,*/ 9


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 114
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 132""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da spento /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 1413, Solo una delle seguenti { 
 /*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  /*54,*/ 9


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da spento /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C2_restoreva_RV2 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_restoreva_rv2_restore)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  minore di  /*55,*/ 4 /*35,*/ e  se il controllo SubClass_C2_controllo_C6 non è  uguale a spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  uguale a  /*53,*/ 14""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (14)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P2 è  minore di  /*55,*/ 4""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 non è  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 1413, Solo una delle seguenti { 
 /*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 8


 } Verifica che   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  /*54,*/ 9


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto, Almeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 1413, Solo una delle seguenti { 
 /*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 7 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v6)  è maggiore di  (7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5 /*36,*/ e  se il timer SubClass_C2_timer_T9 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 non è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T9 è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 1413, Solo una delle seguenti { 
 /*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*47,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 1413, Solo una delle seguenti { 
 /*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C2_contatore_Co7 è  maggiore di  /*54,*/ 1413""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054, Solo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4 /*35,*/ o  se il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 4""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 non è  uguale a RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 13054""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (13054)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,*/   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo, Almeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*44,*/  se  MainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False  /*36,*/ o  se il timer SubClass_C2_timer_T8 non è attivo""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_variabile_V3 del campo  MainClass_C1 di SubClass_C2_lista_L4 è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v3 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T8 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento, Solo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  uguale a spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T8 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C6 è  uguale a spento""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 } Verifica che   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento, Solo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo /*35,*/ e  se il controllo SubClass_C2_controllo_C6 è  diverso da spento""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L10 è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l10' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C6 è  diverso da spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 } Verifica che   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142, Almeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True  /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2 /*35,*/ e  se il controllo SubClass_C2_controllo_C7 è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8 /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 8""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P5 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p5)  è uguale a  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C7 è  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 è  diverso da  /*56,*/ 142""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (142)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto, Almeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1  o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se il controllo ConsDef  è  uguale a FALSE ,  /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  uguale a c120x, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l4')  è uguale a  (state1)) allora ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (c120x))""", [
                            DIBoolExpr("""EqualImpl\n/*111,*/   lo stato del campo  MainClass_C1     /*105,*/ è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è uguale a  (c120x)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P5 è  minore di  /*55,*/ 6""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T4 è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5 /*34,*/ e  se il parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P4 è  minore di  /*55,*/ 3""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 } Verifica che   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*36,*/  se il timer SubClass_C2_timer_T4 è scaduto, Tutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox /*36,*/ o  se il timer SubClass_C2_timer_T8 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1 /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/  se il ripristino dello stato  è  uguale a  /*53,*/  state1  /*107,*/ /*37,*/ e  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""EqualImpl\nil ripristino dello stato  è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v6)  è maggiore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C2_controllo_C8 è  diverso da RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE  /*35,*/ o  se il controllo SubClass_C2_controllo_C7 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo /*34,*/ o  se il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113 /*36,*/ o  se il timer SubClass_C2_timer_T3 è disattivo""", [
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C2_contatore_Co7 è  minore di  /*55,*/ 1113""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T3 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3 /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto""", [
                            DIBoolExpr("""LessThanImpl\nil parametro SubClass_C2_parametro_P9 è  minore di  /*55,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T8 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C7 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 } Verifica che   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9, Tutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  uguale a  /*53,*/ 9""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5, Almeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/ /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 6""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 5""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 } Verifica che   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE , Solo una delle seguenti { 
 /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo o  se il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9 /*34,*/ o  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è minore di  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T1 non è disattivo""", [
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 9""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T1 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2 e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo ConsDef  è  uguale a FALSE  /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 2""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo ConsDef  è  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122, Verifica che   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo /*36,*/ e  se il timer SubClass_C2_timer_T4 è disattivo""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L1 è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l1' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 10""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 è  diverso da  /*56,*/ 5""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C2_contatore_Co7 è  uguale a  /*53,*/ 122""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""LessThanImpl\nche   /*48,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 5""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  uguale a  /*53,*/ 151""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 3""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (3)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""EqualImpl\nche   /*48,49,50,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 6""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (6)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T8 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*47,49,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C2_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche   /*47,*/  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C2_timer_T1 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t1' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (rossogiallox))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2
 /*104,*/ o  che  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,50,51,*/  /*,*/  il timer SubClass_C2_timer_T8 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (rossogiallox))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_parametro_p2)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 13305""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (13305)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,48,50,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P5 non sia  maggiore di  /*54,*/ 7""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p5)  è maggiore di  (7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v6)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P4 non sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p4)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p4)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c8)  è uguale a  (rossogiallox))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""EqualImpl\nche  /*35,*/  il controllo SubClass_C2_controllo_C6 sia  uguale a spento""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   /*48,*/   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False 
 /*104,*/ e  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,*/  /*,*/  il controllo SubClass_C2_controllo_C3 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c3)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c3)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 non sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_variabile_v6)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  uguale a  /*53,*/ 8""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (8)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 12
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 12""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (12)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T9 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t9' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che   il controllo ConsDef  sia  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   il controllo ConsDef  sia  uguale a FALSE""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 non sia  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_parametro_p2)  è maggiore di  (9)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 114
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 1
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 132""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 114
 /*104,*/ e  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 114""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nche  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*38,*/  il contatore SubClass_C2_contatore_Co7 non sia  minore di  /*55,*/ 132""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (132)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m2_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(self.get_subclass_c2_restoreva_rv2_restore() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db((db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 14, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p2() < 4, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db(not db(self.get_subclass_c2_variabile_v6() > 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v6() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t9().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() > 1413, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(not db(self.get_subclass_c2_variabile_v6() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 13054, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l10())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(self.get_subclass_c2_variabile_v6() < 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p5() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 142, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == GlobalEnumeration.c120x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p5() < 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v6() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p4() < 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_stato_restore() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t8().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(self.get_subclass_c2_contatore_co7().get_valore() < 1113, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t3().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_parametro_p9() < 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_controllo_c7() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c2_variabile_v6() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C2.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p2() > 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v6() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() < 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_parametro_p2() > 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l1())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v6() < 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co7().get_valore() == 122, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_subclass_c2_variabile_v6() < 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_variabile_v6() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(self.get_subclass_c2_contatore_co7().get_valore() == 151, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v6() == 6, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db(self.get_subclass_c2_parametro_p2() > 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c2_parametro_p2() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_timer_t1().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_subclass_c2_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_variabile_v6() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() < 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 13305, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db((db(not db(self.get_subclass_c2_parametro_p5() > 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_parametro_p4() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(not db(self.get_subclass_c2_controllo_c3() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(not db(not db(self.get_subclass_c2_variabile_v6() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_parametro_p2() == 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 12, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t9().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(not db(self.get_subclass_c2_parametro_p2() > 9, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_subclass_c2_contatore_co7().get_valore() > 114, di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_variabile_v6() < 1, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 132, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m3")
    def macroSubclass_c2_macrove_m3(self, argomento_ave1, argomento_ave6, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {62,} commento: {110,}  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto commento: {36,} e  se il timer SubClass_C2_timer_T8 non è scaduto commento: {35,} e  se il controllo SubClass_C2_controllo_C8 è  uguale a RossoGiallox, Almeno una delle seguenti { 
         commento: {62,} commento: {37,}  se la variabile SubClass_C2_variabile_V6 non è  minore di  commento: {55,} 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo commento: {39,}  commento: {37,} o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  commento: {54,} 2 commento: {38,} o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 11, Almeno una delle seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P2 è  maggiore di  commento: {54,} 1 commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  minore di  commento: {55,} 3 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  commento: {56,} 124 commento: {36,} o  se il timer SubClass_C2_timer_T8 è disattivo commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  commento: {54,} 152 commento: {38,} e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  commento: {55,} 11, Verifica che   commento: {48,49,50,51,}  commento: {,}  il contatore SubClass_C2_contatore_Co7 sia  diverso da  commento: {56,} 13
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  commento: {54,} 14
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  diverso da  commento: {56,} 7
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T4 sia attivo
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C2_variabile_V6 non sia  minore di  commento: {55,} 1
        
        
         } Verifica che   commento: {47,48,52,}  commento: {,}  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
         commento: {104,} e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox commento: {,} 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C2_parametro_P9 non sia  uguale a  commento: {53,} 7
         commento: {104,} e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo commento: {39,} 
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  maggiore di  commento: {54,} 6
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
         commento: {104,} o  che  commento: {,}  il timer SubClass_C2_timer_T4 sia disattivo
         commento: {104,} o  che  commento: {35,}  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a RossoGiallox, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124 /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  /*53,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo /*39,*/ 


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a RossoGiallox, Almeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124 /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  /*53,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo /*39,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto /*35,*/ e  se il controllo SubClass_C2_controllo_C8 è  uguale a RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/ /*110,*/  se il ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto /*36,*/ e  se il timer SubClass_C2_timer_T8 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C2_restoreTI_TI1 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T8 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C2_controllo_C8 è  uguale a RossoGiallox""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124 /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1


 } Verifica che   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  /*53,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo /*39,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11, Almeno una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124 /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 2 /*38,*/ o  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo /*39,*/  /*37,*/ o  se la variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*37,*/  se la variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5 o  se l'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  minore di  /*55,*/ 5""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v6)  è minore di  (5)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 non  è  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 non è  maggiore di  /*54,*/ 2""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_variabile_v6)  è maggiore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co7)  è maggiore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124 /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11, Verifica che   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124 /*36,*/ o  se il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1 /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124""", [
                            DIBoolExpr("""GreaterThanImpl\nil parametro SubClass_C2_parametro_P2 è  maggiore di  /*54,*/ 1""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124""", [
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C2_variabile_V6 è  minore di  /*55,*/ 3""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  diverso da  /*56,*/ 124""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_contatore_co7)  è uguale a  (124))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (124)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152 /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C2_timer_T8 è disattivo /*38,*/ e  se il contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T8 è disattivo""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  maggiore di  /*54,*/ 152""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c2_contatore_co7)  è maggiore di  (152)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C2_contatore_Co7 non è  minore di  /*55,*/ 11""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_contatore_co7)  è minore di  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14
 /*104,*/ o  che  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,51,*/  /*,*/  il contatore SubClass_C2_contatore_Co7 sia  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_contatore_co7)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C7 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c7)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c7)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore SubClass_C2_contatore_Co7 sia  maggiore di  /*54,*/ 14""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C2_variabile_V6 sia  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C2_variabile_V6 non sia  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c2_variabile_v6)  è minore di  (1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox /*,*/ 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  /*53,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento
 /*104,*/ e  che   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,52,*/  /*,*/  il controllo SubClass_C2_controllo_C6 non sia  uguale a spento""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave6 non  sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave6)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  /*53,*/ 7
 /*104,*/ e  che   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C2_parametro_P9 non sia  uguale a  /*53,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p9)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave1 non  sia  uguale a RossoGialloGiallo""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (rossogiallogiallo)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo
 /*104,*/ o  che  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox
 /*104,*/ o  che  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  maggiore di  /*54,*/ 6
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""GreaterThanImpl\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  maggiore di  /*54,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C8 sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C2_timer_T4 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*35,*/  il controllo SubClass_C2_controllo_C6 non sia  diverso da spento""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_controllo_c6)  è uguale a  (spento))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c6)  è uguale a  (spento)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(self.get_subclass_c2_restoreti_ti1_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db((db(not db(self.get_subclass_c2_variabile_v6() < 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave1 == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_variabile_v6() > 2, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_contatore_co7().get_valore() > 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_subclass_c2_parametro_p2() > 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c2_variabile_v6() < 3, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db((db(self.get_subclass_c2_timer_t8().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() > 152, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c2_contatore_co7().get_valore() < 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db(not db(self.get_subclass_c2_contatore_co7().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_controllo_c7() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_contatore_co7().get_valore() > 14, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_variabile_v6() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]) and db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave6 == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c2_parametro_p9() == 7, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(argomento_ave1 == GlobalEnumeration.rossogiallogiallo, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db(self.get_subclass_c2_variabile_v6() > 6, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(not db(self.get_subclass_c2_controllo_c6() == GlobalEnumeration.spento, di_ctx.subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c2_macrove_m4")
    def macroSubclass_c2_macrove_m4(self, argomento_ave1, argomento_ave2, argomento_ave4, argomento_ave5, argomento_ave6, argomento_ave8, argomento_ave9, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  commento: {105,} è  maggiore di  commento: {54,} 9 commento: {36,} e  se il timer SubClass_C2_timer_T4 non è disattivo commento: {37,} o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  commento: {54,} 8 commento: {36,} o  se il timer SubClass_C2_timer_T4 è disattivo, Solo una delle seguenti { 
         commento: {34,}  se il parametro SubClass_C2_parametro_P2 non è  diverso da  commento: {56,} 9,  commento: {43,}  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C2_timer_T4 non è attivo commento: {37,} e  se la variabile SubClass_C2_variabile_V6 è  diverso da  commento: {56,} 7 commento: {34,} e  se il parametro SubClass_C2_parametro_P2 non è  diverso da  commento: {56,} 7, Verifica che   commento: {48,52,}   l'argomento argomento_ave2 non  sia  diverso da  False  commento: {,} 
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox
        
        
         } Verifica che   commento: {47,48,49,50,52,}  commento: {,}  la variabile SubClass_C2_variabile_V6 sia  minore di  commento: {55,} 6
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C2_parametro_P2 sia  maggiore di  commento: {54,} 8
         commento: {104,} e  che  commento: {,}  il timer SubClass_C2_timer_T8 non sia disattivo
         commento: {104,} e  che   l'argomento argomento_ave4 sia  diverso da RossoGiallox commento: {,} 
        
        
        }
        """
        def populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 8 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 7 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 7, Verifica che   /*48,52,*/   l'argomento argomento_ave2 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox


 } Verifica che   /*47,48,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 8 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo, Solo una delle seguenti { 
 /*34,*/  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 7 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 7, Verifica che   /*48,52,*/   l'argomento argomento_ave2 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 8 /*36,*/ o  se il timer SubClass_C2_timer_T4 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo /*37,*/ o  se la variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  maggiore di  /*54,*/ 9 /*36,*/ e  se il timer SubClass_C2_timer_T4 non è disattivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C2_lista_L4 esiste e  /*105,*/ è  maggiore di  /*54,*/ 9""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c2_lista_l4)  è maggiore di  (9)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T4 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C2_variabile_V6 è  maggiore di  /*54,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C2_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 7 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 7, Verifica che   /*48,52,*/   l'argomento argomento_ave2 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 7 /*34,*/ e  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo /*37,*/ e  se la variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C2_timer_T4 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9,  /*43,*/  se MainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_timer_T10 del campo  MainClass_C1 di SubClass_C2_lista_L2 è attivo, /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c2_lista_l2')  è uguale a  (state1)) allora (il timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo)""", [
                            DIBoolExpr("""EqualImpl\n/*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'mainclass_c1_timer_t10 del campo mainclass_c1 della lista subclass_c2_lista_l2' è attivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C2_timer_T4 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C2_variabile_V6 è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_variabile_v6)  è uguale a  (7)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C2_parametro_P2 non è  diverso da  /*56,*/ 7""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c2_parametro_p2)  è uguale a  (7))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_parametro_p2)  è uguale a  (7)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,52,*/   l'argomento argomento_ave2 non  sia  diverso da  False  /*,*/ 
 /*104,*/ o  che  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,52,*/   l'argomento argomento_ave2 non  sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C2_controllo_C8 sia  uguale a RossoGiallox""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo
 /*104,*/ e  che   l'argomento argomento_ave4 sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 8
 /*104,*/ e  che  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 8""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,48,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 6
 /*104,*/ e  che  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,48,49,50,52,*/  /*,*/  la variabile SubClass_C2_variabile_V6 sia  minore di  /*55,*/ 6""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C2_controllo_C8 non sia  uguale a RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c2_controllo_c8)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro SubClass_C2_parametro_P2 sia  maggiore di  /*54,*/ 8""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C2_timer_T8 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c2_timer_t8' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 sia  diverso da RossoGiallox""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (rossogiallox)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c2_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() > 9, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l4())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_variabile_v6() > 8, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c2_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db((db((db(not db(not db(self.get_subclass_c2_parametro_p2() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_timer_t10().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c2_lista_l2()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_variabile_v6() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c2_parametro_p2() == 7, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db(not db(not db(argomento_ave2 == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db((db((db(self.get_subclass_c2_variabile_v6() < 6, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c2_controllo_c8() == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c2_parametro_p2() > 8, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c2_timer_t8().isDisattivato(), di_ctx.subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(not db(argomento_ave4 == GlobalEnumeration.rossogiallox, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c2_macrova_m9")
    def macroSubclass_c2_macrova_m9(self, argomento_a4, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore RossoGiallox commento: {],}
        }
        """
        def populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c2_macrova_m9_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore RossoGiallox
        return GlobalEnumeration.rossogiallox
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c2_command_comm6DaSender17ae81e7(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c2_command_comm6DaSender17ae81e7')
    
    # for each automatic command, the corresponding method is created
    def eventSubclass_c2_command_comm10(self, notifying_process, argomento_ave3, argomento_ave7):
        notifying_process.response_notify_auto_cmd(self, 'eventSubclass_c2_command_comm10', argomento_ave3=argomento_ave3, argomento_ave7=argomento_ave7)
    

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c2_previousco_c10_prev(self.get_subclass_c2_previousco_c10())
        self.set_subclass_c2_previousco_c4_prev(self.get_subclass_c2_previousco_c4())
        self.set_subclass_c2_previousva_pv1_prev(self.get_subclass_c2_previousva_pv1())
        self.set_subclass_c2_previousva_pv2_prev(self.get_subclass_c2_previousva_pv2())
        self.set_subclass_c2_previousva_pv3_prev(self.get_subclass_c2_previousva_pv3())
        self.set_subclass_c2_previousva_pv4_prev(self.get_subclass_c2_previousva_pv4())

class SubClass_C2_RecordHeaderR1(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled19, recordfiled2, recordfiled8):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled19(recordfiled19)
        self.set_recordfiled2(recordfiled2)
        self.set_recordfiled8(recordfiled8)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled19(self, recordfiled19):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"), recordfiled19)

    def set_recordfiled2(self, recordfiled2):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"), recordfiled2)

    def set_recordfiled8(self, recordfiled8):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"), recordfiled8)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled19(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"))

    def get_recordfiled2(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled2"))

    def get_recordfiled8(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled8"))



class SubClass_C2_RecordHeaderR9(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled10, recordfiled4, recordfiled12):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled10(recordfiled10)
        self.set_recordfiled4(recordfiled4)
        self.set_recordfiled12(recordfiled12)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled10(self, recordfiled10):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"), recordfiled10)

    def set_recordfiled4(self, recordfiled4):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"), recordfiled4)

    def set_recordfiled12(self, recordfiled12):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"), recordfiled12)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled10(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled10"))

    def get_recordfiled4(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled4"))

    def get_recordfiled12(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled12"))



