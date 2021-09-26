# -*- coding: utf-8 -*-

import threading
import time


class CyclicDriver(object):
    def __init__(self, loader, user_callback, rate_sec=0.1):
        self._loader = loader
        if not callable(user_callback):
            raise TypeError

        self._user_callback = user_callback

        self._loop = threading.Thread(target=self._loop)
        self._rate = rate_sec

    def start(self):
        if self._loop.is_alive():
            return

        self._loop.start()

    def wait(self):
        if not self._loop.is_alive():
            return

        self._loop.join()

    def _loop(self):
        while True:
            subject = self._loader.next()
            if subject is None:
                return

            self._user_callback(subject)
            time.sleep(self._rate)
