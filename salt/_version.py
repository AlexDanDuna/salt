# We hardcode this since salt will generate an invalid version if we upgrade packages independently.

from salt.version import SaltStackVersion

__saltstack_version__ = SaltStackVersion(3000, 2, None, 0, '', 0, 10, 'geffff1c00b')