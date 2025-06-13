import os
import sys
import importlib.util

class SceneManager:
    def __init__(self, game_root_dir):
        self.game_root_dir = os.path.abspath(game_root_dir)
        self.scenes = {}
        self.current_scene = None

    def _find_scene_file(self, scene_name, start_dir=None):
        if start_dir is None:
            start_dir = self.game_root_dir
        for root, dirs, files in os.walk(start_dir):
            for file in files:
                if file == f"{scene_name}.py":
                    return os.path.join(root, file)
        return None

    def _load_scene_from_file(self, filepath, scene_name):
        try:
            spec = importlib.util.spec_from_file_location(scene_name, filepath)
            module = importlib.util.module_from_spec(spec)
            sys.modules[scene_name] = module
            spec.loader.exec_module(module)
            if hasattr(module, 'Scene'):
                scene_instance = module.Scene()
                scene_instance.manager = self  # Give scene access to manager
                self.scenes[scene_name] = scene_instance
                return scene_instance
            else:
                print(f"[SceneManager] ERROR: No 'Scene' class in {filepath}")
        except Exception as e:
            print(f"[SceneManager] ERROR loading '{scene_name}': {e}")
        return None

    def change_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]
            print(f"[SceneManager] Loaded scene '{scene_name}' from cache.")
        else:
            path = self._find_scene_file(scene_name)
            if not path:
                print(f"[SceneManager] Scene '{scene_name}' not found.")
                return
            scene = self._load_scene_from_file(path, scene_name)
            if scene:
                self.current_scene = scene
                print(f"[SceneManager] Scene '{scene_name}' loaded.")

        if self.current_scene and hasattr(self.current_scene, 'start'):
            self.current_scene.start()

    def update(self, delta_time):
        if self.current_scene and hasattr(self.current_scene, 'update'):
            self.current_scene.update(delta_time)

    def draw(self, surface):
        if self.current_scene and hasattr(self.current_scene, 'draw'):
            self.current_scene.draw(surface)
