import pandas as pd
import numpy as np
from latent_state_model import LatentStateModel
import argparse
import joblib  # for saving/loading models

def load_data(file_path):
    """
    Load and preprocess data for HMM training.
    
    Expected CSV columns: participant_id, date, features...
    """
    df = pd.read_csv(file_path, parse_dates=['date'])
    
    features = ['fasting_glucose', 'cholesterol_total', 'hdl', 'ldl', 'triglycerides']
    
    # Sort by participant and date to maintain time order
    df = df.sort_values(['participant_id', 'date'])
    
    # Extract feature matrix
    X = df[features].values
    
    return X, df

def main(args):
    # Load data
    X, df = load_data(args.data_file)
    
    # Initialize model
    model = LatentStateModel(n_states=args.n_states, n_iter=args.n_iter)
    
    # Train
    print("Training HMM...")
    model.fit(X)
    
    # Predict latent states
    states = model.predict_states(X)
    
    # Append states to dataframe for inspection or further use
    df['latent_state'] = states
    
    # Save model
    if args.save_model:
        joblib.dump(model, args.save_model)
        print(f"Model saved to {args.save_model}")
    
    # Save annotated data with states
    if args.save_states:
        df.to_csv(args.save_states, index=False)
        print(f"Data with latent states saved to {args.save_states}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train HMM on health data')
    parser.add_argument('--data_file', type=str, required=True, help='Path to input CSV data')
    parser.add_argument('--n_states', type=int, default=3, help='Number of latent states')
    parser.add_argument('--n_iter', type=int, default=100, help='Number of training iterations')
    parser.add_argument('--save_model', type=str, help='Path to save trained model (joblib format)')
    parser.add_argument('--save_states', type=str, help='Path to save CSV with latent states')
    args = parser.parse_args()
    
    main(args)