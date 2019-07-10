from src.model.device import Device, DiscreteScale, ContinuousScale, ToggleSettings, SecuritySettings, ResourceAware

from PyQt5.QtWidgets import QWidget, QDialog, QSlider, QLabel, QHBoxLayout, QCheckBox
from PyQt5.Qt import Qt


class DiscreteScaleView(QWidget):
    def __init__(self, settings):
        super().__init__(flags=Qt.Widget)
        self.settings = settings
        self.def_slider()

    def def_slider(self):
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(len(self.settings.scale) - 1)
        self.slider.setTickInterval(1)
        self.slider.setValue(self.settings.scale.index(self.settings.value))
        self.lbl = QLabel(str(self.scale[self.slider.value()]))
        # TODO: када се промени вредност слајдера, треба да се промени и вредност лабеле

        layout = QHBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def value(self):
        return self.scale[self.slider.value()]

    def disable(self):
        self.slider.setEnabled(False)

    def enable(self):
        self.slider.setEnabled(True)


class ContinuousScaleView(QWidget):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.def_slider()

    def def_slider(self):
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.settings.min_value)
        self.slider.setMaximum(self.settings.max_value)
        self.slider.setValue(self.settings.value)
        self.lbl = QLabel(str(self.slider.value()))
        # TODO: када се промени вредност слајдера, треба да се промени и вредност лабеле

        layout = QHBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def value(self):
        return self.slider.value()

    def disable(self):
        self.slider.setEnabled(False)

    def enable(self):
        self.slider.setDisabled(True)


class ToggleSettingsView(QWidget):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.def_checkbox()

    def def_checkbox(self):
        self.box = QCheckBox('Toggled')
        self.box.setChecked(self.settings.is_on)

        layout = QHBoxLayout()
        layout.addWidget(self.box)
        self.setLayout(layout)

    def value(self):
        return self.box.isChecked()

    def disable(self):
        self.box.setEnabled(False)

    def enable(self):
        self.box.setEnabled(True)


class SecuritySettingsView(QWidget):
    pass


class DeviceView(QDialog):
    def __init__(self, device, permission_table):
        super().__init__(flags=Qt.Dialog)
        self.device = device
        self.permission_table = permission_table
        self.fill()
