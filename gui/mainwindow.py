"""Main application window."""

# pylint: disable=import-error
# pylint: disable=no-name-in-module

import serial
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from forms.main_window import Ui_MainWindow
from logic.constants import Constants
from logic.encounters import RSE, FRLG
from logic.reusable import message_dialog, create_ard_string
from logic.device import MCSerial, list_ports
from timings import rse, frlg


class MainWindow(QMainWindow):
    """Main application window logic where all the functionality is
    placed into a single form. Plans to add additional quick tool forms
    will eventually be implemented. For now this is the primary window"""
    def __init__(self):
        super().__init__()
        self.cons = Constants()
        self.rse_enc = RSE()
        self.frlg_enc = FRLG()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startup()

        self.ui.chk_rse_painting.checkStateChanged.connect(self.enable_painting_timer)
        self.ui.btn_refreshPorts.clicked.connect(self.refresh_ports)
        self.ui.btn_clearDevices.clicked.connect(self.remove_all_devices)
        self.ui.btn_addDevice.clicked.connect(self.add_device)

        self.ui.cmb_frlg_category.currentIndexChanged.connect(self.populate_encounters)
        self.ui.cmb_frlg_category.currentIndexChanged.connect(self.update_requirements_frlg)

        self.ui.cmb_rse_category.currentIndexChanged.connect(self.populate_encounters)
        self.ui.cmb_rse_category.currentIndexChanged.connect(self.update_requirements_rse)

        self.ui.btn_frlg_startSequence.clicked.connect(self.send_to_device_frlg)
        self.ui.btn_rse_startSequence.clicked.connect(self.send_to_device_rse)

    def startup(self) -> None:
        """Tasks that are ran at the startup to populate values"""
        self.populate_defaults()
        self.set_window_defaults()
        self.populate_categories()
        self.populate_encounters()
        self.populate_button_select()
        self.update_requirements_frlg()
        self.update_requirements_rse()

    def set_window_defaults(self) -> None:
        """Sets window defaults to the standard arduino baud rates"""
        self.ui.cmb_buadRate.setCurrentText("9600")
        self.ui.txt_deviceNameEntry.setText("Arduino")

    def populate_defaults(self) -> None:
        """Populates baud rate selections and refreshes port list"""
        self.ui.cmb_buadRate.addItems(self.cons.rate_strings())
        self.refresh_ports()

    def populate_categories(self) -> None:
        """Populates category strings in dropdown selections"""
        self.ui.cmb_rse_category.addItems(self.cons.category_rse)
        self.ui.cmb_frlg_category.addItems(self.cons.category_frlg)

    def populate_button_select(self) -> None:
        """Populates button selection for FRLG sequences"""
        self.ui.cmb_frlg_buttonSel.addItems(list(self.cons.button_map))

    def populate_encounters(self) -> None:
        """Populates encounter strings based on selected category"""
        self.ui.cmb_frlg_enctounterSel.clear()
        self.ui.cmb_rse_encounter.clear()

        enc = self.frlg_enc.get_category_mons(self.ui.cmb_frlg_category.currentText())
        self.ui.cmb_frlg_enctounterSel.addItems(enc)

        enc2 = self.rse_enc.get_category_mons(self.ui.cmb_rse_category.currentText())
        self.ui.cmb_rse_encounter.addItems(enc2)

    def update_requirements_frlg(self) -> None:
        """Clears and appends requirements for FRLG sequences"""
        self.ui.txb_frlg_preReqs.clear()
        selection = self.ui.cmb_frlg_category.currentText()
        self.ui.txb_frlg_preReqs.append(self.frlg_enc.category_reqs[selection])

    def update_requirements_rse(self) -> None:
        """Clears and appends requirements for RSE sequences"""
        self.ui.txb_rse_preReqs.clear()
        selection = self.ui.cmb_rse_category.currentText()
        self.ui.txb_rse_preReqs.append(self.rse_enc.category_reqs[selection])

    def refresh_ports(self) -> None:
        """Clears port string list then runs serial tool to get a fresh list"""
        self.ui.cmb_Port.clear()
        self.ui.cmb_Port.addItems(list_ports())

    def add_device(self) -> None:
        """Adds serial device to device table from selected values"""
        dev_name = self.ui.txt_deviceNameEntry.text()
        baud_rate = self.ui.cmb_buadRate.currentText()
        port = self.ui.cmb_Port.currentText()

        row = self.ui.tbl_deviceTable.rowCount()
        self.ui.tbl_deviceTable.insertRow(row)

        self.ui.tbl_deviceTable.setItem(row, 0, QTableWidgetItem(dev_name))
        self.ui.tbl_deviceTable.setItem(row, 1, QTableWidgetItem(baud_rate))
        self.ui.tbl_deviceTable.setItem(row, 2, QTableWidgetItem(port))

        self.ui.cmb_frlg_deviceSel.addItem(str(row + 1))
        self.ui.cmb_rse_deviceSel.addItem(str(row + 1))

    def remove_all_devices(self) -> None:
        """Clears the device list of all its items"""
        self.ui.cmb_rse_deviceSel.clear()
        self.ui.cmb_frlg_deviceSel.clear()
        while self.ui.tbl_deviceTable.rowCount() > 0:
            self.ui.tbl_deviceTable.removeRow(0)

    def enable_painting_timer(self) -> None:
        """Toggles the painting numerical box when painting check status is changed"""
        self.ui.spb_rse_paintingTime.setEnabled(self.ui.chk_rse_painting.isChecked())

    def get_selection_list(self, game: int) -> list[int]:
        """Pulls all the data from the user inputs and crafts the proper output list
        based on the active game."""
        select = 0
        intro_timer = 0
        total_timer = 0
        mode = 0
        button = 0
        tv_time = 0
        if game == 0:
            select = int(self.ui.chk_frlg_select.isChecked())
            intro_timer = self.ui.spb_frlg_introTimer.value()
            total_timer = self.ui.spb_frlg_totalTime.value()
            button = self.cons.button_map[self.ui.cmb_frlg_buttonSel.currentText()]
            tv_time = self.ui.spb_frlg_tvFrames.value()
            cat = self.ui.cmb_frlg_category.currentText()
            mon = self.ui.cmb_frlg_enctounterSel.currentText()
            mode = self.frlg_enc.get_encounter_value(cat, mon)

        elif game == 1:
            select = int(self.ui.chk_rse_BattleRecord.isChecked())
            total_timer = self.ui.spb_rse_targetAdvance.value()
            tv_time = self.ui.spb_rse_paintingTime.value()
            cat = self.ui.cmb_rse_category.currentText()
            mon = self.ui.cmb_rse_encounter.currentText()
            mode = self.rse_enc.get_encounter_value(cat, mon)
            button = 1 if self.ui.chk_rse_liveBattery.isChecked() else 0

        return [game, select, intro_timer, total_timer, mode, button, tv_time]

    def get_device_data(self, index: int) -> tuple:
        """Gets the selected device data from the specified index.
        The index is based on the device table"""
        if index < 0:
            return None, None

        rate = int(self.ui.tbl_deviceTable.item(index, 1).text())
        port = self.ui.tbl_deviceTable.item(index, 2).text()
        return rate, port

    def send_to_device_frlg(self) -> None:
        """Checks the input values to make sure they meet the timing restrictions
        Then formats the output list into the string that is interpreted by the
        Arduino script. FRLG function only"""
        dev = self.get_device_data(
            int(self.ui.cmb_frlg_deviceSel.currentIndex())
        )
        out_str = self.get_selection_list(0)
        intro = self.ui.spb_frlg_introTimer.value()
        if dev == (None, None):
            message_dialog(
                "No device added! Please make sure you have added and selected the device",
                "Error"
            )
        elif intro > frlg.SEED_UPPER_BOUND or intro < frlg.SEED_LOWER_BOUND:
            message_dialog(
                "Your intro timer is beyond the upper and lower bounds of possible targets\n"
                "Please enter a valid intro timer",
                "Timing Error"
            )
        else:
            total = out_str[3]
            tv = out_str[6]
            enc = frlg.get_seq(self.ui.cmb_frlg_enctounterSel.currentText())
            enc_sum = frlg.sum_timer_seq(enc, tv)

            if not frlg.check_time_difference(enc_sum, intro, total):
                message_dialog(
                    "Your total timer is shorter than the expected value.\n"
                    "Please enter a valid timer",
                    "Timing Error"
                )
            else:
                self.show_enc_string_frlg()
                try:
                    ser = MCSerial(port=dev[1], rate=dev[0])
                    ser.write_to_device(out_str)
                except serial.SerialException as e:
                    message_dialog(
                        message="Serial connection error has occurred.",
                        title="Error",
                        longtext=str(e.args)
                    )

    def send_to_device_rse(self) -> None:
        """Checks the input values to make sure they meet the timing restrictions
        Then formats the output list into the string that is interpreted by the
        Arduino script. RSE function only"""
        dev = self.get_device_data(
            int(self.ui.cmb_rse_deviceSel.currentIndex())
        )
        out_str = self.get_selection_list(1)
        if dev == (None, None):
            message_dialog(
                "No device added! Please make sure you have added and selected the device",
                "Error",
            )
        else:
            total = out_str[3]
            br = bool(out_str[1])
            battery = bool(out_str[5])
            seq = rse.get_seq(self.ui.cmb_rse_encounter.currentText())
            enc_sum = rse.sum_timer_seq(seq, battery, br)

            if not rse.check_time_difference(enc_sum, total):
                message_dialog(
                    "Your total timer is shorter than the expected value.\n"
                    "Please enter a valid timer",
                    "Timing Error"
                )
            else:
                self.show_enc_string_rse()
                try:
                    ser = MCSerial(port=dev[1], rate=dev[0])
                    ser.write_to_device(out_str)
                except serial.SerialException as e:
                    message_dialog(str(e), "Error")

    def show_enc_string_frlg(self) -> None:
        """Prints out the resulting output string and device data to a dialog box"""
        dev = self.get_device_data(
            int(self.ui.cmb_frlg_deviceSel.currentIndex())
        )
        output_string = self.get_selection_list(0)
        message = f"\nRate: {dev[0]}"
        message += f"\nPort: {dev[1]}"
        message += f"\n{create_ard_string(output_string)}"
        message_dialog(
            message,
            title="Output String"
        )

    def show_enc_string_rse(self) -> None:
        """Prints out the resulting output string and device data to a dialog box"""
        dev = self.get_device_data(
            int(self.ui.cmb_rse_deviceSel.currentIndex())
        )
        output_string = self.get_selection_list(1)
        message = f"\nRate: {dev[0]}"
        message += f"\nPort: {dev[1]}"
        message += f"\n{create_ard_string(output_string)}"

        message_dialog(
            message,
            title="Output String"
        )
