import logging

import click

from pymobiledevice3.cli.cli_common import Command, print_json
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.os_trace import OsTraceService

logger = logging.getLogger(__name__)


@click.group()
def cli():
    """ apps cli """
    pass


@cli.group()
def processes():
    """ processes cli """
    pass


@processes.command('ps', cls=Command)
@click.option('--color/--no-color', default=True)
def processes_ps(lockdown: LockdownClient, color):
    """ show process list """
    print_json(OsTraceService(lockdown=lockdown).get_pid_list().get('Payload'), colored=color)


@processes.command('pgrep', cls=Command)
@click.argument('expression')
def processes_pgrep(lockdown: LockdownClient, expression):
    """ try to match processes pid by given expression (like pgrep) """
    processes_list = OsTraceService(lockdown=lockdown).get_pid_list().get('Payload')
    for pid, process_info in processes_list.items():
        process_name = process_info.get('ProcessName')
        if expression in process_name:
            logger.info(f'{pid} {process_name}')
