import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, accuracy_score
from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch

# Load datasets
def load_asap_aes():
    # Assuming downloaded to data/asap_aes
    files = [f for f in os.listdir('data/asap_aes') if f.endswith('.csv')]
    df = pd.concat([pd.read_csv(f'data/asap_aes/{f}') for f in files])
    return df[['essay', 'domain1_score']].rename(columns={'domain1_score': 'score'})

def load_commonlit():
    df = pd.read_csv('data/commonlit/train.csv')
    return df[['excerpt', 'target']].rename(columns={'excerpt': 'essay', 'target': 'score'})

def load_bea2019():
    # Placeholder: load BEA data (grammar errors)
    # Assume CSV with 'sentence', 'label' (0/1 for grammatical)
    try:
        df = pd.read_csv('data/bea2019/processed.csv')
        return df
    except:
        return pd.DataFrame()

def preprocess_data(df, tokenizer, max_len=512):
    def tokenize_function(examples):
        return tokenizer(examples['essay'], truncation=True, padding='max_length', max_length=max_len)
    dataset = Dataset.from_pandas(df)
    tokenized = dataset.map(tokenize_function, batched=True)
    return tokenized

def train_model():
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=1)  # Regression for score

    # Load and combine datasets
    df_aes = load_asap_aes()
    df_commonlit = load_commonlit()
    df_combined = pd.concat([df_aes, df_commonlit], ignore_index=True)
    df_combined['score'] = df_combined['score'].astype(float)

    # Split
    train_df, val_df = train_test_split(df_combined, test_size=0.1)

    train_dataset = preprocess_data(train_df, tokenizer)
    val_dataset = preprocess_data(val_df, tokenizer)

    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=lambda p: {'mae': mean_absolute_error(p.label_ids, p.predictions.squeeze())},
    )

    trainer.train()
    trainer.save_model('./model')

if __name__ == '__main__':
    train_model()
