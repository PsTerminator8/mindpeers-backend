import tarfile
import os

def tar_folder(folder_path, tar_filename):
    with tarfile.open(tar_filename, "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))

# Replace with your folder paths and tar archive names
outputs_pretrained_path = "./outputs_pretrained"
outputs_feedback_path = "./outputs_feedback"
pretrained_tar_filename = "outputs_pretrained.tar.gz"
feedback_tar_filename = "outputs_feedback.tar.gz"

tar_folder(outputs_pretrained_path, pretrained_tar_filename)
tar_folder(outputs_feedback_path, feedback_tar_filename)