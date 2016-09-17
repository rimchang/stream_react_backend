from django.test import TestCase

# Create your tests here.

#for facebook auth test
#curl -X POST -d "client_id=1407746366198745&client_secret=b5749840e10b13f1aa79d7d5a2f4077b&grant_type=password&username=&password=" https://stream-react-rimchang.c9users.io/api/auth/token

#for refresh token test
#curl -X POST -d "grant_type=convert_token&client_id=0GuIBshhVaS0ES3sj9gcnsijf2bhavBIRkoZnUVJ&client_secret=CyeDSwTRKi5BPfNLcwFX5Ex5YvSN2IuAqKzn9bIIzCLkhZakUWoEra5b8TZ8VwjnLxKiTxzPZ1McmZZ5gEQmLBBVJtY1C9oLwK5KwEZcxfpYF0BVMQb48c6lYbBW8w4k&backend=facebook&token=EAAUAVn4XU9kBAH8SyViB94631MVCveTrtdWZA8ZC8n1NS8Wcjk95yIMAW5MXanEwBGZBXZBXZBooTuKCUZBBekCyjWajbb8Bn0VsCqJUQGOWBkcoWx78U5g6VV2adjpf6OUgFZB1dHSrbo6O2lL1R4QdIWsoRc5QEe7WqyZBnYQdugZDZD" https://stream-react-rimchang.c9users.io/api/auth/convert-token

curl -X POST -d "client_id=0GuIBshhVaS0ES3sj9gcnsijf2bhavBIRkoZnUVJ&client_secret=CyeDSwTRKi5BPfNLcwFX5Ex5YvSN2IuAqKzn9bIIzCLkhZakUWoEra5b8TZ8VwjnLxKiTxzPZ1McmZZ5gEQmLBBVJtY1C9oLwK5KwEZcxfpYF0BVMQb48c6lYbBW8w4k&grant_type=password&username=rjs&password=ckdrms11" https://stream-react-rimchang.c9users.io/api/auth/token


curl -H "Authorization: Bearer facebook <backend_token>" https://stream-react-rimchang.c9users.io/api/auth/token

curl -H "Authorization: Bearer <backend_name> <backend_token>" https://stream-react-rimchang.c9users.io/api/auth/token
