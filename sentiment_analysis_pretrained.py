from simpletransformers.classification import ClassificationModel, ClassificationArgs
from sklearn.metrics import accuracy_score, f1_score, precision_score
import torch
import os

cuda_available = torch.cuda.is_available()

model_path = os.path.join(os.path.dirname(__file__), "outputs_pretrained")

model_args = ClassificationArgs()
model_args.num_train_epochs = 10
model_args.learning_rate = 1e-4
model_args.labels_list = [0, 1]
model_args.do_lower_case = True
model_args.output_dir = model_path
model_args.overwrite_output_dir = True
model_args.save_model_every_epoch = False
model_args.save_best_model = True

model = ClassificationModel('bert', model_path, num_labels=2, args=model_args, use_cuda=cuda_available)

def get_sentiment(text: str) -> str:
    predictions, _ = model.predict([text])
    sentiment = "positive" if predictions[0] == 1 else "negative"
    return sentiment