import csv
import inspect
import json
import os
import re
from rest_framework.test import APITestCase
from texttable import Texttable
from django.contrib.auth.models import User


class TestLoginUser(APITestCase):

    @classmethod
    def setUp(cls):
        username = 'ashish'
        password = 'qwerty'
        User.objects.create_user(username=username, password=password)

    @staticmethod
    def api_url():
        return 'http://localhost:8001/'

    def test_login_user(self):
        api_url = 'login/api/v1/login-user/'
        url = self.api_url() + api_url
        print('POST, URL = ', url)

        table_list = []
        table_list.append(['Test Case ID', 'Test Scenario', 'Test Case', 'Test Suite', 'Method', 'URL', 'Test Data',
                           'Expected Result', 'Actual Result', 'Status'])

        # Set API request params
        params = {
            'username': 'ashish',
            'password': 'qwerty'
        }
        response = self.client.post(url, data=params)
        # print('response-status-code = ', response.status_code)
        api_response_byte = response.content
        api_response_utf8 = api_response_byte.decode('utf8').replace("'", '"')
        api_response_json = json.loads(api_response_utf8)
        # print('api_response_json =', api_response_json)

        # Login user with valid username & password.
        expected_api_status_code = 200
        actual_api_status_code = response.status_code
        status_code = True if expected_api_status_code == actual_api_status_code else False
        self.assertEqual(expected_api_status_code, actual_api_status_code)
        status = 'PASS' if status_code else 'FAIL'
        table_list.append(['1.1.1', 'Login user module.',
                           'Login user with valid username & password.', 'Check api response status code.',
                           'POST', api_url, 'params', expected_api_status_code, actual_api_status_code, status])

        expected_api_status_message = 'success'
        actual_api_status_message = api_response_json['status']
        api_status = True if expected_api_status_message == actual_api_status_message else False
        self.assertEqual(expected_api_status_message, actual_api_status_message)
        status = 'PASS' if api_status else 'FAIL'
        table_list.append(['1.1.2', 'Login user module.',
                           'Login user with valid username & password.', 'Check api response status.',
                           'POST', api_url, 'params', expected_api_status_message, actual_api_status_message, status])

        expected_api_message = ["You are successfully logged in."]
        actual_api_message = api_response_json['message']
        api_message = True if expected_api_message == actual_api_message else False
        self.assertEqual(expected_api_message, actual_api_message)
        status = 'PASS' if api_message else 'FAIL'
        table_list.append(['1.1.3', 'Login user module.',
                           'Login user with valid username & password.', 'Check api response message.',
                           'POST', api_url, 'params', expected_api_message, actual_api_message, status])

        token = api_response_json['data'][0]['token']
        expected_api_data = [{'token': token}]
        actual_api_data = api_response_json['data']
        api_data = True if expected_api_data == actual_api_data else False
        self.assertEqual(expected_api_data, actual_api_data)
        status = 'PASS' if api_data else 'FAIL'
        table_list.append(['1.1.4', 'Login user module.',
                           'Login user with valid username & password.', 'Check api response data.',
                           'POST', api_url, 'params', expected_api_data, actual_api_data, status])

        # Set API request params
        params = {
            'username': 'ashish_2',
            'password': 'qwerty'
        }
        response = self.client.post(url, data=params)
        # print('response-status-code = ', response.status_code)
        api_response_byte = response.content
        api_response_utf8 = api_response_byte.decode('utf8').replace("'", '"')
        api_response_json = json.loads(api_response_utf8)
        # print('api_response_json =', api_response_json)

        # Login user with invalid username & password.
        expected_api_status_code = 404
        actual_api_status_code = response.status_code
        status_code = True if expected_api_status_code == actual_api_status_code else False
        self.assertEqual(expected_api_status_code, actual_api_status_code)
        status = 'PASS' if status_code else 'FAIL'
        table_list.append(['1.2.1', 'Login user module.',
                           'Login user with invalid username & password.', 'Check api response status code.',
                           'POST', api_url, 'params', expected_api_status_code, actual_api_status_code, status])

        expected_api_status_message = 'error'
        actual_api_status_message = api_response_json['status']
        api_status = True if expected_api_status_message == actual_api_status_message else False
        self.assertEqual(expected_api_status_message, actual_api_status_message)
        status = 'PASS' if api_status else 'FAIL'
        table_list.append(['1.2.2', 'Login user module.',
                           'Login user with invalid username & password.', 'Check api response status.',
                           'POST', api_url, 'params', expected_api_status_message, actual_api_status_message, status])

        expected_api_message = ["Invalid credentials!"]
        actual_api_message = api_response_json['message']
        api_message = True if expected_api_message == actual_api_message else False
        self.assertEqual(expected_api_message, actual_api_message)
        status = 'PASS' if api_message else 'FAIL'
        table_list.append(['1.2.3', 'Login user module.',
                           'Login user with invalid username & password.', 'Check api response message.',
                           'POST', api_url, 'params', expected_api_message, actual_api_message, status])

        expected_api_data = None
        actual_api_data = api_response_json['data']
        api_data = True if expected_api_data == actual_api_data else False
        self.assertEqual(expected_api_data, actual_api_data)
        status = 'PASS' if api_data else 'FAIL'
        table_list.append(['1.2.4', 'Login user module.',
                           'Login user with invalid username & password.', 'Check api response data.',
                           'POST', api_url, 'params', expected_api_data, actual_api_data, status])

        # Set API request params
        params = {
            'username': 'ashish'
        }
        response = self.client.post(url, data=params)
        # print('response-status-code = ', response.status_code)
        api_response_byte = response.content
        api_response_utf8 = api_response_byte.decode('utf8').replace("'", '"')
        api_response_json = json.loads(api_response_utf8)
        # print('api_response_json =', api_response_json)

        # Login user with username & without password.
        expected_api_status_code = 400
        actual_api_status_code = response.status_code
        status_code = True if expected_api_status_code == actual_api_status_code else False
        self.assertEqual(expected_api_status_code, actual_api_status_code)
        status = 'PASS' if status_code else 'FAIL'
        table_list.append(['1.3.1', 'Login user module.',
                           'Login user with username & without password.', 'Check api response status code.',
                           'POST', api_url, 'params', expected_api_status_code, actual_api_status_code, status])

        expected_api_status_message = 'error'
        actual_api_status_message = api_response_json['status']
        api_status = True if expected_api_status_message == actual_api_status_message else False
        self.assertEqual(expected_api_status_message, actual_api_status_message)
        status = 'PASS' if api_status else 'FAIL'
        table_list.append(['1.3.2', 'Login user module.',
                           'Login user with username & without password.', 'Check api response status.',
                           'POST', api_url, 'params', expected_api_status_message, actual_api_status_message, status])

        expected_api_message = ["Please provide both username and password!"]
        actual_api_message = api_response_json['message']
        api_message = True if expected_api_message == actual_api_message else False
        self.assertEqual(expected_api_message, actual_api_message)
        status = 'PASS' if api_message else 'FAIL'
        table_list.append(['1.3.3', 'Login user module.',
                           'Login user with username & without password.', 'Check api response message.',
                           'POST', api_url, 'params', expected_api_message, actual_api_message, status])

        expected_api_data = None
        actual_api_data = api_response_json['data']
        api_data = True if expected_api_data == actual_api_data else False
        self.assertEqual(expected_api_data, actual_api_data)
        status = 'PASS' if api_data else 'FAIL'
        table_list.append(['1.3.4', 'Login user module.',
                           'Login user with username & without password.', 'Check api response data.',
                           'POST', api_url, 'params', expected_api_data, actual_api_data, status])

        # Draw tables in CMD prompt
        draw_table = Texttable()
        draw_table.add_rows(table_list)
        print(draw_table.draw())

        filepath = re.sub(r'[.]', '/', __package__)
        directory = 'media/testcase/' + filepath
        class_name = __class__.__name__
        function_name = inspect.stack()[0][3]
        filename = directory + '/TestCaseReport_' + class_name + '.csv'
        print('filename = ', filename)

        # Create dir if not present
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create TestCaseReport_***.csv file
        if table_list:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(table_list)
