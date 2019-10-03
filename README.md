curl -X POST -d "username=fyle&password=fyle@123" https://bankdetailapi.herokuapp.com/api/api-token-auth/

you will get a token as follows {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InR2aXNobnUiLCJleHAiOjE1NjcwOTUyNDksImVtYWlsIjoidmlzaG51LnRoZ0BnbWFpbC5jb20ifQ.6MHhQcjIY5w1QJPLQ3ywyqEjkoqfRWruDTbWkLY6iig"}

please use the new genrated token in the places <your-token>

this will give one object data curl -H "Authorization: JWT <your-token>" https://bankdetailapi.herokuapp.com/api/?ifsc=ABHY0065042

this will give list of object data curl -H "Authorization: JWT <your-token>" https://bankdetailapi.herokuapp.com/api/?name=ABHYUDAYA COOPERATIVE BANK LIMITED&city=MUMBAI&limit=10&offset=40
