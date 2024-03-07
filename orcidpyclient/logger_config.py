import logging
import sys

_logger_depth = "INFO"

logger = logging.getLogger("#orcid#")
logger.setLevel(getattr(logging, _logger_depth))

stdout_sh = logging.StreamHandler(sys.stdout)
stdout_sh.setLevel(getattr(logging, _logger_depth))
stdout_sh.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)

logger.addHandler(stdout_sh)
