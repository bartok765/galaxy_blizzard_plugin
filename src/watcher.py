import os
import asyncio
import errno

import logging as log


class FileWatcher(object):
    def __init__(self, path, event, interval):
        self.path = path
        self.event = event
        self.last_modification_time = None
        self.interval = interval
        self.task = asyncio.create_task(self._watcher())

    async def _watcher(self):
        while True:
            try:
                stat = os.stat(self.path)
            except FileNotFoundError:
                continue
            except WindowsError as e:
                # 5 WindowsError access denied
                if e.winerror == 5:
                    continue
                else:
                    raise ()
            except OSError as e:
                if e.errno == errno.EACCES:
                    continue
                else:
                    raise ()
            except Exception as e:
                log.exception(f'Stating {self.path} has failed: {str(e)}')
                raise RuntimeError('Stating failed:' + str(e))
            else:
                if self.last_modification_time is None:
                    self.last_modification_time = stat.st_mtime
                elif stat.st_mtime != self.last_modification_time:
                    self.last_modification_time = stat.st_mtime
                    if not self.event.is_set():
                        self.event.set()
            finally:
                await asyncio.sleep(self.interval)
