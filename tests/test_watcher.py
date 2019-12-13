import pytest
import os


@pytest.fixture()
def waiter():
    async def function(event):
        await event.wait()
        event.clear()
    return function


@pytest.fixture()
def mock_stat(mocker):
    def function():
        a_stat = list(os.stat(__file__))
        stat_results = []
        for x in range(5):
            a_stat[-2] += 1
            stat_results.append(os.stat_result(a_stat))
        mocker.patch('os.stat', side_effect=stat_results)
    return function


# TODO
# def test_watcher(waiter, mock_stat):
#     mock_stat()
#     def 
#     file_watcher = FileWatcher()
#     event = file_watcher.get_event()
#     assert event.is_set()
#     task = asyncio.create_task(waiter()(event))
#     await task
#     assert not event.is_set()
