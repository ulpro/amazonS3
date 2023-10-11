import boto3
import os

def upload_file_to_s3(file_path, bucket_name, object_name):
    # Créer une session AWS
    session = boto3.Session(
        aws_access_key_id='AKIA3PHTF3PC4TPQLUFG',
        aws_secret_access_key='uMl1vI8FgzOP2dZd2Wz2YZXCRdh+wUQgx88uGfJw12'
    )

    # Créer une instance du client S3
    s3_client = session.client('s3')

    # Charger le fichier dans le bucket S3
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print("Le fichier a été téléchargé avec succès sur S3.")
    except Exception as e:
        print("Erreur lors du téléchargement du fichier sur S3:", str(e))

# Obtenir le chemin absolu du fichier à télécharger
file_path = os.path.abspath('D:/projets/fichier.txt')



# Spécifier le nom du bucket S3
bucket_name = 'awss3-bucket1'

# Spécifier le nom du fichier sur S3
object_name = 'test.txt'
 

# Appeler la fonction pour télécharger le fichier mis à jour sur S3
upload_file_to_s3(file_path, bucket_name, object_name)