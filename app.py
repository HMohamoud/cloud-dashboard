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
    cpu_values = get_ec2_cpu('i-1234567890abcdef0')  # Replace with a real EC2 instance ID if available
    s3_size = get_s3_storage('my-demo-bucket')       # Replace with your actual S3 bucket name

    # === Render the dashboard template with live data ===
    return render_template('dashboard.html',
                           cpu_values=cpu_values,
                           s3_size=s3_size)

# === Run the Flask web app locally ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
