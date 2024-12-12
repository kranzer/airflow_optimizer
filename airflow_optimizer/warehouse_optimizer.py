import pandas as pd

WAREHOUSE_SIZES = ['Small', 'Medium', 'Large', 'X-Large']

def optimize_warehouse(data):
    df = pd.DataFrame(data)

    # Filter out invalid data
    df = df[(df['DURATION'] > 0)
            & (df['DURATION'].notnull())
            & df['TASK_ID'].notnull()
    ]

    grouped = df.groupby('TASK_ID').agg({
        'DURATION': 'median',
        'NUMBER_OF_CAMPAIGNS': 'median'
    }).reset_index()

    result = {}
    for _, row in grouped.iterrows():
        task_id = row['TASK_ID']
        duration = row['DURATION']
        campaigns = row['NUMBER_OF_CAMPAIGNS']

        # Assign warehouse based on median duration and campaigns
        if duration < 10:
            warehouse = 'Small'
        elif 10 <= duration <= 20:
            warehouse = 'Medium'
        else:
            warehouse = 'Large' if campaigns < 100 else 'X-Large'

        result[task_id] = warehouse

    return result
