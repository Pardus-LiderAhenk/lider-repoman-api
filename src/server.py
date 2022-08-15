"""Importing flask"""
from flask import Flask
from flask_restful import abort, Api, Resource

# Get commands and command list
import commands
from commands import COMMAND_LIST

# Setup flask rest
app = Flask(__name__)
api = Api(app)


def if_command_exist(command_id):
    """Command check with command id."""
    if command_id in COMMAND_LIST:
        return True


def abort_command_doesnt_exist(command_id):
    """Abort request if command doesnt exist."""
    abort(404, message=f"Command {command_id} doesn't exist")


class RunCommand(Resource):
    """Flask Restfull class for running command."""

    def get(self, command_id):
        """Flask restfull standart get function."""
        if if_command_exist(command_id):
            getattr(commands, command_id)()
            return COMMAND_LIST[command_id]
        else:
            abort_command_doesnt_exist(command_id)


class CommandList(Resource):
    """Flask Restfull class for getting command list."""

    def get(self):
        """Flask restfull standart get function."""
        return COMMAND_LIST


# Setup the Api resource routing
api.add_resource(CommandList, '/commands')
api.add_resource(RunCommand, '/run/<command_id>')

if __name__ == '__main__':
    app.run(debug=True)
