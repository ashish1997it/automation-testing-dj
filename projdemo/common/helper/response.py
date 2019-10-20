from rest_framework import status
from rest_framework.response import Response


class ResponseView:

    # Return payload from validation / services / jobs or other task's
    def api_status(status_code=200, status_message='success', message=None, data=None):
        response_format = {
            'status_code': status_code,
            'status': status_message,  # error / success / exception
            'message': message,  # Message in list format
            'data': data
        }
        return response_format

    # Return response from view
    def api_response(status_code=200, status_message='success', message=[], data=None):
        response_format = {
            'status_code': status_code,
            'status': status_message,  # error / success / exception
            'message': message,  # Message in list format
            'data': data
        }
        return Response(response_format, status_code)

    # Return response from exception
    def api_exception_response(status_code=400, status_message='error', message=[], data=None):
        response_format = {
            'status_code': status_code,
            'status': status_message,
            'message': message.append('Something went wrong!'),
            'data': data
        }
        return Response(response_format, status_code)

    def api_method_response(method=None, resource=None):
        ret = {}

        if 'GET' == method:
            status_code = 200
            msg = resource + ' data found.'
        elif 'POST' == method:
            status_code = 201
            msg = resource + ' created successfully.'
        elif 'PUT' == method:
            status_code = 205
            msg = resource + ' data updated successfully.'
        elif 'PATCH' == method:
            status_code = 206
            msg = resource + ' data updated successfully.'
        elif 'DELETE' == method:
            status_code = 204
            msg = resource + ' deleted successfully.'
        else:
            status_code = 200
            msg = 'Unknown method!'

        ret.update({'status_code': status_code})
        ret.update({'msg': msg})

        return ret
