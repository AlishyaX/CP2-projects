import pandas as pd

def analyze_characters(characters):
    # Create a DataFrame from the list of character dictionaries
    df = pd.DataFrame(characters)

    # Check if the DataFrame is empty
    if df.empty:
        print("No character data available for analysis.")
        return
    
    # Select only numeric columns for analysis
    numeric_df = df.select_dtypes(include=['number'])

    # Perform statistical analysis on numeric columns
    print("Mean stats:")
    print(numeric_df.mean())
    print("\nMax stats:")
    print(numeric_df.max())
    print("\nMin stats:")
    print(numeric_df.min())
