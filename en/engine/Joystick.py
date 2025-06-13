import pygame

class JoystickManager:
    def __init__(self):
        pygame.joystick.init()
        self.joysticks = []
        self._detect_joysticks()

    def _detect_joysticks(self):
        self.joysticks.clear()
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            self.joysticks.append(joystick)
            print(f"Joystick {i}: {joystick.get_name()} connected.")

    def get_button(self, joystick_index, button_index):
        if 0 <= joystick_index < len(self.joysticks):
            return self.joysticks[joystick_index].get_button(button_index)
        return False

    def get_axis(self, joystick_index, axis_index):
        if 0 <= joystick_index < len(self.joysticks):
            return self.joysticks[joystick_index].get_axis(axis_index)
        return 0.0

    def get_joystick_count(self):
        return len(self.joysticks)

    def get_joystick_name(self, index):
        if 0 <= index < len(self.joysticks):
            return self.joysticks[index].get_name()
        return "Unknown"
