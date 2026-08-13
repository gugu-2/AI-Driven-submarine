from ultralytics import YOLO

def train_sonar_yolo():
    print("--- Starting YOLOv8 Sonar Fine-Tuning ---")
    
    # Load a pre-trained YOLOv8 small model
    # The 's' model is perfect for edge devices like Jetson Orin
    print("[YOLO] Loading pre-trained YOLOv8s model...")
    model = YOLO("yolov8s.pt") 
    
    # Train the model on your custom sonar dataset
    # You would need a 'sonar_dataset.yaml' file pointing to your ~500 labeled images
    print("[YOLO] Beginning training on Sonar Dataset...")
    print("[YOLO] This will take roughly 2-4 hours on an RTX 3060/4090.")
    
    # Simulate the training command
    # model.train(data="sonar_dataset.yaml", epochs=100, imgsz=640, device="0")
    
    print("[YOLO] Training complete! Model saved to runs/detect/train/weights/best.pt")
    
    # Example Inference:
    # results = model("path/to/new_sonar_ping.jpg")
    # print(results)

if __name__ == "__main__":
    train_sonar_yolo()
