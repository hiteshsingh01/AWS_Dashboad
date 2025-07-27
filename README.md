
# ☁️ AWS EC2 Automation Dashboard using Streamlit & Boto3

A powerful, web-based EC2 automation tool built with **Python**, **Streamlit**, and **Boto3**.  
Easily launch, start, stop, and terminate EC2 instances in the **Mumbai (ap-south-1)** region — all from a beautiful UI.

---

## 🚀 Features

✅ **Launch EC2 Instances**
- Auto or custom **Key Pair**
- Auto or custom **Security Group** (with SSH access)
- Set custom **Instance Name Tag**

✅ **Create Resources**
- Downloadable `.pem` file for Key Pairs
- SSH-enabled Security Groups

✅ **Manage EC2 Instances**
- View all running instances with details
- Start / Stop / Terminate selected instance


## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jayant77778/aws_ec2_dashboard.git
cd aws_ec2_dashboard
````

### 2. Install Python Packages

*No `requirements.txt` needed!*

```bash
pip install streamlit boto3
```

### 3. Configure AWS CLI

```bash
aws configure
```

* Region: `ap-south-1`
* Credentials: Your IAM user’s Access Key + Secret

---

## ▶️ Run the App

```bash
streamlit run aws_ec2_dashboard.py
```

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🔐 Required IAM Permissions

Your IAM user should have the following EC2 permissions:

* `ec2:RunInstances`
* `ec2:TerminateInstances`
* `ec2:StartInstances`
* `ec2:StopInstances`
* `ec2:DescribeInstances`
* `ec2:CreateKeyPair`
* `ec2:CreateSecurityGroup`
* `ec2:AuthorizeSecurityGroupIngress`
* `ec2:CreateTags`

---

## 🧰 Tech Stack

| Tool      | Use Case                |
| --------- | ----------------------- |
| Python    | Backend logic           |
| Streamlit | UI & web framework      |
| Boto3     | AWS SDK for Python      |
| AWS EC2   | Cloud compute instances |

---

## 📁 Project Structure

```
aws_ec2_dashboard/
├── aws_ec2_dashboard.py     # Streamlit App
└── README.md                # This file
```


## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Jayant Bhati**
🔗 [LinkedIn](https://www.linkedin.com/in/jayantbhati77/)
💻 [GitHub](https://github.com/jayant77778/aws_ec2_dashboard)

---

> Built with ❤️ to simplify DevOps and Cloud automation.


