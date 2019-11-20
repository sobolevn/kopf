from kopf.reactor.registries import HandlerResult
from kopf.reactor.states import HandlerOutcome


def test_creation_for_ignored_handlers():
    outcome = HandlerOutcome(final=True)
    assert outcome.final
    assert outcome.delay is None
    assert outcome.result is None
    assert outcome.exception is None


def test_creation_for_results():
    result = HandlerResult(object())
    outcome = HandlerOutcome(final=True, result=result)
    assert outcome.final
    assert outcome.delay is None
    assert outcome.result is result
    assert outcome.exception is None


def test_creation_for_permanent_errors():
    error = Exception()
    outcome = HandlerOutcome(final=True, exception=error)
    assert outcome.final
    assert outcome.delay is None
    assert outcome.result is None
    assert outcome.exception is error


def test_creation_for_temporary_errors():
    error = Exception()
    outcome = HandlerOutcome(final=False, exception=error, delay=123)
    assert not outcome.final
    assert outcome.delay == 123
    assert outcome.result is None
    assert outcome.exception is error
