import shlex
import subprocess

from .exceptions import CommandExecutionError, CommandParameterError


class Command(object):
    process = None
    command = 'true'
    ignore_output = True
    fail_silently = False
    required_parameters = None
    stdout = subprocess.PIPE
    stderr = subprocess.PIPE

    def __init__(self, **kwargs):
        self.parameters = kwargs
        if not self.validate_parameters():
            raise CommandParameterError(
                'Parameter(s) missing, required parameters: {0}'.format(
                    ', '.join(self.required_parameters)))

    def execute(self, ignore_output=None, fail_silently=None, stdin=None, **kwargs):
        command = self.get_command()
        ignore_output = ignore_output if ignore_output is not None else self.ignore_output
        fail_silently = fail_silently if fail_silently is not None else self.fail_silently

        # Don't automatically merge with os.environ for security reasons.
        # Make this forwarding explicit rather than implicit.
        environ = kwargs.pop('environ', None)
        shell = kwargs.pop('shell', False)

        try:
            self.process = subprocess.Popen(
                command,
                shell=shell,
                universal_newlines=True,
                env=environ,
                stdout=kwargs['stdout'] if 'stdout' in kwargs else self.stdout,
                stderr=kwargs['stderr'] if 'stderr' in kwargs else self.stderr,
                stdin=subprocess.PIPE,
            )
            stdout, stderr = self.process.communicate(input=stdin)
        except OSError as exc:
            raise CommandExecutionError(1, str(exc), self)

        if not fail_silently and (stderr or self.process.returncode != 0):
            raise CommandExecutionError(self.process.returncode, stderr or '', self)

        return True if ignore_output else self.handle_output(stdout)

    def validate_parameters(self):
        return all(k in self.parameters for k in self.required_parameters or [])

    def get_parameters(self):
        return self.parameters

    def get_command(self):
        command = self.command.format(**self.get_parameters())
        return shlex.split(str(command))

    def handle_output(self, output):
        return output

    @property
    def pid(self):
        return self.process.pid if self.process else None
