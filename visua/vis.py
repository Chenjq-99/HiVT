from argoverse.visualization.visualize_sequences import ArgoverseForecastingLoader

root_dir = '/home/chenjq/Project/argoverse-api/motion_forecast_dataset/val/data'

afl = ArgoverseForecastingLoader(root_dir)

from visualize_sequences import viz_sequence

def visualize(seq_id, pred):
    seq_path = f"{root_dir}/{seq_id}.csv"
    viz_sequence(afl.get(seq_path).seq_df, pred=pred, seq_id=seq_id, show=True)