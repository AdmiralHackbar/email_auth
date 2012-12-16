email_auth
==========

A proof-of-concept Django webapp where user authentication is implemented by sending a user with an email that contains a login link. Instead of requiring users to provide a username and password, users must only provide a username and email address to register.

### TODO:
1, Remove login tokens as they are redeemed.

2, Only redeem a token if it is used within 10 minutes of creation.

3, Record the user's ip-address when the token is created. Only redeem the token if the user's ip address matches the ip-address when created.

4, Drop a cookie tied to the token when the token is created. Only redeem the token if this cookie is present.
