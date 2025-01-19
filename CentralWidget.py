# Importieren der benötigten Klassen aus der PyQt6-Bibliothek
from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime

# Definition einer benutzerdefinierten Widget-Klasse, die die QChartView-Klasse erweitert
class CentralWidget(QChartView):
    def __init__(self, parent=None):
        # Initialisierung der Basisklasse QChartView
        super(CentralWidget, self).__init__(parent)

        # Erstellen einer Serie für die Goldpreisentwicklung in Euro
        series_euro = QLineSeries()
        series_euro.setName("Goldpreisentwicklung in €")  # Name der Serie festlegen

        # Hinzufügen von Datenpunkten für die Serie (Datum und Preis in Euro)
        series_euro.append(QDateTime.fromString("2021-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1492.80)
        series_euro.append(QDateTime.fromString("2021-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1590.60)
        series_euro.append(QDateTime.fromString("2022-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1781.90)
        series_euro.append(QDateTime.fromString("2022-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1731.28)
        series_euro.append(QDateTime.fromString("2022-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1690.30)
        series_euro.append(QDateTime.fromString("2022-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1827.45)
        series_euro.append(QDateTime.fromString("2023-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1838.68)
        series_euro.append(QDateTime.fromString("2023-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1763.45)
        series_euro.append(QDateTime.fromString("2023-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1808.75)
        series_euro.append(QDateTime.fromString("2023-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1827.45)
        series_euro.append(QDateTime.fromString("2024-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2004.30)
        series_euro.append(QDateTime.fromString("2024-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2164.99)
        series_euro.append(QDateTime.fromString("2024-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2386.69)

        # Erstellen einer Serie für die Goldpreisentwicklung in US-Dollar
        series_dollar = QLineSeries()
        series_dollar.setName("Goldpreisentwicklung in $")  # Name der Serie festlegen

        # Hinzufügen von Datenpunkten für die Serie (Datum und Preis in Dollar)
        series_dollar.append(QDateTime.fromString("2021-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1750.87)
        series_dollar.append(QDateTime.fromString("2021-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1788.48)
        series_dollar.append(QDateTime.fromString("2022-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1945.22)
        series_dollar.append(QDateTime.fromString("2022-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1827.54)
        series_dollar.append(QDateTime.fromString("2022-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1643.65)
        series_dollar.append(QDateTime.fromString("2022-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1750.40)
        series_dollar.append(QDateTime.fromString("2023-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1982.00)
        series_dollar.append(QDateTime.fromString("2023-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1913.73)
        series_dollar.append(QDateTime.fromString("2023-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1928.80)
        series_dollar.append(QDateTime.fromString("2023-11-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2002.39)
        series_dollar.append(QDateTime.fromString("2024-03-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2166.31)
        series_dollar.append(QDateTime.fromString("2024-06-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 1913.73)
        series_dollar.append(QDateTime.fromString("2024-09-26", "yyyy-MM-dd").toMSecsSinceEpoch(), 2658.13)

        # Erstellen und Konfigurieren der x-Achse (Datum-Achse)
        axis_x = QDateTimeAxis()
        axis_x.setTitleText("Datum")  # Titel der Achse festlegen

        # Einstellen des Bereichs der x-Achse (Start- und Enddatum)
        start_date = QDateTime.fromString("2021-09-26", "yyyy-MM-dd")
        end_date = QDateTime.fromString("2024-09-26", "yyyy-MM-dd")
        axis_x.setRange(start_date, end_date)

        # Festlegen des Anzeigeformats für die Datum-Achse
        axis_x.setFormat("dd.MM.yyyy")

        # Erstellen und Konfigurieren der y-Achse für Euro-Werte
        axis_euro = QValueAxis()
        axis_euro.setTitleText("Goldpreis in €")
        axis_euro.setRange(1250, 2750)  # Bereich der Achse festlegen

        # Erstellen und Konfigurieren der y-Achse für Dollar-Werte
        axis_dollar = QValueAxis()
        axis_dollar.setTitleText("Goldpreis in $")
        axis_dollar.setRange(1250, 2750)  # Bereich der Achse festlegen

        # Erstellen des Diagramms
        q_chart = QChart()
        q_chart.setTitle("Goldpreisentwicklung")  # Titel des Diagramms festlegen

        # Hinzufügen der Achsen zum Diagramm
        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)  # x-Achse unten
        q_chart.addAxis(axis_euro, Qt.AlignmentFlag.AlignLeft)  # y-Achse für Euro links
        q_chart.addAxis(axis_dollar, Qt.AlignmentFlag.AlignRight)  # y-Achse für Dollar rechts

        # Hinzufügen der Datenserien zum Diagramm
        q_chart.addSeries(series_euro)
        q_chart.addSeries(series_dollar)

        # Verknüpfen der Datenserien mit den entsprechenden Achsen
        series_euro.attachAxis(axis_x)
        series_euro.attachAxis(axis_euro)

        series_dollar.attachAxis(axis_x)
        series_dollar.attachAxis(axis_dollar)

        # Festlegen des Diagramms als Anzeigeinhalt
        self.setChart(q_chart)
