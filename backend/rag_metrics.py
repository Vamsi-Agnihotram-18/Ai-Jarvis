import math

def calculate_rag_metrics(retrieved_ids, relevant_id, k=3):
    """
    Calculate RAG evaluation metrics: Recall@K, Precision@K, MAP, MRR, nDCG@K.
    
    Args:
        retrieved_ids (list): List of document IDs retrieved by the system.
        relevant_id (str): The ID of the relevant document (ground truth).
        k (int): The number of top results to consider for metrics like Recall@K, Precision@K, nDCG@K.
    
    Returns:
        dict: Dictionary containing the calculated metrics.
    """
    # Ensure we only consider the top K retrieved IDs
    retrieved_ids = retrieved_ids[:k]
    
    # Binary relevance: 1 if the ID matches the relevant ID, 0 otherwise
    relevance = [1 if doc_id == relevant_id else 0 for doc_id in retrieved_ids]
    
    # Total number of relevant documents (in this case, 1 since we have only one relevant document)
    total_relevant = 1
    
    # Recall@K
    relevant_in_top_k = sum(relevance)
    recall_at_k = relevant_in_top_k / total_relevant if total_relevant > 0 else 0
    
    # Precision@K
    precision_at_k = relevant_in_top_k / k if k > 0 else 0
    
    # MAP (Average Precision for a single query)
    ap = 0
    relevant_count = 0
    for i, rel in enumerate(relevance):
        if rel == 1:
            relevant_count += 1
            ap += relevant_count / (i + 1)
    ap = ap / total_relevant if total_relevant > 0 else 0
    # Since we have only one query, MAP = AP
    map_score = ap
    
    # MRR
    mrr = 0
    for i, rel in enumerate(relevance):
        if rel == 1:
            mrr = 1 / (i + 1)
            break
    
    # nDCG@K
    # DCG: Discounted Cumulative Gain
    dcg = 0
    for i, rel in enumerate(relevance):
        dcg += rel / math.log2(i + 2)  # log2(i+2) because i starts at 0
    # IDCG: Ideal DCG (if the relevant document was at rank 1)
    idcg = 1 / math.log2(2)  # Only one relevant document, ideally at rank 1
    ndcg_at_k = dcg / idcg if idcg > 0 else 0
    
    return {
        "Recall@K": recall_at_k,
        "Precision@K": precision_at_k,
        "MAP": map_score,
        "MRR": mrr,
        "nDCG@K": ndcg_at_k
    }