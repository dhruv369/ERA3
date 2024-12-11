import streamlit as st
import json
import matplotlib.pyplot as plt
import time
import os

def load_training_logs():
    logs_path = os.path.join('results', 'training_logs.json')
    if os.path.exists(logs_path):
        with open(logs_path, 'r') as f:
            return json.load(f)
    return []

def plot_metrics(logs):
    if not logs:
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    epochs = [log['epoch'] for log in logs]
    
    # Plot training and validation loss
    ax1.plot(epochs, [log['loss'] for log in logs], label='Training Loss')
    ax1.plot(epochs, [log['val_loss'] for log in logs], label='Validation Loss')
    ax1.set_title('Model Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.legend()
    
    # Plot training and validation accuracy
    ax2.plot(epochs, [log['accuracy'] for log in logs], label='Training Accuracy')
    ax2.plot(epochs, [log['val_accuracy'] for log in logs], label='Validation Accuracy')
    ax2.set_title('Model Accuracy')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.legend()
    
    return fig

def main():
    st.title('MNIST Model Training Logs')
    
    # Initialize session state
    if 'last_update' not in st.session_state:
        st.session_state.last_update = None
    
    # Create placeholder for the plots
    plot_placeholder = st.empty()
    metrics_placeholder = st.empty()
    
    while True:
        logs = load_training_logs()
        
        if logs:
            # Update plots
            fig = plot_metrics(logs)
            if fig:
                plot_placeholder.pyplot(fig)
                plt.close(fig)
            
            # Display latest metrics
            latest = logs[-1]
            metrics_placeholder.markdown(f"""
            ### Latest Metrics (Epoch {latest['epoch']})
            - Training Loss: {latest['loss']:.4f}
            - Training Accuracy: {latest['accuracy']:.4f}
            - Validation Loss: {latest['val_loss']:.4f}
            - Validation Accuracy: {latest['val_accuracy']:.4f}
            - Timestamp: {latest['timestamp']}
            """)
        
        time.sleep(1)  # Update every second

if __name__ == '__main__':
    main() 