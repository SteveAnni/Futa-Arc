# Futa-Arc
Futa Arc is a Django REST API built with Django + Django REST framework. This API is consumed by a front end hosted on firebase (🌍 https://futa-arc.web.app )

# end points
### auths
##### register
🚩 https://futaarc.herokuapp.com/api/auth/register/ (POST)
#
👉 required fields
* username
* course
* password
* confirm_password
##### login
🚩 https://futaarc.herokuapp.com/api/auth/login/ (POST)
#
👉 required fields
* username
* password
##### logout
🚩 https://futaarc.herokuapp.com/api/auth/logout/ (POST)

### aggregate
🚩 https://futaarc.herokuapp.com/api/add-aggregate-list/ (POST)
👉 optional param
* q=5
🚩 https://futaarc.herokuapp.com/api/get-aggregate-list/ (GET)

### information
🚩 https://futaarc.herokuapp.com/api/info/ (GET)
