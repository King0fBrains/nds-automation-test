"""Reusable static functions"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from PySide6.QtWidgets import QMessageBox


def create_ard_string(inp: list[int]) -> str:
    """Create a string from a list of integers to match
    the desired output to be sent to the Arduino"""
    form = "+".join(map(str, inp))
    return form + "+?"


def message_dialog(message: str, title: str, longtext: str = None) -> None:
    """Creates a simple Qt Dialog box"""
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    if longtext is not None:
        msg_box.setDetailedText(longtext)
    msg_box.exec()
