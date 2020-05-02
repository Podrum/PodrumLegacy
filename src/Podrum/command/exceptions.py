class CommandError(Exception):
    pass


class CommandExecutionError(CommandError):
    def __init__(self, code, stderr, command):
        lines = [str(line) for line in stderr.splitlines()]
        message = 'code: {0} stderr: {1}. Command: {2}'.format(
            code, ' '.join(lines), repr(command.get_command()))
        super().__init__(message)
        self.code = code
        self.stderr = stderr
        self.command = command


class CommandParameterError(CommandError):
    pass
