import pytest
from sigma.backends.mdatp import WindowsDefenderATPBackend

@pytest.fixture
def mdatp_backend():
    return WindowsDefenderATPBackend()

# TODO: implement tests for all backend features that don't belong to the base class defaults, e.g. features that were
# implemented with custom code, deferred expressions etc.



def test_mdatp_format1_output(mdatp_backend : WindowsDefenderATPBackend):
    """Test for output format format1."""
    # TODO: implement a test for the output format

def test_mdatp_format2_output(mdatp_backend : WindowsDefenderATPBackend):
    """Test for output format format2."""
    # TODO: implement a test for the output format

