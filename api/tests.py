from django.test import TestCase

# Create your tests here.

#for facebook auth test
#curl -X POST -d "client_id=1407746366198745&client_secret=b5749840e10b13f1aa79d7d5a2f4077b&grant_type=password&username=&password=" https://stream-react-rimchang.c9users.io/api/auth/token

#for refresh token test
#curl -X POST -d "grant_type=convert_token&client_id=0GuIBshhVaS0ES3sj9gcnsijf2bhavBIRkoZnUVJ&client_secret=CyeDSwTRKi5BPfNLcwFX5Ex5YvSN2IuAqKzn9bIIzCLkhZakUWoEra5b8TZ8VwjnLxKiTxzPZ1McmZZ5gEQmLBBVJtY1C9oLwK5KwEZcxfpYF0BVMQb48c6lYbBW8w4k&backend=facebook&token=EAAUAVn4XU9kBAH8SyViB94631MVCveTrtdWZA8ZC8n1NS8Wcjk95yIMAW5MXanEwBGZBXZBXZBooTuKCUZBBekCyjWajbb8Bn0VsCqJUQGOWBkcoWx78U5g6VV2adjpf6OUgFZB1dHSrbo6O2lL1R4QdIWsoRc5QEe7WqyZBnYQdugZDZD" https://stream-react-rimchang.c9users.io/api/auth/convert-token

curl -X POST -d "client_id=1407746366198745&client_secret=b5749840e10b13f1aa79d7d5a2f4077b" https://stream-react-backend-2-rimchang.c9users.io/auth/login/facebo

curl -X POST -d "client_id=&client_secret=&grant_type=password&username=&password=" https://stream-react-backend-2-rimchang.c9users.io/auth/token 

curl -H "Authorization: Bearer facebook <backend_token>" https://stream-react-backend-2-rimchang.c9users.io/auth/login/facebook

curl -H "Authorization: Bearer <backend_name> <backend_token>" https://stream-react-rimchang.c9users.io/api/auth/token


# new
curl -X POST -d "client_id=ATeNL8NPdWv8Vkq7NnXzfsHSJqy05Mzp2H2jwG2b&client_secret=FkiQ8RWNaSxwtg9Y3goymhmfMtSVIHKaWTKSu10Z4G5aeuGt1JA52vJkep2XRikbdK9CuHRp0bd2ZacKJ6C8T5srIb6isnDt4MsmUgJUXvLuDYAfQ3Dn0xJgJ6cRCATY" https://stream-react-backend-2-rimchang.c9users.io/auth/login/facebook

curl -X POST -d "client_id=ATeNL8NPdWv8Vkq7NnXzfsHSJqy05Mzp2H2jwG2b&client_secret=FkiQ8RWNaSxwtg9Y3goymhmfMtSVIHKaWTKSu10Z4G5aeuGt1JA52vJkep2XRikbdK9CuHRp0bd2ZacKJ6C8T5srIb6isnDt4MsmUgJUXvLuDYAfQ3Dn0xJgJ6cRCATY&backend=facebook" https://stream-react-backend-2-rimchang.c9users.io/auth/authorize/

curl -X POST -d "client_id=ATeNL8NPdWv8Vkq7NnXzfsHSJqy05Mzp2H2jwG2b&client_secret=FkiQ8RWNaSxwtg9Y3goymhmfMtSVIHKaWTKSu10Z4G5aeuGt1JA52vJkep2XRikbdK9CuHRp0bd2ZacKJ6C8T5srIb6isnDt4MsmUgJUXvLuDYAfQ3Dn0xJgJ6cRCATY&backend=facebook" https://stream-react-backend-2-rimchang.c9users.io/auth/token

curl -c cookie.txt https://stream-react-backend-2-rimchang.c9users.io 

curl -I https://stream-react-backend-2-rimchang.c9users.io 

curl -X POST -d "grant_type=convert_token&client_id=HB9K6ZSX6uevgUkzpu5jGFN8aPKma23wLqqWeI6W&client_secret=GSmvkDHxwQPwufACzC6GOWvRCWNyiS6mDYVNXNJeJd81hgKOFdnKhyt5JrRxE75HEYzMqKHhbk7cBtwSolZdabIrh1tUvpVaZ3tyRaDBnLl52YWG9xgn2l5I8CbH6OMu&backend=facebook&token=EAAUDr3AkqHcBAJ1m2Xc67SvzhXnS8CSu9DJGNrxp6lpP1TYXYMn44v46APf1K5OKvYOuKHfubzyDXsymunrJI4FNax747VgAYhMgZBjYeZAP6q4XxgRqlcyC1ccAU0WqPwfMbOTIw8SasRVvqOhGdeyttxtzy9SxbUMkRkNwZDZD" https://stream-react-backend-2-rimchang.c9users.io/auth/convert-token

curl -X POST -d "grant_type=refresh_token&X5WjvIqNInTZACt9gO7EqZCKuIgVVVQDINvyK2XhXm1RlRlQZDZD" https://stream-react-backend-2-rimchang.c9users.io/auth/token