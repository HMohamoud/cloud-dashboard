from flask import Flask, render_template
from metrics import get_ec2_cpu, get_s3_storage  # functions from Step 2

app = Flask(__name__)

@app.route('/')
def dashboard():
    """
    Main route for the cloud monitoring dashboard.
    Fetches metrics from AWS (or simulated data if unavailable)
    and sends them to the HTML template.
    """
    # === Fetch cloud metrics ===
    cpu_values = get_ec2_cpu('i-0bbe24d43de3e4c53')  # I now Replaced it with a real EC2 instance ID
    s3_size = get_s3_storage('cloud-dashboard-hamza')       # Replace with your actual S3 bucket name

    # === Ensure safe defaults for the template ===
    cpu_values = cpu_values if cpu_values else [0]   # at least one value to avoid template errors
    s3_size = s3_size if s3_size else 0              # fallback in case bucket is empty

    # === Render the dashboard template with data ===
    return render_template(
        'dashboard.html',
        cpu_values=cpu_values,
        s3_size=s3_size
    )

# === Run the Flask app locally ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
