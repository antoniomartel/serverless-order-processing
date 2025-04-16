# Serverless Order Processing System AWS Architecture

This project demonstrates a fully serverless, event-driven architecture for processing customer orders on AWS. It is designed to be scalable, asynchronous, and suitable for real-world backend systems.

## Architecture Overview

```plaintext
[Static Frontend (S3)]
        
[API Gateway - POST /order]
        
[AWS Lambda (submit_order)]
        
[AWS SQS Queue]
        
[AWS Lambda (process_order)]
        
[DynamoDB + (optional) SNS notification]
```

## Components Used

- **Amazon S3** - Static frontend hosting (HTML form)
- **API Gateway** - Entry point for order submissions
- **Lambda (submit_order)** - Validates and queues orders
- **SQS** - Stores incoming orders asynchronously
- **Lambda (process_order)** - Processes and stores order in DynamoDB
- **DynamoDB** - Persistent store for orders
- **CloudWatch** - Logs and monitoring

## Folder Structure

```plaintext

lambdas/
     submit_order.py
     process_order.py
static/
     index.html
architecture.png
README.md
```

## How to Test

1. Open the HTML frontend in a browser (from S3 static website)
2. Fill out the form and submit an order
3. Check:
   - CloudWatch logs of both Lambdas
   - SQS queue receives the message
   - DynamoDB table contains the processed order
   - (Optional) Notification email received

## Lessons & Takeaways

- How to decouple services using queues
- Handling async workflows in AWS
- CORS setup and frontend-backend integration
- Role permissions and cross-service triggers in practice

## Author

Antonio Martel  
[LinkedIn](https://www.linkedin.com/in/antoniomartel) - [Blog](https://www.antoniomartel.com)
