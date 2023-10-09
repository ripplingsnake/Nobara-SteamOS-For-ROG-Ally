 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon
import subprocess

class RyzenAdjGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RyzenAdj Wattage Selector")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_wattage = QLabel("Adjust RyzenAdj TDP Wattage:")
        self.label_wattage.setFont(QFont("Helvetica", 12))
        self.layout.addWidget(self.label_wattage)

        self.tdp_wattage_slider = QSlider(Qt.Horizontal)
        self.tdp_wattage_slider.setMinimum(5000)  # Minimum wattage in mW (5W)
        self.tdp_wattage_slider.setMaximum(44000)  # Maximum wattage in mW (44W)
        self.tdp_wattage_slider.setTickInterval(5000)  # Tick interval in mW (5W)
        self.tdp_wattage_slider.setTickPosition(QSlider.TicksBelow)
        self.layout.addWidget(self.tdp_wattage_slider)

        self.silent_button = QPushButton("Silent (9W)")
        self.silent_button.setFont(QFont("Helvetica", 12, QFont.Bold))
        self.silent_button.setStyleSheet("background-color: green; color: white;")
        self.layout.addWidget(self.silent_button)

        self.performance_button = QPushButton("Performance (15W)")
        self.performance_button.setFont(QFont("Helvetica", 12, QFont.Bold))
        self.performance_button.setStyleSheet("background-color: blue; color: white;")
        self.layout.addWidget(self.performance_button)

        self.turbo_button = QPushButton("Turbo (30W)")
        self.turbo_button.setFont(QFont("Helvetica", 12, QFont.Bold))
        self.turbo_button.setStyleSheet("background-color: red; color: white;")
        self.layout.addWidget(self.turbo_button)

        self.central_widget.setLayout(self.layout)

        self.tdp_wattage_slider.valueChanged.connect(self.tdp_wattage_changed)
        self.silent_button.clicked.connect(self.set_silent_wattage)
        self.performance_button.clicked.connect(self.set_performance_wattage)
        self.turbo_button.clicked.connect(self.set_turbo_wattage)

        self.apply_timer = QTimer(self)
        self.apply_timer.timeout.connect(self.apply_ryzenadj_settings)

        self.setWindowIcon(QIcon("icon.png"))

    def tdp_wattage_changed(self):
        value_mw = self.tdp_wattage_slider.value()
        value_watts = value_mw / 1000  # Convert milliwatts to watts
        self.label_wattage.setText(f"Adjust RyzenAdj TDP Wattage: {value_watts}W")

        # Start or restart the timer when the slider value changes
        self.apply_timer.start(1000)  # 1000 milliseconds (1 second)

    def set_silent_wattage(self):
        wattage_mw = 9000  # Set to 9W (9000 mW)
        self.tdp_wattage_slider.setValue(wattage_mw)
        self.apply_ryzenadj_settings()

    def set_performance_wattage(self):
        wattage_mw = 15000  # Set to 15W (15000 mW)
        self.tdp_wattage_slider.setValue(wattage_mw)
        self.apply_ryzenadj_settings()

    def set_turbo_wattage(self):
        wattage_mw = 30000  # Set to 30W (30000 mW)
        self.tdp_wattage_slider.setValue(wattage_mw)
        self.apply_ryzenadj_settings()

    def apply_ryzenadj_settings(self):
        wattage_mw = self.tdp_wattage_slider.value()
        ryzenadj_command = f"sudo ryzenadj --stapm-limit={wattage_mw} --fast-limit={wattage_mw} --slow-limit={wattage_mw}"
        try:
            subprocess.run(ryzenadj_command, shell=True, check=True)
            self.show_notification("Settings Applied", "RyzenAdj settings have been successfully applied.")
        except subprocess.CalledProcessError as e:
            self.show_error("Error Applying Settings", f"An error occurred while applying RyzenAdj settings: {e}")


def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("icon.png"))

    window = RyzenAdjGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
