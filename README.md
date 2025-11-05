# ☁️ Cloud Resource Monitoring Dashboard

![Dashboard Screenshot](static/img/screenshot.png)

## Overview

The **Cloud Resource Monitoring Dashboard** is a real-time web application built with **Flask** that visualises AWS cloud resource metrics. It provides live monitoring of:

- **EC2 CPU utilisation** (last hour)
- **S3 bucket storage size**

This dashboard gives developers and cloud engineers an **instant overview** of their cloud infrastructure health and usage patterns.

---

## ✨ Key Features

- **📊 Live Metrics**: Fetches real-time data from **AWS CloudWatch** and **S3**
- **📱 Responsive Design**: Modern web interface using **Bootstrap 5**
- **🛡️ Fallback Simulation**: Provides simulated data when live metrics are unavailable
- **🔧 Extensible Architecture**: Easily add more AWS services or visualisations
- **⚡ Real-time Updates**: Automatic page refresh for latest metrics
- **🔒 Secure**: Configurable AWS credential management

---

## 🛠 Tech Stack

- **Backend**: Python 3.11, Flask
- **Cloud Services**: AWS EC2, S3, CloudWatch
- **Frontend**: HTML5, Bootstrap 5, JavaScript
- **AWS SDK**: Boto3 for Python
- **Infrastructure**: Configurable across AWS regions

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- AWS Account with appropriate permissions
- AWS CLI configured or IAM role

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/HMohamoud/cloud-dashboard.git
cd cloud-dashboard
