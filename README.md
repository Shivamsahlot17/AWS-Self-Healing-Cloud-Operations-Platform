# AWS Self-Healing Cloud Operations Platform

## 📌 Overview

The AWS Self-Healing Cloud Operations Platform is an automated monitoring and recovery system built using AWS services. It continuously monitors EC2 instance health and resource utilization, sends notifications when thresholds are breached, automatically recovers stopped instances, schedules instance start/stop operations for cost optimization, and performs automated EBS backups for disaster recovery.

---

## 🚀 Features

* 📊 Real-time monitoring using CloudWatch Agent
* 🚨 CPU, Memory, and Disk utilization alarms
* 📧 Email notifications using Amazon SNS
* 🔄 Automatic EC2 recovery using Lambda and EventBridge
* ⏰ Scheduled instance start and stop for cost optimization
* 📈 CloudWatch Dashboard for centralized monitoring
* 💾 Automated EBS snapshot backups using Lifecycle Manager
* 🛠 Event-driven architecture for improved reliability

---



## 🛠 AWS Services Used

* Amazon EC2
* Amazon CloudWatch
* CloudWatch Agent
* Amazon SNS
* AWS Lambda
* Amazon EventBridge
* EventBridge Scheduler
* AWS IAM
* Amazon EBS
* EBS Lifecycle Manager

---

## ⚙ Workflow

### Monitoring

CloudWatch Agent collects:

* CPU metrics
* Memory metrics
* Disk metrics
* Network metrics

### Alerts

CloudWatch Alarms monitor:

* CPU Utilization
* Memory Usage
* Disk Usage

If thresholds are crossed:

```
CloudWatch Alarm
       ↓
SNS Topic
       ↓
Email Notification
```

### Self-Healing

If the EC2 instance stops unexpectedly:

```
EC2 Stopped
      ↓
EventBridge Rule
      ↓
SelfHealingEC2 Lambda
      ↓
EC2 Started Automatically
```

### Cost Optimization

Using EventBridge Scheduler:

```
08:00 AM → Start Instance
11:00 PM → Stop Instance
```

### Backup and Recovery

Daily EBS snapshots are automatically created and retained for seven days.

---


## 🎯 Key Concepts Demonstrated

* Cloud Monitoring
* Event-Driven Architecture
* Infrastructure Automation
* Self-Healing Systems
* Cost Optimization
* Backup and Disaster Recovery
* Serverless Computing
* Cloud Operations

---

## 🔮 Future Enhancements

* Least Privilege IAM Policies
* Multi-instance Auto Recovery
* Slack Notifications
* CloudWatch Logs Integration
* Auto Scaling Integration
* Infrastructure as Code using Terraform

---

## 👨‍💻 Author

**Shivam Sahlot**

B.Tech CSE (CSIT) | KIET Group of Institutions

Interested in Cloud Computing, AWS, DevOps and System Design.
