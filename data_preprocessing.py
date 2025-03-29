import json
import os

def load_json(file_path):
    """Loads the JSON file from the specified path."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def clean_data(data):
    """Cleans the dataset, ensuring each entry has valid 'prompt' and 'response'."""
    cleaned_data = []
    for entry in data:
        if "prompt" in entry and "response" in entry:
            prompt = entry["prompt"]
            response = entry["response"]
            if prompt.strip() and response.strip():  # Remove empty prompts/responses
                cleaned_data.append({"prompt": prompt, "response": response})
    return cleaned_data

def preprocess_for_training(cleaned_data):
    """Preprocesses the data for model fine-tuning."""
    preprocessed_data = []
    for entry in cleaned_data:
        input_text = entry["prompt"]
        output_text = entry["response"]
        preprocessed_data.append({
            "input": input_text,
            "output": output_text
        })
    return preprocessed_data

def save_preprocessed_data(preprocessed_data, output_path):
    """Saves the preprocessed data to a new JSON file."""
    with open(output_path, "w") as outfile:
        json.dump(preprocessed_data, outfile, indent=4)

def run_preprocessing(input_file, output_file):
    """Runs the entire preprocessing pipeline."""
    data = load_json(input_file)
    cleaned_data = clean_data(data)
    preprocessed_data = preprocess_for_training(cleaned_data)
    save_preprocessed_data(preprocessed_data, output_file)

if __name__ == "__main__":
    run_preprocessing("rawDATA.json", "processed_data.json")