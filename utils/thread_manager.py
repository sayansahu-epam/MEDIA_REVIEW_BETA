import threading


def run_in_threads(target_function, args_list):
    """
    Runs the target_function concurrently using threads.

    :param target_function: function to execute
    :param args_list: list of argument tuples
    """
    threads = []

    for args in args_list:
        thread = threading.Thread(
            target=target_function,
            args=args
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
