import streamlit as st
import boto3
from datetime import datetime

# ---------- AWS Setup ----------
REGION = "ap-south-1"
ec2 = boto3.client("ec2", region_name=REGION)

def get_amazon_linux_ami():
    return "ami-0a7cf821b91bcccbc"  # Amazon Linux 2 in Mumbai

def generate_name(prefix):
    return f"{prefix}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

# ---------- AWS Operations ----------
def create_key_pair(key_name):
    try:
        key = ec2.create_key_pair(KeyName=key_name)
        st.success(f"✅ Key Pair Created: `{key_name}`")
        st.download_button("⬇️ Download PEM File", key["KeyMaterial"], file_name=f"{key_name}.pem")
        return key_name
    except Exception as e:
        st.error(f"❌ Key Pair Error: {e}")
        return None

def create_security_group(group_name):
    try:
        res = ec2.create_security_group(GroupName=group_name, Description="Streamlit Auto SG")
        sg_id = res["GroupId"]
        ec2.authorize_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[{
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
            }]
        )
        st.success(f"✅ Security Group Created: `{sg_id}`")
        return sg_id
    except Exception as e:
        st.error(f"❌ Security Group Error: {e}")
        return None

def launch_instance(key_name, sg_id, instance_name):
    try:
        res = ec2.run_instances(
            ImageId=get_amazon_linux_ami(),
            InstanceType="t2.micro",
            KeyName=key_name,
            SecurityGroupIds=[sg_id],
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Name', 'Value': instance_name or generate_name("EC2")}]
                }
            ]
        )
        instance_id = res["Instances"][0]["InstanceId"]
        st.success(f"🚀 Instance Launched: `{instance_id}`")
        return instance_id
    except Exception as e:
        st.error(f"❌ Launch Error: {e}")
        return None

def list_instances():
    instances = ec2.describe_instances()
    data = []
    for r in instances["Reservations"]:
        for i in r["Instances"]:
            data.append({
                "ID": i["InstanceId"],
                "Type": i["InstanceType"],
                "State": i["State"]["Name"],
                "IP": i.get("PublicIpAddress", "-"),
                "Name": next((t["Value"] for t in i.get("Tags", []) if t["Key"] == "Name"), "No Name")
            })
    return data

def start_instance(instance_id):
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        st.success(f"🔄 Started: `{instance_id}`")
    except Exception as e:
        st.error(f"❌ Start Error: {e}")

def stop_instance(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        st.warning(f"🛑 Stopped: `{instance_id}`")
    except Exception as e:
        st.error(f"❌ Stop Error: {e}")

def terminate_instance(instance_id):
    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        st.error(f"🔥 Terminated: `{instance_id}`")
    except Exception as e:
        st.error(f"❌ Termination Error: {e}")

# ---------- Streamlit UI ----------
st.set_page_config(page_title="AWS EC2 Dashboard", layout="centered")
st.markdown("<h1 style='text-align:center;'>☁️ AWS EC2 Automation Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([
    "🚀 Launch Instance", "🛠️ Create Resources",
    "📋 View Instances", "⚙️ Manage Instance"
])

# ---------------- Tab 1: Launch EC2 ----------------
with tab1:
    st.subheader("🚀 Launch a New EC2 Instance")

    col1, col2 = st.columns(2)
    with col1:
        key_input = st.text_input("🔑 Key Pair Name (Leave blank to auto-create)")
    with col2:
        sg_input = st.text_input("🛡️ Security Group ID (Leave blank to auto-create)")

    instance_name = st.text_input("📝 Instance Name (for AWS Tag)")

    if st.button("Launch EC2 Instance"):
        if not key_input:
            key_input = generate_name("auto-key")
            create_key_pair(key_input)

        if not sg_input:
            sg_input = create_security_group(generate_name("auto-sg"))

        if key_input and sg_input:
            launch_instance(key_input, sg_input, instance_name)

# ---------------- Tab 2: Create Key/SG ----------------
with tab2:
    st.subheader("🛠️ Create AWS Resources")

    with st.expander("➕ Create Key Pair"):
        key_name = st.text_input("Enter Key Pair Name")
        if st.button("Create Key Pair"):
            if key_name:
                create_key_pair(key_name)

    with st.expander("➕ Create Security Group"):
        sg_name = st.text_input("Enter Security Group Name")
        if st.button("Create Security Group"):
            if sg_name:
                create_security_group(sg_name)

# ---------------- Tab 3: List Instances ----------------
with tab3:
    st.subheader("📋 List of EC2 Instances")

    instance_data = list_instances()
    if instance_data:
        for inst in instance_data:
            st.markdown(f"""
                🔹 **ID:** `{inst['ID']}`  
                💻 **Type:** `{inst['Type']}`  
                🌐 **State:** `{inst['State']}`  
                📡 **Public IP:** `{inst['IP']}`  
                🏷️ **Name:** `{inst['Name']}`
                ---
            """)
    else:
        st.info("No EC2 instances found.")

# ---------------- Tab 4: Manage Instances ----------------
with tab4:
    st.subheader("⚙️ Start / Stop / Terminate EC2 Instance")

    instance_ids = [i["ID"] for i in list_instances()]
    if instance_ids:
        selected_id = st.selectbox("Select Instance ID", instance_ids)

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("▶️ Start"):
                start_instance(selected_id)
        with col2:
            if st.button("⏸️ Stop"):
                stop_instance(selected_id)
        with col3:
            if st.button("💀 Terminate"):
                terminate_instance(selected_id)
    else:
        st.warning("No instances available to manage.")
