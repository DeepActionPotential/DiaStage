from utils import load_artifacts
from ui import build_ui

# Load model and scaler
model, scaler = load_artifacts()

# Build Gradio UI
iface = build_ui(model, scaler)

if __name__ == "__main__":
    iface.launch()
