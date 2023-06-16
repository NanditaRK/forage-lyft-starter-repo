from car import Car
from battery.nubbin_battery import Nubbin
from battery.spindler_battery import Spindler
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


# I couldn't find which car had which type of tire so I randomly assigned.

class CarFactory():
    @staticmethod
    def create_callisope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
    