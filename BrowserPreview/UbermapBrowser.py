import os, signal, subprocess, sys
import Live
from Ubermap.UbermapLibs import log, config

class UbermapBrowser:
    player_process = None

    def __init__(self):
        self.cfg = config.load('browser')

    def preview(self, selected, contents, level):
        if not self.cfg.get('enabled') or  level < 1:
            return

        # Ignore items that aren't content items
        if not (hasattr(selected, 'content') and hasattr(selected.content, 'name')):
            self._kill_player(True)
            return
        # Ignore non-audio items
        if not any(audio_format in selected.content.name for audio_format in self.cfg.get('audio_formats')):
            log('INFO ' + selected.content.name + ' is not a known audio format')
            self._kill_player(True)
            return

        library_top_level = str(contents[1][0].selected_item)
        # Ignore any top-level paths we don't know how to handle
        if not library_top_level in self.cfg.get('LibraryPaths'):
            log('INFO path ' + library_top_level + ' not found in config')
            return

        path = []
        for parent_level in range(1, level):
            path.append(str(contents[parent_level][0].selected_item))
        path.append(selected.content.name)

        path = os.path.join(*path)
        realpath = self.cfg.get('LibraryPaths', library_top_level) + path

        self._kill_player()

        log('INFO playing ' + realpath)
        self.player_process = subprocess.Popen([self.cfg.get('player_bin'), realpath])

    def _kill_player(self, force = False):
        if(self.player_process and (force or self.cfg.get('kill_player'))):
            os.kill(self.player_process.pid, signal.SIGKILL)
