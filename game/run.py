from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QScrollArea, QLineEdit
import sys
import threading
import pandas as pd
from game import Game
from menus import MenuGUI
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QDialog, QLabel
from PyQt5.QtGui import QPixmap
from graph import DataVisualizer
import subprocess
import os

class StartMenuUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HE-1 HE-I-M Start Menu")
        self.setGeometry(100, 100, 400, 400)
        self.__graph = DataVisualizer()
        self.__graph.run_all_methods()

        # Central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Title Label
        title_label = QPushButton("HE-1 HE-I-M")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setEnabled(False)
        layout.addWidget(title_label)

        # Buttons
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_game)
        layout.addWidget(start_button)

        stats_button = QPushButton("Statistics")
        stats_button.clicked.connect(self.show_statistics)
        layout.addWidget(stats_button)

        player_stats_button = QPushButton("Player Statistics")
        player_stats_button.clicked.connect(self.show_player_statistics)
        layout.addWidget(player_stats_button)

        player_graph_button = QPushButton("Player Graph")
        player_graph_button.clicked.connect(self.show_player_graph)
        layout.addWidget(player_graph_button)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_game(self):
        # Launch both the Game and MenuGUI classes in separate threads
        threading.Thread(target=self.run_menu, daemon=True).start()
        self.run_game()

    def run_game(self):
        game = Game()
        game.run()

    def run_menu(self):
        menu = MenuGUI()
        menu.mainloop()
    
    def show_statistics(self):
        # Create a new dialog window to display the graphs
        stats_window = QDialog(self)
        stats_window.setWindowTitle("Statistics Graphs")
        stats_window.setGeometry(150, 150, 800, 600)

        layout = QVBoxLayout()

        # Load and plot graphs
        self.__graph.load_customer_data()
        self.__graph.load_player_data()
        self.__graph.load_item_data()
        self.__graph.run_all_methods()

        # Load graph images
        customer_frequency_graph = QLabel()
        customer_frequency_pixmap = QPixmap("data/graph/customer_frequency.png")
        if not customer_frequency_pixmap.isNull():
            customer_frequency_graph.setPixmap(customer_frequency_pixmap)

        customer_satisfaction_graph = QLabel()
        customer_satisfaction_pixmap = QPixmap("data/graph/customer_satisfaction.png")
        if not customer_satisfaction_pixmap.isNull():
            customer_satisfaction_graph.setPixmap(customer_satisfaction_pixmap)

        average_money_graph = QLabel()
        average_money_pixmap = QPixmap("data/graph/average_money_per_day.png")
        if not average_money_pixmap.isNull():
            average_money_graph.setPixmap(average_money_pixmap)

        # Load additional graph images
        item_purchase_frequency_graph = QLabel()
        item_purchase_frequency_pixmap = QPixmap("data/graph/item_purchase_frequency.png")
        if not item_purchase_frequency_pixmap.isNull():
            item_purchase_frequency_graph.setPixmap(item_purchase_frequency_pixmap)

        item_correlation_graph = QLabel()
        item_correlation_pixmap = QPixmap("data/graph/item_correlation.png")
        if not item_correlation_pixmap.isNull():
            item_correlation_graph.setPixmap(item_correlation_pixmap)

        # Add graphs to the layout if they are valid
        if not customer_frequency_pixmap.isNull():
            layout.addWidget(customer_frequency_graph)
        if not customer_satisfaction_pixmap.isNull():
            layout.addWidget(customer_satisfaction_graph)
        if not average_money_pixmap.isNull():
            layout.addWidget(average_money_graph)
        if not item_purchase_frequency_pixmap.isNull():
            layout.addWidget(item_purchase_frequency_graph)
        if not item_correlation_pixmap.isNull():
            layout.addWidget(item_correlation_graph)

        # Make the statistics window scrollable
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_content.setLayout(layout)

        scroll_area.setWidget(scroll_content)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)

        stats_window.setLayout(main_layout)
        stats_window.exec_()

    def show_player_statistics(self):
        # Sample data for player statistics
        player_stats = pd.read_csv("data/csv/player.csv").sort_values("_PlayerData__player_id").to_dict(orient='records')

        # Create a dialog to display the statistics
        stats_dialog = QDialog(self)
        stats_dialog.setWindowTitle("Statistics")
        stats_dialog.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        # Create a table widget
        table = QTableWidget()
        table.setRowCount(len(player_stats))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Player ID", "Day", "Money"])

        # Populate the table with data
        for row, stat in enumerate(player_stats):
            table.setItem(row, 0, QTableWidgetItem(str(stat["_PlayerData__player_id"]//1000)))
            table.setItem(row, 1, QTableWidgetItem(str(stat["_PlayerData__day"])))

        layout.addWidget(table)
        stats_dialog.setLayout(layout)
        stats_dialog.exec_()

    def show_player_graph(self):
        # Create a new dialog window to input player ID and display the graph
        player_graph_window = QDialog(self)
        player_graph_window.setWindowTitle("Player Graph")
        player_graph_window.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        # Add a table of player IDs
        player_id_table_label = QLabel("Available Player IDs:")
        layout.addWidget(player_id_table_label)

        player_ids = pd.read_csv("data/csv/player.csv")["_PlayerData__player_id"].drop_duplicates().sort_values()
        player_id_table = QTableWidget()
        player_id_table.setRowCount(len(player_ids))
        player_id_table.setColumnCount(1)
        player_id_table.setHorizontalHeaderLabels(["Player ID"])

        for row, player_id in enumerate(player_ids):
            player_id_table.setItem(row, 0, QTableWidgetItem(str(int(player_id)//1000)))

        layout.addWidget(player_id_table)

        # Input field for player ID
        player_id_label = QLabel("Enter Player ID:")
        layout.addWidget(player_id_label)

        player_id_input = QLineEdit()
        layout.addWidget(player_id_input)

        # Button to generate the graph
        generate_button = QPushButton("Generate Graph")
        layout.addWidget(generate_button)

        # Graph display area
        graph_label = QLabel()
        layout.addWidget(graph_label)

        def generate_graph():
            player_id = player_id_input.text()
            if not player_id.isdigit():
                QMessageBox.warning(player_graph_window, "Invalid Input", "Please enter a valid numeric Player ID.")
                return

            player_id = int(player_id)
            self.__graph.plot_player_money_vs_rent(player_id)

            graph_pixmap = QPixmap(f"data/graph/player_{player_id}_money_vs_rent.png")
            if not graph_pixmap.isNull():
                graph_label.setPixmap(graph_pixmap)
            else:
                QMessageBox.warning(player_graph_window, "Graph Not Found", "Could not generate the graph for the given Player ID.")

        generate_button.clicked.connect(generate_graph)

        player_graph_window.setLayout(layout)
        player_graph_window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = StartMenuUI()
    main_window.show()
    sys.exit(app.exec_())
