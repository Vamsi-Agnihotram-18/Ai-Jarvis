import os
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(_name_)

# Directory to save the models
MODEL_DIR = "./models/"
os.makedirs(MODEL_DIR, exist_ok=True)

MODELS_TO_DOWNLOAD = [
    "facebook/bart-large-cnn",  # BART model fine-tuned 
    "t5-small",                 # Smaller T5 model
    "google/pegasus-xsum"       # PEGASUS model fine-tuned 
]

def download_transformer_models():
    """
    Download and save transformer models and their tokenizers to the local models/ directory.
    """
    for model_name in MODELS_TO_DOWNLOAD:
        logger.info(f"Downloading model: {model_name}")
        try:
            # Download and save the model
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=MODEL_DIR)
            # Download and save the tokenizer
            tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=MODEL_DIR)
            
            # Save the model and tokenizer explicitly to the models/ directory
            model_save_path = os.path.join(MODEL_DIR, model_name.replace("/", "_"))
            tokenizer_save_path = os.path.join(MODEL_DIR, model_name.replace("/", "_"))
            
            model.save_pretrained(model_save_path)
            tokenizer.save_pretrained(tokenizer_save_path)
            
            logger.info(f"Successfully downloaded and saved {model_name} to {model_save_path}")
        except Exception as e:
            logger.error(f"Failed to download {model_name}: {str(e)}")

def summarize_with_transformer(text, model_name="facebook/bart-large-cnn", max_length=150, min_length=30):
    """
    Summarize the given text using a transformer model.
    
    Args:
        text (str): The input text to summarize.
        model_name (str): The name of the transformer model to use.
        max_length (int): Maximum length of the summary.
        min_length (int): Minimum length of the summary.
    
    Returns:
        str: The summarized text.
    """
    logger.info(f"Loading pipeline with model: {model_name}")
    
    # Use the local model if already downloaded, otherwise download it
    model_path = os.path.join(MODEL_DIR, model_name.replace("/", "_"))
    if os.path.exists(model_path):
        summarizer = pipeline("summarization", model=model_path, tokenizer=model_path)
    else:
        summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)
    
    logger.info(" text...")
    try:
        # Summarize the text
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        logger.info("Response given successfully.")
        return summary
    except Exception as e:
        logger.error(f"Response failure: {str(e)}")
        return "Error: Could not summarize the text."

if _name_ == "_main_":
    # Step 1: Download the transformer models
    download_transformer_models()
    
    # Step 2: Example text to summarize (simulating a bank statement)
    sample_text = """
    you are an expert rag agent help me summarize the input document
    """
    
    # Step 3: Summarize the sample text using facebook/bart-large-cnn
    summary = summarize_with_transformer(sample_text, model_name="facebook/bart-large-cnn")
    print("Original Text:")
    print(sample_text)
    print("\nSummary:")
    print(summary)
    
    # Note: To use other models, simply change the model_name parameter:
    # summary = summarize_with_transformer(sample_text, model_name="t5-small")
    # summary = summarize_with_transformer(sample_text, model_name="google/pegasus-xsum")