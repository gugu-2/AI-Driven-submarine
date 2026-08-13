import requests
import json
import base64

class LlamaVisionCommander:
    def __init__(self):
        # Assumes Ollama is running locally on the Jetson/PC
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "llama3.2-vision"
        print(f"[Llama Vision] Initialized. Connecting to local Ollama ({self.model})...")

    def analyze_anomaly(self, image_path, mission_context):
        """
        Sends an image of an anomaly and the mission context to Llama 3 Vision.
        Requires ZERO training. Just good prompting.
        """
        print(f"[Llama Vision] Encoding image: {image_path}")
        
        # In a real script, you'd read and encode the image
        # with open(image_path, "rb") as image_file:
        #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        encoded_string = "mock_base64_image_data"
        
        prompt = (
            f"You are the tactical AI commander of a military autonomous submarine. "
            f"Mission context: {mission_context}. "
            f"The sonar/camera has detected an anomaly. Analyze this image. "
            f"Is this a threat, biological (marine life), or infrastructure? What should the submarine do?"
        )
        
        print("[Llama Vision] Sending prompt to local LLM...")
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "images": [encoded_string],
            "stream": False
        }
        
        # Mocking the request to Ollama
        # response = requests.post(self.ollama_url, json=payload)
        # result = response.json()['response']
        
        # Mock response
        result = (
            "Based on the acoustic shadow and metallic geometry in the image, this appears to be "
            "unexploded ordnance (UXO) or a submerged mine. This is a severe threat. "
            "RECOMMENDATION: Immediately halt forward progress, maintain a 50-meter standoff distance, "
            "and alert HQ via acoustic modem."
        )
        
        print(f"\n[Llama Vision] RESPONSE:\n{result}\n")
        return result

if __name__ == "__main__":
    commander = LlamaVisionCommander()
    commander.analyze_anomaly("mock_sonar_anomaly.jpg", "Patrolling sector 7G for enemy assets.")
