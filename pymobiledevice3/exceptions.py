__all__ = [
    'PyMobileDevice3Exception', 'DeviceVersionNotSupportedError', 'IncorrectModeError', 'DeviceVersionFormatError',
    'NotTrustedError', 'PairingError', 'NotPairedError', 'CannotStopSessionError',
    'PasswordRequiredError', 'StartServiceError', 'FatalPairingError', 'NoDeviceConnectedError', 'MuxException',
    'MuxVersionError', 'ArgumentError', 'AfcException', 'AfcFileNotFoundError', 'DvtException', 'DvtDirListError',
    'NotMountedError', 'AlreadyMountedError', 'UnsupportedCommandError', 'ExtractingStackshotError',
    'ConnectionTerminatedError', 'WirError', 'WebInspectorNotEnabledError', 'RemoteAutomationNotEnabledError',
    'ArbitrationError', 'InternalError', 'DeveloperModeIsNotEnabledError', 'DeviceAlreadyInUseError', 'LockdownError',
    'PairingDialogResponsePendingError', 'UserDeniedPairingError', 'InvalidHostIDError', 'SetProhibitedError',
    'MissingValueError', 'PasscodeRequiredError', 'AmfiError', 'DeviceHasPasscodeSetError', 'NotificationTimeoutError',
    'DeveloperModeError', 'ProfileError', 'IRecvError', 'IRecvNoDeviceConnectedError',
    'NoDeviceSelectedError', 'MessageNotSupportedError', 'InvalidServiceError', 'InspectorEvaluateError',
    'LaunchingApplicationError', 'BadCommandError', 'BadDevError', 'ConnectionFailedError',
]


class PyMobileDevice3Exception(Exception):
    pass


class DeviceVersionNotSupportedError(PyMobileDevice3Exception):
    pass


class IncorrectModeError(PyMobileDevice3Exception):
    pass


class DeviceVersionFormatError(PyMobileDevice3Exception):
    pass


class NotTrustedError(PyMobileDevice3Exception):
    pass


class PairingError(PyMobileDevice3Exception):
    pass


class NotPairedError(PyMobileDevice3Exception):
    pass


class CannotStopSessionError(PyMobileDevice3Exception):
    pass


class PasswordRequiredError(PairingError):
    pass


class StartServiceError(PyMobileDevice3Exception):
    pass


class FatalPairingError(PyMobileDevice3Exception):
    pass


class NoDeviceConnectedError(PyMobileDevice3Exception):
    pass


class MuxException(PyMobileDevice3Exception):
    pass


class MuxVersionError(MuxException):
    pass


class BadCommandError(MuxException):
    pass


class BadDevError(MuxException):
    pass


class ConnectionFailedError(MuxException):
    pass


class ArgumentError(PyMobileDevice3Exception):
    pass


class AfcException(PyMobileDevice3Exception, OSError):
    def __init__(self, message, status):
        OSError.__init__(self, status, message)
        self.status = status


class AfcFileNotFoundError(AfcException):
    pass


class DvtException(PyMobileDevice3Exception):
    """ Domain exception for DVT operations. """
    pass


class UnrecognizedSelectorError(DvtException):
    """ Attempted to call an unrecognized selector from DVT. """
    pass


class DvtDirListError(DvtException):
    """ Raise when directory listing fails. """
    pass


class NotMountedError(PyMobileDevice3Exception):
    """ Given image for umount wasn't mounted in the first place """
    pass


class AlreadyMountedError(PyMobileDevice3Exception):
    """ Given image for mount has already been mounted in the first place """
    pass


class MissingManifestError(PyMobileDevice3Exception):
    """ No manifest could be found """
    pass


class UnsupportedCommandError(PyMobileDevice3Exception):
    """ Given command isn't supported for this iOS version """
    pass


class ExtractingStackshotError(PyMobileDevice3Exception):
    """ Raise when stackshot is not received in the core profile session. """
    pass


class ConnectionTerminatedError(PyMobileDevice3Exception):
    """ Raise when a connection is terminated abruptly. """
    pass


class StreamClosedError(ConnectionTerminatedError):
    """ Raise when trying to send a message on a closed stream. """
    pass


class WebInspectorNotEnabledError(PyMobileDevice3Exception):
    """ Raise when Web Inspector is not enabled. """
    pass


class RemoteAutomationNotEnabledError(PyMobileDevice3Exception):
    """ Raise when Web Inspector remote automation is not enabled. """
    pass


class WirError(PyMobileDevice3Exception):
    """ Raise when Webinspector WIR command fails. """
    pass


class InternalError(PyMobileDevice3Exception):
    """ Some internal Apple error """
    pass


class ArbitrationError(PyMobileDevice3Exception):
    """ Arbitration failed """
    pass


class DeviceAlreadyInUseError(ArbitrationError):
    """ Device is already checked-in by someone """

    @property
    def message(self):
        return self.args[0].get('message')

    @property
    def owner(self):
        return self.args[0].get('owner')

    @property
    def result(self):
        return self.args[0].get('result')


class DeveloperModeIsNotEnabledError(PyMobileDevice3Exception):
    """ Raise when mounting failed because developer mode is not enabled. """
    pass


class DeveloperDiskImageNotFoundError(PyMobileDevice3Exception):
    """ Failed to locate the correct DeveloperDiskImage.dmg """
    pass


class DeveloperModeError(PyMobileDevice3Exception):
    """ Raise when amfid failed to enable developer mode. """
    pass


class LockdownError(PyMobileDevice3Exception):
    """ lockdown general error """
    pass


class SetProhibitedError(LockdownError):
    pass


class PairingDialogResponsePendingError(PairingError):
    """ User hasn't yet confirmed the device is trusted """
    pass


class UserDeniedPairingError(PairingError):
    pass


class InvalidHostIDError(PairingError):
    pass


class MissingValueError(LockdownError):
    """ raised when attempting to query non-existent domain/key """
    pass


class InvalidConnectionError(LockdownError):
    pass


class PasscodeRequiredError(LockdownError):
    """ passcode must be present for this action """
    pass


class AmfiError(PyMobileDevice3Exception):
    pass


class DeviceHasPasscodeSetError(AmfiError):
    pass


class NotificationTimeoutError(PyMobileDevice3Exception, TimeoutError):
    pass


class ProfileError(PyMobileDevice3Exception):
    pass


class IRecvError(PyMobileDevice3Exception):
    pass


class IRecvNoDeviceConnectedError(IRecvError):
    pass


class NoDeviceSelectedError(PyMobileDevice3Exception):
    pass


class MessageNotSupportedError(PyMobileDevice3Exception):
    pass


class InvalidServiceError(LockdownError):
    pass


class InspectorEvaluateError(PyMobileDevice3Exception):
    pass


class LaunchingApplicationError(PyMobileDevice3Exception):
    pass


class AppInstallError(PyMobileDevice3Exception):
    pass
