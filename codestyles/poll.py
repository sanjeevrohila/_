def poll(predicate, msg, timeout, sleep, *args, **kwargs):
    """
    This method accepts a method which returns True or False
    If the expectation is other than True/ False
    then expects the expected output for a time given in the timeout.

    An extractor method is also passed if the output is required
    to be processed further.

    in case the passed method upon calling return a False, it
    retries for timeout time, with a hold of sleep within
    retrying the method.

    :param predicate: the method to continue get the information
    :type predicate: ``function``
    :param msg: a message about the predicate function
    :type msg: ``str``
    :param timeout: the timeout for that the poll method has to wait
                    for the predicate function to be executed for an
                    expected output
    :type timeout: ``int`` seconds
    :param sleep: the wait time for for each attempt of predicate
    :type sleep: ``int``
    :param args: the non keyword arguments to be passed to predicate
    :type args: ``tuple``
    :param kwargs: the keywords arguments to be passed to predicate
    :type kwargs: ``dict``
    :param extractor: any method to further process the predicate output
                      to compare with the expected output - optional
    :type extractor: ``function``
    :param raise_: decide if the function should raise Error or return value
    :type raise_: ``bool``
    :returns: the output of the function passed to predicate
    :rtype: ``complex`` depend upon the passed method

    """
    expected_output = kwargs.pop("expected_output", True)
    extractor = kwargs.pop("extractor", None)
    raise_ = kwargs.pop("raise_", True)
    printer.printinfo(f"waiting maximum {timeout} seconds for {msg}")

    start = time.time()
    while time.time() < start + timeout:
        try:
            resp = predicate(*args, **kwargs)
            printer.printv(f"{predicate.__qualname__} response - {resp}")
            if extractor:
                resp_extracted = extractor(resp)
            else:
                resp_extracted = resp
            printer.printv(
                f"{extractor.__qualname__} response - {resp_extracted}"
            )
        except Exception as exc:
            printer.printwarn(exc)
            time.sleep(sleep)
            continue

        if resp_extracted == expected_output:
            printer.printinfo(
                f"done waiting for {msg} after "
                f"{int(time.time() - start)} seconds"
            )
            return resp
        time.sleep(sleep)

    if raise_:
        raise RuntimeError(f"timeout exceeded while waiting for {msg} ")
    else:
        return resp
