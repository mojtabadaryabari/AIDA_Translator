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

class SubClass_C3(ProcessImpl):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses
    def __init__(self, *args, **kwds):
        super(SubClass_C3, self).__init__(*args, **kwds)

        # initialize the state variables

        self.set_subclass_c3_previousva_pv1(False)
        self.set_subclass_c3_previousva_pv2(False)
        self.set_subclass_c3_previousva_pv3(GlobalEnumeration.c180)
        self.set_subclass_c3_previousva_pv4(False)
        self.set_subclass_c3_previousva_pv5(GlobalEnumeration.avanzamento)
        self.set_subclass_c3_restoreva_rv1(0)
        self.set_subclass_c3_restoreva_rv2(GlobalEnumeration.avanzamento)
        self.set_subclass_c3_restoreva_rv3(False)
        self.set_subclass_c3_restoreva_rv4(0)
        self.set_subclass_c3_variabile_v2(GlobalEnumeration.rossogialloaverdea)
        self.set_subclass_c3_variabile_v5(0)
        self.set_subclass_c3_variabile_v6(False)
        self.set_subclass_c3_variabile_v7(GlobalEnumeration.gialloaverdea)
        self.set_subclass_c3_variabile_v8(False)

        self._expected_commands_map = {
            Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1 : set([]),
        }

    def set_expected_cmds_response(self):
        # for each manual command of SubClass_C3
        if self.is_triggered('eventSubclass_c3_command_comm10DaSender4471a7d8'):
            self.set_man_cmd_response('eventSubclass_c3_command_comm10DaSender4471a7d8',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c3_command_comm10DaSender4471a7d8',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c3_command_comm3'):
            self.set_man_cmd_response('eventSubclass_c3_command_comm3',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c3_command_comm3',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c3_command_comm7'):
            self.set_man_cmd_response('eventSubclass_c3_command_comm7',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c3_command_comm7',self.ManCmdResponse.NOOP)
        if self.is_triggered('eventSubclass_c3_command_comm8DaSender7a3d0e35'):
            self.set_man_cmd_response('eventSubclass_c3_command_comm8DaSender7a3d0e35',self.ManCmdResponse.UNEXPECTED)
        else:
            self.set_man_cmd_response('eventSubclass_c3_command_comm8DaSender7a3d0e35',self.ManCmdResponse.NOOP)



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
    def init_configuration(self, subclass_c3_lista_l1, subclass_c3_lista_l5, subclass_c3_lista_l6, subclass_c3_parametro_p5, subclass_c3_parametro_p7, subclass_c3_parametro_p8):
        # initialize the record type parameters
        self.set_subclass_c3_lista_l1(subclass_c3_lista_l1)
        self.set_subclass_c3_lista_l5(subclass_c3_lista_l5)
        self.set_subclass_c3_lista_l6(subclass_c3_lista_l6)
        # initialize the simple type parameters
        self.set_subclass_c3_parametro_p5(subclass_c3_parametro_p5)
        self.set_subclass_c3_parametro_p7(subclass_c3_parametro_p7)
        self.set_subclass_c3_parametro_p8(subclass_c3_parametro_p8)

        # initialize the timers
        self.set_subclass_c3_restoreti_ti1(521000)
        self.set_subclass_c3_restoreti_ti1_restore(521000)
        self.set_subclass_c3_restoreti_ti2(25000)
        self.set_subclass_c3_restoreti_ti2_restore(25000)
        self.set_subclass_c3_restoreti_ti3(104000)
        self.set_subclass_c3_restoreti_ti3_restore(104000)
        self.set_subclass_c3_restoreti_ti4(4321000)
        self.set_subclass_c3_restoreti_ti4_restore(4321000)
        self.set_subclass_c3_restoreti_ti5(45000)
        self.set_subclass_c3_restoreti_ti5_restore(45000)
        self.set_subclass_c3_timer_t4(550000)
        self.set_subclass_c3_timer_t6(343000)

        self.timers = [self.subclass_c3_restoreti_ti1,self.subclass_c3_restoreti_ti1_restore,self.subclass_c3_restoreti_ti2,self.subclass_c3_restoreti_ti2_restore,self.subclass_c3_restoreti_ti3,self.subclass_c3_restoreti_ti3_restore,self.subclass_c3_restoreti_ti4,self.subclass_c3_restoreti_ti4_restore,self.subclass_c3_restoreti_ti5,self.subclass_c3_restoreti_ti5_restore,self.subclass_c3_timer_t4,self.subclass_c3_timer_t6,]

        # initialize the counters
        self.set_subclass_c3_contatore_co10(0)
        self.set_subclass_c3_contatore_co2(0)
        self.set_subclass_c3_contatore_co8(0)
        self.set_subclass_c3_contatore_co9(0)

    # setters for record type parameters
    def set_subclass_c3_lista_l1(self, subclass_c3_lista_l1):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l1",subclass_c3_lista_l1)

    def set_subclass_c3_lista_l5(self, subclass_c3_lista_l5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l5",subclass_c3_lista_l5)

    def set_subclass_c3_lista_l6(self, subclass_c3_lista_l6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l6",subclass_c3_lista_l6)


    # getters for record type parameters
    def get_subclass_c3_lista_l1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l1")

    def get_subclass_c3_lista_l5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l5")

    def get_subclass_c3_lista_l6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_lista_l6")


    # setters for simple type parameters
    def set_subclass_c3_parametro_p5(self, subclass_c3_parametro_p5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p5",subclass_c3_parametro_p5)

    def set_subclass_c3_parametro_p7(self, subclass_c3_parametro_p7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p7",subclass_c3_parametro_p7)

    def set_subclass_c3_parametro_p8(self, subclass_c3_parametro_p8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p8",subclass_c3_parametro_p8)


    # getters for simple type parameters
    def get_subclass_c3_parametro_p5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p5")

    def get_subclass_c3_parametro_p7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p7")

    def get_subclass_c3_parametro_p8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_parametro_p8")


    # setters for comandi al piazzale
    def set_subclass_c3_comando_c3(self, subclass_c3_comando_c3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c3",subclass_c3_comando_c3)

    def set_subclass_c3_comando_c5(self, subclass_c3_comando_c5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c5",subclass_c3_comando_c5)

    def set_subclass_c3_comando_c7(self, subclass_c3_comando_c7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c7",subclass_c3_comando_c7)

    def set_subclass_c3_comando_c8(self, subclass_c3_comando_c8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c8",subclass_c3_comando_c8)

    def set_subclass_c3_comando_c9(self, subclass_c3_comando_c9):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_comando_c9",subclass_c3_comando_c9)


    # getters for controlli dal piazzale
    def get_consdef(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"consdef")

    def get_subclass_c3_controllo_c5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c5")

    def get_subclass_c3_controllo_c7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c7")

    def get_subclass_c3_controllo_c8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c8")

    def get_subclass_c3_controllo_c9(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_controllo_c9")

    def get_subclass_c3_previousco_c1(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c1")

    def get_subclass_c3_previousco_c10(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c10")

    def get_subclass_c3_previousco_c2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c2")

    def get_subclass_c3_previousco_c4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c4")

    def get_subclass_c3_previousco_c6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c6")


    # setters for state variables
    def set_subclass_c3_previousco_c1_prev(self, subclass_c3_previousco_c1_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c1_prev",subclass_c3_previousco_c1_prev)
    def set_subclass_c3_previousco_c10_prev(self, subclass_c3_previousco_c10_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c10_prev",subclass_c3_previousco_c10_prev)
    def set_subclass_c3_previousco_c2_prev(self, subclass_c3_previousco_c2_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c2_prev",subclass_c3_previousco_c2_prev)
    def set_subclass_c3_previousco_c4_prev(self, subclass_c3_previousco_c4_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c4_prev",subclass_c3_previousco_c4_prev)
    def set_subclass_c3_previousco_c6_prev(self, subclass_c3_previousco_c6_prev):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c6_prev",subclass_c3_previousco_c6_prev)
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
    def set_subclass_c3_restoreva_rv3(self, subclass_c3_restoreva_rv3):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv3",subclass_c3_restoreva_rv3)
    def set_subclass_c3_restoreva_rv4(self, subclass_c3_restoreva_rv4):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv4",subclass_c3_restoreva_rv4)
    def set_subclass_c3_variabile_v2(self, subclass_c3_variabile_v2):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v2",subclass_c3_variabile_v2)
    def set_subclass_c3_variabile_v5(self, subclass_c3_variabile_v5):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v5",subclass_c3_variabile_v5)
    def set_subclass_c3_variabile_v6(self, subclass_c3_variabile_v6):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v6",subclass_c3_variabile_v6)
    def set_subclass_c3_variabile_v7(self, subclass_c3_variabile_v7):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v7",subclass_c3_variabile_v7)
    def set_subclass_c3_variabile_v8(self, subclass_c3_variabile_v8):
        self.memory.set_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v8",subclass_c3_variabile_v8)

    # getters for state variables
    def get_stato_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"stato_restore")

    def get_subclass_c3_previousco_c1_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c1_prev")

    def get_subclass_c3_previousco_c10_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c10_prev")

    def get_subclass_c3_previousco_c2_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c2_prev")

    def get_subclass_c3_previousco_c4_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c4_prev")

    def get_subclass_c3_previousco_c6_prev(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_previousco_c6_prev")

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

    def get_subclass_c3_restoreva_rv3(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv3")

    def get_subclass_c3_restoreva_rv3_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv3_restore")

    def get_subclass_c3_restoreva_rv4(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv4")

    def get_subclass_c3_restoreva_rv4_restore(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_restoreva_rv4_restore")

    def get_subclass_c3_variabile_v2(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v2")

    def get_subclass_c3_variabile_v5(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v5")

    def get_subclass_c3_variabile_v6(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v6")

    def get_subclass_c3_variabile_v7(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v7")

    def get_subclass_c3_variabile_v8(self):
        return self.memory.get_var(self.station_name,self.name,self.instance_name,"subclass_c3_variabile_v8")


    # setters for timers
    def set_subclass_c3_restoreti_ti1(self, timerDuration):
        self.subclass_c3_restoreti_ti1 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti1", self.memory)

    def set_subclass_c3_restoreti_ti1_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti1_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti1_restore", self.memory)

    def set_subclass_c3_restoreti_ti2(self, timerDuration):
        self.subclass_c3_restoreti_ti2 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti2", self.memory)

    def set_subclass_c3_restoreti_ti2_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti2_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti2_restore", self.memory)

    def set_subclass_c3_restoreti_ti3(self, timerDuration):
        self.subclass_c3_restoreti_ti3 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti3", self.memory)

    def set_subclass_c3_restoreti_ti3_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti3_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti3_restore", self.memory)

    def set_subclass_c3_restoreti_ti4(self, timerDuration):
        self.subclass_c3_restoreti_ti4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti4", self.memory)

    def set_subclass_c3_restoreti_ti4_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti4_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti4_restore", self.memory)

    def set_subclass_c3_restoreti_ti5(self, timerDuration):
        self.subclass_c3_restoreti_ti5 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti5", self.memory)

    def set_subclass_c3_restoreti_ti5_restore(self, timerDuration):
        self.subclass_c3_restoreti_ti5_restore = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_restoreti_ti5_restore", self.memory)

    def set_subclass_c3_timer_t4(self, timerDuration):
        self.subclass_c3_timer_t4 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t4", self.memory)

    def set_subclass_c3_timer_t6(self, timerDuration):
        self.subclass_c3_timer_t6 = Timer(timerDuration, self.station_name, self.name, self.instance_name, "subclass_c3_timer_t6", self.memory)


    # getters for timers
    def get_subclass_c3_restoreti_ti1(self):
        return self.subclass_c3_restoreti_ti1

    def get_subclass_c3_restoreti_ti1_restore(self):
        return self.subclass_c3_restoreti_ti1_restore

    def get_subclass_c3_restoreti_ti2(self):
        return self.subclass_c3_restoreti_ti2

    def get_subclass_c3_restoreti_ti2_restore(self):
        return self.subclass_c3_restoreti_ti2_restore

    def get_subclass_c3_restoreti_ti3(self):
        return self.subclass_c3_restoreti_ti3

    def get_subclass_c3_restoreti_ti3_restore(self):
        return self.subclass_c3_restoreti_ti3_restore

    def get_subclass_c3_restoreti_ti4(self):
        return self.subclass_c3_restoreti_ti4

    def get_subclass_c3_restoreti_ti4_restore(self):
        return self.subclass_c3_restoreti_ti4_restore

    def get_subclass_c3_restoreti_ti5(self):
        return self.subclass_c3_restoreti_ti5

    def get_subclass_c3_restoreti_ti5_restore(self):
        return self.subclass_c3_restoreti_ti5_restore

    def get_subclass_c3_timer_t4(self):
        return self.subclass_c3_timer_t4

    def get_subclass_c3_timer_t6(self):
        return self.subclass_c3_timer_t6


    # setters for counters
    def set_subclass_c3_contatore_co10(self, counterInitValue):
        self.subclass_c3_contatore_co10 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co10", self.memory)

    def set_subclass_c3_contatore_co2(self, counterInitValue):
        self.subclass_c3_contatore_co2 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co2", self.memory)

    def set_subclass_c3_contatore_co8(self, counterInitValue):
        self.subclass_c3_contatore_co8 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co8", self.memory)

    def set_subclass_c3_contatore_co9(self, counterInitValue):
        self.subclass_c3_contatore_co9 = Counter(counterInitValue, self.station_name, self.name, self.instance_name, "subclass_c3_contatore_co9", self.memory)


    # getters for counters
    def get_subclass_c3_contatore_co10(self):
        return self.subclass_c3_contatore_co10

    def get_subclass_c3_contatore_co2(self):
        return self.subclass_c3_contatore_co2

    def get_subclass_c3_contatore_co8(self):
        return self.subclass_c3_contatore_co8

    def get_subclass_c3_contatore_co9(self):
        return self.subclass_c3_contatore_co9



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

        self.set_subclass_c3_previousco_c1_prev(False)
        self.set_subclass_c3_previousco_c10_prev(GlobalEnumeration.rossoverde)
        self.set_subclass_c3_previousco_c2_prev(False)
        self.set_subclass_c3_previousco_c4_prev(GlobalEnumeration.rossogialloverde)
        self.set_subclass_c3_previousco_c6_prev(False)
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
    def macroSubclass_c3_macroef_m2(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {37,}  se la variabile SubClass_C3_variabile_V6 è  diverso da  False ,  Applica gli effetti
               della macro SubClass_C3_macroef_M6  commento: {73,}
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  True 
        
        
         commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI5 è scaduto,  Applica gli effetti
               della macro SubClass_C3_macroef_M6  commento: {73,}
        
           
        
        }
        """
        def populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*37,*/  se la variabile SubClass_C3_variabile_V6 è  diverso da  False ,  Applica gli effetti
       della macro SubClass_C3_macroef_M6  /*73,*/

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V6 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M6"""),#1
                            ]),#0
                            DIStatement("""ITStatement\n/*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI5 è scaduto,  Applica gli effetti
       della macro SubClass_C3_macroef_M6""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C3_restoreTI_TI5 è scaduto""", [
                            ]),#0
                            DIEffectMacro("""Chiamata Macro Effetti\nApplica gli effetti
       della macro SubClass_C3_macroef_M6"""),#1
                            ]),#1
                ])

        populate_macroSubclass_c3_macroef_m2_SrfMacroDefInfo(di_ctx)
        #  /*37,*/  se la variabile SubClass_C3_variabile_V6 è  diverso da  False ,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M6  /*73,*/
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  True
        if db(not db(self.get_subclass_c3_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.macroSubclass_c3_macroef_m6(di_ctx.subs[0].subs[1])
        else:
            self.set_subclass_c3_variabile_v8(True)
        #  /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI5 è scaduto,  Applica gli effetti
        #         della macro SubClass_C3_macroef_M6
        if db(self.get_subclass_c3_restoreti_ti5_restore().isScaduto(), di_ctx.subs[1].subs[0]):
            self.macroSubclass_c3_macroef_m6(di_ctx.subs[1].subs[1])
    
    def macroSubclass_c3_macroef_m6(self, di_ctx: DIEffectMacro):
        """
        CNL corrispondente:
        
        { commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False , commento: {71,}Decrementa il contatore SubClass_C3_contatore_Co10
        
         ,altrimenti  commento: {67,} Assegna alla variabile SubClass_C3_variabile_V8 il valore  False 
        
        
        
        }
        """
        def populate_macroSubclass_c3_macroef_m6_SrfMacroDefInfo(macroDebInfo: DIEffectMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITEStatementImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False , /*71,*/Decrementa il contatore SubClass_C3_contatore_Co10

 ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv3_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macroef_m6_SrfMacroDefInfo(di_ctx)
        #  /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False , /*71,*/Decrementa il contatore SubClass_C3_contatore_Co10
        #   ,altrimenti  /*67,*/ Assegna alla variabile SubClass_C3_variabile_V8 il valore  False
        if db(not db(self.get_subclass_c3_restoreva_rv3_restore() == False, di_ctx.subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0]):
            self.get_subclass_c3_contatore_co10().decrementa()
        else:
            self.set_subclass_c3_variabile_v8(False)
    
    # verify macros
    @srf_value_macro("macroSubclass_c3_macrove_m4")
    def macroSubclass_c3_macrove_m4(self, argomento_ave3, argomento_ave4, argomento_ave7, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {63,} commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False  commento: {36,} o  se il timer SubClass_C3_timer_T4 è scaduto commento: {38,} o  se il contatore SubClass_C3_contatore_Co8 è  minore di  commento: {55,} 1515 e  se l'argomento argomento_ave4 non  è  uguale a RossoVerde commento: {39,} , Solo una delle seguenti { 
         commento: {62,} commento: {38,}  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  commento: {53,} 130 commento: {35,} o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde commento: {36,} o  se il timer SubClass_C3_timer_T6 non è scaduto commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde commento: {35,} e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Almeno una delle seguenti { 
         commento: {61,} commento: {34,}  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde commento: {37,} e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
         commento: {109,}  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  commento: {53,} 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde commento: {39,}  commento: {37,} o  se la variabile SubClass_C3_variabile_V5 è  minore di  commento: {55,} 1, Verifica che   commento: {47,50,51,52,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 124
         commento: {104,} e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde commento: {,} 
         commento: {104,} e  che  commento: {38,}  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  commento: {54,} 13
         commento: {104,} o  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
        
        
         } Verifica che   commento: {50,51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  minore di  commento: {55,} 1532
         commento: {104,} e  che  commento: {,}  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
        
        
         } Verifica che   commento: {47,51,52,}  commento: {,}  il contatore SubClass_C3_contatore_Co8 sia  minore di  commento: {55,} 15
         commento: {104,} e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox commento: {,} 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P7 sia  maggiore di  commento: {54,} 3
        
        
         } Verifica che   commento: {47,49,}  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T4 sia attivo
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m4_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  minore di  /*55,*/ 1515 e  se l'argomento argomento_ave4 non  è  uguale a RossoVerde /*39,*/ , Solo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde /*36,*/ o  se il timer SubClass_C3_timer_T6 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1, Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1532
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 15
 /*104,*/ e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 sia  maggiore di  /*54,*/ 3


 } Verifica che   /*47,49,*/  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia attivo""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  minore di  /*55,*/ 1515 e  se l'argomento argomento_ave4 non  è  uguale a RossoVerde /*39,*/ , Solo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde /*36,*/ o  se il timer SubClass_C3_timer_T6 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1, Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1532
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 15
 /*104,*/ e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 sia  maggiore di  /*54,*/ 3


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  minore di  /*55,*/ 1515 e  se l'argomento argomento_ave4 non  è  uguale a RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nil ripristino della variabile  SubClass_C3_restoreva_RV3 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_restoreva_rv3_restore)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T4 è scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C3_contatore_Co8 è  minore di  /*55,*/ 1515 e  se l'argomento argomento_ave4 non  è  uguale a RossoVerde""", [
                            DIBoolExpr("""LessThanImpl\nil contatore SubClass_C3_contatore_Co8 è  minore di  /*55,*/ 1515""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave4 non  è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde /*36,*/ o  se il timer SubClass_C3_timer_T6 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1, Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1532
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 


 } Verifica che   /*47,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 15
 /*104,*/ e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 sia  maggiore di  /*54,*/ 3


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde /*36,*/ o  se il timer SubClass_C3_timer_T6 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Almeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1, Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1532
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde /*36,*/ o  se il timer SubClass_C3_timer_T6 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde /*36,*/ o  se il timer SubClass_C3_timer_T6 non è scaduto /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde /*36,*/ o  se il timer SubClass_C3_timer_T6 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*62,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130 /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co2 non è  uguale a  /*53,*/ 130""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (130)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T6 non è scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1, Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1532
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è disattivo, Tutte le seguenti { 
 /*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1, Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*34,*/  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V6 non è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V6 non è  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T4 non è disattivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t4' è inattivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1, Verifica che   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde /*39,*/  /*37,*/ o  se la variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*109,*/  se il ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4 o  se l'argomento argomento_ave4 è  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\nil ripristino della variabile  SubClass_C3_restoreva_RV1 è  uguale a  /*53,*/ 4""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave4 è  uguale a RossoVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""LessThanImpl\nla variabile SubClass_C3_variabile_V5 è  minore di  /*55,*/ 1""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13
 /*104,*/ o  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124
 /*104,*/ e  che   l'argomento argomento_ave4 non  sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,50,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 124""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co2)  è uguale a  (124))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (124)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave4 non  sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((argomento_ave4)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave4)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*38,*/  il contatore SubClass_C3_contatore_Co2 sia  maggiore di  /*54,*/ 13""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p5)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1532
 /*104,*/ e  che  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True""", [
                            DIBoolExpr("""LessThanImpl\nche   /*50,51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  minore di  /*55,*/ 1532""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 15
 /*104,*/ e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 sia  maggiore di  /*54,*/ 3""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 15
 /*104,*/ e  che   l'argomento argomento_ave3 sia  diverso da avanzamentox""", [
                            DIBoolExpr("""LessThanImpl\nche   /*47,51,52,*/  /*,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 15""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave3 sia  diverso da avanzamentox""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave3)  è uguale a  (avanzamentox)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""GreaterThanImpl\nche  /*34,*/  il parametro SubClass_C3_parametro_P7 sia  maggiore di  /*54,*/ 3""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,*/  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,*/  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p5)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T4 sia attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m4_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db((db(not db(self.get_subclass_c3_restoreva_rv3_restore() == False, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c3_contatore_co8().get_valore() < 1515, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(argomento_ave4 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((((db(not db((db((db((db((db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 130, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(self.get_subclass_c3_controllo_c7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_controllo_c8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db((db(self.get_subclass_c3_restoreva_rv1_restore() == 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(argomento_ave4 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v5() < 1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db((db((db(not db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 124, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(not db(argomento_ave4 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_contatore_co2().get_valore() > 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(self.get_subclass_c3_contatore_co2().get_valore() < 1532, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0])) + (db((db((db(self.get_subclass_c3_contatore_co8().get_valore() < 15, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(argomento_ave3 == GlobalEnumeration.avanzamentox, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) and db(self.get_subclass_c3_parametro_p7() > 3, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db(not db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[1].subs[0]) or db(self.get_subclass_c3_timer_t4().isAttivato(), di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    @srf_value_macro("macroSubclass_c3_macrove_m9")
    def macroSubclass_c3_macrove_m9(self, argomento_ave1, argomento_ave10, argomento_ave4, argomento_ave5, di_ctx: DIVerifyMacro):
        """
        CNL corrispondente:
        
        { commento: {61,} commento: {38,}  se il contatore SubClass_C3_contatore_Co8 non è  diverso da  commento: {56,} 1121 commento: {35,} o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
         commento: {63,} commento: {34,}  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  commento: {36,} e  se il timer SubClass_C3_timer_T6 è disattivo commento: {35,} o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False , Solo una delle seguenti { 
         commento: {61,} commento: {37,}  se la variabile SubClass_C3_variabile_V5 non è  minore di  commento: {55,} 8,  commento: {45,}  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  commento: {105,} è  minore di  commento: {55,} 15504, commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  commento: {53,} 14321 commento: {34,} e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde commento: {38,} o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  commento: {56,} 13 commento: {34,} e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
         commento: {61,} commento: {110,}  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
         commento: {61,} commento: {38,}  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  commento: {56,} 1350,  commento: {44,}  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  commento: {105,} è  diverso da c270x, commento: {88,} quando  commento: {42,}    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex commento: {36,} o  se il timer SubClass_C3_timer_T4 è disattivo commento: {36,} o  se il timer SubClass_C3_timer_T4 è scaduto commento: {37,} e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 commento: {36,} e  se il timer SubClass_C3_timer_T4 non è attivo commento: {35,} o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
         commento: {62,}  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  commento: {40,}  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  commento: {55,} 13432, Almeno una delle seguenti { 
         commento: {63,} commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  commento: {105,} è  diverso da  True  commento: {35,} o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde commento: {39,}  o  se l'argomento argomento_ave1 è  diverso da RossoVerde commento: {39,}  e  se l'argomento argomento_ave1 è  uguale a RossoVerde commento: {39,}  commento: {38,} e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  commento: {55,} 1115, Solo una delle seguenti { 
         commento: {62,} commento: {34,}  se lo stato  non è  uguale a  commento: {53,}  state1  commento: {106,}, Almeno una delle seguenti { 
         commento: {61,} commento: {42,}  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex commento: {34,} e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde commento: {35,} e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde commento: {35,} e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
         commento: {63,} commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  commento: {105,} è  uguale a  commento: {53,}  state1  commento: {36,} e  se il timer SubClass_C3_timer_T4 non è attivo commento: {37,} o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  commento: {37,} o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
         commento: {61,} commento: {44,}  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  diverso da  False  commento: {36,} o  se il timer SubClass_C3_timer_T4 è disattivo commento: {37,} o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  commento: {36,} e  se il timer SubClass_C3_timer_T4 è attivo commento: {35,} o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde commento: {37,} e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
         commento: {41,}  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde commento: {39,} , Verifica che   commento: {47,50,52,}  commento: {,}  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
         commento: {104,} e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde commento: {,} 
        
        
         } Verifica che   commento: {51,}  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 133
        
        
         } Verifica che   commento: {47,52,}   l'argomento argomento_ave1 sia  diverso da RossoVerde commento: {,} 
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde
        
        
         } Verifica che   commento: {52,}   l'argomento argomento_ave1 sia  uguale a RossoVerde commento: {,} 
         commento: {104,} e  che   l'argomento argomento_ave10 non  sia  uguale a  False  commento: {39,} 
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 
        
        
         } Verifica che   commento: {47,49,50,51,}  commento: {34,}  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T4 sia scaduto
         commento: {104,} o  che  commento: {,}  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  diverso da  commento: {56,} 11
        
        
         } Verifica che   commento: {47,48,}  commento: {34,}  il parametro SubClass_C3_parametro_P7 non sia  diverso da  commento: {56,} 9
         commento: {104,} o  che  commento: {,}  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
         commento: {104,} e  che  commento: {34,}  il parametro SubClass_C3_parametro_P7 non sia  minore di  commento: {55,} 4
        
        
         } Verifica che   commento: {50,51,}  commento: {,}  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  commento: {56,} 12
        
        
         } Verifica che   commento: {48,49,50,}  commento: {,}  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
         commento: {104,} e  che  commento: {37,}  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
         commento: {104,} o  che  commento: {,}  il timer SubClass_C3_timer_T6 sia scaduto
        
        
         } Verifica che   commento: {50,}  commento: {,}  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 
        
        
         } Verifica che   commento: {48,49,51,52,}  commento: {,}  il timer SubClass_C3_timer_T6 non sia scaduto
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  diverso da  commento: {56,} 11
         commento: {104,} o  che  commento: {38,}  il contatore SubClass_C3_contatore_Co8 sia  minore di  commento: {55,} 155
         commento: {104,} e  che  commento: {36,}  il timer SubClass_C3_timer_T6 non sia scaduto
         commento: {104,} o  che   l'argomento argomento_ave10 non  sia  uguale a  True  commento: {,} 
         commento: {104,} e  che  commento: {,}  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde
        
        
         } Verifica che   commento: {50,51,52,}  commento: {,}  la variabile SubClass_C3_variabile_V6 sia  uguale a  True 
         commento: {104,} e  che   l'argomento argomento_ave1 sia  uguale a RossoVerde commento: {,} 
         commento: {104,} e  che  commento: {,}  il contatore SubClass_C3_contatore_Co2 sia  uguale a  commento: {53,} 1504
        
        
        }
        """
        def populate_macroSubclass_c3_macrove_m9_SrfMacroDefInfo(macroDebInfo: DIVerifyMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co8 non è  diverso da  /*56,*/ 1121 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T6 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False , Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 155
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde


 } Verifica che   /*50,51,52,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  uguale a  /*53,*/ 1504""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co8 non è  diverso da  /*56,*/ 1121 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T6 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False , Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 155
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co8 non è  diverso da  /*56,*/ 1121 /*35,*/ o  se il controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co8 non è  diverso da  /*56,*/ 1121""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co8)  è uguale a  (1121))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co8)  è uguale a  (1121)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C7 è  uguale a RossoGialloVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*34,*/  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T6 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False , Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 


 } Verifica che   /*48,49,51,52,*/  /*,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 155
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*34,*/  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T6 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False , Solo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*34,*/  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T6 è disattivo /*35,*/ o  se il controllo SubClass_C3_controllo_C9 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*34,*/  se il parametro SubClass_C3_parametro_P8 è  uguale a  True  /*36,*/ e  se il timer SubClass_C3_timer_T6 è disattivo""", [
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C3_parametro_P8 è  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T6 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil controllo SubClass_C3_controllo_C9 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  diverso da  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True , Tutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde /*38,*/ o  se il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321 /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*37,*/  se la variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8,  /*45,*/  se  MainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V5 non è  minore di  /*55,*/ 8""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_variabile_v5)  è minore di  (8)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_contatore_Co5 del campo  MainClass_C1 di SubClass_C3_lista_L1 esiste e  /*105,*/ è  minore di  /*55,*/ 15504, /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_contatore_co1 del campo mainclass_c1 della lista subclass_c3_lista_l1)  è uguale a  (14321)) allora ((mainclass_c1_contatore_co5 del campo mainclass_c1 della lista subclass_c3_lista_l1)  è minore di  (15504))""", [
                            DIBoolExpr("""EqualImpl\n/*45,*/    MainClass_C1_contatore_Co1 del campo  MainClass_C1     è  uguale a  /*53,*/ 14321""", [
                            ]),#0
                            DIBoolExpr("""LessThanImpl\n(mainclass_c1_contatore_co5 del campo mainclass_c1 della lista subclass_c3_lista_l1)  è minore di  (15504)""", [
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C3_parametro_P5 è  uguale a RossoVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13 /*34,*/ e  se il parametro SubClass_C3_parametro_P8 è  uguale a  True""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co8 è  diverso da  /*56,*/ 13""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co8)  è uguale a  (13)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nil parametro SubClass_C3_parametro_P8 è  uguale a  True""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 } Verifica che   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*110,*/  se il ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo, Tutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 }""", [
                            DIBoolExpr("""Predicato Oggetto\nil ripristino del timer  SubClass_C3_restoreTI_TI3 è attivo""", [
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 } Verifica che   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*36,*/ o  se il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*38,*/  se il contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350,  /*44,*/  se  MainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co2 non è  diverso da  /*56,*/ 1350""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co2)  è uguale a  (1350))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (1350)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V8 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da c270x, /*88,*/ quando  /*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c3_lista_l5)  è uguale a  (gialloxverdex)) allora (negazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l5)  è uguale a  (c270x)))""", [
                            DIBoolExpr("""EqualImpl\n/*42,*/    MainClass_C1_controllo_C7 del campo  MainClass_C1     è  uguale a GialloxVerdex""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l5)  è uguale a  (c270x))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v8 del campo mainclass_c1 della lista subclass_c3_lista_l5)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120 /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse il timer SubClass_C3_timer_T4 è scaduto /*37,*/ e  se la variabile SubClass_C3_variabile_V2 non è  uguale a c120""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T4 è scaduto""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V2 non è  uguale a c120""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v2)  è uguale a  (c120)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T4 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 } Verifica che   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432, Almeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*62,*/  se la macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False  /*40,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432""", [
                            DIBoolExpr("""Operatore Logico Not\nla macro  SubClass_C3_macrova_M3 ( con argomento_a2   uguale a RossoGialloaVerdea ,argomento_a8   uguale a RossoVerde ,argomento_a6   uguale a RossoVerde  e argomento_a9   uguale a c180 )  non  è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m3')  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(chiamata alla macro valorizzata 'macroSubclass_c3_macrova_m3')  è uguale a  (False)""", [
                            DIValueMacro("""MacroCallValorizzataImpl\nchiamata alla macro valorizzata 'macroSubclass_c3_macrova_m3'"""),#0
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 13432""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co9)  è minore di  (13432)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 } Verifica che   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115, Solo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  o  se l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde o  se l'argomento argomento_ave1 è  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True  /*35,*/ o  se il controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c3_lista_l5)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c3_lista_l5)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C5 è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c5)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 è  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde /*39,*/  /*38,*/ e  se il contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nse l'argomento argomento_ave1 è  diverso da RossoVerde /*39,*/  e  se l'argomento argomento_ave1 è  uguale a RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nl'argomento argomento_ave1 è  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave1 è  uguale a RossoVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil contatore SubClass_C3_contatore_Co9 non è  minore di  /*55,*/ 1115""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_contatore_co9)  è minore di  (1115)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 } Verifica che   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*62,*/ /*34,*/  se lo stato  non è  uguale a  /*53,*/  state1  /*106,*/, Almeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 }""", [
                            DIBoolExpr("""Operatore Logico Not\nlo stato  non è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'self')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nAlmeno una delle seguenti { 
 /*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 } Verifica che   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False  /*39,*/ 


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde, Tutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 }""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde /*35,*/ e  se il controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*61,*/ /*42,*/  se  MainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex /*34,*/ e  se il parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde""", [
                            DIBoolExpr("""Predicato ForAll\nMainClass_C1_controllo_C7 del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a GialloxVerdex""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_controllo_c7 del campo mainclass_c1 della lista subclass_c3_lista_l1)  è uguale a  (gialloxverdex)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil parametro SubClass_C3_parametro_P5 è  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C7 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C8 non è  uguale a RossoGialloVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c8)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nTutte le seguenti { 
 /*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 } Verifica che   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True , Solo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False  /*37,*/ o  se la variabile SubClass_C3_variabile_V6 non è  diverso da  True""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo /*37,*/ o  se la variabile SubClass_C3_variabile_V6 è  uguale a  False""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n/*63,*/ /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1  /*36,*/ e  se il timer SubClass_C3_timer_T4 non è attivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nlo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 esiste e  /*105,*/ è  uguale a  /*53,*/  state1""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nil timer SubClass_C3_timer_T4 non è attivo""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t4' è attivo""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nla variabile SubClass_C3_variabile_V6 è  uguale a  False""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V6 non è  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (XOR)\nSolo una delle seguenti { 
 /*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 } Verifica che   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133


 }""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False , Tutte le seguenti { 
 /*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde /*,*/ 


 }""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo /*35,*/ o  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo /*37,*/ o  se la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*61,*/ /*44,*/  se  MainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False  /*36,*/ o  se il timer SubClass_C3_timer_T4 è disattivo""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_variabile_V6 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (False))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_variabile_v6 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T4 è disattivo""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse la variabile SubClass_C3_variabile_V8 non è  uguale a  False  /*36,*/ e  se il timer SubClass_C3_timer_T4 è attivo""", [
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 non è  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nil timer SubClass_C3_timer_T4 è attivo""", [
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nse il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde /*37,*/ e  se la variabile SubClass_C3_variabile_V8 è  diverso da  False""", [
                            DIBoolExpr("""Operatore Logico Not\nil controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nla variabile SubClass_C3_variabile_V8 è  diverso da  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""ImpliesLogicOpImpl\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde /*39,*/ , Verifica che   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*41,*/  se MainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x o  se l'argomento argomento_ave5 è  uguale a RossoVerde""", [
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nMainClass_C1_parametro_P3 del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  uguale a c270x""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_parametro_p3 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (c270x)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""EqualImpl\nl'argomento argomento_ave5 è  uguale a RossoVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde
 /*104,*/ e  che   l'argomento argomento_ave5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\nche   /*47,50,52,*/  /*,*/  la variabile SubClass_C3_variabile_V8 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave5 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*51,*/  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 133""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co2)  è uguale a  (133))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (133)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde /*,*/ 
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,52,*/   l'argomento argomento_ave1 sia  diverso da RossoVerde""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave1)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P5 non sia  diverso da RossoVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p5)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che   l'argomento argomento_ave10 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\nche   /*52,*/   l'argomento argomento_ave1 sia  uguale a RossoVerde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V8 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v8)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto
 /*104,*/ o  che  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,49,50,51,*/  /*34,*/  il parametro SubClass_C3_parametro_P8 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p8)  è uguale a  (False)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T4 sia scaduto""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\nche  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  False""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9
 /*104,*/ o  che  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*47,48,*/  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  diverso da  /*56,*/ 9""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p7)  è uguale a  (9))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p7)  è uguale a  (9)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde
 /*104,*/ e  che  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C5 non sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c5)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c5)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*34,*/  il parametro SubClass_C3_parametro_P7 non sia  minore di  /*55,*/ 4""", [
                            DIBoolExpr("""LessThanImpl\n(subclass_c3_parametro_p7)  è minore di  (4)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""EqualImpl\nche   /*50,51,*/  /*,*/  la variabile SubClass_C3_variabile_V7 sia  uguale a RossoGialloVerde""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C3_contatore_Co2 non sia  diverso da  /*56,*/ 12""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_contatore_co2)  è uguale a  (12))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (12)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True 
 /*104,*/ o  che  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False 
 /*104,*/ e  che  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 non sia  diverso da  True""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_variabile_v6)  è uguale a  (True))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C9 non sia  uguale a  False""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c9)  è uguale a  (False)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*37,*/  la variabile SubClass_C3_variabile_V6 non sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Predicato Oggetto\nche  /*,*/  il timer SubClass_C3_timer_T6 sia scaduto""", [
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche   /*50,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  diverso da  True""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_variabile_v6)  è uguale a  (True)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,52,*/  /*,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 155
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ o  che   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\nche   /*48,49,51,52,*/  /*,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11
 /*104,*/ o  che  /*38,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 155
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T6 non sia scaduto""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*48,49,51,52,*/  /*,*/  il timer SubClass_C3_timer_T6 non sia scaduto
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""Operatore Logico Not\nche   /*48,49,51,52,*/  /*,*/  il timer SubClass_C3_timer_T6 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  diverso da  /*56,*/ 11""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_contatore_co2)  è uguale a  (11)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche  /*38,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 155
 /*104,*/ e  che  /*36,*/  il timer SubClass_C3_timer_T6 non sia scaduto""", [
                            DIBoolExpr("""LessThanImpl\nche  /*38,*/  il contatore SubClass_C3_contatore_Co8 sia  minore di  /*55,*/ 155""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*36,*/  il timer SubClass_C3_timer_T6 non sia scaduto""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_timer_t6' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   l'argomento argomento_ave10 non  sia  uguale a  True  /*,*/ 
 /*104,*/ e  che  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nche   l'argomento argomento_ave10 non  sia  uguale a  True""", [
                            DIBoolExpr("""EqualImpl\n(argomento_ave10)  è uguale a  (True)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nche  /*,*/  il controllo SubClass_C3_controllo_C7 non sia  diverso da RossoGialloVerde""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,52,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  uguale a RossoVerde /*,*/ 
 /*104,*/ e  che  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  uguale a  /*53,*/ 1504""", [
                            DIBoolExpr("""NAryLogicOP (AND)\nche   /*50,51,52,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  True 
 /*104,*/ e  che   l'argomento argomento_ave1 sia  uguale a RossoVerde""", [
                            DIBoolExpr("""EqualImpl\nche   /*50,51,52,*/  /*,*/  la variabile SubClass_C3_variabile_V6 sia  uguale a  True""", [
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche   l'argomento argomento_ave1 sia  uguale a RossoVerde""", [
                            ]),#1
                            ]),#0
                            DIBoolExpr("""EqualImpl\nche  /*,*/  il contatore SubClass_C3_contatore_Co2 sia  uguale a  /*53,*/ 1504""", [
                            ]),#1
                            ]),#1
                            ]),#0
                ])

        populate_macroSubclass_c3_macrove_m9_SrfMacroDefInfo(di_ctx)
        return db((db(not db((db(not db(not db(self.get_subclass_c3_contatore_co8().get_valore() == 1121, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db((db(not db((db((db(self.get_subclass_c3_parametro_p8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_timer_t6().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(not db(self.get_subclass_c3_variabile_v5() < 8, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_contatore_co5().get_valore() < 15504, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l1()) if db(it.get_mainclass_c1().get_mainclass_c1_contatore_co1().get_valore() == 14321, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_contatore_co8().get_valore() == 13, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_parametro_p8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_restoreti_ti3_restore().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db((db(not db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 1350, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v8() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l5()) if db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db((db(self.get_subclass_c3_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v2() == GlobalEnumeration.c120, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db(not db(not db(db(self.macroSubclass_c3_macrova_m3(GlobalEnumeration.rossogialloaverdea,GlobalEnumeration.rossoverde,GlobalEnumeration.rossoverde,GlobalEnumeration.c180, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co9().get_valore() < 13432, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l5())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_controllo_c5() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(not db(argomento_ave1 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db((db(not db(argomento_ave1 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]) and db(argomento_ave1 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_contatore_co9().get_valore() < 1115, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db(not db(self.get_fsmState() == Stazione.LdS.Logica.Enumeratives.SubClass_C3.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(all(db(it.get_mainclass_c1().get_mainclass_c1_controllo_c7() == GlobalEnumeration.gialloxverdex, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l1())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c8() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((db(not db((db((db((db(all_notempty(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l5())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db(not db(not db(self.get_subclass_c3_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db((((db(not db((db((db((db(all_notempty(db(not db(it.get_mainclass_c1().get_mainclass_c1_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t4().isDisattivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_timer_t4().isAttivato(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0]) or db((db(not db(not db(self.get_subclass_c3_controllo_c7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_variabile_v8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(not db((db(all_notempty(db(it.get_mainclass_c1().get_mainclass_c1_parametro_p3() == GlobalEnumeration.c270x, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l6())), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[0]) or db(argomento_ave5 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(argomento_ave5 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 133, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(not db(argomento_ave1 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db(argomento_ave1 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(argomento_ave10 == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c3_variabile_v8() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) or db((db((db(not db(self.get_subclass_c3_parametro_p8() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) or db(self.get_subclass_c3_timer_t4().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(self.get_subclass_c3_variabile_v6() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(not db(not db(self.get_subclass_c3_parametro_p7() == 9, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(not db(self.get_subclass_c3_controllo_c5() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(self.get_subclass_c3_parametro_p7() < 4, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db(self.get_subclass_c3_variabile_v7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 12, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[0]) and db((db((db((db(not db(not db(self.get_subclass_c3_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_controllo_c9() == False, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[0]) and db(not db(self.get_subclass_c3_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]) or db(self.get_subclass_c3_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[0])) + (db(not db(self.get_subclass_c3_variabile_v6() == True, di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1].subs[1]))) == 1), di_ctx.subs[0].subs[0].subs[1].subs[0].subs[1]), di_ctx.subs[0].subs[0].subs[1].subs[0]) and db((db((db((db(not db(self.get_subclass_c3_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0]) and db(not db(self.get_subclass_c3_contatore_co2().get_valore() == 11, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[0]) or db((db(self.get_subclass_c3_contatore_co8().get_valore() < 155, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0]) and db(not db(self.get_subclass_c3_timer_t6().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[0]) or db((db(not db(argomento_ave10 == True, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[0]) and db(not db(not db(self.get_subclass_c3_controllo_c7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[1]), di_ctx.subs[0].subs[0]) and db((db((db(self.get_subclass_c3_variabile_v6() == True, di_ctx.subs[0].subs[1].subs[0].subs[0]) and db(argomento_ave1 == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[1].subs[0].subs[1])), di_ctx.subs[0].subs[1].subs[0]) and db(self.get_subclass_c3_contatore_co2().get_valore() == 1504, di_ctx.subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[1])), di_ctx.subs[0])
    
    # value macros
    @srf_value_macro("macroSubclass_c3_macrova_m1")
    def macroSubclass_c3_macrova_m1(self, argomento_a1, argomento_a10, argomento_a5, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[} commento: {35,}  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {111,}   lo stato del campo  MainClass_C1     è  uguale a  commento: {53,}  state1  commento: {38,} e  se il contatore SubClass_C3_contatore_Co8 è  maggiore di  commento: {54,} 12,  commento: {111,}  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  commento: {105,} è  diverso da  commento: {56,}  state1 , commento: {88,} quando  commento: {45,}    MainClass_C1_contatore_Co2 del campo  MainClass_C1     è  diverso da  commento: {56,} 113 commento: {34,} o  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde commento: {111,} e  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a  commento: {53,}  state1  commento: {110,} o  se il ripristino del timer  SubClass_C3_restoreTI_TI4 non è scaduto , assegna alla macro il valore RossoGialloVerde
        
         commento: {46,} assegna alla macro il valore RossoGialloVerde commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m1_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                            DIStatement("""ITStatement\n/*[*/ /*35,*/  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*38,*/ e  se il contatore SubClass_C3_contatore_Co8 è  maggiore di  /*54,*/ 12,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co2 del campo  MainClass_C1     è  diverso da  /*56,*/ 113 /*34,*/ o  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a  /*53,*/  state1  /*110,*/ o  se il ripristino del timer  SubClass_C3_restoreTI_TI4 non è scaduto , assegna alla macro il valore RossoGialloVerde""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n/*[*/ /*35,*/  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*38,*/ e  se il contatore SubClass_C3_contatore_Co8 è  maggiore di  /*54,*/ 12,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co2 del campo  MainClass_C1     è  diverso da  /*56,*/ 113 /*34,*/ o  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a  /*53,*/  state1  /*110,*/ o  se il ripristino del timer  SubClass_C3_restoreTI_TI4 non è scaduto""", [
                            DIBoolExpr("""NAryLogicOP (OR)\n( ( ( negazione di (negazione di ((subclass_c3_controllo_c7)  è uguale a  (rossogialloverde))) )  e  ( per ognuna delle seguenti {se ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)))} ) )  e  
( ( (subclass_c3_contatore_co8)  è maggiore di  (12) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (113))) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1)))} ) ) )  o  
( ( negazione di ((subclass_c3_parametro_p5)  è uguale a  (rossoverde)) )  e  
( per ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l1')  è uguale a  (state1))} ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( ( negazione di (negazione di ((subclass_c3_controllo_c7)  è uguale a  (rossogialloverde))) )  e  ( per ognuna delle seguenti {se ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)))} ) )  e  
( ( (subclass_c3_contatore_co8)  è maggiore di  (12) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (113))) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1)))} ) )""", [
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di (negazione di ((subclass_c3_controllo_c7)  è uguale a  (rossogialloverde))) )  e  ( per ognuna delle seguenti {se ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (negazione di ((subclass_c3_controllo_c7)  è uguale a  (rossogialloverde)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_controllo_c7)  è uguale a  (rossogialloverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_controllo_c7)  è uguale a  (rossogialloverde)""", [
                            ]),#0
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {se ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)""", [
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l5')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( (subclass_c3_contatore_co8)  è maggiore di  (12) )  e  ( per ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (113))) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1)))} )""", [
                            DIBoolExpr("""GreaterThanImpl\n(subclass_c3_contatore_co8)  è maggiore di  (12)""", [
                            ]),#0
                            DIBoolExpr("""ForAllPredicateNotEmptyImpl\nper ognuna delle seguenti con lista non vuota {se (negazione di ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (113))) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1)))}""", [
                            DIBoolExpr("""ImpliesLogicOpImpl\nse (negazione di ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (113))) allora (negazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1)))""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (113))""", [
                            DIBoolExpr("""EqualImpl\n(mainclass_c1_contatore_co2 del campo mainclass_c1 della lista subclass_c3_lista_l6)  è uguale a  (113)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1))""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l6')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""NAryLogicOP (AND)\n( negazione di ((subclass_c3_parametro_p5)  è uguale a  (rossoverde)) )  e  
( per ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l1')  è uguale a  (state1))} )""", [
                            DIBoolExpr("""Operatore Logico Not\nnegazione di ((subclass_c3_parametro_p5)  è uguale a  (rossoverde))""", [
                            DIBoolExpr("""EqualImpl\n(subclass_c3_parametro_p5)  è uguale a  (rossoverde)""", [
                            ]),#0
                            ]),#0
                            DIBoolExpr("""Predicato ForAll\nper ognuna delle seguenti {((lo stato di 'mainclass_c1 della lista subclass_c3_lista_l1')  è uguale a  (state1))}""", [
                            DIBoolExpr("""EqualImpl\n(lo stato di 'mainclass_c1 della lista subclass_c3_lista_l1')  è uguale a  (state1)""", [
                            ]),#0
                            ]),#1
                            ]),#1
                            ]),#0
                            DIBoolExpr("""Operatore Logico Not\nnegazione di (il timer 'subclass_c3_restoreti_ti4_restore' è scaduto)""", [
                            DIBoolExpr("""Predicato Oggetto\nil timer 'subclass_c3_restoreti_ti4_restore' è scaduto""", [
                            ]),#0
                            ]),#1
                            ]),#0
                            ]),#0
                ])

        populate_macroSubclass_c3_macrova_m1_SrfMacroDefInfo(di_ctx)
        #  /*[*/ /*35,*/  se il controllo SubClass_C3_controllo_C7 non è  diverso da RossoGialloVerde,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L5 è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*111,*/   lo stato del campo  MainClass_C1     è  uguale a  /*53,*/  state1  /*38,*/ e  se il contatore SubClass_C3_contatore_Co8 è  maggiore di  /*54,*/ 12,  /*111,*/  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L6 esiste e  /*105,*/ è  diverso da  /*56,*/  state1 , /*88,*/ quando  /*45,*/    MainClass_C1_contatore_Co2 del campo  MainClass_C1     è  diverso da  /*56,*/ 113 /*34,*/ o  se il parametro SubClass_C3_parametro_P5 non è  uguale a RossoVerde /*111,*/ e  se lo stato del campo  MainClass_C1 di SubClass_C3_lista_L1 è  uguale a  /*53,*/  state1  /*110,*/ o  se il ripristino del timer  SubClass_C3_restoreTI_TI4 non è scaduto , assegna alla macro il valore RossoGialloVerde
        if db((db((db((db((db(not db(not db(self.get_subclass_c3_controllo_c7() == GlobalEnumeration.rossogialloverde, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[0]) and db(all(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l5()) if db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[0]) and db((db(self.get_subclass_c3_contatore_co8().get_valore() > 12, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[0]) and db(all_notempty(db(not db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[1].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[1][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l6()) if db(not db(it.get_mainclass_c1().get_mainclass_c1_contatore_co2().get_valore() == 113, di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0].subs[0][idx]), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1].subs[0].subs[0][idx])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[0]) or db((db(not db(self.get_subclass_c3_parametro_p5() == GlobalEnumeration.rossoverde, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0].subs[0]), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[0]) and db(all(db(it.get_mainclass_c1().get_fsmState() == Stazione.LdS.Logica.Enumeratives.MainClass_C1.Stateenumerator.state1, di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1].subs[0][idx]) for idx, it in enumerate(self.get_subclass_c3_lista_l1())), di_ctx.subs[0].subs[0].subs[0].subs[1].subs[1])), di_ctx.subs[0].subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0].subs[0]) or db(not db(self.get_subclass_c3_restoreti_ti4_restore().isScaduto(), di_ctx.subs[0].subs[0].subs[1].subs[0]), di_ctx.subs[0].subs[0].subs[1])), di_ctx.subs[0].subs[0]):
            return GlobalEnumeration.rossogialloverde
        #  /*46,*/ assegna alla macro il valore RossoGialloVerde
        return GlobalEnumeration.rossogialloverde
    
    @srf_value_macro("macroSubclass_c3_macrova_m10")
    def macroSubclass_c3_macrova_m10(self, argomento_a3, argomento_a7, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore avanzamentox commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m10_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c3_macrova_m10_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore avanzamentox
        return GlobalEnumeration.avanzamentox
    
    @srf_value_macro("macroSubclass_c3_macrova_m3")
    def macroSubclass_c3_macrova_m3(self, argomento_a2, argomento_a6, argomento_a8, argomento_a9, di_ctx: DIValueMacro):
        """
        CNL corrispondente:
        
        { commento: {[}
         commento: {46,} assegna alla macro il valore  False  commento: {],}
        }
        """
        def populate_macroSubclass_c3_macrova_m3_SrfMacroDefInfo(macroDebInfo: DIValueMacro):
            #if macroDebInfo is not yet populated
            if not macroDebInfo.is_initialized() :
                macroDebInfo.initialize([
                ])

        populate_macroSubclass_c3_macrova_m3_SrfMacroDefInfo(di_ctx)
        
        #  /*[*/
        #   /*46,*/ assegna alla macro il valore  False
        return False
    
    # for each manual command, the corresponding method is created
    def eventSubclass_c3_command_comm10DaSender4471a7d8(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c3_command_comm10DaSender4471a7d8')
    
    def eventSubclass_c3_command_comm3(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c3_command_comm3')
    
    def eventSubclass_c3_command_comm7(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c3_command_comm7')
    
    def eventSubclass_c3_command_comm8DaSender7a3d0e35(self, notifying_process):
        notifying_process.response_notify_man_cmd(self, 'eventSubclass_c3_command_comm8DaSender7a3d0e35')
    
    # for each automatic command, the corresponding method is created

    def update_precedente(self):
        # update the variables with previous value
        self.set_subclass_c3_previousco_c1_prev(self.get_subclass_c3_previousco_c1())
        self.set_subclass_c3_previousco_c10_prev(self.get_subclass_c3_previousco_c10())
        self.set_subclass_c3_previousco_c2_prev(self.get_subclass_c3_previousco_c2())
        self.set_subclass_c3_previousco_c4_prev(self.get_subclass_c3_previousco_c4())
        self.set_subclass_c3_previousco_c6_prev(self.get_subclass_c3_previousco_c6())
        self.set_subclass_c3_previousva_pv1_prev(self.get_subclass_c3_previousva_pv1())
        self.set_subclass_c3_previousva_pv2_prev(self.get_subclass_c3_previousva_pv2())
        self.set_subclass_c3_previousva_pv3_prev(self.get_subclass_c3_previousva_pv3())
        self.set_subclass_c3_previousva_pv4_prev(self.get_subclass_c3_previousva_pv4())
        self.set_subclass_c3_previousva_pv5_prev(self.get_subclass_c3_previousva_pv5())

class SubClass_C3_RecordHeaderR2(ParamRecord):
    # ProcessImpl is the class that is extended.
    # ProcessImpl contains the get/set methods for the current state variable and
    # the methods that generate the responses

    # method called by the configurator before the use of the scheduler
    # it creates the references of the processes needed
    def init_configuration(self, mainclass_c1, recordfiled11, recordfiled7):
        self.set_mainclass_c1(mainclass_c1)
        self.set_recordfiled11(recordfiled11)
        self.set_recordfiled7(recordfiled7)

    # setters for the fields of record
    def set_mainclass_c1(self, mainclass_c1):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"), mainclass_c1)

    def set_recordfiled11(self, recordfiled11):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"), recordfiled11)

    def set_recordfiled7(self, recordfiled7):
        self.memory.set_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"), recordfiled7)


    # getters for the fields of record
    def get_mainclass_c1(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "mainclass_c1"))

    def get_recordfiled11(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled11"))

    def get_recordfiled7(self):
        return self.memory.get_var(self.station_name,self.record_fq_name,self.instance_name,"{}.{}".format(self.param_name, "recordfiled7"))



