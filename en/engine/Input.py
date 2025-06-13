import pygame

class InputHandler:
    def __init__(self):
        self.key_states = pygame.key.get_pressed()
        self.mouse_buttons = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rel = (0, 0)
        self.scroll = 0

    def update(self):
        self.key_states = pygame.key.get_pressed()
        self.mouse_buttons = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rel = pygame.mouse.get_rel()
        self.scroll = 0

        for event in pygame.event.get([pygame.MOUSEWHEEL]):
            if event.type == pygame.MOUSEWHEEL:
                self.scroll += event.y

    def is_key_down(self, key):
        return self.key_states[key]

    def is_mouse_button_down(self, button_index):
        return self.mouse_buttons[button_index]

    def get_mouse_position(self):
        return self.mouse_pos

    def get_mouse_movement(self):
        return self.mouse_rel

    def get_scroll(self):
        return self.scroll
