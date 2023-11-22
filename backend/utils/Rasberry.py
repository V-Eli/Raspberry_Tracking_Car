import Jetson.GPIO as GPIO
import time

class Car:
    def __init__(self) -> None:
        # Lista de pines que deseas habilitar
        GPIO.setmode(GPIO.BOARD)
        pines = [17, 18]  # Ejemplo de pines GPIO
        pwm_gpio = 12
        frequence = 50
        GPIO.setup(pwm_gpio, GPIO.OUT)
        self.pwm = GPIO.PWM(pwm_gpio, frequence)

        # Configura los pines como salida
        for pin in pines:
            GPIO.setup(pin, GPIO.OUT)

        self.pwm.start(self.angle_to_percent(0))

    def forward(self) -> None:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)

    def backward(self) -> None:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    def stop(self) -> None:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)

    def direction(self, direction: str) -> None:
        if direction >= 180:
            direction -= 180
            direction = self.inverse_map(direction)
        
        self.pwm.ChangeDutyCycle(self.angle_to_percent(int(direction)))

    @staticmethod
    def angle_to_percent (angle) :
        if angle > 180 or angle < 0 :
            return False

        start = 4
        end = 12.5
        ratio = (end - start)/180 #Calcul ratio from angle to percent

        angle_as_percent = angle * ratio

        return start + angle_as_percent
    
    @staticmethod
    def inverse_map(value):
        # Ensure the input value is in the range [0, 180]
        value = max(0, min(180, value))
        
        # Calculate the inversely mapped value
        inverse_value = 180 - value
        
        return inverse_value

    def __del__(self) -> None:
        GPIO.cleanup()

if __name__ == "__main__":
    # Example usage:
    # input_value = 91
    # result = inverse_map(input_value)
    # print(f"The inversely mapped value for {input_value} is {result}")
