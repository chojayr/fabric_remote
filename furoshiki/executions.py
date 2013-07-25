#This is a crappy in-memory database. Maybe replace this with a real database someday.

MAX_EXECUTIONS = 50

current_execution_index = 0
executions = {}

class ExecutionStream(object):
    def __init__(self, ps_handle, stream):
        self._ps_handle = ps_handle
        self._stream = stream
        self._output_buffer = ""
        self._results_buffer = []
        self._finished = False

    def output(self):
        if self._finished:
            yield self._output_buffer
            return
        for line in self._stream:
            if "output" in line:
                self._output_buffer += line["output"]
                yield line["output"]
            elif "results" in line:
                self._results_buffer.append(line["results"])
        self._finished = True

    def results(self):
        if self._ps_handle.is_alive():
            return {"finished": False}
        #Consume generator so we can get the results
        [x for x in self.output()]
        return {
            "finished": True,
            "results": self._results_buffer,
        }

def add(tasks, ps_handle, output_stream):
    global executions
    global current_execution_index
    executions[current_execution_index] = {
        "tasks": tasks,
        "stream": ExecutionStream(ps_handle, output_stream),
    }
    if current_execution_index > MAX_EXECUTIONS:
        print "deleting old execution # {0}".format(current_execution_index - MAX_EXECUTIONS)
        del executions[current_execution_index - MAX_EXECUTIONS]
    current_execution_index += 1
    return current_execution_index -1

def get(execution_id):
    return executions[execution_id]

