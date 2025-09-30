import gradio as gr
from utils import preprocess_input, predict_stage

def build_ui(model, scaler):
    inputs = [
        gr.Dropdown(choices=[0, 1], label="Gender (0 = Female, 1 = Male)"),
        gr.Number(label="Age"),
        gr.Number(label="Urea"),
        gr.Number(label="Creatinine (Cr)"),
        gr.Number(label="HbA1c"),
        gr.Number(label="Cholesterol"),
        gr.Number(label="Triglycerides (TG)"),
        gr.Number(label="HDL"),
        gr.Number(label="LDL"),
        gr.Number(label="VLDL"),
        gr.Number(label="BMI"),
    ]

    def inference(gender, age, urea, cr, hba1c, chol, tg, hdl, ldl, vldl, bmi):
        df = preprocess_input(gender, age, urea, cr, hba1c, chol, tg, hdl, ldl, vldl, bmi)
        stage = predict_stage(model, scaler, df)
        return f"Predicted Diabetes Stage: {stage}"

    iface = gr.Interface(
        fn=inference,
        inputs=inputs,
        outputs=gr.Textbox(label="Prediction"),
        title="Diabetes Stage Predictor",
        description="Enter patient details to predict diabetes stage (Non-diabetic, Diabetic, or Prediabetic)."
    )
    return iface
