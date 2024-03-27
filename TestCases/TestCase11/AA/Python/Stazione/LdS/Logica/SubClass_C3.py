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

class SubClass_C3(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C3, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c3_previousva_pv1(False)
        self.set_subclass_c3_previousva_pv2(False)
        self.set_subclass_c3_previousva_pv3(False)
        self.set_subclass_c3_previousva_pv4(GlobalEnumeration.spento)
        self.set_subclass_c3_previousva_pv5(False)
        self.set_subclass_c3_restoreva_rv1(GlobalEnumeration.rossogiallox)
        self.set_subclass_c3_restoreva_rv2(GlobalEnumeration.rossogiallox)
        self.set_subclass_c3_variabile_v9(0)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C3
        if self.is_triggered('eventSubclass_c3_command_comm4DaSender41f3f0dc'):
            self.set_man_cmd_response('eventSubclass_c3_command_comm4DaSender41f3f0dc',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c3_command_comm4DaSender41f3f0dc',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, subclass_c3_lista_l1, subclass_c3_lista_l10, subclass_c3_lista_l4, subclass_c3_lista_l6, subclass_c3_lista_l7, subclass_c3_parametro_p10, subclass_c3_parametro_p4, subclass_c3_parametro_p5, subclass_c3_parametro_p7, subclass_c3_parametro_p8):
        # initialize the record type parameters
        self.set_subclass_c3_lista_l1(subclass_c3_lista_l1)
        self.set_subclass_c3_lista_l10(subclass_c3_lista_l10)
        self.set_subclass_c3_lista_l4(subclass_c3_lista_l4)
        self.set_subclass_c3_lista_l6(subclass_c3_lista_l6)
        self.set_subclass_c3_lista_l7(subclass_c3_lista_l7)
        # initialize the simple type parameters
        self.set_subclass_c3_parametro_p10(subclass_c3_parametro_p10)
        self.set_subclass_c3_parametro_p4(subclass_c3_parametro_p4)
        self.set_subclass_c3_parametro_p5(subclass_c3_parametro_p5)
        self.set_subclass_c3_parametro_p7(subclass_c3_parametro_p7)
        self.set_subclass_c3_parametro_p8(subclass_c3_parametro_p8)

        # initialize the timers
        self.set_subclass_c3_restoreti_ti1(345000)
        self.set_subclass_c3_restoreti_ti1_restore(345000)
        self.set_subclass_c3_restoreti_ti2(40213000)
        self.set_subclass_c3_restoreti_ti2_restore(40213000)
        self.set_subclass_c3_timer_t10(350213000)
        self.set_subclass_c3_timer_t5(4000)
        self.set_subclass_c3_timer_t7(5000)

        self.timers = [self.subclass_c3_restoreti_ti1,self.subclass_c3_restoreti_ti1_restore,self.subclass_c3_restoreti_ti2,self.subclass_c3_restoreti_ti2_restore,self.subclass_c3_timer_t10,self.subclass_c3_timer_t5,self.subclass_c3_timer_t7,]

        # initialize the counters
        self.set_subclass_c3_contatore_co3(0)

    # setters for record type parameters
    def set_subclass_c3_lista_l1(self, subclass_c3_lista_l1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l1",subclass_c3_lista_l1)

    def set_subclass_c3_lista_l10(self, subclass_c3_lista_l10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l10",subclass_c3_lista_l10)

    def set_subclass_c3_lista_l4(self, subclass_c3_lista_l4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l4",subclass_c3_lista_l4)

    def set_subclass_c3_lista_l6(self, subclass_c3_lista_l6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l6",subclass_c3_lista_l6)

    def set_subclass_c3_lista_l7(self, subclass_c3_lista_l7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l7",subclass_c3_lista_l7)


    # getters for record type parameters
    def get_subclass_c3_lista_l1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l1")

    def get_subclass_c3_lista_l10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l10")

    def get_subclass_c3_lista_l4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l4")

    def get_subclass_c3_lista_l6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l6")

    def get_subclass_c3_lista_l7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l7")


    # setters for simple type parameters
    def set_subclass_c3_parametro_p10(self, subclass_c3_parametro_p10):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p10",subclass_c3_parametro_p10)

    def set_subclass_c3_parametro_p4(self, subclass_c3_parametro_p4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p4",subclass_c3_parametro_p4)

    def set_subclass_c3_parametro_p5(self, subclass_c3_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p5",subclass_c3_parametro_p5)

    def set_subclass_c3_parametro_p7(self, subclass_c3_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p7",subclass_c3_parametro_p7)

    def set_subclass_c3_parametro_p8(self, subclass_c3_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p8",subclass_c3_parametro_p8)


    # getters for simple type parameters
    def get_subclass_c3_parametro_p10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p10")

    def get_subclass_c3_parametro_p4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p4")

    def get_subclass_c3_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p5")

    def get_subclass_c3_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p7")

    def get_subclass_c3_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p8")


    # setters for comandi al piazzale
    def set_subclass_c3_comando_c6(self, subclass_c3_comando_c6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c6",subclass_c3_comando_c6)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c3_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c9")

    def get_subclass_c3_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c1")

    def get_subclass_c3_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c10")

    def get_subclass_c3_previousco_c3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3")

    def get_subclass_c3_previousco_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c7")

    def get_subclass_c3_previousco_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c8")


    # setters for state variables
    def set_subclass_c3_previousco_c1_prev(self, subclass_c3_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c1_prev",subclass_c3_previousco_c1_prev)
    def set_subclass_c3_previousco_c10_prev(self, subclass_c3_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c10_prev",subclass_c3_previousco_c10_prev)
    def set_subclass_c3_previousco_c3_prev(self, subclass_c3_previousco_c3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3_prev",subclass_c3_previousco_c3_prev)
    def set_subclass_c3_previousco_c7_prev(self, subclass_c3_previousco_c7_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c7_prev",subclass_c3_previousco_c7_prev)
    def set_subclass_c3_previousco_c8_prev(self, subclass_c3_previousco_c8_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c8_prev",subclass_c3_previousco_c8_prev)
    def set_subclass_c3_previousva_pv1(self, subclass_c3_previousva_pv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1",subclass_c3_previousva_pv1)
    def set_subclass_c3_previousva_pv1_prev(self, subclass_c3_previousva_pv1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1_prev",subclass_c3_previousva_pv1_prev)
    def set_subclass_c3_previousva_pv2(self, subclass_c3_previousva_pv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2",subclass_c3_previousva_pv2)
    def set_subclass_c3_previousva_pv2_prev(self, subclass_c3_previousva_pv2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2_prev",subclass_c3_previousva_pv2_prev)
    def set_subclass_c3_previousva_pv3(self, subclass_c3_previousva_pv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3",subclass_c3_previousva_pv3)
    def set_subclass_c3_previousva_pv3_prev(self, subclass_c3_previousva_pv3_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3_prev",subclass_c3_previousva_pv3_prev)
    def set_subclass_c3_previousva_pv4(self, subclass_c3_previousva_pv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4",subclass_c3_previousva_pv4)
    def set_subclass_c3_previousva_pv4_prev(self, subclass_c3_previousva_pv4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4_prev",subclass_c3_previousva_pv4_prev)
    def set_subclass_c3_previousva_pv5(self, subclass_c3_previousva_pv5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv5",subclass_c3_previousva_pv5)
    def set_subclass_c3_previousva_pv5_prev(self, subclass_c3_previousva_pv5_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv5_prev",subclass_c3_previousva_pv5_prev)
    def set_subclass_c3_restoreva_rv1(self, subclass_c3_restoreva_rv1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv1",subclass_c3_restoreva_rv1)
    def set_subclass_c3_restoreva_rv2(self, subclass_c3_restoreva_rv2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv2",subclass_c3_restoreva_rv2)
    def set_subclass_c3_variabile_v9(self, subclass_c3_variabile_v9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v9",subclass_c3_variabile_v9)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c3_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c1_prev")

    def get_subclass_c3_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c10_prev")

    def get_subclass_c3_previousco_c3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c3_prev")

    def get_subclass_c3_previousco_c7_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c7_prev")

    def get_subclass_c3_previousco_c8_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c8_prev")

    def get_subclass_c3_previousva_pv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1")

    def get_subclass_c3_previousva_pv1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv1_prev")

    def get_subclass_c3_previousva_pv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2")

    def get_subclass_c3_previousva_pv2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv2_prev")

    def get_subclass_c3_previousva_pv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3")

    def get_subclass_c3_previousva_pv3_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv3_prev")

    def get_subclass_c3_previousva_pv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4")

    def get_subclass_c3_previousva_pv4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv4_prev")

    def get_subclass_c3_previousva_pv5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv5")

    def get_subclass_c3_previousva_pv5_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousva_pv5_prev")

    def get_subclass_c3_restoreva_rv1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv1")

    def get_subclass_c3_restoreva_rv1_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv1_restore")

    def get_subclass_c3_restoreva_rv2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv2")

    def get_subclass_c3_restoreva_rv2_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv2_restore")

    def get_subclass_c3_variabile_v9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v9")


    # setters for timers
    def set_subclass_c3_restoreti_ti1(self, timerDuration):
        self.subclass_c3_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti1", self.memory)

    def set_subclass_c3_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti1_restore", self.memory)

    def set_subclass_c3_restoreti_ti2(self, timerDuration):
        self.subclass_c3_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti2", self.memory)

    def set_subclass_c3_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti2_restore", self.memory)

    def set_subclass_c3_timer_t10(self, timerDuration):
        self.subclass_c3_timer_t10 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t10", self.memory)

    def set_subclass_c3_timer_t5(self, timerDuration):
        self.subclass_c3_timer_t5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t5", self.memory)

    def set_subclass_c3_timer_t7(self, timerDuration):
        self.subclass_c3_timer_t7 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t7", self.memory)


    # getters for timers
    def get_subclass_c3_restoreti_ti1(self):
        return self.subclass_c3_restoreti_ti1

    def get_subclass_c3_restoreti_ti1_restore(self):
        return self.subclass_c3_restoreti_ti1_restore

    def get_subclass_c3_restoreti_ti2(self):
        return self.subclass_c3_restoreti_ti2

    def get_subclass_c3_restoreti_ti2_restore(self):
        return self.subclass_c3_restoreti_ti2_restore

    def get_subclass_c3_timer_t10(self):
        return self.subclass_c3_timer_t10

    def get_subclass_c3_timer_t5(self):
        return self.subclass_c3_timer_t5

    def get_subclass_c3_timer_t7(self):
        return self.subclass_c3_timer_t7


    # setters for counters
    def set_subclass_c3_contatore_co3(self, counterInitValue):
        self.subclass_c3_contatore_co3 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co3", self.memory)


    # getters for counters
    def get_subclass_c3_contatore_co3(self):
        return self.subclass_c3_contatore_co3



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
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.StatoIniziale, Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,
                         guard=(self.dbs[0], ),
                         effect=(),
                         phase = TransPhase.Stato
                         ),
            # transizioni della fase manuale
            # transizioni della fase di stato
            TransDebInfo(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1,
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1)
            self.effect_INITIALIZATION_StatoIniziale_state1_000()
            self.response_wait()

        self.set_subclass_c3_previousco_c1_prev(True)
        self.set_subclass_c3_previousco_c10_prev(GlobalEnumeration.gialloaverdea)
        self.set_subclass_c3_previousco_c3_prev(True)
        self.set_subclass_c3_previousco_c7_prev(True)
        self.set_subclass_c3_previousco_c8_prev(True)
        self.set_subclass_c3_previousva_pv1_prev(self.get_subclass_c3_previousva_pv1())
        self.set_subclass_c3_previousva_pv2_prev(self.get_subclass_c3_previousva_pv2())
        self.set_subclass_c3_previousva_pv3_prev(self.get_subclass_c3_previousva_pv3())
        self.set_subclass_c3_previousva_pv4_prev(self.get_subclass_c3_previousva_pv4())
        self.set_subclass_c3_previousva_pv5_prev(self.get_subclass_c3_previousva_pv5())

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
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
                pass #return ERROR("the current state variable is not set (command: %s)" % command)
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_state_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
                if(self.guard_PERMANENCE_state1_000()):
                    self.curr_transition = self.Transition._State1__State1__stateSheet_0__permanence
            else:
                # if the current state variable is not set, an exception will be raised
                return ERROR("the current state variable is not set (command: %s)" % command)

        if self.is_automatic_phase():
            if self.is_current_state(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1):
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
            self.set_fsmState(Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1)
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
    def macroSubclass_c3_macroef_m1(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  commento: {105,} è  uguale a  commento: {53,} 1 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 1250213 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  commento: {54,} 4, commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 5
        
           
         commento: {36,}  se il timer SubClass_C3_timer_T5 non è scaduto commento: {36,} o  se il timer SubClass_C3_timer_T5 non è disattivo commento: {37,} o  se la variabile SubClass_C3_variabile_V9 è  diverso da  commento: {56,} 4 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 non è  diverso da  commento: {56,} 4 commento: {36,} o  se il timer SubClass_C3_timer_T5 è disattivo, commento: {68,}Attiva il timer SubClass_C3_timer_T7
        
           
        
        }
        """
        def populate_macroSubclass_c3_macroef_m1_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  /*105,*/ è  uguale a  /*53,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 1250213 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 4, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  /*105,*/ è  uguale a  /*53,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 1250213 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 4""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (1))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_contatore_co3)  è maggiore di  (1250213)) )  e  
( negazione di ((subclass_c3_variabile_v9)  è maggiore di  (4)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è maggiore di  (1250213))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co3)  è maggiore di  (1250213)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v9)  è maggiore di  (4))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v9)  è maggiore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*36,*/  se il timer SubClass_C3_timer_T5 non è scaduto /*36,*/ o  se il timer SubClass_C3_timer_T5 non è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V9 è  diverso da  /*56,*/ 4 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 non è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C3_timer_T5 è disattivo, /*68,*/Attiva il timer SubClass_C3_timer_T7""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*36,*/  se il timer SubClass_C3_timer_T5 non è scaduto /*36,*/ o  se il timer SubClass_C3_timer_T5 non è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V9 è  diverso da  /*56,*/ 4 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 non è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C3_timer_T5 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( negazione di (il timer 'subclass_c3_timer_t5' è scaduto) )  o  
( negazione di (il timer 'subclass_c3_timer_t5' è inattivo) ) )  o  
( ( negazione di ((subclass_c3_variabile_v9)  è uguale a  (4)) )  e  
( negazione di (negazione di ((subclass_c3_variabile_v9)  è uguale a  (4))) ) )""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( negazione di (il timer 'subclass_c3_timer_t5' è scaduto) )  o  
( negazione di (il timer 'subclass_c3_timer_t5' è inattivo) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t5' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t5' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t5' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t5' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_variabile_v9)  è uguale a  (4)) )  e  
( negazione di (negazione di ((subclass_c3_variabile_v9)  è uguale a  (4))) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v9)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v9)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_variabile_v9)  è uguale a  (4)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v9)  è uguale a  (4))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v9)  è uguale a  (4)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t5' è inattivo""", [
                            ]),#1
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c3_macroef_m1_SrfMacroDefInfo(di_ctx)
        #  /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  /*105,*/ è  uguale a  /*53,*/ 1 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 1250213 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 4, /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 5
        if db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v6() == 1, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l4())), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_contatore_co3().get_valore() > 1250213, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v9() > 4, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c3_variabile_v9(5)
        #  /*36,*/  se il timer SubClass_C3_timer_T5 non è scaduto /*36,*/ o  se il timer SubClass_C3_timer_T5 non è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V9 è  diverso da  /*56,*/ 4 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 non è  diverso da  /*56,*/ 4 /*36,*/ o  se il timer SubClass_C3_timer_T5 è disattivo, /*68,*/Attiva il timer SubClass_C3_timer_T7
        if db((db((db((db(not db(self.get_subclass_c3_timer_t5().isScaduto(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t5().isDisattivato(), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v9() == 4, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_variabile_v9() == 4, di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t5().isDisattivato(), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.get_subclass_c3_timer_t7().attiva()
    
    def macroSubclass_c3_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C3_timer_T7 non è scaduto,  Applica gli effetti
               della macro SubClass_C3_macroef_M6  commento: {73,}
        
           
         commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  diverso da  False , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 4
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  True 
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto,  Applica gli effetti
       della macro SubClass_C3_macroef_M6""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l1')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l1')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M6"""),#1
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*73,*/

   
 /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  diverso da  False , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 4

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  True""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            ]),#1
                ])

        populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è scaduto,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M6
        if db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l1())), di_ctx.subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c3_macroef_m6(di_ctx.subs[0].subs[1])
        #  /*73,*/
        #     
        #   /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L10 è  diverso da  False , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 4
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  True
        if db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == False, di_ctx.subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[1].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l10())), di_ctx.subs[1].subs[0]):
            self.set_subclass_c3_variabile_v9(4)
        else:
            self.set_subclass_c3_comando_c6(True)
    
    def macroSubclass_c3_macroef_m4(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {41,}  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da c270, commento: {70,}Incrementa il contatore SubClass_C3_contatore_Co3
        
           
         commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a AC,  Applica gli effetti
               della macro SubClass_C3_macroef_M1  commento: {73,}
        
         ,altrimenti  commento: {69,}Disattiva il timer SubClass_C3_timer_T7
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m4_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da c270, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a AC,  Applica gli effetti
       della macro SubClass_C3_macroef_M1  /*73,*/

 ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T7""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a AC""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv1_restore)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M1"""),#1
                            ]),#1
                ])

        populate_macroSubclass_c3_macroef_m4_SrfMacroDefInfo(di_ctx)
        #  /*41,*/  se MainClass_C1_parametro_P1 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da c270, /*70,*/Incrementa il contatore SubClass_C3_contatore_Co3
        if db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l4())), di_ctx.subs[0].subs[0]):
            self.get_subclass_c3_contatore_co3().incrementa()
        #  /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 non è  uguale a AC,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M1  /*73,*/
        #   ,altrimenti  /*69,*/Disattiva il timer SubClass_C3_timer_T7
        if db(not db(self.get_subclass_c3_restoreva_rv1_restore() == GlobalEnumeration.ac, di_ctx.subs[1].subs[0].subs[0]), di_ctx.subs[1].subs[0]):
            self.macroSubclass_c3_macroef_m1(di_ctx.subs[1].subs[1])
        else:
            self.get_subclass_c3_timer_t7().disattiva()
    
    def macroSubclass_c3_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {34,}  se il parametro SubClass_C3_parametro_P5 è  diverso da  commento: {56,} 10 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 è  minore di  commento: {55,} 6 commento: {35,} e  se il controllo SubClass_C3_controllo_C9 è  uguale a  True  commento: {35,} e  se il controllo SubClass_C3_controllo_C9 non è  diverso da  False , commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  False 
        
         ,altrimenti   commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 1 commento: {67,}
        
        
         commento: {35,}  se il controllo SubClass_C3_controllo_C9 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  commento: {36,} e  se il timer SubClass_C3_timer_T10 non è attivo e  se il controllo ConsDef  è  uguale a FALSE , commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 6
        
           
         commento: {37,}  se la variabile SubClass_C3_variabile_V9 è  maggiore di  commento: {54,} 2,  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V9 il valore 7 commento: {67,}
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  False 
        
        
         commento: {35,}  se il controllo SubClass_C3_controllo_C9 è  diverso da  True  commento: {36,} e  se il timer SubClass_C3_timer_T7 non è disattivo, commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  False 
        
         ,altrimenti  commento: {66,} Assegna al comando SubClass_C3_comando_C6 il valore  True 
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*34,*/  se il parametro SubClass_C3_parametro_P5 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 6 /*35,*/ e  se il controllo SubClass_C3_controllo_C9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C9 non è  diverso da  False , /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  False 

 ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 1""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*34,*/  se il parametro SubClass_C3_parametro_P5 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 6 /*35,*/ e  se il controllo SubClass_C3_controllo_C9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C9 non è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di ((subclass_c3_parametro_p5)  è uguale a  (10)) )  e  ( (subclass_c3_variabile_v9)  è minore di  (6) ) )  e  ( (subclass_c3_controllo_c9)  è uguale a  (True) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_parametro_p5)  è uguale a  (10)) )  e  ( (subclass_c3_variabile_v9)  è minore di  (6) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p5)  è uguale a  (10))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v9)  è minore di  (6)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c9)  è uguale a  (True)""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_controllo_c9)  è uguale a  (False)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                            DIStatement("""ITStatement\n/*67,*/


 /*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C3_timer_T10 non è attivo e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 6""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*67,*/


 /*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C3_timer_T10 non è attivo e  se il controllo ConsDef  è  uguale a FALSE""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c9)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( (consdef)  è uguale a  (False) )  e  ( negazione di (il timer 'subclass_c3_timer_t10' è attivo) ) )  e  
( (consdef)  è uguale a  (False) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( (consdef)  è uguale a  (False) )  e  ( negazione di (il timer 'subclass_c3_timer_t10' è attivo) )""", [
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t10' è attivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t10' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\n(consdef)  è uguale a  (False)""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#1
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C3_variabile_V9 è  maggiore di  /*54,*/ 2,  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 7 /*67,*/

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  False""", [
                            DIBoolExpr("""GreaterThanImpl\nla variabile SubClass_C3_variabile_V9 è  maggiore di  /*54,*/ 2""", [
                            ]),#0
                            ]),#2
                            DIStatement("""ITEStatementImpl\n/*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo, /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  False 

 ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_timer_t7' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#3
                ])

        populate_macroSubclass_c3_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*34,*/  se il parametro SubClass_C3_parametro_P5 è  diverso da  /*56,*/ 10 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 6 /*35,*/ e  se il controllo SubClass_C3_controllo_C9 è  uguale a  True  /*35,*/ e  se il controllo SubClass_C3_controllo_C9 non è  diverso da  False , /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  False 
        #   ,altrimenti   /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 1
        if db((db((db((db(not db(self.get_subclass_c3_parametro_p5() == 10, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v9() < 6, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_controllo_c9() == True, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            self.set_subclass_c3_comando_c6(False)
        else:
            self.set_subclass_c3_variabile_v9(1)
        #  /*67,*/
        #   /*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  False  o  se il controllo ConsDef  è  uguale a FALSE  /*36,*/ e  se il timer SubClass_C3_timer_T10 non è attivo e  se il controllo ConsDef  è  uguale a FALSE , /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 6
        if db((db(not db(self.get_subclass_c3_controllo_c9() == False, di_ctx.subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[1].subs[0].subs[0]) or db((db((db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t10().isAttivato(), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0].subs[1].subs[0]) and db(self.get_consdef() == False, di_ctx.subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[1].subs[0].subs[1])), di_ctx.subs[1].subs[0]):
            self.set_subclass_c3_variabile_v9(6)
        #  /*37,*/  se la variabile SubClass_C3_variabile_V9 è  maggiore di  /*54,*/ 2,  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V9 il valore 7 /*67,*/
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  False
        if db(self.get_subclass_c3_variabile_v9() > 2, di_ctx.subs[2].subs[0]):
            self.set_subclass_c3_variabile_v9(7)
        else:
            self.set_subclass_c3_comando_c6(False)
        #  /*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  True  /*36,*/ e  se il timer SubClass_C3_timer_T7 non è disattivo, /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  False 
        #   ,altrimenti  /*66,*/ Assegna al comando SubClass_C3_comando_C6 il valore  True
        if db((db(not db(self.get_subclass_c3_controllo_c9() == True, di_ctx.subs[3].subs[0].subs[0].subs[0]), di_ctx.subs[3].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t7().isDisattivato(), di_ctx.subs[3].subs[0].subs[1].subs[0]), di_ctx.subs[3].subs[0].subs[1])), di_ctx.subs[3].subs[0]):
            self.set_subclass_c3_comando_c6(False)
        else:
            self.set_subclass_c3_comando_c6(True)
    
    # verify macros
    @srf_value_macro("macroSubclass_c3_macrove_m3")
    def macroSubclass_c3_macrove_m3(self, argomento_ave10, argomento_ave5, argomento_ave6, argomento_ave7, argomento_ave8, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {36,}  se il timer SubClass_C3_timer_T5 è attivo,  commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  commento: {55,} 4 commento: {34,} e  se il parametro SubClass_C3_parametro_P5 non è  minore di  commento: {55,} 2 commento: {37,} o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  commento: {54,} 5 commento: {36,} o  se il timer SubClass_C3_timer_T7 non è attivo o  se l'argomento argomento_ave8 è  uguale a  True  commento: {39,}  o  se l'argomento argomento_ave7 non  è  diverso da AC commento: {39,} , Solo una delle seguenti { 
         commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} o  se il timer SubClass_C3_timer_T10 è scaduto commento: {36,} e  se il timer SubClass_C3_timer_T10 non è disattivo commento: {34,} o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  commento: {37,} o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  commento: {54,} 5 o  se l'argomento argomento_ave8 non  è  diverso da  False  commento: {39,} , Verifica che   commento: {47,48,49,}  commento: {,}  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
         commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T5 sia disattivo
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T7 sia scaduto
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  commento: {54,} 6
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False 
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  il timer SubClass_C3_timer_T5 sia attivo
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C9 sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V9 non sia  minore di  commento: {55,} 10
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m3_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  o  se l'argomento argomento_ave7 non  è  diverso da AC /*39,*/ , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ o  se il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 o  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/ , Verifica che   /*47,48,49,*/  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T7 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False 


 } Verifica che   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T5 sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V9 non sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  o  se l'argomento argomento_ave7 non  è  diverso da AC /*39,*/ , Solo una delle seguenti { 
 /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ o  se il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 o  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/ , Verifica che   /*47,48,49,*/  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T7 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo o  se l'argomento argomento_ave8 è  uguale a  True  /*39,*/  o  se l'argomento argomento_ave7 non  è  diverso da AC""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo o  se l'argomento argomento_ave8 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 /*36,*/ o  se il timer SubClass_C3_timer_T7 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2 /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*36,*/  se il timer SubClass_C3_timer_T5 è attivo,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T5 è attivo""", [
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  diverso da  False , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è minore di  (4)) allora (negazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (False)))""", [
                            DIBoolExpr("""LessThanImpl\n/*41,*/   MainClass_C1_parametro_P2 del campo  MainClass_C1     è  minore di  /*55,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P5 non è  minore di  /*55,*/ 2""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p5)  è minore di  (2)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v9)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T7 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave8 è  uguale a  True""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave7 non  è  diverso da AC""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave7)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave7)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ o  se il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 o  se l'argomento argomento_ave8 non  è  diverso da  False  /*39,*/ , Verifica che   /*47,48,49,*/  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T7 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ o  se il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5 o  se l'argomento argomento_ave8 non  è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ o  se il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True  /*37,*/ o  se la variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ o  se il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo /*34,*/ o  se il parametro SubClass_C3_parametro_P10 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ o  se il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C3_timer_T10 è scaduto /*36,*/ e  se il timer SubClass_C3_timer_T10 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T10 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T10 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t10' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P10 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p10)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V9 non è  maggiore di  /*54,*/ 5""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_variabile_v9)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave8 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave8)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T7 sia scaduto
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,49,*/  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True 
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T7 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,49,*/  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T7 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True 
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T5 sia disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*36,*/  il timer SubClass_C3_timer_T7 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  /*54,*/ 6
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  maggiore di  /*54,*/ 6""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_parametro_p5)  è maggiore di  (6)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P10 non sia  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p10)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T5 sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 sia  uguale a  False 
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V9 non sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T5 sia attivo
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 sia  uguale a  False""", [
                            DIBoolExpr("""Predicato Oggetto\nche   /*48,49,50,*/  /*,*/  il timer SubClass_C3_timer_T5 sia attivo""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il controllo SubClass_C3_controllo_C9 sia  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V9 non sia  minore di  /*55,*/ 10""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v9)  è minore di  (10)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m3_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db((db((db(self.get_subclass_c3_timer_t5().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l4()) if db(it.get_mainclass_c1().get_mainclass_c1_parametro_p2() < 4, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p5() < 2, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v9() > 5, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t7().isAttivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(argomento_ave8 == True, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave7 == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db((db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c3_timer_t10().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t10().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_parametro_p10() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_variabile_v9() > 5, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db(not db(not db(argomento_ave8 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0]) or db((db((db(not db(not db(self.get_subclass_c3_controllo_c9() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db((db(not db(self.get_subclass_c3_parametro_p10() == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t5().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_timer_t7().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c3_parametro_p5() > 6, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p10() == False, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_subclass_c3_timer_t5().isAttivato(), di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(self.get_subclass_c3_controllo_c9() == False, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) or db(not db(self.get_subclass_c3_variabile_v9() < 10, di_ctx.subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m7")
    def macroSubclass_c3_macrove_m7(self, argomento_ave1, argomento_ave2, argomento_ave3, argomento_ave4, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {38,}  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 12 commento: {37,} e  se la variabile SubClass_C3_variabile_V9 è  minore di  commento: {55,} 9 commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  commento: {54,} 11 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  commento: {56,} 144 commento: {38,} o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  commento: {53,} 13 o  se l'argomento argomento_ave2 non  è  diverso da  False  commento: {39,} , Verifica che   commento: {49,50,}  commento: {,}  la variabile SubClass_C3_variabile_V9 sia  diverso da  commento: {56,} 10
         commento: {104,} e  che  commento: {,}  il timer SubClass_C3_timer_T7 non sia disattivo
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m7_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9 /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 144 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 13 o  se l'argomento argomento_ave2 non  è  diverso da  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V9 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*38,*/  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9 /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 144 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 13 o  se l'argomento argomento_ave2 non  è  diverso da  False  /*39,*/ , Verifica che   /*49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V9 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9 /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 144 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 13 o  se l'argomento argomento_ave2 non  è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9 /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 144 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*38,*/  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9 /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 11 /*38,*/ o  se il contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 144""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9 /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*38,*/  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12 /*37,*/ e  se la variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 12""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co3)  è maggiore di  (12)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C3_variabile_V9 è  minore di  /*55,*/ 9""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nil contatore SubClass_C3_contatore_Co3 è  maggiore di  /*54,*/ 11""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co3 non è  diverso da  /*56,*/ 144""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è uguale a  (144))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co3)  è uguale a  (144)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil contatore SubClass_C3_contatore_Co3 è  uguale a  /*53,*/ 13""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave2 non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave2)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave2)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V9 sia  diverso da  /*56,*/ 10
 /*104,*/ e  che  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V9 sia  diverso da  /*56,*/ 10""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v9)  è uguale a  (10)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il timer SubClass_C3_timer_T7 non sia disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t7' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m7_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db((db((db((db(not db(self.get_subclass_c3_contatore_co3().get_valore() > 12, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_variabile_v9() < 9, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co3().get_valore() > 11, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_contatore_co3().get_valore() == 144, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_contatore_co3().get_valore() == 13, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(not db(not db(argomento_ave2 == False, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v9() == 10, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t7().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c3_macrova_m2")
    def macroSubclass_c3_macrova_m2(self, argomento_a10, argomento_a5, argomento_a7, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo SubClass_C3_controllo_C9 è  diverso da  True ,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {41,}   MainClass_C1_parametro_P1 del campo  MainClass_C1     commento: {105,} è  diverso da c270 , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m2_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  True ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P1 del campo  MainClass_C1     /*105,*/ è  diverso da c270 , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*[*/ /*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  True ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P1 del campo  MainClass_C1     /*105,*/ è  diverso da c270""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c9)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c9)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (c270))) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l4')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (c270))) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l4')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (c270))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p1 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (c270)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l4')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l4')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macrova_m2_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo SubClass_C3_controllo_C9 è  diverso da  True ,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L4 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*41,*/   MainClass_C1_parametro_P1 del campo  MainClass_C1     /*105,*/ è  diverso da c270 , assegna alla macro il valore  False
        if db((db(not db(self.get_subclass_c3_controllo_c9() == True, di_ctx.subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l4()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_parametro_p1() == GlobalEnumeration.c270, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    @srf_value_macro("macroSubclass_c3_macrova_m5")
    def macroSubclass_c3_macrova_m5(self, argomento_a1, argomento_a2, argomento_a3, argomento_a4, argomento_a6, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo commento: {110,} e  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è scaduto commento: {41,} e  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C3_lista_L7 è  maggiore di  commento: {54,} 5 commento: {109,} o  se il ripristino della variabile  SubClass_C3_restoreva_RV2 non è  uguale a AC commento: {38,} e  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  commento: {54,} 15 commento: {44,} o  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  uguale a  False  , assegna alla macro il valore  False 
        
         commento: {46,} assegna alla macro il valore  True  commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m5_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo /*110,*/ e  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è scaduto /*41,*/ e  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C3_lista_L7 è  maggiore di  /*54,*/ 5 /*109,*/ o  se il ripristino della variabile  SubClass_C3_restoreva_RV2 non è  uguale a AC /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 15 /*44,*/ o  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  uguale a  False  , assegna alla macro il valore  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo /*110,*/ e  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è scaduto /*41,*/ e  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C3_lista_L7 è  maggiore di  /*54,*/ 5 /*109,*/ o  se il ripristino della variabile  SubClass_C3_restoreva_RV2 non è  uguale a AC /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 15 /*44,*/ o  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (il timer 'subclass_c3_restoreti_ti2_restore' è inattivo) )  e  ( il timer 'subclass_c3_restoreti_ti2_restore' è scaduto ) )  e  
( per ognuna delle seguenti {((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c3_lista_l7)  è maggiore di  (5))} ) )  o  
( ( negazione di ((subclass_c3_restoreva_rv2_restore)  è uguale a  (ac)) )  e  
( negazione di ((subclass_c3_contatore_co3)  è maggiore di  (15)) ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (il timer 'subclass_c3_restoreti_ti2_restore' è inattivo) )  e  ( il timer 'subclass_c3_restoreti_ti2_restore' è scaduto ) )  e  
( per ognuna delle seguenti {((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c3_lista_l7)  è maggiore di  (5))} )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (il timer 'subclass_c3_restoreti_ti2_restore' è inattivo) )  e  ( il timer 'subclass_c3_restoreti_ti2_restore' è scaduto )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_restoreti_ti2_restore' è inattivo)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti2_restore' è inattivo""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti2_restore' è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c3_lista_l7)  è maggiore di  (5))}""", [
                            DIBoolExpr("""GreaterThanImpl\n(mainclass_c1_parametro_p2 del campo mainclass_c1 della lista subclass_c3_lista_l7)  è maggiore di  (5)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_restoreva_rv2_restore)  è uguale a  (ac)) )  e  
( negazione di ((subclass_c3_contatore_co3)  è maggiore di  (15)) )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_restoreva_rv2_restore)  è uguale a  (ac))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv2_restore)  è uguale a  (ac)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co3)  è maggiore di  (15))""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co3)  è maggiore di  (15)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (False))}""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l4)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macrova_m5_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI2 non è disattivo /*110,*/ e  se il ripristino del timer  SubClass_C3_restoreTI_TI2 è scaduto /*41,*/ e  se MainClass_C1_parametro_P2 del campo  MainClass_C1 di SubClass_C3_lista_L7 è  maggiore di  /*54,*/ 5 /*109,*/ o  se il ripristino della variabile  SubClass_C3_restoreva_RV2 non è  uguale a AC /*38,*/ e  se il contatore SubClass_C3_contatore_Co3 non è  maggiore di  /*54,*/ 15 /*44,*/ o  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L4 è  uguale a  False  , assegna alla macro il valore  False
        if db((db((db((db((db(not db(self.get_subclass_c3_restoreti_ti2_restore().isDisattivato(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_restoreti_ti2_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p2() > 5, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l7())), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_restoreva_rv2_restore() == GlobalEnumeration.ac, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_contatore_co3().get_valore() > 15, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(all(db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l4())), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return False
        #  /*46,*/ assegna alla macro il valore  True
        return True
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c3_command_comm4DaSender41f3f0dc(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c3_command_comm4DaSender41f3f0dc')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c3_previousco_c1_prev(self.get_subclass_c3_previousco_c1())
        self.set_subclass_c3_previousco_c10_prev(self.get_subclass_c3_previousco_c10())
        self.set_subclass_c3_previousco_c3_prev(self.get_subclass_c3_previousco_c3())
        self.set_subclass_c3_previousco_c7_prev(self.get_subclass_c3_previousco_c7())
        self.set_subclass_c3_previousco_c8_prev(self.get_subclass_c3_previousco_c8())
        self.set_subclass_c3_previousva_pv1_prev(self.get_subclass_c3_previousva_pv1())
        self.set_subclass_c3_previousva_pv2_prev(self.get_subclass_c3_previousva_pv2())
        self.set_subclass_c3_previousva_pv3_prev(self.get_subclass_c3_previousva_pv3())
        self.set_subclass_c3_previousva_pv4_prev(self.get_subclass_c3_previousva_pv4())
        self.set_subclass_c3_previousva_pv5_prev(self.get_subclass_c3_previousva_pv5())

class SubClass_C3_RecordHeaderR10(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled20, recordfiled5, recordfiled9, recordfiled19):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled20(recordfiled20)
        self.set_recordfiled5(recordfiled5)
        self.set_recordfiled9(recordfiled9)
        self.set_recordfiled19(recordfiled19)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled20(self, recordfiled20):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"), recordfiled20)

    def set_recordfiled5(self, recordfiled5):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"), recordfiled5)

    def set_recordfiled9(self, recordfiled9):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"), recordfiled9)

    def set_recordfiled19(self, recordfiled19):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"), recordfiled19)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled20(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled20"))

    def get_recordfiled5(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled5"))

    def get_recordfiled9(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled9"))

    def get_recordfiled19(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled19"))



