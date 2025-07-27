# ☁️ AWS EC2 Automation Dashboard using Streamlit & Boto3

A powerful, web-based EC2 automation tool built with **Python**, **Streamlit**, and **Boto3**.
Easily launch, start, stop, and terminate EC2 instances in the **Mumbai (ap-south-1)** region — all from a beautiful UI.

---

## 🚀 Features

✅ **Launch EC2 Instances**

* Auto or custom **Key Pair**
* Auto or custom **Security Group** (with SSH access)
* Set custom **Instance Name Tag**

✅ **Create Resources**

* Downloadable `.pem` file for Key Pairs
* SSH-enabled Security Groups

✅ **Manage EC2 Instances**

* View all running instances with details
* Start / Stop / Terminate selected instance(s)

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hiteshsingh01/AWS_Dashboad.git
cd AWS_Dashboad
```

### 2. Install Python Packages

> No `requirements.txt` needed!

```bash
pip install streamlit boto3
```

### 3. Configure AWS CLI

```bash
aws configure
```

* Region: `ap-south-1`
* Credentials: Your IAM user’s Access Key & Secret Key

---

## ▶️ Run the App

```bash
streamlit run aws_ec2_dashboard.py
```

Open: [http://localhost:8501](http://localhost:8501)

---

## 🔐 Required IAM Permissions

Ensure your IAM user has these EC2 permissions:

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

| Tool      | Purpose              |
| --------- | -------------------- |
| Python    | Backend scripting    |
| Streamlit | Web app interface    |
| Boto3     | AWS automation       |
| AWS EC2   | Cloud infrastructure |

---

## 📁 Project Structure

```
AWS_Dashboad/
├── aws_ec2_dashboard.py     # Streamlit app
└── README.md                # Project documentation
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Hitesh Singh**
🔗 [LinkedIn – Hitesh Singh](https://www.linkedin.com/in/hiteshsingh01/)
💻 [GitHub – hiteshsingh01](https://github.com/hiteshsingh01)

---

> Built with ❤️ to simplify DevOps and AWS Cloud automation.

---

