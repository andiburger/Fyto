#!/bin/bash

# Get the directory of the current script
PROJECT_DIR="$(dirname "$(realpath "$0")")"
VENV_DIR="$PROJECT_DIR/venv"
SERVICE_NAME="smart_plant_pot.service"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME"

# Check if the service already exists
if systemctl list-units --full --all | grep -Fq "$SERVICE_NAME"; then
  echo "Service $SERVICE_NAME is already installed."
else
  # Create virtual environment if it doesn't exist
  if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
  fi

  # Activate virtual environment and install dependencies
  echo "Activating virtual environment and installing dependencies..."
  source "$VENV_DIR/bin/activate"
  pip install -r "$PROJECT_DIR/requirements.txt"

  # Ensure the Python script has the necessary permissions
  chmod +x "$PROJECT_DIR/main.py"

  # Create systemd service file
  echo "Creating systemd service file..."

  cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=Smart Plant Pot Service
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$PROJECT_DIR
ExecStart=$VENV_DIR/bin/python $PROJECT_DIR/main.py
Restart=always
Environment=PATH=$VENV_DIR/bin:$PATH
Environment=VIRTUAL_ENV=$VENV_DIR
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

  # Set proper permissions for the service file
  chmod 644 "$SERVICE_FILE"

  # Reload systemd daemon to recognize the new service
  echo "Reloading systemd daemon..."
  sudo systemctl daemon-reload

  # Enable the service to start on boot
  echo "Enabling service to start on boot..."
  sudo systemctl enable "$SERVICE_NAME"

  # Start the service
  echo "Starting the service..."
  sudo systemctl start "$SERVICE_NAME"

  echo "Installation and service setup complete."
fi