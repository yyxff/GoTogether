# RideShareService
ECE 568 porject 1
## Team members

if you met any problems like expired token of gmail api, please feel free to contact us by duke email

### Junyan Li (NetID:jl1355)

### Yangfan Ye (NetID:yy465)

## Quick Start

```bash
cd ./docker-depoly
sudo docker-compose up
```

## User Guide

### homepage

- sign up by real email (you may check your spam)
- click `Ride`, you can...
    - `New Rides`: you can create a new ride order here
    - `My Rides`: you can view and revise all your related rides here
    - `All Shared Rides`: you can view all shared ride and join them here
- if you want to be a driver, you need to click `Register` and register your vehicle information first
- then you can click `Driver` in homepage
    - `My Car Info`: you can view and revise your car info here
    - `All Ride Requests`: you can view pending ride requests and accept them here
- if you want to sign out, click `Sign out`

### rider owner
- you can create a ride order with specific vehicle type, passengers number, destination or if you share it...
- you can view the order details by `Show`
- you can revise it before confirmed by `Revise`
- you can delete it before confirmed by `Delete`
- you can see the driver info once it was confirmed

### ride sharer
- you can join a pending ride 
- you can search by specific demands
- you can cancel your joining by `Cancel`
- you can view order details by `Show`
- you actions on orders will send email to the ride owner

### ride driver
- you can view order details by `Show`
- you can then confirm it by `Confirm`
- you can complete it by `Complete`
- you can cancel it by `Cancel`
- you actions on orders will send email to the ride owner and shares

## Features

### More Info:
- The owner and shares of ride order will receive emails when anyone's actions influenced the order

### Verification Code:
- In sign up, we will send a verification code to your email, and verify it then. So we can make sure you own the email

### Finite States Machine
- We define the status of an order as `pending`,`confirmed`,`complete`. We implemented it by FSM offered by `django-fsm`
- So the status of orders can only be changed in specific situations and to specific targets, avoiding illegal changes

### Log System
- We implemented a log system with `info`,`debug`,`danger` log files, you can check them in `./docker-deploy/web-app/logs`
- the `danger` file indicates danger behaviors like 'writing data into database'

## Lib requirments
```
Django>3.0
psycopg2==2.9.10
django-fsm==3.0.0
click==8.0.3
google-auth==2.38.0
google-auth-oauthlib==1.2.1
google-api-python-client==2.160.0
```
