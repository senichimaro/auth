#!/bin/bash

curl --request POST \
  --url https://dev-72bpne5u.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"i5gAgOA382bJdSM0EraKLNXCdIF9lX9n","client_secret":"4XQcHljpuLpgaI632cYZjNIHb6QKkrJtcl6JVhweYsAwtHrNWQtQ6j2JV0STO9Mm","audience":"dev","grant_type":"client_credentials"}'