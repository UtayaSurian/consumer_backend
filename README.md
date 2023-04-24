# Consumer Backend

## The consumer backend acts as a RabbitMQ consumer that responsible to fecth incoming data from queue

The consumer.py is the main file (starting point) where it will keep listening 
on any available jobs in queue server. It will use worker basis instead
round robin. This is to ensure all consumers able to process jobs. All data will be stored inside
data.csv in the root folder. 

**Note:** The number of consumers is depend on how many consumer containers are running or consumer.py scripts
are running at the same time. As per the requirement, only one consumer container
is required for this assessment.
