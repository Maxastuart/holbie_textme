/**
 * Copyright 2018, Google LLC
 * Licensed under the Apache License, Version 2.0 (the `License`);
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an `AS IS` BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// [START gae_python37_log]
'use strict';

$(document).ready(function () {
  console.log('hehe');
  $('#submit').click(() => {
    const data = {
      'studentId': $('#studentId').val(),
      'password': $('#password').val(),
      'apiKey': $('#apiKey').val(),
      'cohort': $('#cohort').val(),
      'sendText': $('#sendText').is(':checked'),
      'phone': $('#phone').val(),
      'nApi': $('#nApi').val(),
      'nSecret': $('#nSecret').val(),
      'sendEmail': $('#sendEmail').is(':checked')
    };
    fetch('http://127.0.0.1:8080/api/user', {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
  });
});
// window.addEventListener('load', function () {
//   const submitButton = document.getElementById('submit');
//   submitButton.on

//   console.log("Hello World!");

// });
// [END gae_python37_log]
