"""
This example demonstrates how you can structure code so that changes in one part
(weather measurements) automatically update multiple other parts (various displays)
in a clean, modular way.

Observer Pattern: The main design here, used to decouple the weather data (subject)
from the displays (observers).
Flexibility: New display elements can be added or removed without modifying the core
WeatherData class.
Real-World Analogy: Think of a news service (WeatherData) that pushes out news updates
to subscribers (observers) who then display the news in different formats
(current conditions, statistics, forecast).
"""
from abc import abstractmethod, ABC

###############################################################################
# Observables
###############################################################################
class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def registerObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except:
            pass

    def notifyObservers(self):
        for obs in self._observers:
            obs.update(self._temperature, self._humidity, self._pressure)

    def setMeasurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure

        self.notifyObservers()

###############################################################################
# Observers
###############################################################################

class Observer(ABC):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self._current_temperature = 70.0
        self._last_temperature = 0.0
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self._last_temperature = self._current_temperature
        self._current_temperature = temperature
        self._humidity = humidity

        self.display()

    def display(self):
        print("Current conditions: " + str(self._current_temperature) +
              "F degrees and " + str(self._humidity) + " % humidity")
        if self._current_temperature > self._last_temperature:
            print("It got hotter!!!")
        elif self._current_temperature == self._last_temperature:
            print("Same temperature")
        elif self._current_temperature < self._last_temperature:
            print("It is colder!!!")
        print('***********************************************')

class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self._max_temp = 0.0
        self._min_temp = 200
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self._temp_sum += temp
        self._num_readings += 1

        if temp > self._max_temp:
            self._max_temp = temp

        if temp < self._min_temp:
            self._min_temp = temp

        self.display()

    def display(self):
        avg_temp = self._temp_sum / self._num_readings
        print("Statistics Avg/Max/Min temperature = {0}/{1}/{2}".format(
            avg_temp, self._max_temp, self._min_temp))

        print('***********************************************')

class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self._current_pressure = 29.92
        self._last_pressure = 0.0
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: "),
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        elif self._current_pressure < self._last_pressure:
            print("Watch out for cooler, rainy weather")

        print('***********************************************')

if __name__ == '__main__':
    # TODO: instantiate an object of Subject
    # Can't instantiate abstract class Subject with abstract methods

    # TODO: instantiate an object of Observer
    # Can't instantiate abstract class Observer with abstract methods

    # TODO: instantiate an object of WeatherData
    weatherData = WeatherData()

    # TODO: instantiate an object of CurrentConditionsDisplay
    currentConditions = CurrentConditionsDisplay(weatherData)

    # TODO: instantiate an object of StatisticsDisplay
    stats = StatisticsDisplay(weatherData)

    # TODO: instantiate an object of ForecastDisplay
    forecast = ForecastDisplay(weatherData)

    # TODO: create multiple events
    weatherData.setMeasurements(76.0,65,30.4)
    print(" NEW EVENT ")
    weatherData.setMeasurements(72.0, 70, 30.1)
    print(" NEW EVENT ")
    weatherData.setMeasurements(80.0, 70, 30.1)